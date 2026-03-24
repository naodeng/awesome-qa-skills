---
name: performance-test-k6
description: Provide k6 performance scope, reusable scripts, and runnable entry points for load/stress/spike/soak.
---

# performance-test-k6 (EN)

## Use Cases

Use before major release/events to validate throughput, latency, and failure rate under load.

## Objective

Provide k6 performance scope, reusable scripts, and runnable entry points for load/stress/spike/soak.

## Input

- Optional: target URL, auth data, concurrency settings, env vars

## Output

- Output: run summary and performance results

## Prerequisites

- Install k6
- Configure reachable target environment
- Start from smoke/load baseline

## Quick Start

```bash
bash scripts/run-tests.sh load
```

## Offline Demo (Local Runnable)

```bash
bash scripts/run-local-smoke.sh
```

## Validation Checklist

- Command starts execution
- Summary and threshold results are visible

## Common Issues

- If failure rate is high, validate target URL/network first
- If command not found, install k6

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
