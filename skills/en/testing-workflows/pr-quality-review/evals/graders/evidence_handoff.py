#!/usr/bin/env python3
"""Check that an English workflow handoff preserves evidence and its pending action."""
from __future__ import annotations

import os
import re
import sys


REQUIRED_SIGNALS = {
    "evidence ID": re.compile(r"\bE-91\b", re.IGNORECASE),
    "source path": re.compile(r"\bbilling/retry\.py\b", re.IGNORECASE),
    "duplicate-charge retry risk": re.compile(
        r"\bduplicate\b[^.!?\n]{0,48}\bcharges?\b|\bcharges?\b[^.!?\n]{0,48}\bduplicate\b",
        re.IGNORECASE,
    ),
    "retry scope": re.compile(r"\bretr(?:y|ies)\b", re.IGNORECASE),
    "inference status": re.compile(r"\binference\b|\binferred\b", re.IGNORECASE),
    "input SHA": re.compile(r"\babc123\b", re.IGNORECASE),
    "pending follow-up": re.compile(r"\b(?:pending\s+)?follow[- ]up\b", re.IGNORECASE),
    "payment sandbox": re.compile(r"\bpayment\s+sandbox\b", re.IGNORECASE),
    "same idempotency key": re.compile(r"\bsame\s+idempotency\s+key\b", re.IGNORECASE),
    "single-charge outcome": re.compile(
        r"\b(?:one|single|1)\s+charge\b|\bonly\s+(?:one|a\s+single)\s+charge\b",
        re.IGNORECASE,
    ),
}


def grade(text: str, exit_code: object) -> None:
    if str(exit_code) != "0":
        raise ValueError("engine did not exit successfully")
    missing = [name for name, marker in REQUIRED_SIGNALS.items() if not marker.search(text)]
    if missing:
        raise ValueError("handoff evidence or follow-up not preserved: " + ", ".join(missing))


if __name__ == "__main__":
    try:
        grade(os.environ.get("EVAL_FINAL_MESSAGE", ""), os.environ.get("EVAL_EXIT_CODE", ""))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print("Evidence handoff and pending action preserved")
