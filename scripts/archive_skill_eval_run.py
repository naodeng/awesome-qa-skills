#!/usr/bin/env python3
"""Create a path-sanitized, provenance-preserving Eval archive from a run."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


CASE_STATES = {"PASS", "FAIL", "ERROR", "BLOCKED", "UNKNOWN", "NOT_RUN", "STALE"}


def _sanitize(value, *, repo_root: Path, skill_id: str, skill_source: str):
    if isinstance(value, str):
        sanitized = value
        package_prefix = re.compile(
            rf"/(?:[^/\s<>\"']+/)*skill-up-[^/\s<>\"']+/(?:\.codex/skills/)?{re.escape(skill_id)}/"
        )
        sanitized = package_prefix.sub(f"{skill_source}/", sanitized)
        repo_prefix = str(repo_root.resolve()).rstrip("/") + "/"
        sanitized = sanitized.replace(repo_prefix, "")
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item, repo_root=repo_root, skill_id=skill_id, skill_source=skill_source) for item in value]
    if isinstance(value, dict):
        return {
            key: _sanitize(item, repo_root=repo_root, skill_id=skill_id, skill_source=skill_source)
            for key, item in value.items()
        }
    return value


def _cases(report: dict, manifest: dict) -> list[dict]:
    for key in ("case_results", "cases", "results"):
        value = report.get(key)
        if isinstance(value, list):
            return value
    return manifest.get("cases", []) if isinstance(manifest.get("cases"), list) else []


def _overall_status(manifest_status: str, cases: list[dict]) -> str:
    status = manifest_status.upper()
    case_states = [
        str(case.get("status", "UNKNOWN")).upper()
        for case in cases if isinstance(case, dict)
    ]
    if status == "STALE" or "STALE" in case_states:
        return "STALE"
    if status == "ERROR" or "ERROR" in case_states:
        return "ERROR"
    if status == "FAIL" or "FAIL" in case_states:
        return "FAIL"
    if status == "BLOCKED" or any(state in {"BLOCKED", "UNKNOWN", "NOT_RUN"} for state in case_states):
        return "BLOCKED"
    if status == "PASS" and case_states and all(state == "PASS" for state in case_states):
        return "PASS"
    return "UNKNOWN"


def archive_run(manifest_path: Path, skill_dir: Path, repo_root: Path, locale: str, output: Path) -> dict:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    skill_dir = skill_dir.resolve(strict=True)
    repo_root = repo_root.resolve(strict=True)
    if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
        raise ValueError("--skill-dir must point to a Skill package")
    if not skill_dir.is_relative_to(repo_root):
        raise ValueError("--skill-dir must be inside --repo-root")
    skill_id = skill_dir.name
    if manifest.get("skill_id") != skill_id:
        raise ValueError("run manifest skill_id does not match --skill-dir")
    report_relative = manifest.get("raw_report_path")
    if not isinstance(report_relative, str) or not report_relative:
        raise ValueError("run manifest does not identify a raw report")
    run_dir = manifest_path.resolve(strict=True).parent
    report_path = (run_dir / report_relative).resolve(strict=True)
    if not report_path.is_relative_to(run_dir) or not report_path.is_file():
        raise ValueError("raw report must be a file inside the run directory")
    raw = report_path.read_bytes()
    raw_hash = hashlib.sha256(raw).hexdigest()
    expected_hash = manifest.get("raw_report_sha256")
    if raw_hash != expected_hash:
        raise ValueError("raw report SHA-256 does not match the run manifest")
    report = json.loads(raw)
    if not isinstance(report, dict):
        raise ValueError("raw report must be a JSON object")
    cases = _cases(report, manifest)
    status = _overall_status(str(manifest.get("status", "UNKNOWN")), cases)
    counts = {state: 0 for state in ("PASS", "FAIL", "ERROR", "BLOCKED", "UNKNOWN", "NOT_RUN", "STALE")}
    for case in cases:
        if isinstance(case, dict):
            state = str(case.get("status", "UNKNOWN")).upper()
            counts[state if state in counts else "UNKNOWN"] += 1
    skill_source = skill_dir.relative_to(repo_root).as_posix()
    sanitized_cases = _sanitize(cases, repo_root=repo_root, skill_id=skill_id, skill_source=skill_source)
    expected_count = len(cases)
    archive = {
        "record_version": "workflow-eval-run/v1",
        "run_id": manifest.get("run_id", "unknown"),
        "workflow_id": skill_id,
        "locale": locale,
        "execution_type": "model_eval",
        "runner": manifest.get("runner", {}),
        "engine": {
            "name": manifest.get("engine", report.get("engine_name", "unknown")),
            "version": manifest.get("engine_version", report.get("engine_version", "not reported")),
            "model_id_reported": report.get("model_name") or "not reported",
        },
        "engine_version_capture": "captured before run" if manifest.get("engine_version") not in (None, "unknown") else "not reported",
        "repo_head_at_archive": manifest.get("commit_sha", "unknown"),
        "worktree_state_at_archive": (
            f"dirty; {manifest['dirty_path_count']} paths changed"
            if isinstance(manifest.get("dirty_path_count"), int) and manifest["dirty_path_count"] > 0
            else "clean" if manifest.get("dirty_path_count") == 0 else "unknown"
        ),
        "input_fingerprint_capture": "captured before run",
        "input_fingerprint": manifest.get("input_fingerprint"),
        "input_fingerprint_after": manifest.get("input_fingerprint_after"),
        "skill_package_sha256_at_start": manifest.get("skill_package_sha256"),
        "raw_result_sha256": raw_hash,
        "started_at": manifest.get("started_at"),
        "finished_at": manifest.get("finished_at"),
        "summary": {
            "case_count": expected_count,
            "passed": counts["PASS"],
            "failed": counts["FAIL"],
            "errors": counts["ERROR"],
            "blocked": counts["BLOCKED"],
            "unknown": counts["UNKNOWN"] + counts["NOT_RUN"],
            "overall_status": status,
        },
        "execution_notes": (
            "Generated from the raw skill-up report. Input fingerprint was captured before execution; "
            "post-run fingerprint equality is available in this record."
        ),
        "redaction": (
            "Absolute repository and ephemeral skill-up install prefixes in case data were replaced with "
            "repository-relative Skill paths. raw_result_sha256 identifies the unmodified report."
        ),
        "cases": sanitized_cases,
        "archived_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    if status == "STALE":
        archive["stale_reason"] = manifest.get("stale_reason", "input fingerprint changed during run")
    output = output.resolve(strict=False)
    if output.is_relative_to(skill_dir):
        raise ValueError("--output must be outside the Skill package")
    if output.exists():
        raise ValueError("--output already exists; refusing to overwrite an archive")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return archive


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--skill-dir", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--locale", required=True, choices=("zh-CN", "en-US"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        archive = archive_run(args.manifest, args.skill_dir, args.repo_root, args.locale, args.output)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"{archive['summary']['overall_status']}: {args.output.resolve()}")
    return 0 if archive["summary"]["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
