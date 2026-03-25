---
name: requirements-analysis
description: Use this skill when you need to analyze requirements, identify test points, boundaries, dependencies, and risks before test design; triggers include requirements analysis and test point analysis.
---

# Requirements Analysis (English)

**中文版：** 见对应中文技能。

## When to Use

- Need help with requirements analysis in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.

## Output Format Options

Markdown by default. If you need Excel, CSV, JSON, Word, or other supported formats, append the format request at the end and check [output-formats.md](output-formats.md).

## How to Use

1. Open `prompts/requirements-analysis.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- `prompts/requirements-analysis.md`: main prompt for this skill.
- `output-formats.md`: optional output format instructions.
- `references/`: supporting notes loaded only when needed.
- `scripts/`: helper scripts or converters for this skill.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
