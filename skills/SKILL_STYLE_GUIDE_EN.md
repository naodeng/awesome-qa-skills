<div align="right"><a href="./SKILL_STYLE_GUIDE.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skill Style Guide

This guide defines the current structure and writing standard for `SKILL.md` and primary prompt files.

## Goals

- Keep activation entries short and usable.
- Make prompts practical, risk-driven, and executable.
- Remove generic theory, long persona setup, and repeated examples.
- Keep Chinese and English counterparts aligned in intent and structure.

## Frontmatter

```yaml
---
name: <skill-id>
description: Use this skill when ...; triggers include ...
---
```

- Keep only `name` and `description`.
- Use trigger-oriented language, not a capability-only description.
- Match the directory name and metadata key.

## Required `SKILL.md` Sections

English entries use:

1. `## When to Use`
2. `## Output Format Options`
3. `## How to Use`
4. `## Reference Files`
5. `## Common Pitfalls`
6. `## Best Practices`

Chinese entries use the equivalent `何时使用`, `输出格式选项`, `如何使用`, `参考文件`, `常见误区`, and `最佳实践` headings. Workflow Skills may also include workflow steps.

## Required Prompt Sections

English prompts:

1. Title
2. Optional one-line `## Role`
3. `## Input`
4. `## What to do`
5. `## Execution Rules`
6. `## Minimum Coverage Checklist`
7. `## Output`
8. `## Quality Bar`

Chinese prompts use the corresponding `角色定位`, `输入`, `你要做的事`, `执行规则`, `最低覆盖清单`, `输出`, and `质量要求` headings.

## Writing Rules

Prompts should:

- state the task in one short sentence;
- list realistic input sources;
- explain the decisions the agent must make;
- enforce minimum coverage;
- define output order;
- require facts, assumptions, gaps, evidence, and risk boundaries;
- keep quality requirements short and concrete.

Entry files should explain invocation and loading behavior without copying the entire prompt.

## Progressive Disclosure

- Use `references/` for deep rules and troubleshooting.
- Use `examples/` for sample inputs and outputs.
- Use `scripts/` for helper tooling.
- Use `output-formats.md` only when alternative formats are supported.
- Do not assume an optional directory exists.

## Language Pairing

Chinese and English Skills align on frontmatter style, trigger intent, section structure, loading flow, prompt skeleton, and evaluation intent. Use natural technical language rather than literal translation.

## Do

- Keep prompts direct, domain-specific, and risk-focused.
- Make missing information and assumptions explicit.
- Provide verifiable expected behavior and evidence.
- Preserve the established toolchain and safe defaults.

## Do Not

- Add long persona backstories.
- Add copy-and-paste ceremony.
- Duplicate baseline and Plus content inside one prompt.
- Put large examples or scripts in `SKILL.md`.
- Use fixed templates so large that they hide the actual decision.
