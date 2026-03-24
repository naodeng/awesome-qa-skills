---
name: api-test-bruno
description: Parse multi-format API definitions and generate Bruno collections for API regression.
---

# api-test-bruno (EN)

## Use Cases

Use when API sources are scattered and need to be unified into Bruno requests quickly.

## Objective

Parse multi-format API definitions and generate Bruno collections for API regression.

## Input

- Supported: curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## Output

- Output: normalized API data + Bruno collection folder

## Prerequisites

- Install Python 3
- Install Bruno CLI for execution
- Use `examples/` or real API sources as input

## Quick Start

```bash
bash scripts/run.sh examples
```

## Validation Checklist

- Bruno collection folder is generated
- If Bruno CLI is installed, regression can run directly

## Common Issues

- Without Bruno CLI, generation still works
- If parsing returns empty results, validate source files first

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
