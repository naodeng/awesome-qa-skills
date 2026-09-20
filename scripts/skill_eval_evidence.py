#!/usr/bin/env python3
"""Evidence metadata helpers shared by the local Skill evaluation runners."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import subprocess
import uuid
from typing import Iterable


EVIDENCE_STATES = (
    "PASS",
    "FAIL",
    "BLOCKED",
    "NOT_RUN",
    "INSUFFICIENT_EVIDENCE",
)
FAILURE_CLASSIFICATIONS = (
    "SKILL_DEFECT",
    "EVAL_DEFECT",
    "INFRASTRUCTURE_DEFECT",
    "UNKNOWN",
)


@dataclass(frozen=True)
class RunMetadata:
    run_id: str
    case_id: str
    variant: str
    skill_version: str
    eval_version: str
    skill_up_version: str
    engine: str
    provider: str
    requested_model: str
    observed_model: str
    judge_type: str
    judge_model: str
    environment: str
    timestamp: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    def for_case(self, case_id: str) -> "RunMetadata":
        return replace(self, case_id=_unknown(case_id))


def _unknown(value: str | None) -> str:
    return value.strip() if isinstance(value, str) and value.strip() else "unknown"


def _sha256(paths: Iterable[Path]) -> str:
    """Hash eval inputs without making the version depend on checkout paths."""

    digest = hashlib.sha256()
    files: list[tuple[str, bytes]] = []
    for path in (Path(item) for item in paths):
        if not path.is_file():
            continue
        files.append((path.name, path.read_bytes()))

    for name, contents in sorted(files, key=lambda item: (item[0], item[1])):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(contents)
        digest.update(b"\0")
    return digest.hexdigest() if files else "unknown"


def _git_revision(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(path),
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return "unknown"
    revision = _unknown(result.stdout if result.returncode == 0 else None)
    if revision == "unknown":
        return revision

    try:
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", "."],
            cwd=str(path),
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        status = None

    content_hash = _directory_sha256(path)
    if content_hash == "unknown":
        return revision
    if status is None or status.returncode != 0:
        state = "unknown"
    else:
        state = "dirty" if status.stdout.strip() else "clean"
    return f"{revision}+{state}-{content_hash[:16]}"


def _directory_sha256(root: Path) -> str:
    if not root.is_dir():
        return "unknown"

    digest = hashlib.sha256()
    files = [
        path
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(root).parts
    ]
    for path in sorted(files, key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest() if files else "unknown"


def command_version(command: str) -> str:
    """Return a short version string without installing or contacting a service."""

    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return "unknown"
    if result.returncode != 0:
        return "unknown"
    first_line = (result.stdout or result.stderr).strip().splitlines()
    return _unknown(first_line[0] if first_line else None)


def build_run_metadata(
    *,
    skill_root: Path,
    eval_paths: Iterable[Path],
    engine: str | None,
    requested_model: str | None,
    provider: str | None,
    environment: str | None,
    skill_up_version: str | None = None,
    run_id: str | None = None,
    case_id: str | None = None,
    variant: str | None = None,
    observed_model: str | None = None,
    judge_type: str | None = None,
    judge_model: str | None = None,
) -> RunMetadata:
    """Build reproducibility metadata while keeping unavailable values explicit."""

    return RunMetadata(
        run_id=_unknown(run_id) if run_id else f"run-{uuid.uuid4().hex}",
        case_id=_unknown(case_id),
        variant=_unknown(variant),
        skill_version=_git_revision(skill_root),
        eval_version=_sha256(eval_paths),
        skill_up_version=_unknown(skill_up_version) if skill_up_version else command_version("skill-up"),
        engine=_unknown(engine),
        provider=_unknown(provider),
        requested_model=_unknown(requested_model),
        observed_model=_unknown(observed_model),
        judge_type=_unknown(judge_type),
        judge_model=_unknown(judge_model),
        environment=_unknown(environment),
        timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    )


def evidence_state(
    *,
    dry_run: bool,
    runner_exit_code: int | None,
    eval_exit_code: int | None,
    trace_event_count: int,
    trace_error_count: int = 0,
) -> str:
    """Map runner observations to a bounded evidence state."""

    if dry_run:
        return "NOT_RUN"
    if trace_error_count > 0:
        return "FAIL"
    if runner_exit_code is None or trace_event_count <= 0:
        return "BLOCKED"
    if eval_exit_code == 1 or runner_exit_code != 0:
        return "FAIL"
    if eval_exit_code == 2:
        return "BLOCKED"
    if eval_exit_code == 0:
        return "PASS"
    return "INSUFFICIENT_EVIDENCE"


def failure_classification(
    *,
    state: str,
    trace_event_count: int,
    requested: str | None,
    trace_error_count: int = 0,
) -> str | None:
    """Return explicit attribution, never infer a Skill defect from a failure."""

    if state in {"PASS", "NOT_RUN"}:
        return None
    if trace_error_count > 0 and state == "BLOCKED":
        return "UNKNOWN"
    if requested is not None:
        normalized = requested.strip().upper()
        if normalized not in FAILURE_CLASSIFICATIONS:
            allowed = ", ".join(FAILURE_CLASSIFICATIONS)
            raise ValueError(f"failure classification must be one of {allowed}")
        return normalized
    if state == "BLOCKED" and trace_event_count == 0:
        return "INFRASTRUCTURE_DEFECT"
    return "UNKNOWN"


def summary_counts(states: Iterable[str]) -> dict[str, int]:
    counts = {state: 0 for state in EVIDENCE_STATES}
    for state in states:
        counts[state] = counts.get(state, 0) + 1
    return counts
