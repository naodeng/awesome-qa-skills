---
name: requirements-analysis-plus
description: Parse Word/HTML/JSON/Markdown/Excel requirement files and produce a structured analysis conclusion.
---

# requirements-analysis-plus (EN)

## Use Cases

Use before test design to identify key rules, risks, and open questions from requirement files.

## Objective

Parse Word/HTML/JSON/Markdown/Excel requirement files and produce a structured analysis conclusion.

## Input

- Required: requirement file (Word/HTML/JSON/Markdown/Excel)
- Optional: explicit input format

## Output

- Output: requirement analysis conclusion (Markdown by default)

## Prerequisites

- Install Python 3
- Prepare a requirement document
- Start with `examples/` for a first run

## Quick Start

```bash
python3 scripts/run_analysis.py --input examples/requirements-sample.md --output examples/requirements-sample.analysis.md
```

## Validation Checklist

- Output file is created
- Includes summary, functional points, non-functional points, ambiguities, and test focus

## Common Issues

- If parsing fails, verify file extension and content format
- If output is too short, check input document quality and completeness

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
