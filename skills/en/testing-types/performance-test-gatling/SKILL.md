---
name: performance-test-gatling
description: Provide Gatling performance scope, reusable simulations, and runnable entry points.
---

# performance-test-gatling (EN)

**中文版：** 见对应中文技能。

## When to Use

- Need performance outputs that should land in Gatling structure.
- The project already uses Gatling or wants Gatling-ready scenarios.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/performance-test-gatling.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- `prompts/performance-test-gatling.md`: main prompt for this skill.
- `references/`: supporting notes loaded only when needed.
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
