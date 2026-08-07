---
name: performance-test-jmeter
description: Use this skill when you need to design JMeter test plans with Thread Groups, samplers, data sets, assertions, timers, CLI runs, and HTML reports; triggers include JMeter performance testing, performance testing, and performance-test-jmeter.
---

# JMeter Performance Testing (EN)

**中文版：** 见对应中文技能。

## When to Use

- Need outputs that should land in a JMeter performance testing workflow.
- The project already uses JMeter or wants JMeter-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/performance-test-jmeter.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- `prompts/performance-test-jmeter.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
