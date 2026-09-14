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
    from .skill_eval_rules import EvalReport, evaluate_trace, load_jsonl
except ImportError:  # pragma: no cover - supports direct script execution
    from skill_eval_rules import EvalReport, evaluate_trace, load_jsonl


CASE_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


@dataclass(frozen=True)
class PromptCase:
    case_id: str
    should_trigger: bool
    prompt: str
    mode: str | None = None


@dataclass
class BatchReport:
    cases: list[dict[str, Any]]

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
    """Load the small article-style ``id,should_trigger,prompt`` CSV."""

    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"id", "should_trigger", "prompt"}
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(required - fieldnames)
        if missing:
            raise ValueError(f"prompt CSV missing columns: {', '.join(missing)}")
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


def build_codex_command(prompt: str, full_auto: bool = False, codex_bin: str = "codex") -> list[str]:
    command = [codex_bin, "exec", "--json"]
    if full_auto:
        command.append("--full-auto")
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


def _dry_case(case: PromptCase, project_root: Path, full_auto: bool, codex_bin: str) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "should_trigger": case.should_trigger,
        "mode": case.mode,
        "project_dir": str(project_root / case.case_id),
        "command": build_codex_command(case.prompt, full_auto=full_auto, codex_bin=codex_bin),
        "shell_command": shlex.join(build_codex_command(case.prompt, full_auto=full_auto, codex_bin=codex_bin)),
        "dry_run": True,
        "exit_code": 0,
    }


def run_cases(
    prompts_path: Path,
    config_path: Path,
    project_root: Path,
    output_root: Path,
    *,
    full_auto: bool = False,
    dry_run: bool = True,
    codex_bin: str = "codex",
) -> BatchReport:
    """Run or preview isolated cases; the default is preview-only."""

    cases = load_prompt_cases(prompts_path)
    base_config = _load_config(config_path)
    if dry_run:
        return BatchReport([_dry_case(case, project_root, full_auto, codex_bin) for case in cases])

    project_root.mkdir(parents=True, exist_ok=True)
    output_root.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    for case in cases:
        case_dir = project_root / case.case_id
        if case_dir.exists():
            raise ValueError(f"case directory already exists; refusing to reuse it: {case_dir}")
        case_dir.mkdir()
        trace_path, stderr_path, report_path = _case_paths(output_root, case.case_id)
        command = build_codex_command(case.prompt, full_auto=full_auto, codex_bin=codex_bin)
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
            }
        )
        report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        results.append(payload)
    return BatchReport(results)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompts", required=True, type=Path, help="CSV with id,should_trigger,prompt[,mode]")
    parser.add_argument("--config", required=True, type=Path, help="JSON rule configuration")
    parser.add_argument("--project-root", required=True, type=Path, help="Empty root for per-case project directories")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for JSONL, stderr, and rule reports")
    parser.add_argument("--run", action="store_true", help="Actually invoke codex; without this flag only preview the commands")
    parser.add_argument("--full-auto", action="store_true", help="Pass --full-auto to codex; only applies with --run")
    parser.add_argument("--codex-bin", default="codex", help="Codex executable to invoke")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = run_cases(
            prompts_path=args.prompts,
            config_path=args.config,
            project_root=args.project_root,
            output_root=args.output_dir,
            full_auto=args.full_auto,
            dry_run=not args.run,
            codex_bin=args.codex_bin,
        )
    except (OSError, csv.Error, json.JSONDecodeError, ValueError) as exc:
        print(f"skill trace eval failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
