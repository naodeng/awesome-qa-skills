---
name: daily-testing-workflow
description: Use this skill when you need a day-by-day QA routine including planning, execution, bug reporting, and end-of-day wrap-up; triggers include daily testing workflow and daily QA routine.
---

# Daily Testing Workflow

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need a one-day QA cadence: morning plan, execution, defects, EOD wrap-up.
- Need stage gates and handoffs to type skills—not a single isolated testing task.

## Workflow

1. Read and follow `prompts/daily-testing-workflow.md` (stages, gates, handoffs, output structure).
2. Add only context that changes the result: day scope, environment, constraints, risks, carryover defects.
3. After locating the stage, optionally read matching stage files under `prompts/`; name other skills by name only.
4. If input is incomplete, draft a usable day plan and mark assumptions and gaps.

## Core Constraints

- Own phases and gates; hand full cases/strategy/reports to type skills.
- Prioritize by risk; gates must be checkable.
- Separate confirmed facts from assumptions.
- Do not invent missing details; no relative-path links to other skill files.

## Progressive Disclosure

- Before producing output, read and follow `prompts/daily-testing-workflow.md`.
- For step ↔ stage prompt mapping: read `reference.md`.
- When deep-diving a stage: read the matching file under this skill’s `prompts/` (e.g. `bug-reporting.md`).
- When a template fits: use matching files under `output-templates/`.

## Pre-delivery Checklist

- [ ] Followed the main prompt’s output structure
- [ ] Includes today’s scope/won’t-do, gate status, priority queue, next skill
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not turn the daily workflow into a functional-testing encyclopedia.
- Do not leave work forever “in progress” without exit criteria.
- Do not hand off multiple equal primary skills at once.
- Do not pretend execution succeeded on a red environment.
