---
name: daily-testing-workflow-en
version: 1.0.0
description: Guides daily QA workflow—morning review, test cases, automation, exploratory testing, bug reporting. Use for daily testing.
---

# Daily Testing Workflow

**中文版：** 见技能 `daily-testing-workflow`。

Based on [awesome-qa-prompt](https://github.com/awesome-qa-prompt). Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **daily testing**, **today's test plan**, or **day-to-day testing**
- Need to plan or run a full day of testing activities
- **Trigger:** e.g. “Help me with today’s test plan” or “Walk me through daily QA routine”

---

## Morning Routine (5–25 min)

1. **Review test plan (5–10 min):** Requirements Analysis + Test Strategy → review today's stories, priorities, blockers.
2. **Set up environment (10–15 min):** Automation Testing + Test Strategy → verify environment, prepare data, update local automation.

## Test Cases (30–60 min)

- **New features:** Test Case Writing → Requirements Analysis (edge cases) → Functional Testing checklist → record in test management tool.
- **Bug fixes:** Functional Testing regression → verify fix cases → anti-regression cases.

## Automation (1–2 h)

- **New tests:** Selenium/Playwright use Automation Testing prompts, API use API Testing; generate → review → run locally → commit.
- **Maintenance:** Automation Testing maintenance strategy + AI-Assisted Testing; fix flaky cases, update selectors, refactor duplicate code.

## Exploratory Testing (30–45 min)

Manual Testing exploratory scenarios + charters; time-box 60–90 min; log findings and bugs. Charters: mission, duration, area, heuristics (SFDPOT/FEW HICCUPS).

## Bug Reporting (15–30 min)

Bug Reporting template → title, steps, expected vs actual, environment, screenshots/logs → log in issue tracker.

## Optional: Visual & E2E (30 min–2 h)

Visual: Accessibility Testing + visual regression (Percy/Applitools/BackstopJS). E2E: Functional Testing end-to-end; critical journeys (login→purchase, register→first action).

## Afternoon Review (~30 min)

CI/CD results, failed cases, reports; Test Reporting + Test Strategy → coverage, defect metrics, quality dashboard; team sync.

## End of Day (~15 min)

Commit code, update docs, log time, update tasks, plan tomorrow; optional sharing and wiki.

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

## Troubleshooting

- Pipeline failures: check automation/CI → debug → fix and re-run.
- Flaky tests: maintenance strategy + waits + retries.
- Blocked: log blockers, alternate areas, Test Strategy reprioritization.

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** sprint-testing-workflow-en, release-testing-workflow-en.
