#!/usr/bin/env python3
"""Run one skill-up Eval with start-time provenance and mutation detection."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid


EXCLUDED_PARTS = {".git", "__pycache__"}
ALLOWED_CASE_STATES = {"PASS", "FAIL", "ERROR", "BLOCKED", "UNKNOWN", "NOT_RUN"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def package_manifest(skill_dir: Path) -> tuple[str, list[dict[str, str]]]:
    entries: list[dict[str, str]] = []
    for path in sorted(skill_dir.rglob("*"), key=lambda item: item.relative_to(skill_dir).as_posix()):
        relative = path.relative_to(skill_dir)
        if any(part in EXCLUDED_PARTS for part in relative.parts) or path.name == ".DS_Store":
            continue
        if path.is_symlink():
            entries.append({
                "path": relative.as_posix(),
                "kind": "symlink",
                "sha256": hashlib.sha256(os.readlink(path).encode("utf-8")).hexdigest(),
            })
        elif path.is_file():
            entries.append({
                "path": relative.as_posix(),
                "kind": "file",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            })
    encoded = json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest(), entries


def repository_revision(path: Path) -> tuple[str, int | None]:
    try:
        root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], cwd=path,
            capture_output=True, text=True, check=False,
        )
        if root.returncode != 0:
            return "unknown", None
        repo_root = Path(root.stdout.strip())
        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=repo_root,
            capture_output=True, text=True, check=False,
        )
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all"], cwd=repo_root,
            capture_output=True, text=True, check=False,
        )
    except OSError:
        return "unknown", None
    if revision.returncode != 0:
        return "unknown", None
    dirty_count = len(status.stdout.splitlines()) if status.returncode == 0 else None
    return revision.stdout.strip(), dirty_count


def configured_engine(eval_file: Path) -> str:
    text = eval_file.read_text(encoding="utf-8")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        document = None
    if isinstance(document, dict):
        engine = document.get("engine")
        if isinstance(engine, dict) and isinstance(engine.get("name"), str):
            return engine["name"]
    inline = re.search(r"(?m)^engine\s*:\s*\{[^\n}]*\bname\s*:\s*['\"]?([A-Za-z0-9_-]+)", text)
    if inline:
        return inline.group(1)
    block = re.search(r"(?ms)^engine\s*:\s*\n((?:^[ \t]+[^\n]*\n?)*)", text)
    if block:
        name = re.search(r"(?m)^[ \t]+name\s*:\s*['\"]?([A-Za-z0-9_-]+)", block.group(1))
        if name:
            return name.group(1)
    return "unknown"


def engine_cli_version(engine: str) -> str:
    binary = {
        "claude_code": "claude",
        "claude-code": "claude",
        "claude": "claude",
        "codex": "codex",
    }.get(engine, engine)
    executable = shutil.which(binary)
    if not executable:
        return "unknown"
    try:
        result = subprocess.run([executable, "--version"], capture_output=True, text=True, check=False)
    except OSError:
        return "unknown"
    if result.returncode != 0:
        return "unknown"
    lines = (result.stdout or result.stderr).strip().splitlines()
    return lines[0].strip() if lines and lines[0].strip() else "unknown"


def write_json_atomic(path: Path, value: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def report_cases(report: dict) -> list[dict]:
    for key in ("case_results", "cases", "results"):
        candidate = report.get(key)
        if isinstance(candidate, list):
            return candidate
    return []


def classify(report: dict | None, process_exit: int) -> tuple[str, list[dict[str, str]], str | None]:
    if report is None:
        return "ERROR", [], "skill-up did not produce a readable report.json"
    cases: list[dict[str, str]] = []
    for index, case in enumerate(report_cases(report)):
        if not isinstance(case, dict):
            return "ERROR", cases, f"report case at index {index} is not an object"
        case_id = case.get("case_id", case.get("id", f"case-{index + 1}"))
        raw_state = case.get("status", case.get("result"))
        state = raw_state.upper() if isinstance(raw_state, str) else ""
        if state not in ALLOWED_CASE_STATES:
            return "ERROR", cases, f"report case {case_id!r} has no recognized status"
        cases.append({"case_id": str(case_id), "status": state})
    summary = report.get("summary")
    summary_state = None
    if isinstance(summary, dict):
        value = summary.get("overall_status", summary.get("status"))
        if isinstance(value, str):
            summary_state = value.upper()
    if not cases and summary_state not in ALLOWED_CASE_STATES:
        return "ERROR", cases, "report has no recognized case results or overall status"
    states = [case["status"] for case in cases]
    if summary_state:
        states.append(summary_state)
    if "ERROR" in states or process_exit not in (0, 1):
        return "ERROR", cases, f"skill-up returned exit code {process_exit} or reported an error"
    if "FAIL" in states or process_exit == 1:
        return "FAIL", cases, None
    if "BLOCKED" in states or "UNKNOWN" in states or "NOT_RUN" in states:
        return "BLOCKED", cases, "one or more cases did not produce a decisive result"
    if states and all(state == "PASS" for state in states) and process_exit == 0:
        return "PASS", cases, None
    return "BLOCKED", cases, "report status is incomplete"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", type=Path, required=True)
    parser.add_argument("--eval-file", required=True, help="Eval config path relative to --skill-dir")
    parser.add_argument("--output-dir", type=Path, required=True, help="Must be a new directory outside the Skill package")
    parser.add_argument("--skill-up-bin", default="skill-up")
    parser.add_argument("--engine", help="Optional explicit engine override; otherwise the Eval config is authoritative")
    parser.add_argument("skill_up_args", nargs=argparse.REMAINDER, help="Arguments after -- are passed to skill-up run")
    args = parser.parse_args(argv)
    if args.skill_up_args and args.skill_up_args[0] == "--":
        args.skill_up_args = args.skill_up_args[1:]
    if any(arg == "--output-dir" or arg.startswith("--output-dir=") for arg in args.skill_up_args):
        parser.error("--output-dir is controlled by this evidence runner")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        skill_dir = args.skill_dir.resolve(strict=True)
        eval_path = (skill_dir / args.eval_file).resolve(strict=True)
        output_dir = args.output_dir.resolve(strict=False)
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
            raise ValueError("--skill-dir must point to a Skill package containing SKILL.md")
        if not eval_path.is_relative_to(skill_dir) or not eval_path.is_file():
            raise ValueError("--eval-file must be an existing file inside the Skill package")
        if output_dir.is_relative_to(skill_dir):
            raise ValueError("--output-dir must be outside the Skill package")
        input_fingerprint_before, files_before = package_manifest(skill_dir)
        revision, dirty_path_count = repository_revision(skill_dir)
        engine = args.engine or configured_engine(eval_path)
        engine_version = engine_cli_version(engine)
        fingerprint_payload = {
            "skill_package_sha256": input_fingerprint_before,
            "eval_file": eval_path.relative_to(skill_dir).as_posix(),
            "skill_up_args_sha256": hashlib.sha256(
                json.dumps(args.skill_up_args, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "engine": engine,
            "engine_version": engine_version,
            "commit_sha": revision,
        }
        input_fingerprint = hashlib.sha256(
            json.dumps(fingerprint_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        output_dir.mkdir(exist_ok=False)
        started_at = utc_now()
        run_id = f"skill-up-{skill_dir.name}-{uuid.uuid4().hex}"
        try:
            version_result = subprocess.run(
                [args.skill_up_bin, "--version"], capture_output=True,
                text=True, check=False,
            )
            version = ((version_result.stdout or version_result.stderr).strip().splitlines() or ["unknown"])[0]
        except OSError:
            version = "unknown"
        manifest = {
            "record_version": "skill-up-run-manifest/v1",
            "run_id": run_id,
            "skill_id": skill_dir.name,
            "status": "RUNNING",
            "started_at": started_at,
            "finished_at": None,
            "runner": {"name": "skill-up", "version": version},
            "engine": engine,
            "engine_version": engine_version,
            "commit_sha": revision,
            "dirty_path_count": dirty_path_count,
            "input_fingerprint": input_fingerprint,
            "input_fingerprint_after": None,
            "skill_package_sha256": input_fingerprint_before,
            "skill_file_count": len(files_before),
            "raw_report_path": None,
            "raw_report_sha256": None,
            "process_exit_code": None,
            "cases": [],
            "error": None,
            "stale_reason": None,
        }
        manifest_path = output_dir / "run-manifest.json"
        write_json_atomic(manifest_path, manifest)
        command = [args.skill_up_bin, "run", eval_path.relative_to(skill_dir).as_posix()]
        if args.engine:
            command.extend(["--engine", args.engine])
        command.extend(args.skill_up_args)
        command.extend(["--output-dir", str(output_dir)])
        try:
            process = subprocess.run(command, cwd=skill_dir, check=False)
            process_exit = process.returncode
        except OSError as exc:
            process_exit = 127
            manifest["error"] = f"could not start skill-up: {exc.__class__.__name__}"
        report_paths = sorted(
            path for path in output_dir.rglob("report.json")
            if path.is_file() and not path.is_symlink()
        )
        report = None
        if len(report_paths) == 1:
            report_path = report_paths[0]
            manifest["raw_report_path"] = report_path.relative_to(output_dir).as_posix()
            raw_bytes = report_path.read_bytes()
            manifest["raw_report_sha256"] = hashlib.sha256(raw_bytes).hexdigest()
            try:
                parsed = json.loads(raw_bytes)
                report = parsed if isinstance(parsed, dict) else None
            except (json.JSONDecodeError, UnicodeDecodeError):
                report = None
        elif len(report_paths) > 1:
            manifest["error"] = "multiple report.json files found; report selection is ambiguous"
        status, cases, classify_error = classify(report, process_exit)
        manifest["cases"] = cases
        manifest["process_exit_code"] = process_exit
        if classify_error and not manifest["error"]:
            manifest["error"] = classify_error
        fingerprint_after, files_after = package_manifest(skill_dir)
        manifest["input_fingerprint_after"] = hashlib.sha256(
            json.dumps({
                "skill_package_sha256": fingerprint_after,
                "eval_file": eval_path.relative_to(skill_dir).as_posix(),
                "skill_up_args_sha256": fingerprint_payload["skill_up_args_sha256"],
                "engine": engine,
                "engine_version": engine_version,
                "commit_sha": revision,
            }, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        manifest["skill_file_count_after"] = len(files_after)
        if fingerprint_after != input_fingerprint_before:
            status = "STALE"
            manifest["stale_reason"] = "Skill package inputs changed during run"
        manifest["status"] = status
        manifest["finished_at"] = utc_now()
        write_json_atomic(manifest_path, manifest)
        print(f"{status}: {manifest_path}")
        return 0 if status == "PASS" else (1 if status in {"FAIL", "STALE"} else 2)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
