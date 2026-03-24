---
name: api-test-pytest
description: Parse multi-format API definitions and generate executable Pytest API tests.
---

# api-test-pytest (EN)

## Use Cases

Use in Python QA stacks to quickly bootstrap API regression tests.

## Objective

Parse multi-format API definitions and generate executable Pytest API tests.

## Input

- Supported: curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## Output

- Output: normalized API data + Pytest test file

## Prerequisites

- Install Python 3
- Install pytest and requests dependencies
- Run first with `examples/`

## Quick Start

```bash
bash scripts/run.sh examples
```

## Validation Checklist

- Pytest test file is generated
- Tests run when dependencies are installed

## Common Issues

- If dependency errors appear, install requirements first
- If generated tests are too few, provide richer API sources

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
