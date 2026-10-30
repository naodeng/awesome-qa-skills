#!/usr/bin/env python3
"""Check phase-bound decisions; explanations still need human review."""
import os
import sys

def grade(expected):
    if os.environ.get("EVAL_EXIT_CODE", "0") != "0":
        raise ValueError("engine did not exit successfully")
    found = {key: [] for key in expected}
    for line in os.environ.get("EVAL_FINAL_MESSAGE", "").splitlines():
        if "|" not in line:
            continue
        cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].upper() in found:
            found[cells[0].upper()].append((cells[1], "|".join(cells[2:]).strip()))
    for phase, status in expected.items():
        rows = found[phase]
        if len(rows) != 1 or rows[0][0] != status or not rows[0][1]:
            raise ValueError(f"{phase}: expected one {status} row with evidence; got {rows}")


EXPECTED = {'RED': 'NOT_EXECUTED', 'GREEN': 'NOT_EXECUTED', 'REFACTOR': 'NOT_EXECUTED', 'MUTATION': 'EXECUTED'}
try:
    grade(EXPECTED)
except ValueError as error:
    print(error, file=sys.stderr)
    raise SystemExit(1)
print("Phase-bound decisions passed; explanation requires human review")
