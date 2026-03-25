---
name: discover-testing
description: Use this skill when you need to quickly route a request to the best testing-type or testing-workflow skill.
---

# Testing Skill Discovery (English)

**中文版：** 见对应中文技能。

## When to Use

- Need to decide which testing skill should be used before execution.
- The request mixes multiple testing directions or phases.

## Output Format Options

Markdown by default. If you need Excel, CSV, JSON, Word, or other supported formats, append the format request at the end and check [output-formats.md](output-formats.md).

## How to Use

1. Read the user request and identify the main testing goal.
2. Use the routing prompt under `prompts/` to choose one primary skill and, only if needed, one supporting skill.
3. Pass the request to the selected skill instead of trying to do the whole task here.

## Reference Files

- `prompts/discover-testing.md`: main prompt for this skill.
- `reference.md`: step-to-prompt mapping and workflow routing.
- `output-formats.md`: optional output format instructions.
- `scripts/`: helper scripts or converters for this skill.

## Common Pitfalls

- Do not recommend many skills at once.
- Do not use this skill when the target skill is already obvious.
- Do not turn routing into execution.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
