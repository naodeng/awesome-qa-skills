#!/usr/bin/env python3
"""Grade a captured Skill JSONL trace with local deterministic rules."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Sequence

try:
    from .skill_eval_rules import evaluate_trace, load_jsonl
except ImportError:  # pragma: no cover - supports direct script execution
    from skill_eval_rules import evaluate_trace, load_jsonl


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", required=True, type=Path, help="JSONL trace captured with codex exec --json")
    parser.add_argument("--config", required=True, type=Path, help="JSON rule configuration")
    parser.add_argument("--project-dir", required=True, type=Path, help="Project directory containing captured artifacts")
    parser.add_argument("--report", type=Path, help="Optional path for the JSON report")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            raise ValueError("rule config must be a JSON object")
        trace = load_jsonl(args.trace)
        report = evaluate_trace(trace, config, args.project_dir)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"skill trace grading failed: {exc}", file=sys.stderr)
        return 1

    payload = report.to_dict()
    payload["trace"] = str(args.trace)
    payload["project_dir"] = str(args.project_dir)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
