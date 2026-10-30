#!/usr/bin/env python3
"""Shared evidence checks for this standalone Skill's phase evals."""
from __future__ import annotations

import os
import re


def _rows(message: str, expected: dict[str, str]) -> dict[str, list[tuple[str, str]]]:
    found = {phase: [] for phase in expected}
    for line in message.splitlines():
        if "|" not in line:
            continue
        cells = [cell.strip().strip("`* ") for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].upper() in found:
            found[cells[0].upper()].append((cells[1].upper(), "|".join(cells[2:]).strip()))
    return found


def _has_all_evidence(evidence: str, groups: tuple[tuple[str, ...], ...]) -> bool:
    folded = evidence.casefold().replace("`", "").replace("*", "")
    return all(any(candidate.casefold() in folded for candidate in group) for group in groups)


def _contains_positive_pass_claim(text: str) -> bool:
    unquoted = re.sub(r"“[^”]*”|「[^」]*」|\"[^\"]*\"|'[^']*'|`[^`]*`", " ", text)
    patterns = (
        re.compile(r"\b(?:(?:all|every)\s+(?:(?:of\s+)?the\s+)?)?(?:tests?|quality gates?)\s+(?:have\s+)?passed\b", re.IGNORECASE),
        re.compile(r"所有(?:测试|质量门禁|门禁)(?:都|均)?(?:已|已经)?通过"),
    )
    negation = re.compile(r"\b(?:no|not|never|without|cannot|can't|did not|didn't|don't)\b(?:\s+\w+){0,3}\s*$", re.IGNORECASE)
    chinese_negation = re.compile(r"(?:未|没有|并未|不|不能|无法).{0,12}$")
    for pattern in patterns:
        for match in pattern.finditer(unquoted):
            prefix = unquoted[max(0, match.start() - 45):match.start()]
            if not negation.search(prefix) and not chinese_negation.search(prefix):
                return True
    return False


def _contradicts_status(status: str, evidence: str) -> bool:
    if status == "NOT_EXECUTED":
        return _contains_positive_pass_claim(evidence)
    if status.startswith("VERIFIED_") or status == "EXECUTED":
        return bool(re.search(
            r"(?:test|tests|pytest|regression|mutation tests?).{0,40}"
            r"(?:never ran|never executed|not run|not executed|did not run|was not run|not rerun)|"
            r"(?:测试|回归|变异测试).{0,30}(?:未执行|没有执行|未运行|没有运行|未重跑)",
            evidence,
            re.IGNORECASE,
        ))
    return False


def grade(
    expected: dict[str, str],
    required_evidence: dict[str, tuple[tuple[str, ...], ...]] | None = None,
) -> None:
    if os.environ.get("EVAL_EXIT_CODE", "0") != "0":
        raise ValueError("engine did not exit successfully")
    found = _rows(os.environ.get("EVAL_FINAL_MESSAGE", ""), expected)
    required_evidence = required_evidence or {}
    for phase, status in expected.items():
        rows = found[phase]
        if len(rows) != 1 or rows[0][0] != status or not rows[0][1]:
            raise ValueError(f"{phase}: expected one {status} row with evidence; got {rows}")
        evidence = rows[0][1]
        if _contradicts_status(status, evidence):
            raise ValueError(f"{phase}: evidence conflicts with {status}: {evidence}")
        groups = required_evidence.get(phase, ())
        if groups and not _has_all_evidence(evidence, groups):
            missing = [
                " or ".join(group)
                for group in groups
                if not any(candidate.casefold() in evidence.casefold() for candidate in group)
            ]
            raise ValueError(f"{phase}: verified evidence is missing required artifact details: {missing}")


def reject_blanket_pass_claim(message: str) -> None:
    """Reject direct blanket pass assertions without treating quoted text as a claim."""
    unquoted = re.sub(r"“[^”]*”|「[^」]*」|\"[^\"]*\"|'[^']*'|`[^`]*`", " ", message)
    patterns = (
        r"\ball\s+(?:of\s+the\s+)?tests?\s+(?:have\s+)?passed\b",
        r"\ball\s+(?:of\s+the\s+)?quality gates?\s+(?:have\s+)?passed\b",
        r"所有测试(?:都|均)?(?:已|已经)?通过",
        r"所有质量门禁(?:都|均)?(?:已|已经)?通过",
    )
    if any(re.search(pattern, unquoted, re.IGNORECASE) for pattern in patterns):
        raise ValueError("blanket pass claim conflicts with the non-executed phase evidence")

EXPECTED = {'RED': 'INCONCLUSIVE', 'GREEN': 'INCONCLUSIVE', 'REFACTOR': 'NOT_EXECUTED', 'MUTATION': 'NOT_EXECUTED'}
REQUIRED_EVIDENCE = {'RED': (('log', '日志'), ('record', '记录'), ('revision', '版本')), 'GREEN': (('log', '日志'), ('record', '记录'), ('revision', '版本'))}

try:
    grade(EXPECTED, REQUIRED_EVIDENCE)
except ValueError as error:
    raise SystemExit(str(error))

print("Phase evidence contract passed; full explanation still needs human review")
