# Skill Style Guide

This guide defines the current standard for `SKILL.md` and prompt files in this repository.

## Goals

- Keep entry files short and easy to use.
- Make prompts practical, risk-driven, and directly executable.
- Remove nonessential filler such as long role setup, generic theory, and repeated examples.
- Keep same-type files aligned across Chinese, English, and workflow reuse copies.

## Frontmatter

Keep frontmatter minimal:

```yaml
---
name: <skill-id>
description: Use this skill when ...; triggers include ...
---
```

Rules:
- Keep only `name` and `description`.
- `description` must be trigger-oriented, not capability-only.
- Use the sentence pattern: `Use this skill when ...; triggers include ...`.

## SKILL.md Required Sections

All `SKILL.md` files must use these sections:

1. `## When to Use` / `## 何时使用`
2. `## Output Format Options` / `## 输出格式选项`
3. `## How to Use` / `## 如何使用`
4. `## Reference Files` / `## 参考文件`
5. `## Common Pitfalls` / `## 常见误区`
6. `## Best Practices` / `## 最佳实践`

Workflow skills may also include:
- `## Workflow Steps` / `## 工作流步骤`

## Prompt Required Sections

All prompt files must use this structure:

For English prompts:
1. Title
2. Optional `## Role` with one short persona line
3. `## Input`
4. `## What to do`
5. `## Execution Rules`
6. `## Minimum Coverage Checklist`
7. `## Output`
8. `## Quality Bar`

For Chinese prompts:
1. 标题
2. 可选 `## 角色定位`，只保留一行简短人设
3. `## 输入`
4. `## 你要做的事`
5. `## 执行规则`
6. `## 最低覆盖清单`
7. `## 输出`
8. `## 质量要求`

## Writing Rules

Prompt files should:
- say what the task is in one short sentence
- keep a concise professional persona when that identity helps output quality
- list realistic input sources
- explain the main decisions the model should make
- enforce a minimum coverage checklist so short prompts do not become incomplete
- define output order clearly
- keep quality requirements short and concrete

`SKILL.md` files should:
- explain when to use the skill in simple trigger-based language
- point to the prompt file or workflow reference first
- keep reference links short and practical
- avoid restating the whole prompt inside `SKILL.md`

## Standard How-to Pattern

Testing-type:
1. Open the prompt file in `prompts/`.
2. Add only the context that actually affects the result.
3. If the request is incomplete, return a usable first version and mark gaps.

Workflow:
1. Check `reference.md` first.
2. Open the prompt for the current step.
3. Run step by step and adjust priorities when blockers or scope changes appear.

## Progressive Disclosure

Keep `SKILL.md` and prompts concise. Move heavy detail to support files.

Use:
- `references/` for deep rules, troubleshooting, FAQs, or long background notes
- `examples/` for sample inputs and outputs
- `scripts/` for helper tooling

Do not paste large examples or long script usage blocks into `SKILL.md`.

## Language Pairing

For each Chinese skill, keep one English counterpart aligned on:
- frontmatter style
- trigger intent
- section structure
- how-to flow
- prompt skeleton

## Do / Don't

Do:
- keep prompts short, direct, and risk-focused
- keep section names stable and consistent
- keep same-name prompt copies aligned across workflow folders
- make missing information and assumptions explicit

Don't:
- add long role descriptions such as `Role / Context / Task` blocks
- add long persona backstory, but a one-line professional role is allowed
- add copy-paste instructions like “copy below the divider line”
- keep baseline-plus duplication inside prompt files
- overload `SKILL.md` with code samples, quick-start scripts, or audit metadata
- use large fixed templates when a concise output order is enough
