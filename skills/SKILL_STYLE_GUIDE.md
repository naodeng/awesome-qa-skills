# Skill Style Guide

This guide defines the standard structure for all skills in this repository.

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

## Required Sections

For testing-type skills:
1. `## When to Use` / `## 何时使用`
2. `## Output Format Options` / `## 输出格式选项`
3. `## How to Use` / `## 如何使用`
4. `## Reference Files` / `## 参考文件`
5. `## Common Pitfalls` / `## 常见误区 | Common Pitfalls`

For workflow skills:
1. `## When to Use` / `## 何时使用`
2. `## How to Use` / `## 如何使用`
3. Workflow timeline/phase sections
4. `## Common Pitfalls` / `## 常见误区`
5. `## Best Practices` / `## 最佳实践`
6. `## Reference Files` / `## 参考文件`

## Standard How-to Templates

Testing-type (EN):
1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

Testing-type (ZH):
1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

Workflow (EN):
1. Check `reference.md` to find the prompt file for the current step.
2. Open the corresponding file in `prompts/`, then combine it with the current context.
3. Run step by step, and update priorities or gates based on outputs and blockers.

Workflow (ZH):
1. 先查看 `reference.md`，定位当前步骤对应的提示词文件。
2. 打开 `prompts/` 下对应文件，并结合当前上下文一起使用。
3. 按步骤推进执行，并根据产出与阻塞动态调整优先级或门禁条件。

## Progressive Disclosure

Keep `SKILL.md` concise and move heavy details to references.

Use:
- `references/troubleshooting.md` for long troubleshooting blocks.
- Other `references/*.md` for large examples, deep rules, or long checklists.

In `SKILL.md`, keep a short entry point, for example:

```md
## Troubleshooting
Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
```

## Language Pairing

For each Chinese skill, keep one English counterpart (`-en`) aligned on:
- frontmatter style
- trigger intent in description
- section structure
- how-to flow

## Do / Don't

Do:
- keep trigger keywords explicit in `description`
- keep section titles stable and consistent
- split oversized sections into `references/`

Don't:
- add nonessential frontmatter metadata
- overload `SKILL.md` with long troubleshooting details
- use different section names for the same purpose across skills
