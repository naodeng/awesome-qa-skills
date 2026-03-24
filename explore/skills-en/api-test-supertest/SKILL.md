---
name: api-test-supertest
description: Parse multi-format API definitions and generate executable Supertest automation.
---

# api-test-supertest (EN)

## Use Cases

Use in Node projects to bootstrap API regression tests quickly from existing API sources.

## Objective

Parse multi-format API definitions and generate executable Supertest automation.

## Input

- Supported: curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## Output

- Output: normalized API data + Supertest test file

## Prerequisites

- Install Python 3
- Install Node and npm for execution
- Validate generation flow with `examples/` first

## Quick Start

```bash
bash scripts/run.sh examples
```

## Validation Checklist

- Test file is generated
- If npm is available, tests can run immediately

## Common Issues

- To generate only, run parse and generate scripts separately
- If npm dependencies are missing, install them before running

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
