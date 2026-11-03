---
name: change-to-regression
description: Use this skill when you need to select explainable regression scope from a change and its risk; triggers include change-to-regression, 变更回归, and Change-to-Regression Workflow.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-workflows"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Change-to-Regression Workflow

## When to Use

Use this Skill to select explainable regression scope from a change and its risk.

## Output Format Options

Default to Markdown with a required/deferred/excluded regression table. If JSON is requested, preserve the prompt's separate facts, inferences, plans, execution states, and sources.

## Core constraints

Compose existing specialist Skills without copying their analysis rules. Mark host installation `UNKNOWN` without evidence. Do not report plans or static analysis as executed results. Read-only by default; external writes require authorization.

## How to Use

Read `prompts/change-to-regression.md` first; validate inputs, complete each stage, preserve sources, and return risk and handoff details. Use `README.md` for invocation examples and FAQ.

## Reference Files

- `prompts/change-to-regression.md`: full workflow, coverage, output, and recovery rules.
- `README.md`: usage examples and FAQ.
- `evals/`: trigger and behavior regression cases.

## Before delivery

- [ ] Input scope and assumptions are explicit
- [ ] Handoffs preserve sources, status, and gaps
- [ ] Execution evidence is separate from plans
- [ ] Next steps and permission boundary are clear

## Common Pitfalls

Do not invent input, assume dependencies are installed, or present recommendations as execution or approval.

## Best Practices

Provide exact base/head SHA, the full diff, test runtimes, and environment limits. After execution, attach its time, Commit, and run record.
