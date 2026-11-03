#!/usr/bin/env python3
"""Check that an underspecified request gets useful written questions."""
from __future__ import annotations

import os
import re
import sys


FEATURE = re.compile(r"\bfeature\b", re.IGNORECASE)
SCOPE = re.compile(
    r"\b(?:scope|repository|repo|pr|url|module|project|app|page|behaviors?|behaviours?|user journeys?|user flows?|scenarios?|area|boundary)\b",
    re.IGNORECASE,
)
PHASE = re.compile(r"\b(?:phase|stage|design|development|implementation|deployed|release)\b", re.IGNORECASE)
DELIVERABLE = re.compile(r"\b(?:deliver\w*|test cases?|test strategy|test plan|test type|testing|run checks?|execution|report)\b", re.IGNORECASE)
PREMATURE_ROUTE = re.compile(r"\bprimary\s+(?:recommendation|skill)\b|\bprimary:\s*`?[a-z][a-z0-9-]+", re.IGNORECASE)


def grade(text: str, exit_code: object) -> None:
    if str(exit_code) != "0":
        raise ValueError("engine did not exit successfully")
    checks = (FEATURE, SCOPE, PHASE, DELIVERABLE)
    missing = [pattern.pattern for pattern in checks if not pattern.search(text)]
    if missing:
        raise ValueError("clarification is missing feature, scope, phase, or deliverable questions")
    if PREMATURE_ROUTE.search(text):
        raise ValueError("selected a route before clarifying the underspecified goal")


if __name__ == "__main__":
    try:
        grade(os.environ.get("EVAL_FINAL_MESSAGE", ""), os.environ.get("EVAL_EXIT_CODE", ""))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print("Feature, scope, phase, and deliverable questions passed")
