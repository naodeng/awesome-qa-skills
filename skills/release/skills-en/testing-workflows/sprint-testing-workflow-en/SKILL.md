---
name: sprint-testing-workflow-en
description: Use this skill when you need a sprint-based QA workflow from planning through review and retrospective; triggers include sprint testing workflow and sprint QA flow.
---

# Sprint Testing Workflow

**中文版：** 见技能 `sprint-testing-workflow`。

Complete testing workflow for a 2-week sprint. Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **sprint testing**, **iteration planning**, or **sprint retrospective**
- Need phase-by-phase sprint testing (planning → review → retrospective)
- **Trigger:** e.g. “Help me plan sprint testing” or “Walk me through the sprint test flow”

**Phases:** Day 1 Planning → Days 2–3 Setup & early testing → Days 4–8 Active testing → Days 9–10 Intensive (regression, integration, visual) → Day 11 Stabilization → Day 12 Review & demo → Day 13 Retrospective & next sprint.

---

## Day 1: Sprint Planning

### ☑️ Morning·Planning Meeting Checklist

- [ ] **Pre-meeting preparation**
  - [ ] Review product backlog
  - [ ] Analyze upcoming user stories
  - [ ] Use prompts: test-strategy

- [ ] **Meeting participation**
  - [ ] Understand acceptance criteria
  - [ ] Identify testable requirements
  - [ ] Estimate testing effort
  - [ ] Mark testing dependencies

### ☑️ Afternoon·Test Planning Checklist

- [ ] **Test strategy development**
  - [ ] Create test strategy document
  - [ ] Define test scope
  - [ ] Determine environment requirements
  - [ ] Plan test data needs
  - [ ] Identify automation candidates
  - [ ] Use prompts: test-strategy, requirements-analysis

- [ ] **Deliverables completion**
  - [ ] Sprint number and basic info
  - [ ] User story list
  - [ ] Test focus and priorities
  - [ ] Automation plan
  - [ ] Risk assessment

## Days 2–3: Setup & Early Testing

### ☑️ Environment Setup Checklist

- [ ] **Test environment preparation**
  - [ ] Set up test environment
  - [ ] Configure CI/CD pipeline
  - [ ] Prepare test data
  - [ ] Verify environment availability
  - [ ] Use prompts: automation-testing, test-strategy

### ☑️ Early Testing Checklist

- [ ] **Test case creation**
  - [ ] Generate test cases for early completed stories
  - [ ] Review cases with development team
  - [ ] Use prompts: test-case-writing

- [ ] **Exploratory testing**
  - [ ] Perform exploratory testing on completed work
  - [ ] Record discovered issues
  - [ ] Use prompts: manual-testing

## Days 4–8: Active Development & Testing

### ☑️ Daily Activities Checklist

- [ ] **Daily standup**
  - [ ] Report yesterday's completed work
  - [ ] State today's plan
  - [ ] Raise blockers and issues

- [ ] **Manual testing**
  - [ ] Execute test cases for completed stories
  - [ ] Explore new features
  - [ ] Record discovered defects
  - [ ] Use prompts: manual-testing, bug-reporting

- [ ] **Automation test development**
  - [ ] Write automation tests for completed stories
  - [ ] Code review and optimization
  - [ ] Integrate into CI/CD
  - [ ] Use prompts: automation-testing, api-testing

- [ ] **Defect management**
  - [ ] Review new defects
  - [ ] Define priorities with team
  - [ ] Regression test fixed defects
  - [ ] Update defect status

### ☑️ Days 5–6·Mid-Sprint Review Checklist

- [ ] **Progress review**
  - [ ] Review test execution progress
  - [ ] Adjust test plan if necessary
  - [ ] Identify risky stories
  - [ ] Update automation coverage

- [ ] **Key metrics check**
  - [ ] Test execution rate
  - [ ] Defect discovery rate
  - [ ] Automation coverage
  - [ ] Story completion vs test completion comparison

## Days 9–10: Intensive Testing

### ☑️ Regression Testing Checklist

- [ ] **Automated regression**
  - [ ] Execute full automated regression suite
  - [ ] Analyze failed cases
  - [ ] Fix or update tests
  - [ ] Use prompts: functional-testing, ai-assisted-testing

- [ ] **Manual regression**
  - [ ] Execute critical path manual tests
  - [ ] Cross-browser testing
  - [ ] Mobile testing
  - [ ] Use prompts: functional-testing

### ☑️ Integration Testing Checklist

- [ ] **End-to-end testing**
  - [ ] Test complete user journeys
  - [ ] Verify system integration
  - [ ] Test data flows
  - [ ] Verify third-party integrations
  - [ ] Use prompts: functional-testing, api-testing

### ☑️ Visual Testing Checklist

- [ ] **UI and accessibility testing**
  - [ ] Visual regression testing
  - [ ] UI change verification
  - [ ] Responsive design testing
  - [ ] Accessibility testing
  - [ ] Use prompts: accessibility-testing

## Day 11: Stabilization

### ☑️ Bug Bash Checklist

- [ ] **Optional: Bug bash activity**
  - [ ] Organize 2-hour focused testing
  - [ ] Use exploratory testing charters
  - [ ] Record discovered issues
  - [ ] Use prompts: manual-testing

### ☑️ Final Defect Handling Checklist

- [ ] **Defect priority handling**
  - [ ] Critical defects must be fixed
  - [ ] High priority defects assessed
  - [ ] Medium/low priority defects moved to backlog

### ☑️ Completion Check Checklist

- [ ] **Sprint completion verification**
  - [ ] All stories tested
  - [ ] Critical defects fixed and regressed
  - [ ] Regression tests passed
  - [ ] Automation tests updated
  - [ ] Test report generated

## Day 12: Review & Demo

### ☑️ Review Preparation Checklist

- [ ] **Test report preparation**
  - [ ] Create executive summary
  - [ ] Compile defect metrics
  - [ ] Calculate automation coverage
  - [ ] Prepare quality dashboard
  - [ ] Use prompts: test-reporting, test-strategy

### ☑️ Review Meeting Checklist

- [ ] **Results presentation**
  - [ ] Present testing achievements
  - [ ] Share quality metrics
  - [ ] Explain known issues
  - [ ] Assess next sprint risks
  - [ ] Demo automation and coverage

## Day 13: Retrospective & Next Sprint Prep

### ☑️ Retrospective Meeting Checklist

- [ ] **Retrospective discussion**
  - [ ] Discuss what went well in testing
  - [ ] Identify challenges encountered
  - [ ] Propose process improvements
  - [ ] Create action items for next sprint

- [ ] **Specialized discussion**
  - [ ] Automation test effectiveness
  - [ ] Defect discovery timing
  - [ ] Environment and tool issues

### ☑️ Next Sprint Preparation Checklist

- [ ] **Forward planning**
  - [ ] Review upcoming stories
  - [ ] Identify testing challenges
  - [ ] Plan automation needs
  - [ ] Update test strategy

---

## How to Use

1. Check [reference.md](reference.md) to find the prompt file for the current step.
2. Open the corresponding file in `prompts/`, then combine it with the current context (scope, environment, risks, constraints).
3. Run step by step, and update priorities or gates based on outputs and blockers.

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
