---
name: change-to-regression
description: Use this skill when you need to select explainable regression scope from a change and its risk; triggers include change-to-regression and Change-to-Regression Workflow.
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

**Chinese version:** See `README.md`.

## When to use

Use this Skill to select explainable regression scope from a change and its risk.

## Workflow

Read `prompts/change-to-regression.md` first; validate inputs, complete each stage, preserve sources, and return risk and handoff details.

## Core constraints

Compose existing specialist Skills without copying their analysis rules. Mark host installation `UNKNOWN` without evidence. Do not report plans or static analysis as executed results. Read-only by default; external writes require authorization.

## Load on demand

- Main process: `prompts/change-to-regression.md`
- Usage and FAQ: `README_EN.md`
- Evals: `evals/`

## Before delivery

- [ ] Input scope and assumptions are explicit
- [ ] Handoffs preserve sources, status, and gaps
- [ ] Execution evidence is separate from plans
- [ ] Next steps and permission boundary are clear

## Common mistakes

Do not invent input, assume dependencies are installed, or present recommendations as execution or approval.
