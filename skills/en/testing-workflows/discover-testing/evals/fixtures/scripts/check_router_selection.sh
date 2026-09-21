#!/usr/bin/env bash
# Structured selection script judge for the discover-testing Router Pilot.
set -euo pipefail

text="${EVAL_FINAL_MESSAGE:-}"
if [[ -z "$text" && -n "${EVAL_TRANSCRIPT_PATH:-}" && -f "$EVAL_TRANSCRIPT_PATH" ]]; then
  text="$(cat "$EVAL_TRANSCRIPT_PATH")"
fi
if [[ -z "$text" && -f "outputs/response.md" ]]; then
  text="$(cat outputs/response.md)"
fi
if [[ -z "$text" ]]; then
  echo "FAIL: no final response was provided" >&2
  exit 1
fi
if [[ "${EVAL_EXIT_CODE:-0}" != "0" ]]; then
  echo "FAIL: the Skill run exited with ${EVAL_EXIT_CODE}" >&2
  exit 1
fi

expected_path="${EVAL_ROUTER_EXPECTED_PATH:-evals/fixtures/router-expected.json}"
if [[ ! -f "$expected_path" ]]; then
  echo "FAIL: missing router expectation file: $expected_path" >&2
  exit 1
fi

export EVAL_ROUTER_TEXT="$text"
python3 - "$expected_path" <<'PY'
from pathlib import Path
import json
import os
import re
import sys

expected = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
text = os.environ.get("EVAL_ROUTER_TEXT", "")
blocks = re.findall(r"```json\s*\r?\n(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
if len(blocks) != 1:
    print("FAIL: expected exactly one fenced JSON selection block", file=sys.stderr)
    raise SystemExit(1)

try:
    payload = json.loads(blocks[0])
except json.JSONDecodeError as error:
    print(f"FAIL: invalid JSON selection block: {error}", file=sys.stderr)
    raise SystemExit(1)

required = {"route", "primary", "optional"}
if not isinstance(expected, dict) or set(expected) != required:
    print("FAIL: router expectation must contain exactly route, primary, optional", file=sys.stderr)
    raise SystemExit(1)
if not isinstance(payload, dict) or set(payload) != required:
    print("FAIL: selection must contain exactly route, primary, optional", file=sys.stderr)
    raise SystemExit(1)
if not isinstance(payload["route"], str) or not isinstance(payload["primary"], str):
    print("FAIL: route and primary must be strings", file=sys.stderr)
    raise SystemExit(1)
if payload["optional"] is not None and not isinstance(payload["optional"], str):
    print("FAIL: optional must be a string or null", file=sys.stderr)
    raise SystemExit(1)
if payload != expected:
    print(f"FAIL: expected {expected}, observed {payload}", file=sys.stderr)
    raise SystemExit(1)

print(f"PASS: exact route selection {payload}")
PY
