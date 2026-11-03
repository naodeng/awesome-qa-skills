#!/usr/bin/env python3
"""Require stale checkpoint status and a recovery action for affected stages."""
from __future__ import annotations

import os
import re
import sys


STALE_STATUS = re.compile(r"\bSTALE\b", re.IGNORECASE)
STAGE_MARKER = re.compile(r"(?:阶段|\bstages?\b)", re.IGNORECASE)
RECOVERY_ACTION = re.compile(
    r"(?:重跑|重审|重新(?:审查|复核|检查|执行|分析|读取|固定)|"
    r"\bre-?run\b|\bre-?review\b|\breassess(?:ment)?\b|"
    r"\brecheck\b|\bre-?evaluate\b|\bre-?execute\b|\breview again\b)",
    re.IGNORECASE,
)


def grade(text: str, exit_code: object) -> None:
    if str(exit_code) != "0":
        raise ValueError("engine did not exit successfully")
    if not STALE_STATUS.search(text):
        raise ValueError("STALE checkpoint status is missing")
    if not STAGE_MARKER.search(text):
        raise ValueError("affected workflow stages are missing")
    if not RECOVERY_ACTION.search(text):
        raise ValueError("stage re-review or rerun action is missing")


if __name__ == "__main__":
    try:
        grade(os.environ.get("EVAL_FINAL_MESSAGE", ""), os.environ.get("EVAL_EXIT_CODE", ""))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print("Stale checkpoint status and affected-stage recovery action passed")
