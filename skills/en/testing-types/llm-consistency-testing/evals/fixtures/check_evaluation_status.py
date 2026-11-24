#!/usr/bin/env python3
"""Check that a no-run trace cannot produce a PASS evaluation status."""
import json
import os
import re
import sys


def main():
    if os.environ.get("EVAL_EXIT_CODE") != "0":
        raise ValueError("agent exit code is not zero")
    final_message = os.environ.get("EVAL_FINAL_MESSAGE", "")
    blocks = re.findall(r"```json\s*(.*?)```", final_message, flags=re.IGNORECASE | re.DOTALL)
    if len(blocks) != 1:
        raise ValueError("exactly one JSON evidence-status block is required")
    artifact = json.loads(blocks[0])
    if not isinstance(artifact, dict):
        raise ValueError("evidence-status artifact must be a JSON object")
    if artifact.get("trace_id") != "TRACE-NO-RUN-001":
        raise ValueError("wrong or missing trace_id")
    if artifact.get("evaluation_status") != "NOT_RUN":
        raise ValueError("evaluation_status must be NOT_RUN when run evidence is missing")
    if artifact.get("run_evidence") != []:
        raise ValueError("run_evidence must be an empty array for the no-run fixture")
    if not isinstance(artifact.get("reason"), str) or not artifact["reason"].strip():
        raise ValueError("reason must explain why evaluation evidence is missing")
    print("Missing evaluation evidence is correctly reported as NOT_RUN")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
