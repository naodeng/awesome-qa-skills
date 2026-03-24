---
name: performance-test-gatling
description: Provide Gatling performance scope, reusable simulations, and runnable entry points.
---

# performance-test-gatling (EN)

## Use Cases

Use for long-running or complex concurrency simulations before release.

## Objective

Provide Gatling performance scope, reusable simulations, and runnable entry points.

## Input

- Optional: test type (load/stress/spike/soak) and environment params

## Output

- Output: run result and report directory

## Prerequisites

- Install Gatling CLI
- Configure reachable target environment
- Select test type based on objective

## Quick Start

```bash
bash scripts/run-tests.sh load
```

## Offline Demo (Local Runnable)

```bash
bash scripts/run-local-smoke.sh
```

## Validation Checklist

- Selected simulation starts correctly
- Reports are produced after run

## Common Issues

- If `gatling` is missing, install it or set `GATLING_BIN`
- If output looks abnormal, reduce load and establish baseline first

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
