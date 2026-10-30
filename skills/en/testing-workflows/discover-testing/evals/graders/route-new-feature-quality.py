#!/usr/bin/env python3
"""Check the selected route and the required rationale and handoff content."""
import json
import os
import re


def fail(message):
    raise SystemExit(message)


if os.environ.get("EVAL_EXIT_CODE", "0") != "0":
    fail("Agent did not exit successfully")
text = os.environ.get("EVAL_FINAL_MESSAGE", "")
blocks = re.findall(r"```json\s*\r?\n(.*?)```", text, re.IGNORECASE | re.DOTALL)
if len(blocks) != 1:
    fail("Expected one JSON route selection")
try:
    result = json.loads(blocks[0])
except json.JSONDecodeError as error:
    fail(f"Invalid JSON route selection: {error}")
if not isinstance(result, dict) or set(result) != {"route", "primary", "optional"}:
    fail("Expected route, primary, and optional fields only")
if result["route"] != "new-feature-quality" or result["primary"] != "requirements-analysis":
    fail(f"Incorrect route or primary Skill: {result}")
if result["optional"] not in (None, "test-strategy"):
    fail(f"Unexpected optional Skill: {result['optional']}")

fields = {"GOAL": [], "RATIONALE": [], "HANDOFF": []}
for line in text.splitlines():
    cells = [cell.strip().strip("`* ") for cell in line.strip().strip("|").split("|")]
    if len(cells) >= 2 and cells[0].upper() in fields:
        fields[cells[0].upper()].append("|".join(cells[1:]).strip())
if any(len(values) != 1 or not values[0] for values in fields.values()):
    fail(f"Expected one nonempty GOAL, RATIONALE, and HANDOFF line; got {fields}")
goal, rationale, handoff = (fields[name][0].casefold() for name in ("GOAL", "RATIONALE", "HANDOFF"))
if "membership" not in goal or "point" not in goal:
    fail("GOAL must identify the membership-points feature")
if "draft" not in rationale or "acceptance" not in rationale or "requirements" not in rationale:
    fail("RATIONALE must connect the incomplete draft and acceptance criteria to requirements analysis")
if "acceptance" not in handoff or "risk" not in handoff:
    fail("HANDOFF must include acceptance conditions and major risks")
if re.search(r"\bTODO\b|\bI cannot provide (?:the )?(?:goal|rationale|next|handoff)", text, re.IGNORECASE):
    fail("GOAL, RATIONALE, and HANDOFF must contain usable content, not a placeholder")
print("Exact route, goal, rationale, and handoff passed; human review still applies")
