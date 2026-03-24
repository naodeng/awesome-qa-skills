---
name: test-strategy-plus
description: Generate a structured test strategy from requirement, analysis, technical, and plan documents.
---

# test-strategy-plus (EN)

## Use Cases

Use at sprint/release planning to create actionable strategy and quality gates.

## Objective

Generate a structured test strategy from requirement, analysis, technical, and plan documents.

## Input

- Required: requirement file
- Optional: analysis/technical/plan/other files

## Output

- Output: test strategy (Markdown default, Word/JSON/Excel available)

## Prerequisites

- Install Python 3
- Prepare at least the requirement file
- Add technical and plan docs for better coverage

## Quick Start

```bash
python3 scripts/run_strategy.py --requirement examples/requirement-sample.md --analysis examples/analysis-sample.md --tech examples/tech-sample.md --plan examples/plan-sample.md --output-format markdown --output examples/requirement-sample.strategy.md
```

## Validation Checklist

- Strategy file is created
- Includes scope, methods, gates, risks, and milestones

## Common Issues

- If output is too generic, provide richer technical/project inputs
- If output format is wrong, verify `--output-format`

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

- Last Verified: 2026-03-24
- Skill Doc Version: 1.1.0
