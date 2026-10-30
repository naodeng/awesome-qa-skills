#!/usr/bin/env python3
"""Check the new-feature route; the declared helper is optional."""
import json
import os
import re
import sys

if os.environ.get("EVAL_EXIT_CODE", "0") != "0":
    raise SystemExit("Agent did not exit successfully")
text = os.environ.get("EVAL_FINAL_MESSAGE", "")
blocks = re.findall(r"```json\s*\r?\n(.*?)```", text, re.IGNORECASE | re.DOTALL)
if len(blocks) != 1:
    raise SystemExit("Expected one JSON route selection")
try:
    result = json.loads(blocks[0])
except json.JSONDecodeError as error:
    raise SystemExit(f"Invalid JSON route selection: {error}")
if not isinstance(result, dict) or set(result) != {"route", "primary", "optional"}:
    raise SystemExit("Expected route, primary, and optional fields only")
if result["route"] != "new-feature-quality" or result["primary"] != "requirements-analysis":
    raise SystemExit(f"Incorrect route or primary Skill: {result}")
if result["optional"] not in (None, "test-strategy"):
    raise SystemExit(f"Unexpected optional Skill: {result['optional']}")
print("Exact route and allowed optional choice passed; explanation requires human review")
