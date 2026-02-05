---
name: sprint-testing-workflow-en
description: Guides QA and Scrum teams through a 2-week sprint testing cycle—planning, setup, execution, regression, stabilization, review, and retrospective. Use when planning or running sprint testing.
---

# Sprint Testing Workflow

**中文版：** 见技能 `sprint-testing-workflow`。

Complete testing workflow for a 2-week sprint. Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **sprint testing**, **iteration planning**, or **sprint retrospective**
- Need phase-by-phase sprint testing (planning → review → retrospective)
- **Trigger:** e.g. “Help me plan sprint testing” or “Walk me through the sprint test flow”

---

## Day 1: Sprint Planning

- **Morning:** Review backlog + Test Strategy story analysis; in meeting understand acceptance criteria, testable requirements, estimates, dependencies.
- **Afternoon:** Test Strategy + Requirements Analysis → test strategy doc, scope, environment & data, automation candidates. Template: iteration/story/test focus/automation/risks.

## Days 2–3: Setup & Early Testing

Environment + CI/CD + test data (Automation Testing, Test Strategy). Early stories: Test Case Writing → review with dev → exploratory testing.

## Days 4–8: Active Testing

- Daily: standup; run cases + manual exploratory + Bug Reporting; automation (Automation Testing, API Testing); defect triage.
- Days 5–6 mid-sprint review: progress, adjust plan, at-risk stories, automation coverage; metrics: execution rate, defect rate, coverage, story vs tests.

## Days 9–10: Intensive Testing

- Regression: Functional Testing + AI-Assisted Testing; automation regression + critical path manual + cross-browser/mobile.
- Integration: Functional Testing E2E + API Testing; end-to-end, system integration, data flow.
- Visual: Accessibility Testing; visual regression, UI, responsive.

## Day 11: Stabilization

Optional defect blitz (2 h + manual testing charters). Critical must-fix, high-priority assess, medium/low to backlog. Check: stories tested, critical fixed and regressed, regression pass, automation updated, reports generated.

## Day 12: Review & Demo

Test Reporting + Test Strategy → summary, defect metrics, coverage, quality dashboard. Present outcomes, metrics, known issues, next-sprint risks; demo automation if applicable.

## Day 13: Retrospective & Next Sprint Prep

Retro: what went well/challenges/improvements/action items; automation effectiveness, defect timing, environment & tools. Next sprint: review stories, challenges, automation plan, update strategy.

## Ongoing (whole sprint)

Daily: run cases, defects, automation, CI/CD, sync. Every 2–3 days: metrics, coverage, refactor, docs. Weekly: team sync, strategy, risks, sharing.

## Phase Focus & Red Flags

- **Early (1–4):** planning & setup. **Mid (5–8):** functional testing, defects, automation, exploration. **Late (9–12):** regression, integration, verification, reporting.
- Testing behind: escalate, reprioritize, support, adjust scope. Quality issues: Test Strategy risk analysis, critical path, extend or tech-debt sprint. Environment: document, DevOps, fallback, local verification.

## Sprint Checklist

Start: plan, environment, data, automation, alignment. Mid: 50%+ tested, automation in progress, no major blockers. End: all tested, regression pass, critical fixed, report & demo.

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
