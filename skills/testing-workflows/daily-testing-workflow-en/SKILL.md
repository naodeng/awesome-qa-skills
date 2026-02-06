---
name: daily-testing-workflow-en
description: Guides QA engineers through daily testing activities—morning review, test case creation, automation, exploratory testing, bug reporting, and end-of-day wrap-up. Use when planning or executing day-to-day testing or when the user asks about daily testing workflow.
---

# Daily Testing Workflow

**中文版：** 见技能 `daily-testing-workflow`。

Use **this directory's `prompts/`**. Step→prompt mapping: [reference.md](reference.md).

## When to Use

- User mentions **daily testing**, **today's test plan**, or **day-to-day testing**
- Need to plan or run a full day of testing activities
- **Trigger:** e.g. “Help me with today’s test plan” or “Walk me through daily QA routine”

---

## Morning Routine (5–25 min)

1. **Review test plan (5–10 min):** requirements-analysis, test-strategy → stories, priorities, blockers.
2. **Set up environment (10–15 min):** automation-testing, test-strategy → environment, data, local automation.

## Test Case Creation (30–60 min)

**New features:** test-case-writing → requirements-analysis (edge cases) → functional-testing checklist → record in test tool. **Bug fixes:** functional-testing regression → verify fix → anti-regression cases.

## Test Automation (1–2 h)

**New:** Selenium/Playwright → automation-testing; API → api-testing. Generate → review → run locally → commit. **Maintenance:** automation-testing + ai-assisted-testing; fix flaky, update selectors, refactor.

## Exploratory Testing (30–45 min)

manual-testing charters; time-box 60–90 min; log findings and bugs.

## Bug Reporting (15–30 min)

bug-reporting template → title, steps, expected vs actual, environment, screenshots/logs → issue tracker.

## Optional: Visual & E2E (30 min–2 h)

accessibility-testing + visual regression; functional-testing E2E (critical journeys).

## Afternoon Review (~30 min)

CI/CD results, failed tests; test-reporting, test-strategy → coverage, defect metrics, dashboard; team sync.

## End of Day (~15 min)

Commit code, update docs, log time, update tasks, plan tomorrow.

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

Pipeline failure → check automation/CI, debug, fix and re-run. Flaky tests → maintenance strategy + wait/retry. Blocked → log blockers, alternate area, reprioritize.

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** sprint-testing-workflow-en, release-testing-workflow-en.
