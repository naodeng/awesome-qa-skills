---
name: testcase-writer-plus
description: Parse requirement and analysis files, then generate high-quality test cases.
---

# testcase-writer-plus (EN)

## Use Cases

Use after requirement review to quickly produce a first test-case set with consistent fields.

## Objective

Parse requirement and analysis files, then generate high-quality test cases.

## Input

- Required: requirement file + analysis file
- Supported: Word/HTML/JSON/Markdown/Excel

## Output

- Output: test cases (Markdown default, Word/JSON/Excel available)

## Prerequisites

- Install Python 3
- Prepare requirement and analysis files
- Default output format is Markdown

## Quick Start

```bash
python3 scripts/run_writer.py --requirement examples/requirement-sample.md --analysis examples/analysis-sample.md --output-format markdown --output examples/requirement-sample.testcases.md
```

## Validation Checklist

- Output file is created
- Cases include title, priority, type, precondition, steps, data, expected result

## Common Issues

- If format is wrong, check `--output-format`
- If case count is low, add more explicit rules in input documents

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
