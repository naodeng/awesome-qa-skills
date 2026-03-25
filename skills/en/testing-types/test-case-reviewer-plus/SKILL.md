---
name: test-case-reviewer-plus
description: Review test cases using requirement, strategy, and supporting documents, then output structured findings.
---

# test-case-reviewer-plus (EN)

**中文版：** 见对应中文技能。

## When to Use

- Need a stricter review of existing test cases before test execution or release.
- Need issue severity, business impact, and retest order to be explicit.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/test-case-reviewer-plus.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- `prompts/test-case-reviewer-plus.md`: main prompt for this skill.
- `examples/`: sample inputs or outputs.
- `scripts/`: helper scripts or converters for this skill.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
