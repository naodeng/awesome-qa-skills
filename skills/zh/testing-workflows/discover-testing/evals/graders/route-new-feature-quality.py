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

fields = {"目标": [], "理由": [], "交接": []}
for line in text.splitlines():
    cells = [cell.strip().strip("`* ") for cell in line.strip().strip("|").split("|")]
    if len(cells) >= 2 and cells[0] in fields:
        fields[cells[0]].append("|".join(cells[1:]).strip())
if any(len(values) != 1 or not values[0] for values in fields.values()):
    fail(f"Expected one nonempty 目标、理由、交接 line; got {fields}")
goal, rationale, handoff = (fields[name][0] for name in ("目标", "理由", "交接"))
if "会员" not in goal or "积分" not in goal:
    fail("目标 must identify the 会员积分 feature")
if not all(term in rationale for term in ("需求", "草稿", "验收")):
    fail("理由 must connect the incomplete draft and acceptance criteria to requirements analysis")
if "验收" not in handoff or "风险" not in handoff:
    fail("交接 must include acceptance conditions and major risks")
if re.search(r"\bTODO\b|I cannot provide|无法提供(?:目标|理由|交接|下一步)|待补", text, re.IGNORECASE):
    fail("目标、理由和交接必须是可用内容，不能是占位符")
print("Exact route, 目标, 理由, and 交接 passed; human review still applies")
