#!/usr/bin/env python3
"""Validate the repository-level Skill Evaluation Quality Loop contract.

This validator checks only local declarations and package structure.  It does
not run a model, a Skill, a target application, or a judge.
"""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_DOCUMENTS = (
    "docs/governance/SKILL_EVALUATION_DESIGN.md",
    "docs/governance/SKILL_EVALUATION_DESIGN_EN.md",
    "docs/governance/SKILL_EVALUATION_CONTRACT.md",
    "docs/governance/SKILL_EVALUATION_CONTRACT_EN.md",
    "docs/governance/SKILL_EVALUATION_PILOTS.md",
    "docs/governance/SKILL_EVALUATION_PILOTS_EN.md",
)
REQUIRED_STATUS_MARKERS = (
    "PASS",
    "FAIL",
    "BLOCKED",
    "NOT_RUN",
    "NOT_SCORED",
    "UNASSESSED",
    "INSUFFICIENT_EVIDENCE",
)
REQUIRED_PILOTS = ("requirements-analysis", "ui-test-playwright")
META_SKILLS = ("skill-quality-review", "skill-evaluation")
LANGUAGES = ("zh", "en")
REQUIRED_PACKAGE_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "evals/eval.yaml",
)


def _text(root: Path, relative: str) -> str:
    path = root / relative
    return path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""


def validate(root: Path) -> list[str]:
    """Return actionable findings for the local design and package contract."""

    root = root.resolve()
    findings: list[str] = []
    for relative in REQUIRED_DOCUMENTS:
        if not (root / relative).is_file():
            findings.append(f"missing required evaluation document: {relative}")

    contract_text = "\n".join(
        _text(root, relative)
        for relative in REQUIRED_DOCUMENTS
        if "CONTRACT" in relative
    )
    for marker in REQUIRED_STATUS_MARKERS:
        if marker not in contract_text:
            findings.append(f"evaluation contract is missing status marker: {marker}")

    design_text = "\n".join(
        _text(root, relative)
        for relative in REQUIRED_DOCUMENTS
        if "DESIGN" in relative
    )
    for marker in ("skill-up", "skill-evaluation", "Regression", "Definition of Done"):
        if marker not in design_text:
            findings.append(f"evaluation design is missing marker: {marker}")

    pilot_text = "\n".join(
        _text(root, relative)
        for relative in REQUIRED_DOCUMENTS
        if "PILOTS" in relative
    )
    for pilot in REQUIRED_PILOTS:
        if pilot not in pilot_text:
            findings.append(f"evaluation pilot record is missing: {pilot}")
    for marker in ("NOT_RUN", "agent_judge", "script"):
        if marker not in pilot_text:
            findings.append(f"evaluation pilot record is missing marker: {marker}")

    for language in LANGUAGES:
        for skill in META_SKILLS:
            package = root / "skills" / language / "skill-engineering" / skill
            for relative in REQUIRED_PACKAGE_FILES:
                if not (package / relative).is_file():
                    findings.append(
                        f"missing {language} {skill} package file: "
                        f"{(package / relative).relative_to(root)}"
                    )
            cases = package / "evals" / "cases"
            case_files = sorted(cases.glob("*.yaml")) if cases.is_dir() else []
            if len(case_files) < 3:
                findings.append(
                    f"{language} {skill} needs at least three eval cases; found {len(case_files)}"
                )

    return sorted(findings)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    findings = validate(Path(args.repo_root))
    for finding in findings:
        print(f"- {finding}")
    print(f"skill_evaluation_contract_findings={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
