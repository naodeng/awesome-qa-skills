#!/usr/bin/env python3
"""Check the routed canonical ID; review the explanation separately."""
import os
import sys

rows = []
for line in os.environ.get("EVAL_FINAL_MESSAGE", "").splitlines():
    cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
    if len(cells) >= 3 and cells[0] == "ROUTE":
        rows.append((cells[1], cells[2]))
if os.environ.get("EVAL_EXIT_CODE", "0") != "0" or len(rows) != 1 or rows[0][0] != "tdd-quality-workflow" or not rows[0][1]:
    print(f"Expected one sourced tdd-quality-workflow route, got {rows}", file=sys.stderr)
    raise SystemExit(1)
print("Exact router target passed; review availability and explanation separately")
