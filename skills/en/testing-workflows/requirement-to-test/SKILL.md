---
name: requirement-to-test
description: Use this skill when you need to turn requirements into testable, risk-driven, traceable test design; triggers include requirement-to-test, 需求到测试, and Requirement-to-Test Workflow.
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

# Requirement-to-Test Workflow

## When to Use

Use this Skill to turn requirements into testable, risk-driven, traceable test design.

## Output Format Options

Default to Markdown with test cases and a requirement traceability matrix. If JSON is requested, preserve the prompt's separate facts, inferences, plans, execution states, and sources.

## Core constraints

Compose existing specialist Skills without copying their analysis rules. Mark host installation `UNKNOWN` without evidence. Do not report plans or static analysis as executed results. Read-only by default; external writes require authorization.

## How to Use

Read `prompts/requirement-to-test.md` first; validate inputs, complete each stage, preserve sources, and return testability findings, test design, and coverage gaps. Use `README.md` for invocation examples and FAQ.

## Reference Files

- `prompts/requirement-to-test.md`: full requirement analysis, test design, output, and recovery rules.
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

Preserve requirement IDs, ask about missing thresholds, state each case's source and design method, and explain uncovered areas.
