#!/usr/bin/env python3
"""Run a prompt CSV through Codex and grade each captured JSONL trace locally."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
from typing import Any, Sequence

try:
    from .skill_eval_rules import EvalReport, TRIGGER_MODES, evaluate_trace, load_jsonl
    from .skill_eval_evidence import (
        build_run_metadata,
        evidence_state,
        failure_classification,
        summary_counts,
    )
except ImportError:  # pragma: no cover - supports direct script execution
    from skill_eval_rules import EvalReport, TRIGGER_MODES, evaluate_trace, load_jsonl
    from skill_eval_evidence import build_run_metadata, evidence_state, failure_classification, summary_counts


CASE_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


@dataclass(frozen=True)
class PromptCase:
    case_id: str
    should_trigger: bool
    prompt: str
    mode: str


@dataclass
class BatchReport:
    cases: list[dict[str, Any]]
    run_metadata: dict[str, str]

    @property
    def exit_code(self) -> int:
        exit_codes = [int(case.get("exit_code", 0)) for case in self.cases]
        if 1 in exit_codes:
            return 1
        if 2 in exit_codes:
            return 2
        return 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "exit_code": self.exit_code,
            "case_count": len(self.cases),
            "run_metadata": self.run_metadata,
            "summary": summary_counts(case.get("evidence_state", "INSUFFICIENT_EVIDENCE") for case in self.cases),
            "cases": self.cases,
        }


def _parse_bool(value: str, field_name: str, case_id: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise ValueError(f"{field_name} must be boolean for case {case_id!r}")


def load_prompt_cases(path: Path) -> list[PromptCase]:
    """Load the trigger prompt CSV with one explicit mode per case."""

    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"id", "should_trigger", "prompt"}
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(required - fieldnames)
        if missing:
            raise ValueError(f"prompt CSV missing columns: {', '.join(missing)}")
        if not {"mode", "trigger_mode"}.intersection(fieldnames):
            raise ValueError("prompt CSV missing columns: mode or trigger_mode")
        cases: list[PromptCase] = []
        seen: set[str] = set()
        for row_number, row in enumerate(reader, 2):
            case_id = (row.get("id") or "").strip()
            if not case_id:
                raise ValueError(f"empty case id on CSV row {row_number}")
            if not CASE_ID_PATTERN.fullmatch(case_id):
                raise ValueError(f"unsafe case id: {case_id!r}")
            if case_id in seen:
                raise ValueError(f"duplicate case id: {case_id}")
            seen.add(case_id)
            prompt = (row.get("prompt") or "").strip()
            if not prompt:
                raise ValueError(f"empty prompt for case {case_id!r}")
            mode = (row.get("mode") or row.get("trigger_mode") or "").strip() or None
            if mode is None:
                raise ValueError(f"mode is required for case {case_id!r}")
            if mode not in TRIGGER_MODES:
                allowed = ", ".join(sorted(TRIGGER_MODES))
                raise ValueError(f"invalid trigger mode {mode!r} for case {case_id!r}; expected one of {allowed}")
            cases.append(
                PromptCase(
                    case_id=case_id,
                    should_trigger=_parse_bool(row.get("should_trigger") or "", "should_trigger", case_id),
                    prompt=prompt,
                    mode=mode,
                )
            )
    if not cases:
        raise ValueError("prompt CSV contains no cases")
    return cases


def build_codex_command(prompt: str, approve_for_me: bool = False, codex_bin: str = "codex") -> list[str]:
    command = [codex_bin, "exec", "--json", "--skip-git-repo-check"]
    if approve_for_me:
        command.append("--approve-for-me")
    command.append(prompt)
    return command


def _load_config(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("rule config must be a JSON object")
    return value


def _case_config(base: dict[str, Any], case: PromptCase) -> dict[str, Any]:
    config = dict(base)
    if case.mode:
        config["trigger_mode"] = case.mode
    config["should_trigger"] = case.should_trigger
    return config


def _case_paths(output_root: Path, case_id: str) -> tuple[Path, Path, Path]:
    return (
        output_root / f"{case_id}.jsonl",
        output_root / f"{case_id}.stderr.log",
        output_root / f"{case_id}.rules.json",
    )


def _dry_case(
    case: PromptCase,
    project_root: Path,
    approve_for_me: bool,
    codex_bin: str,
    metadata: dict[str, str],
) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "should_trigger": case.should_trigger,
        "mode": case.mode,
        "project_dir": str(project_root / case.case_id),
        "command": build_codex_command(case.prompt, approve_for_me=approve_for_me, codex_bin=codex_bin),
        "shell_command": shlex.join(build_codex_command(case.prompt, approve_for_me=approve_for_me, codex_bin=codex_bin)),
        "dry_run": True,
        "exit_code": 0,
        "evidence_state": "NOT_RUN",
        "failure_classification": None,
        "run_metadata": metadata,
    }


def run_cases(
    prompts_path: Path,
    config_path: Path,
    project_root: Path,
    output_root: Path,
    *,
    approve_for_me: bool = False,
    dry_run: bool = True,
    codex_bin: str = "codex",
    skill_root: Path | None = None,
    engine: str = "codex",
    provider: str | None = None,
    requested_model: str | None = None,
    environment: str = "none",
    judge_type: str | None = None,
    judge_model: str | None = None,
    failure_classification_name: str | None = None,
    run_id: str | None = None,
    variant: str = "default",
) -> BatchReport:
    """Run or preview isolated cases; the default is preview-only."""

    cases = load_prompt_cases(prompts_path)
    base_config = _load_config(config_path)
    metadata = build_run_metadata(
        skill_root=(skill_root or prompts_path.parent),
        eval_paths=[prompts_path, config_path],
        engine=engine,
        requested_model=requested_model,
        provider=provider,
        environment=environment,
        run_id=run_id,
        case_id=None,
        variant=variant,
        judge_type=judge_type or str(base_config.get("judge_type", "rule_based")),
        judge_model=judge_model,
    )
    if dry_run:
        return BatchReport(
            [
                _dry_case(
                    case,
                    project_root,
                    approve_for_me,
                    codex_bin,
                    metadata.for_case(case.case_id).to_dict(),
                )
                for case in cases
            ],
            metadata.to_dict(),
        )

    project_root.mkdir(parents=True, exist_ok=True)
    output_root.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    for case in cases:
        case_dir = project_root / case.case_id
        if case_dir.exists():
            raise ValueError(f"case directory already exists; refusing to reuse it: {case_dir}")
        case_dir.mkdir()
        trace_path, stderr_path, report_path = _case_paths(output_root, case.case_id)
        command = build_codex_command(case.prompt, approve_for_me=approve_for_me, codex_bin=codex_bin)
        completed = subprocess.run(
            command,
            cwd=str(case_dir),
            capture_output=True,
            text=True,
            check=False,
        )
        trace_path.write_text(completed.stdout or "", encoding="utf-8")
        stderr_path.write_text(completed.stderr or "", encoding="utf-8")
        trace = load_jsonl(trace_path)
        eval_report: EvalReport = evaluate_trace(trace, _case_config(base_config, case), case_dir)
        case_exit_code = 1 if completed.returncode != 0 else eval_report.exit_code
        state = evidence_state(
            dry_run=False,
            runner_exit_code=completed.returncode,
            eval_exit_code=eval_report.exit_code,
            trace_event_count=len(trace.events),
            trace_error_count=len(trace.errors),
        )
        classification = failure_classification(
            state=state,
            trace_event_count=len(trace.events),
            requested=failure_classification_name,
            trace_error_count=len(trace.errors),
        )
        payload = eval_report.to_dict()
        payload.update(
            {
                "case_id": case.case_id,
                "should_trigger": case.should_trigger,
                "mode": case.mode,
                "prompt": case.prompt,
                "runner_exit_code": completed.returncode,
                "trace": str(trace_path),
                "stderr": str(stderr_path),
                "project_dir": str(case_dir),
                "exit_code": case_exit_code,
                "evidence_state": state,
                "failure_classification": classification,
                "trace_error_count": len(trace.errors),
                "trace_raw_line_count": trace.raw_line_count,
                "run_metadata": metadata.for_case(case.case_id).to_dict(),
            }
        )
        report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        results.append(payload)
    return BatchReport(results, metadata.to_dict())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompts", required=True, type=Path, help="CSV with id,should_trigger,prompt,mode")
    parser.add_argument("--config", required=True, type=Path, help="JSON rule configuration")
    parser.add_argument("--project-root", required=True, type=Path, help="Empty root for per-case project directories")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for JSONL, stderr, and rule reports")
    parser.add_argument("--run", action="store_true", help="Actually invoke codex; without this flag only preview the commands")
    parser.add_argument(
        "--approve-for-me",
        action="store_true",
        help="Pass the current Codex approval flag; only applies with --run",
    )
    parser.add_argument("--codex-bin", default="codex", help="Codex executable to invoke")
    parser.add_argument("--skill-root", type=Path, help="Skill root used for version metadata")
    parser.add_argument("--engine", default="codex", help="Engine name recorded in run metadata")
    parser.add_argument("--provider", help="Provider name recorded in run metadata")
    parser.add_argument("--model", dest="requested_model", help="Requested model recorded in run metadata")
    parser.add_argument("--environment", default="none", help="Evaluation environment recorded in run metadata")
    parser.add_argument("--judge-type", help="Judge type recorded in run metadata")
    parser.add_argument("--judge-model", help="Judge model recorded in run metadata")
    parser.add_argument(
        "--failure-classification",
        choices=("SKILL_DEFECT", "EVAL_DEFECT", "INFRASTRUCTURE_DEFECT", "UNKNOWN"),
        help="Explicit attribution for a failing case; omitted failures remain UNKNOWN",
    )
    parser.add_argument("--run-id", help="Stable run identifier; generated when omitted")
    parser.add_argument("--variant", default="default", help="Evaluation variant recorded in run metadata")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = run_cases(
            prompts_path=args.prompts,
            config_path=args.config,
            project_root=args.project_root,
            output_root=args.output_dir,
            approve_for_me=args.approve_for_me,
            dry_run=not args.run,
            codex_bin=args.codex_bin,
            skill_root=args.skill_root,
            engine=args.engine,
            provider=args.provider,
            requested_model=args.requested_model,
            environment=args.environment,
            judge_type=args.judge_type,
            judge_model=args.judge_model,
            failure_classification_name=args.failure_classification,
            run_id=args.run_id,
            variant=args.variant,
        )
    except (OSError, csv.Error, json.JSONDecodeError, ValueError) as exc:
        print(f"skill trace eval failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
