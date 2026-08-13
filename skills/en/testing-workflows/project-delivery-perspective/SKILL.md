---
name: project-delivery-perspective
description: Use this skill when project delivery constraints or action tracking are needed for test strategy, test strategy review, or test report review; triggers include project delivery perspective, delivery planning, schedule and capacity, and 项目交付视角.
---

# Project Delivery Perspective (English)

**中文版：** See the corresponding Chinese skill.

## When to use

- A supported quality stage needs attributable schedule, capacity, dependency, milestone, owner, or action-status input.
- Delivery participants need to surface constraints or track follow-up actions without changing quality facts.

## Inputs

- `stage` (required): `test-strategy`, `test-strategy-review`, or `test-report-review`.
- Supplied project-delivery facts: schedule, capacity, dependencies, milestones, owners, action status, and the source for each statement.
- Optional quality facts from their owning source, recorded only to preserve context and route follow-up.

## Workflow

1. Validate `stage`. If it is missing or unsupported, return **Not applicable**, state that only `test-strategy`, `test-strategy-review`, and `test-report-review` are supported, and request a valid stage. Do not produce planning, action, or quality conclusions.
2. Load and follow exactly one Prompt from the table for a valid stage. Never combine stage Prompts.
3. Record project constraints and actions only when their schedule, owner, status, or dependency source is supplied. Mark absent information as a gap; never infer dates, capacity, ownership, or status.
4. Keep quality facts in a separate, source-attributed preservation section. Do not decide, rewrite, downgrade, close, pass, approve, or otherwise override defect, execution, evidence, quality, or release facts.

| `stage` | Only prompt to load |
| --- | --- |
| `test-strategy` | `prompts/test-strategy.md` |
| `test-strategy-review` | `prompts/test-strategy-review.md` |
| `test-report-review` | `prompts/test-report-review.md` |

## Responsibilities and boundaries

- Focus on delivery feasibility inputs: schedule, capacity, dependencies, milestones, accountable owners, action status, escalation needs, and delivery risk caused by constraints.
- Preserve every project and quality statement with its supplied source. A stakeholder request is a request, not evidence that changes a fact.
- This Skill is not a QA, engineering, product, security, or release authority. It never produces a quality verdict or changes defect status, execution status, test results, evidence, quality status, or release approval.

## Output contract

Unless returning **Not applicable**, output in this order: **Summary, Project constraints, Action tracking, Preserved quality facts, Information gaps, Coordination questions, Next delivery actions, Confidence**. For every factual item, include its source; place unverified requests under questions or actions, not facts.

## Pre-delivery checklist

- [ ] The stage is one of the three supported values and exactly one Prompt was loaded
- [ ] Every schedule, capacity, dependency, milestone, owner, and status statement carries its supplied source
- [ ] Project constraints/actions are separate from preserved quality facts
- [ ] No defect, execution, evidence, quality, or release fact was changed or concluded
- [ ] Unknown ownership, dates, capacity, dependencies, and status are explicit gaps

## Progressive disclosure

- After stage validation, read only the mapped file in `prompts/`.
- For evaluation or regression, use `evals/`; never treat eval scenarios as project evidence.

## Common pitfalls

- Do not turn deadline pressure into a claim that a defect is closed, testing passed, or release quality is acceptable.
- Do not present a requested fact change as a source-backed fact.
- Do not create a delivery plan from unprovided capacity, owners, dates, or dependencies.
