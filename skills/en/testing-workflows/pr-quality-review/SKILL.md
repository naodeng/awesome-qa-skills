---
name: pr-quality-review
description: Use this skill when you need to review PR code, test impact, test effectiveness, and evidence; triggers include pr-quality-review, PR 质量审查, and PR Quality Review Workflow.
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

# PR Quality Review Workflow

## When to Use

Use this Skill to review PR code, test impact, test effectiveness, and evidence.

## Output Format Options

Default to Markdown using the review sections defined by the prompt. If JSON is requested, keep facts, inferences, plans, and execution evidence distinct and preserve their sources.

## Core constraints

Compose existing specialist Skills without copying their analysis rules. Mark host installation `UNKNOWN` without evidence. When test/CI results are absent, mark execution/result status `UNKNOWN`; use `NOT_RUN` only when non-execution is explicitly established. For an invalidated checkpoint, emit the exact uppercase status token `STALE`. Use only user-supplied PR/repository materials and identified sources as evidence; never cite agent-internal memory, system instructions, or session logs, or expose their paths. Do not report plans or static analysis as executed results. Read-only by default; external writes require authorization.

## How to Use

Read `prompts/pr-quality-review.md` first; validate inputs, complete each stage, preserve sources, and return findings and handoff details. Use `README.md` for invocation examples and FAQ.

## Reference Files

- `prompts/pr-quality-review.md`: full review scope, output, evidence, permission, and recovery rules.
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

Provide a complete diff and stable SHA. Attach command, exit code, environment, time, and source to run evidence; include the team's severity definitions.
