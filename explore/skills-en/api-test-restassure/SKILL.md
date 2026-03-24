---
name: api-test-restassure
description: Parse multi-format API definitions and generate Rest Assured Java test classes.
---

# api-test-restassure (EN)

## Use Cases

Use in Java projects for continuous API regression before release.

## Objective

Parse multi-format API definitions and generate Rest Assured Java test classes.

## Input

- Supported: curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## Output

- Output: normalized API data + generated Java test class

## Prerequisites

- Install Python 3
- Install Maven for execution
- Validate generation with `examples/` first

## Quick Start

```bash
bash scripts/run.sh examples
```

## Validation Checklist

- Java test class is generated
- Tests run when Maven is available

## Common Issues

- Without Maven, generation still works
- Adjust output path if project package structure differs

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
