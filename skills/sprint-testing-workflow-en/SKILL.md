---
name: sprint-testing-workflow-en
description: Guides QA and Scrum teams through a 2-week sprint testing cycle—planning, setup, execution, regression, stabilization, review, retrospective. Use when planning or running sprint testing.
---

# Sprint Testing Workflow

**中文版：** 见技能 `sprint-testing-workflow`。

Complete testing workflow for a 2-week sprint. Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **sprint testing**, **iteration planning**, or **sprint retrospective**
- Need phase-by-phase sprint testing (planning → review → retrospective)
- **Trigger:** e.g. “Help me plan sprint testing” or “Walk me through the sprint test flow”

**Phases:** Day 1 Planning → Days 2–3 Setup & early testing → Days 4–8 Active testing → Days 9–10 Intensive (regression, integration, visual) → Day 11 Stabilization → Day 12 Review & demo → Day 13 Retrospective & next sprint.

## How to Use the Prompts

For each step: 1) Check [reference.md](reference.md) for the prompt file; 2) Open that file under this directory’s `prompts/`; 3) Combine the prompt with the current sprint context (stories, environment, scope) and run with the AI.

## Common Pitfalls

- ❌ Skipping planning and testing ad hoc → ✅ Clarify stories and acceptance criteria first, then write and run cases
- ❌ No mid-sprint review → ✅ Run a mid-sprint check on days 5–6 and adjust plan/priority as needed
- ❌ Leaving regression to the last day → ✅ Run intensive regression on days 9–10 and keep day 11 for stabilization

## Best Practices

- Day 1: use [reference.md](reference.md) for planning, test strategy, and requirements prompts
- Around daily standups: use bug-reporting and test-reporting prompts to log and sync
- Day 11: complete the checklist (stories tested, regression passed, critical bugs fixed) before review
- When red flags appear: use test-strategy prompts for risk analysis and communication

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** daily-testing-workflow-en, release-testing-workflow-en.
