---
name: daily-testing-workflow-en
description: Use this skill when you need a day-by-day QA routine including planning, execution, bug reporting, and end-of-day wrap-up; triggers include daily testing workflow and daily QA routine.
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

### ☑️ Step Tracking Checklist

- [ ] **Review test plan (5–10 min)**
  - [ ] Review today's user stories and tasks
  - [ ] Confirm test priorities
  - [ ] Identify potential blockers and dependencies
  - [ ] Use prompts: requirements-analysis, test-strategy

- [ ] **Set up environment (10–15 min)**
  - [ ] Verify test environment availability
  - [ ] Prepare test data
  - [ ] Update local automation scripts
  - [ ] Check CI/CD pipeline status
  - [ ] Use prompts: automation-testing, test-strategy

## Test Case Creation (30–60 min)

### ☑️ Step Tracking Checklist

- [ ] **New feature test cases**
  - [ ] Analyze requirements and acceptance criteria
  - [ ] Identify boundary values and equivalence classes
  - [ ] Write functional test cases
  - [ ] Record in test management tool
  - [ ] Use prompts: test-case-writing, requirements-analysis, functional-testing

- [ ] **Bug fix verification cases**
  - [ ] Write bug verification test cases
  - [ ] Create anti-regression test cases
  - [ ] Update regression test suite
  - [ ] Use prompts: functional-testing

## Test Automation (1–2 h)

### ☑️ Step Tracking Checklist

- [ ] **New automation test development**
  - [ ] Select appropriate test framework (Selenium/Playwright/API)
  - [ ] Generate automation test scripts
  - [ ] Code review and optimization
  - [ ] Run locally to verify
  - [ ] Commit code to version control
  - [ ] Use prompts: automation-testing, api-testing

- [ ] **Automation test maintenance**
  - [ ] Fix flaky test cases
  - [ ] Update element locators
  - [ ] Refactor test code
  - [ ] Optimize test execution time
  - [ ] Use prompts: automation-testing, ai-assisted-testing

## Exploratory Testing (30–45 min)

### ☑️ Step Tracking Checklist

- [ ] **Exploratory testing execution**
  - [ ] Create test charter (mission, duration, area)
  - [ ] Apply heuristics (SFDPOT, FEW HICCUPS)
  - [ ] Time-box execution (60–90 min)
  - [ ] Record findings and observations
  - [ ] Report discovered bugs
  - [ ] Use prompts: manual-testing

## Bug Reporting (15–30 min)

### ☑️ Step Tracking Checklist

- [ ] **Bug documentation**
  - [ ] Write clear bug title
  - [ ] Record detailed reproduction steps
  - [ ] Describe expected vs actual results
  - [ ] Add environment information
  - [ ] Attach screenshots and logs
  - [ ] Record in issue tracker
  - [ ] Use prompts: bug-reporting

## Optional: Visual & E2E (30 min–2 h)

### ☑️ Step Tracking Checklist

- [ ] **Accessibility and visual testing**
  - [ ] Execute accessibility tests
  - [ ] Perform visual regression tests
  - [ ] Use prompts: accessibility-testing

- [ ] **End-to-end testing**
  - [ ] Test critical user journeys
  - [ ] Verify system integration points
  - [ ] Use prompts: functional-testing

## Afternoon Review (~30 min)

### ☑️ Step Tracking Checklist

- [ ] **CI/CD results review**
  - [ ] Check pipeline execution results
  - [ ] Analyze failed test cases
  - [ ] Record issues needing fixes

- [ ] **Quality metrics review**
  - [ ] Review test coverage
  - [ ] Analyze defect metrics
  - [ ] Update quality dashboard
  - [ ] Use prompts: test-reporting, test-strategy

- [ ] **Team sync**
  - [ ] Share testing progress
  - [ ] Discuss blockers and risks
  - [ ] Coordinate tomorrow's plan

## End of Day (~15 min)

### ☑️ Step Tracking Checklist

- [ ] **Code and documentation**
  - [ ] Commit all code changes
  - [ ] Update test documentation
  - [ ] Log work time

- [ ] **Task management**
  - [ ] Update task status
  - [ ] Plan tomorrow's work
  - [ ] Record incomplete items

## How to Use

1. Check [reference.md](reference.md) to find the prompt file for the current step.
2. Open the corresponding file in `prompts/`, then combine it with the current context (scope, environment, risks, constraints).
3. Run step by step, and update priorities or gates based on outputs and blockers.

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

## Target Audience

- QA engineers and developers executing this testing domain in real projects
- Team leads who need structured, reproducible testing outputs
- AI users who need fast, format-ready deliverables for execution and reporting

## Not Recommended For

- Pure production incident response without test scope/context
- Decisions requiring legal/compliance sign-off without expert review
- Requests lacking minimum inputs (scope, environment, expected behavior)

## Critical Success Factors

- Provide clear scope, environment, and acceptance criteria before generation
- Validate generated outputs against real system constraints before execution
- Keep artifacts traceable (requirements -> test points -> defects -> decisions)

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
  - `template-word.md` (Word-friendly structure)
  - `template-excel.tsv` (Excel paste-ready)
  - `template-xmind.md` (XMind-friendly outline)
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- Parser scripts directory: `scripts/`
  - Parse (generic): `parse_output_formats.py`
  - Parse (per-format): `parse_word.py`, `parse_excel.py`, `parse_xmind.py`, `parse_json.py`, `parse_csv.py`, `parse_markdown.py`
  - Convert (generic): `convert_output_formats.py`
  - Convert (per-format): `convert_to_word.py`, `convert_to_excel.py`, `convert_to_xmind.py`, `convert_to_json.py`, `convert_to_csv.py`, `convert_to_markdown.py`
  - Batch convert: `batch_convert_templates.py` (outputs into `artifacts/`)

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
