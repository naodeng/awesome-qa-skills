#!/usr/bin/env python3
"""Maintain explicit, host-neutral Workflow checkpoints without executing Skills."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid

from validate_workflow_contracts import validate_run_state, validate_workflow


RUN_ID_RE = re.compile(r"^run-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$")
TERMINAL_STAGE_STATES = {"COMPLETED", "SKIPPED"}
IGNORED_PARTS = {".git", "__pycache__"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def workflow_package_sha256(workflow_file: Path) -> str:
    package_dir = workflow_file.resolve(strict=True).parent
    digest = hashlib.sha256()
    for path in sorted(package_dir.rglob("*"), key=lambda item: item.relative_to(package_dir).as_posix()):
        relative = path.relative_to(package_dir)
        if any(part in IGNORED_PARTS for part in relative.parts) or path.name == ".DS_Store":
            continue
        if path.is_symlink():
            contents = os.readlink(path).encode("utf-8")
            kind = b"symlink"
        elif path.is_file():
            contents = path.read_bytes()
            kind = b"file"
        else:
            continue
        digest.update(kind + b"\0" + relative.as_posix().encode("utf-8") + b"\0" + contents + b"\0")
    return digest.hexdigest()


def _write_atomic(path: Path, state: dict) -> None:
    errors = validate_run_state(state)
    if errors:
        raise ValueError("refusing to write invalid run state: " + "; ".join(errors))
    temporary = path.with_name(path.name + f".{uuid.uuid4().hex}.tmp")
    encoded = (json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    descriptor = os.open(temporary, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _create_exclusive(path: Path, state: dict) -> None:
    errors = validate_run_state(state)
    if errors:
        raise ValueError("refusing to write invalid run state: " + "; ".join(errors))
    temporary = path.with_name(path.name + f".{uuid.uuid4().hex}.tmp")
    encoded = (json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    descriptor = os.open(temporary, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError as exc:
            raise ValueError(f"run already exists: {path.stem}") from exc
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def _locked_state(path: Path):
    original_path = path.expanduser()
    if original_path.is_symlink():
        raise ValueError("--state-file cannot be a symbolic link")
    path = original_path.resolve(strict=True)
    if not path.is_file():
        raise ValueError("--state-file must be a regular file")
    lock_path = path.with_name(path.name + ".lock")
    descriptor = os.open(lock_path, os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        state = json.loads(path.read_text(encoding="utf-8"))
        yield path, state
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def _emit(path: Path, state: dict, **extra) -> None:
    print(json.dumps({"state_file": str(path), "state": state, **extra}, ensure_ascii=False, indent=2))


def _mark_stale(state: dict, reason: str) -> None:
    timestamp = now()
    state["status"] = "STALE"
    state["stale_reason"] = reason
    for stage in state["stages"]:
        if stage["status"] not in TERMINAL_STAGE_STATES:
            stage["status"] = "STALE"
            stage["finished_at"] = timestamp
    state["updated_at"] = timestamp


def _expected_match(state: dict, fingerprint: str, commit_sha: str, workflow_source_sha256: str) -> bool:
    reasons = []
    if state["input_fingerprint"] != fingerprint:
        reasons.append("input fingerprint changed")
    if state["commit_sha"] != commit_sha:
        reasons.append("commit SHA changed")
    if state["workflow_source_sha256"] != workflow_source_sha256:
        reasons.append("Workflow package changed")
    if reasons:
        _mark_stale(state, "; ".join(reasons))
        return False
    return True


def _step(workflow: dict, stage_id: str) -> tuple[dict, dict]:
    for stage in workflow["steps"]:
        if stage["id"] == stage_id:
            return stage, workflow
    raise ValueError(f"unknown stage id: {stage_id}")


def _state_stage(state: dict, stage_id: str) -> dict:
    for stage in state["stages"]:
        if stage["id"] == stage_id:
            return stage
    raise ValueError(f"unknown stage id: {stage_id}")


def _refresh_status(state: dict) -> None:
    statuses = [stage["status"] for stage in state["stages"]]
    if all(status in TERMINAL_STAGE_STATES for status in statuses):
        state["status"] = "COMPLETED"
    elif "FAILED" in statuses:
        state["status"] = "FAILED"
    elif "BLOCKED" in statuses or "STALE" in statuses:
        state["status"] = "BLOCKED"
    elif "RUNNING" in statuses:
        state["status"] = "RUNNING"
    else:
        state["status"] = "NOT_STARTED"
    state["updated_at"] = now()


def create_run(args: argparse.Namespace) -> int:
    workflow_path = args.workflow_file.resolve(strict=True)
    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    errors = validate_workflow(workflow, workflow_path.parent)
    if errors:
        raise ValueError("invalid Workflow contract: " + "; ".join(errors))
    if not re.fullmatch(r"[a-fA-F0-9]{64}", args.input_fingerprint):
        raise ValueError("--input-fingerprint must be a SHA-256 hex digest")
    if not re.fullmatch(r"(?:[a-fA-F0-9]{40}|[a-fA-F0-9]{64})", args.commit_sha):
        raise ValueError("--commit-sha must be a 40- or 64-character Git SHA")
    run_id = args.run_id or f"run-{uuid.uuid4().hex}"
    if not RUN_ID_RE.fullmatch(run_id):
        raise ValueError("--run-id must match run-<letters-numbers-hyphens>")
    state_dir = args.state_dir.resolve(strict=False) / workflow["id"]
    state_dir.mkdir(parents=True, exist_ok=True)
    state_path = state_dir / f"{run_id}.json"
    timestamp = now()
    state = {
        "schema_version": "1.0.0",
        "run_id": run_id,
        "workflow_id": workflow["id"],
        "workflow_version": workflow["version"],
        "status": "NOT_STARTED",
        "input_fingerprint": args.input_fingerprint.lower(),
        "workflow_source_sha256": workflow_package_sha256(workflow_path),
        "commit_sha": args.commit_sha.lower(),
        "created_at": timestamp,
        "updated_at": timestamp,
        "stages": [
            {"id": step["id"], "status": "NOT_STARTED", "attempt": 0, "evidence_refs": []}
            for step in workflow["steps"]
        ],
        "artifacts": [],
        "idempotency_keys": [],
    }
    if args.output_dir:
        state_dir = args.output_dir.resolve(strict=False)
        state_dir.mkdir(parents=True, exist_ok=True)
        state_path = state_dir / f"{run_id}.json"
    _create_exclusive(state_path, state)
    _emit(state_path, state)
    return 0


def fingerprint_inputs(args: argparse.Namespace) -> int:
    base = args.base_dir.resolve(strict=True)
    entries: list[tuple[str, bytes]] = []
    for source in args.input:
        path = source.resolve(strict=True)
        if not path.is_relative_to(base):
            raise ValueError(f"input path must be inside --base-dir: {source}")
        if path.is_file():
            entries.append((path.relative_to(base).as_posix(), path.read_bytes()))
        elif path.is_dir():
            for item in sorted(path.rglob("*")):
                relative = item.relative_to(base)
                if any(part in {".git", "__pycache__"} for part in relative.parts) or item.name == ".DS_Store":
                    continue
                if item.is_symlink():
                    raise ValueError(f"symbolic links are not fingerprinted; select the resolved source explicitly: {relative}")
                if item.is_file():
                    entries.append((relative.as_posix(), item.read_bytes()))
        else:
            raise ValueError(f"input must be a regular file or directory: {source}")
    if not entries:
        raise ValueError("at least one non-empty input file is required")
    digest = hashlib.sha256()
    for relative, contents in sorted(entries):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(contents)
        digest.update(b"\0")
    digest.update(args.commit_sha.encode("ascii"))
    print(json.dumps({"algorithm": "sha256-tree-commit-v1", "input_fingerprint": digest.hexdigest(), "file_count": len(entries)}))
    return 0


def mutate_state(args: argparse.Namespace) -> int:
    with _locked_state(args.state_file) as (path, state):
        if args.command == "start-stage":
            if state["status"] in {"STALE", "COMPLETED", "BLOCKED"}:
                raise ValueError(f"cannot start a stage while run status is {state['status']}; inspect or create a new run")
            if state["status"] == "FAILED":
                failed_stages = [stage for stage in state["stages"] if stage["status"] == "FAILED"]
                if (
                    not failed_stages
                    or any(stage["status"] in {"BLOCKED", "STALE"} for stage in state["stages"])
                    or any(
                        _step(args.workflow, stage["id"])[0].get("on_failure") != "continue_with_gap"
                        for stage in failed_stages
                    )
                ):
                    raise ValueError("cannot start a stage while run status is FAILED; inspect or create a new run")
            package_fingerprint = workflow_package_sha256(args.workflow_file)
            if not _expected_match(state, args.expected_input_fingerprint, args.expected_commit_sha, package_fingerprint):
                _write_atomic(path, state)
                _emit(path, state, error="checkpoint is stale; refusing stage execution")
                return 1
            stage_contract, workflow = _step(args.workflow, args.stage_id)
            stage = _state_stage(state, args.stage_id)
            if stage["status"] != "NOT_STARTED":
                raise ValueError(f"stage {args.stage_id} is {stage['status']}; automatic replay is disabled")
            for dependency in stage_contract.get("depends_on", []):
                dependency_state = _state_stage(state, dependency)["status"]
                if dependency_state not in TERMINAL_STAGE_STATES:
                    raise ValueError(f"stage {args.stage_id} depends on {dependency} ({dependency_state})")
            requires_approval = stage_contract.get("approval_required") or stage_contract.get("permission") == "write"
            if requires_approval and (not args.confirm or not args.approved_by.strip()):
                raise ValueError("high-risk stage requires --confirm and --approved-by <human identifier>")
            if args.confirm and not args.approved_by.strip():
                raise ValueError("--confirm requires --approved-by <human identifier>")
            key = f"{state['run_id']}:{args.stage_id}:{state['input_fingerprint']}"
            if key in state["idempotency_keys"]:
                raise ValueError(f"idempotency key already claimed: {key}")
            state["idempotency_keys"].append(key)
            stage["attempt"] += 1
            stage["status"] = "RUNNING"
            stage["started_at"] = now()
            if requires_approval:
                stage["approval"] = {
                    "status": "APPROVED",
                    "approved_by": args.approved_by.strip(),
                    "approved_at": now(),
                    "scope": f"{args.stage_id}:{stage_contract['permission']}",
                }
            state["status"] = "RUNNING"
            state["updated_at"] = now()
        elif args.command == "complete-stage":
            stage = _state_stage(state, args.stage_id)
            if stage["status"] != "RUNNING":
                raise ValueError(f"stage {args.stage_id} cannot complete from {stage['status']}")
            if not args.evidence_ref or any(not ref.strip() for ref in args.evidence_ref):
                raise ValueError("completion requires at least one non-empty --evidence-ref")
            stage["status"] = "COMPLETED"
            stage["evidence_refs"] = list(dict.fromkeys(ref.strip() for ref in args.evidence_ref))
            if args.checkpoint_ref:
                stage["checkpoint_ref"] = args.checkpoint_ref
            stage["finished_at"] = now()
            _refresh_status(state)
        elif args.command in {"fail-stage", "block-stage"}:
            stage = _state_stage(state, args.stage_id)
            if stage["status"] != "RUNNING":
                raise ValueError(f"stage {args.stage_id} cannot transition from {stage['status']}")
            stage["status"] = "FAILED" if args.command == "fail-stage" else "BLOCKED"
            stage["checkpoint_ref"] = f"{args.command}:{args.reason.strip()}"
            stage["finished_at"] = now()
            _refresh_status(state)
        elif args.command == "skip-stage":
            stage_contract, _ = _step(args.workflow, args.stage_id)
            stage = _state_stage(state, args.stage_id)
            if stage["status"] != "NOT_STARTED":
                raise ValueError(f"stage {args.stage_id} cannot be skipped from {stage['status']}")
            for dependency in stage_contract.get("depends_on", []):
                dependency_state = _state_stage(state, dependency)["status"]
                if dependency_state not in TERMINAL_STAGE_STATES:
                    raise ValueError(f"stage {args.stage_id} depends on {dependency} ({dependency_state})")
            allowed_reasons = {entry.get("reason") for entry in stage_contract.get("skip_when", []) if isinstance(entry, dict)}
            if not allowed_reasons or args.reason not in allowed_reasons:
                raise ValueError("skip reason must exactly match a declared workflow skip_when reason")
            stage["status"] = "SKIPPED"
            stage["checkpoint_ref"] = f"skip:{args.reason}"
            stage["finished_at"] = now()
            _refresh_status(state)
        else:
            raise ValueError(f"unsupported state operation: {args.command}")
        _write_atomic(path, state)
        _emit(path, state)
        return 0


def resume(args: argparse.Namespace) -> int:
    with _locked_state(args.state_file) as (path, state):
        package_fingerprint = workflow_package_sha256(args.workflow_file)
        if not _expected_match(state, args.expected_input_fingerprint, args.expected_commit_sha, package_fingerprint):
            _write_atomic(path, state)
            _emit(path, state, resume_status="STALE", error="inputs changed; all non-terminal checkpoints are invalid")
            return 1
        interrupted = []
        for stage in state["stages"]:
            if stage["status"] == "RUNNING":
                stage["status"] = "BLOCKED"
                stage["finished_at"] = now()
                stage["checkpoint_ref"] = "recovery-review-required: review before retry and inspect side effects"
                interrupted.append(stage["id"])
        if interrupted:
            state["status"] = "BLOCKED"
            state["updated_at"] = now()
            _write_atomic(path, state)
            _emit(path, state, resume_status="REVIEW_REQUIRED", interrupted_stages=interrupted, ready_stages=[], automatic_replay=False)
            return 0
        if state["status"] in {"BLOCKED", "FAILED"}:
            _emit(path, state, resume_status="REVIEW_REQUIRED", ready_stages=[], automatic_replay=False)
            return 0
        if state["status"] == "COMPLETED":
            _emit(path, state, resume_status="ALREADY_COMPLETED", ready_stages=[], automatic_replay=False)
            return 0
        ready = []
        for step in args.workflow["steps"]:
            stage = _state_stage(state, step["id"])
            if stage["status"] == "NOT_STARTED" and all(
                _state_stage(state, dependency)["status"] in TERMINAL_STAGE_STATES
                for dependency in step.get("depends_on", [])
            ):
                ready.append(stage["id"])
        _emit(path, state, resume_status="CHECKPOINT_VALID", ready_stages=ready, automatic_replay=False)
        return 0


def add_workflow_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--workflow-file", type=Path, required=True)


def load_workflow(path: Path) -> dict:
    workflow_path = path.resolve(strict=True)
    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    errors = validate_workflow(workflow, workflow_path.parent)
    if errors:
        raise ValueError("invalid Workflow contract: " + "; ".join(errors))
    return workflow


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    create = subparsers.add_parser("create", help="create a durable run-state checkpoint")
    add_workflow_argument(create)
    create.add_argument("--state-dir", type=Path, required=True)
    create.add_argument("--output-dir", type=Path, help="optional exact state directory")
    create.add_argument("--input-fingerprint", required=True)
    create.add_argument("--commit-sha", required=True)
    create.add_argument("--run-id")

    fingerprint = subparsers.add_parser("fingerprint", help="hash input files plus a commit SHA")
    fingerprint.add_argument("--base-dir", type=Path, default=Path.cwd())
    fingerprint.add_argument("--input", type=Path, action="append", required=True)
    fingerprint.add_argument("--commit-sha", required=True)

    for operation in ("start-stage", "complete-stage", "fail-stage", "block-stage", "skip-stage"):
        command = subparsers.add_parser(operation)
        command.add_argument("--state-file", type=Path, required=True)
        command.add_argument("--stage-id", required=True)
        if operation in {"start-stage", "skip-stage"}:
            add_workflow_argument(command)
        if operation == "start-stage":
            command.add_argument("--expected-input-fingerprint", required=True)
            command.add_argument("--expected-commit-sha", required=True)
            command.add_argument("--confirm", action="store_true", help="record an explicit human approval for a high-risk stage")
            command.add_argument("--approved-by", default="")
        if operation == "complete-stage":
            command.add_argument("--evidence-ref", action="append", required=True)
            command.add_argument("--checkpoint-ref")
        if operation in {"fail-stage", "block-stage", "skip-stage"}:
            command.add_argument("--reason", required=True)

    resume_parser = subparsers.add_parser("resume", help="validate a checkpoint; never replay a stage")
    resume_parser.add_argument("--state-file", type=Path, required=True)
    add_workflow_argument(resume_parser)
    resume_parser.add_argument("--expected-input-fingerprint", required=True)
    resume_parser.add_argument("--expected-commit-sha", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            return create_run(args)
        if args.command == "fingerprint":
            if not re.fullmatch(r"(?:[a-fA-F0-9]{40}|[a-fA-F0-9]{64})", args.commit_sha):
                raise ValueError("--commit-sha must be a 40- or 64-character Git SHA")
            return fingerprint_inputs(args)
        if args.command in {"start-stage", "skip-stage", "resume"}:
            args.workflow = load_workflow(args.workflow_file)
        if args.command == "resume":
            return resume(args)
        return mutate_state(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
