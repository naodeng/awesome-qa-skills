#!/usr/bin/env python3
"""Create an explicit candidate regression case without changing a Skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Sequence


CASE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


def _yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _block_scalar(value: str) -> str:
    if "\x00" in value:
        raise ValueError("prompt must not contain a NUL character")
    lines = value.splitlines() or [""]
    return "\n".join(f"    {line}" for line in lines)


def write_case(
    *,
    skill_root: Path,
    case_id: str,
    title: str,
    description: str,
    prompt: str,
    must_contain: Sequence[str],
    must_not_contain: Sequence[str],
) -> Path:
    if not CASE_ID_RE.fullmatch(case_id):
        raise ValueError(f"unsafe case id: {case_id!r}")
    if not title.strip() or not description.strip() or not prompt.strip():
        raise ValueError("title, description, and prompt are required")
    if not must_contain:
        raise ValueError("at least one must-contain assertion is required")

    skill_root = skill_root.resolve()
    cases_dir = skill_root / "evals" / "cases"
    if not cases_dir.is_dir():
        raise FileNotFoundError(f"Skill eval cases directory is missing: {cases_dir}")
    output = cases_dir / f"{case_id}.yaml"
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing regression case: {output}")

    lines = [
        f"id: {case_id}",
        f"title: {_yaml_scalar(title)}",
        f"description: {_yaml_scalar(description)}",
        "metadata:",
        "  category: REGRESSION",
        "  lifecycle: CANDIDATE",
        "  evidence_state: NOT_RUN",
        "input:",
        "  prompt: |",
        _block_scalar(prompt),
        "expect:",
        "  must_contain:",
    ]
    lines.extend(f"    - {_yaml_scalar(value)}" for value in must_contain)
    if must_not_contain:
        lines.append("  must_not_contain:")
        lines.extend(f"    - {_yaml_scalar(value)}" for value in must_not_contain)
    lines.extend(
        [
            "judge:",
            "  type: rule_based",
            "  success:",
            "    - output_contains:",
            "        all:",
        ]
    )
    lines.extend(f"          - {_yaml_scalar(value)}" for value in must_contain)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", required=True, type=Path)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--must-contain", required=True, nargs="+")
    parser.add_argument("--must-not-contain", nargs="*", default=[])
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = write_case(
        skill_root=args.skill_root,
        case_id=args.case_id,
        title=args.title,
        description=args.description,
        prompt=args.prompt,
        must_contain=args.must_contain,
        must_not_contain=args.must_not_contain,
    )
    print(f"created={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
