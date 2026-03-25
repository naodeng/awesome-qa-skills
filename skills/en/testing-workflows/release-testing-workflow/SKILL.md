---
name: release-testing-workflow
description: Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include release testing workflow and release readiness testing.
---

# Release Testing Workflow

**中文版：** 见对应中文技能。

## When to Use

- Need a structured release testing workflow flow instead of a single testing task.
- Need to move step by step across a testing phase with the matching prompts.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Check [reference.md](reference.md) first and find the prompt file for the current step.
2. Open the matching file under `prompts/` and add only the context that matters: scope, environment, risks, constraints, and expected output.
3. Run step by step, and adjust priorities when blockers, risks, or scope changes appear.

## Workflow Steps

- `accessibility-testing.md`
- `ai-assisted-testing.md`
- `automation-testing.md`
- `functional-testing.md`
- `manual-testing.md`
- `performance-testing.md`
- `requirements-analysis.md`
- `security-testing.md`
- `test-case-writing.md`
- `test-reporting.md`
- `test-strategy.md`

## Reference Files

- `prompts/`: prompt files used by this skill.
- `reference.md`: step-to-prompt mapping and workflow routing.
- `references/`: supporting notes loaded only when needed.
- `scripts/`: helper scripts or converters for this skill.

## Common Pitfalls

- Do not jump into execution before confirming the current step.
- Do not try to run the whole workflow with one giant prompt.
- Do not ignore blockers and reprioritization.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
