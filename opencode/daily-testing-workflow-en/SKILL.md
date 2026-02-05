---
name: daily-testing-workflow-en
description: Guides QA engineers through daily testing activities—morning review, test case creation, automation, exploratory testing, bug reporting, and end-of-day wrap-up. Use when planning or executing day-to-day testing or when the user asks about daily testing workflow.
---

# Daily Testing Workflow

**中文版：** 见技能 `daily-testing-workflow`。

Practical workflow guide for QA engineers. Based on [awesome-qa-prompt](https://github.com/awesome-qa-prompt) workflows. Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **daily testing**, **today's test plan**, or **day-to-day testing**
- Need to plan or run a full day of testing activities
- **Trigger:** e.g. “Help me with today’s test plan” or “Walk me through daily QA routine”

---

## Morning Routine (5–25 min)

### 1. Review Test Plan (5–10 min)
- Use **Requirements Analysis** and **Test Strategy** prompts to review sprint/goals and high-risk areas
- Actions: Review user stories → Set priorities → Check blockers

### 2. Set Up Test Environment (10–15 min)
- Use **Automation Testing** and **Test Strategy** for pipeline status and test data
- Actions: Verify environment → Prepare test data → Update local automation

---

## Test Case Creation (30–60 min)

**New features:** Use **Test Case Writing** → add **Requirements Analysis** edge cases → review with **Functional Testing** checklist → record in test management tool.

**Bug fixes:** Use **Functional Testing** regression scenarios → add tests to verify fix and prevent regression.

---

## Test Automation (1–2 h)

**New tests:** Selenium/Playwright → **Automation Testing**; API → **API Testing**. Generate → review → run locally → commit.

**Maintenance:** **Automation Testing** maintenance + **AI-Assisted Testing**; fix flaky tests, update selectors, refactor.

---

## Exploratory Testing (30–45 min)

Use **Manual Testing** prompts for charters; time-box 60–90 min; log findings and bugs.

---

## Bug Reporting (15–30 min)

Use **Bug Reporting** prompt; include title, steps, expected vs actual, environment, screenshots/logs; log in issue tracker.

---

## Optional: Visual & E2E (30 min–2 h)

Visual: **Accessibility Testing** + visual regression (Percy/Applitools/BackstopJS). E2E: **Functional Testing** for critical journeys (login→purchase, registration→first action).

---

## Afternoon Review (~30 min)

Check CI/CD results and failed tests; use **Test Reporting** and **Test Strategy** for coverage, defect metrics, quality dashboard; team sync.

---

## End of Day (~15 min)

Commit code, update docs, log time, update tasks, plan tomorrow; optional knowledge sharing.

## How to Use the Prompts

For each step: 1) Check [reference.md](reference.md) for the prompt file for that step; 2) Open that file under this directory’s `prompts/`; 3) Combine the prompt content with the user’s context (requirements, environment, scope) and run with the AI.

## Common Pitfalls

- ❌ Skipping morning review and jumping to writing cases → ✅ Clarify stories and priorities first, then write cases
- ❌ Exploratory testing without charter or time-box → ✅ Use manual-testing prompts for charters; time-box 60–90 min
- ❌ Describing bugs verbally only → ✅ Use bug-reporting prompt for title, steps, expected vs actual, environment

## Best Practices

- Start the morning with [reference.md](reference.md) and the review/environment prompts
- For new features: requirements/edge analysis first, then concrete test cases
- Run generated automation locally before committing
- Afternoon review: use test reporting + test strategy for coverage and defect metrics

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** sprint-testing-workflow-en, release-testing-workflow-en.
