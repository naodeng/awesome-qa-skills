---
name: test-case-reviewer-plus
description: Review test cases using requirement, strategy, and supporting documents, then output structured findings.
---

# test-case-reviewer-plus (EN)

## Use Cases

Use before handoff/release to identify missing coverage and prioritize fixes.

## Objective

Review test cases using requirement, strategy, and supporting documents, then output structured findings.

## Input

- Required: requirement file + test case file
- Optional: analysis/technical/plan/strategy/other files

## Output

- Output: review result (Markdown default, Word/JSON/Excel available)

## Prerequisites

- Install Python 3
- Prepare current test case document
- Add strategy document for stronger review context

## Quick Start

```bash
python3 scripts/run_review.py --requirement examples/requirement-sample.md --testcase examples/testcase-sample.md --analysis examples/analysis-sample.md --tech examples/tech-sample.md --plan examples/plan-sample.md --strategy examples/strategy-sample.md --output-format markdown --output examples/testcase-sample.review.md
```

## Validation Checklist

- Review output is created
- Includes conclusion, P0/P1 findings, missing scenarios, and action plan

## Common Issues

- If findings are weak, improve input quality and completeness
- If priority split is missing, include stronger risk context

## Folder Notes

- `prompts/`: prompt content
- `scripts/`: parser/generator/runner scripts
- `examples/`: sample input/output files
- `output-templates/`: output templates when present
- `references/`: scope and framework references when present

## Independence Statement

- This skill can be used independently from other folders.
- Required files are contained in the current skill directory.
- Documentation and examples are self-contained.

## Review Metadata

- Last Verified: 2026-03-23
- Skill Doc Version: 1.1.0
