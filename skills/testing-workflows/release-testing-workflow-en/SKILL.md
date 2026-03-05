---
name: release-testing-workflow-en
description: Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include release testing workflow and release readiness testing.
---

# Release Testing Workflow

**中文版：** 见技能 `release-testing-workflow`。

End-to-end release testing (1–2 weeks before release through post-release). Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **release testing**, **Go/No-Go**, or **release readiness**
- Need timeline: T-14 planning → T-7 feature freeze → T-5–T-4 specialized testing → T-3 RC → T-2 quality assessment → T-1 Go/No-Go → T-day release → T+1–T+7 post-release
- **Trigger:** e.g. “How do we schedule pre-release testing?” or “Go/No-Go checklist”

## How to Use

1. Check [reference.md](reference.md) to find the prompt file for the current step.
2. Open the corresponding file in `prompts/`, then combine it with the current context (scope, environment, risks, constraints).
3. Run step by step, and update priorities or gates based on outputs and blockers.

## Common Pitfalls

- ❌ Adding features after T-7 → ✅ Feature freeze: only defect fixes; non-critical code freeze
- ❌ Releasing without Go/No-Go → ✅ Release only after gates pass, team alignment, and rollback readiness
- ❌ No post-release monitoring → ✅ T+1 intensive monitoring and fast response; follow incident procedures

## Best Practices

- T-14: use test strategy and requirements prompts for release plan and risk assessment
- T-2: use test reporting and test strategy for quality gates and known-issue assessment
- Before deploy: confirm rollback tested, communication plan and support brief ready
- **Principle:** When in doubt, delay release.

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** daily-testing-workflow-en, sprint-testing-workflow-en.


---

## T-14: Release Planning

### ☑️ Planning Meeting Checklist

- [ ] **Meeting preparation**
  - [ ] Confirm participants (Product, Engineering, QA, DevOps)
  - [ ] Prepare meeting agenda
  - [ ] Use prompts: test-strategy, requirements-analysis

- [ ] **Meeting agenda execution**
  - [ ] Define release scope
  - [ ] Identify high-risk features
  - [ ] Define quality gates
  - [ ] Develop test strategy

### ☑️ Deliverables Completion Checklist

- [ ] **Documentation delivery**
  - [ ] Release test plan
  - [ ] Risk assessment document
  - [ ] Environment plan
  - [ ] Regression test scope
  - [ ] Performance test plan

## T-10 to T-8: Test Preparation

### ☑️ Environment Preparation Checklist

- [ ] **Test environment setup**
  - [ ] Set up pre-production environment
  - [ ] Prepare production-like data
  - [ ] Configure monitoring and logging
  - [ ] Create test accounts
  - [ ] Use prompts: automation-testing, test-strategy

### ☑️ Test Suite Update Checklist

- [ ] **Test suite updates**
  - [ ] Update regression test suite
  - [ ] Update performance test scripts
  - [ ] Update security test scenarios
  - [ ] Update accessibility tests
  - [ ] Update visual test baselines

### ☑️ Readiness Verification Checklist

- [ ] **Readiness validation**
  - [ ] Critical path automation ready
  - [ ] Regression tests updated
  - [ ] Performance test baseline set
  - [ ] Visual test baseline set

## T-7: Feature Freeze & Testing Acceleration

### ☑️ Feature Freeze Rules Confirmation

- [ ] **Freeze rules enforcement**
  - [ ] Confirm no new features added
  - [ ] Only allow defect fixes
  - [ ] Non-critical code freeze

### ☑️ Functional Testing Checklist

- [ ] **New feature testing**
  - [ ] Test new features
  - [ ] Test modified features
  - [ ] Test critical user journeys
  - [ ] Test integration points
  - [ ] Use prompts: functional-testing, test-case-writing

### ☑️ Regression Testing Checklist

- [ ] **Full regression execution**
  - [ ] Execute full automated regression
  - [ ] Execute critical path manual tests
  - [ ] Cross-browser testing
  - [ ] Mobile testing
  - [ ] Use prompts: functional-testing, ai-assisted-testing

### ☑️ End-to-End Testing Checklist

- [ ] **E2E test execution**
  - [ ] Test complete user journeys
  - [ ] Test multi-system integration
  - [ ] Verify data flows
  - [ ] Test third-party integrations
  - [ ] Use prompts: functional-testing

## T-5 to T-4: Specialized Testing

### ☑️ Performance Testing Checklist

- [ ] **Performance test execution**
  - [ ] Load testing
  - [ ] Stress testing
  - [ ] Spike testing
  - [ ] Endurance testing (24h+)
  - [ ] Use prompts: performance-testing

- [ ] **Performance metrics analysis**
  - [ ] Analyze P95/P99 response times
  - [ ] Check throughput
  - [ ] Analyze error rates
  - [ ] Monitor resource usage

### ☑️ Security Testing Checklist

- [ ] **Security test execution**
  - [ ] Vulnerability scanning
  - [ ] Penetration testing
  - [ ] Authentication/authorization testing
  - [ ] Encryption verification
  - [ ] Security headers check
  - [ ] Use prompts: security-testing

### ☑️ Accessibility Testing Checklist

- [ ] **Accessibility test execution**
  - [ ] Screen reader testing
  - [ ] Keyboard navigation testing
  - [ ] Contrast checking
  - [ ] ARIA attribute verification
  - [ ] Use prompts: accessibility-testing

### ☑️ Visual Testing Checklist

- [ ] **Visual test execution**
  - [ ] Visual regression testing
  - [ ] Cross-browser visual testing
  - [ ] Responsive design testing
  - [ ] UI consistency checking
  - [ ] Use prompts: accessibility-testing

## T-3: Release Candidate (RC) Testing

### ☑️ RC Deployment Checklist

- [ ] **Release candidate preparation**
  - [ ] Deploy RC to pre-production
  - [ ] Code freeze
  - [ ] Tag version

### ☑️ Smoke Testing Checklist

- [ ] **Quick smoke test (1–2 hours)**
  - [ ] Test critical features
  - [ ] Confirm no critical defects
  - [ ] Verify deployment success

### ☑️ Final Regression Checklist

- [ ] **Full regression execution**
  - [ ] Execute full automated regression
  - [ ] Execute manual critical path tests
  - [ ] Execute exploratory testing
  - [ ] Use prompts: manual-testing

### ☑️ Defect Triage Checklist

- [ ] **Defect handling decisions**
  - [ ] Critical defects: must fix → retest → new RC
  - [ ] High priority: assess risk
  - [ ] Medium/low priority: move to next version

## T-2: Quality Assessment

### ☑️ Quality Metrics Review Checklist

- [ ] **Test metrics review**
  - [ ] Test execution rate
  - [ ] Test pass rate
  - [ ] Critical/high priority defect count
  - [ ] Test coverage
  - [ ] Performance benchmark achievement
  - [ ] Use prompts: test-reporting, test-strategy

### ☑️ Quality Gate Check Checklist

- [ ] **Gate verification**
  - [ ] Critical defects fixed
  - [ ] Regression tests 100% passed
  - [ ] Performance meets SLA
  - [ ] Security scan passed
  - [ ] No unresolved P1/P2 defects
  - [ ] Accessibility compliance

### ☑️ Risk Assessment Checklist

- [ ] **Risk analysis**
  - [ ] Known issues and workarounds
  - [ ] Load test performance
  - [ ] Third-party dependency risks
  - [ ] Rollback plan readiness

## T-1: Go/No-Go

### ☑️ Go/No-Go Meeting Checklist

- [ ] **Meeting preparation**
  - [ ] Confirm participants (Product, Engineering, QA, DevOps, Leadership)
  - [ ] Prepare meeting materials

- [ ] **Meeting review content**
  - [ ] Test summary
  - [ ] Defect status and trends
  - [ ] Performance test results
  - [ ] Security test results
  - [ ] Known risks
  - [ ] Rollback plan

### ☑️ GO Decision Criteria Check

- [ ] **GO conditions verification**
  - [ ] Quality gates passed
  - [ ] No critical unresolved defects
  - [ ] Performance acceptable
  - [ ] Team confident
  - [ ] Rollback plan ready

### ☑️ NO-GO Risk Identification

- [ ] **NO-GO conditions check**
  - [ ] Are there critical defects
  - [ ] Did quality gates fail
  - [ ] Are there performance issues
  - [ ] Are there high risks
  - [ ] Does team lack confidence

### ☑️ Pre-Release Checklist

- [ ] **Release preparation verification**
  - [ ] Release notes prepared
  - [ ] Deployment runbook ready
  - [ ] Monitoring configured
  - [ ] Rollback plan tested
  - [ ] Support team briefed
  - [ ] Communication plan ready

## T-Day: Release Day

### ☑️ Pre-Deployment Checklist (2–4 hours before)

- [ ] **Final preparation**
  - [ ] RC final smoke test
  - [ ] Deployment checklist confirmation
  - [ ] Team on-call confirmation
  - [ ] Communication channels ready

### ☑️ During Deployment Monitoring Checklist

- [ ] **Real-time monitoring**
  - [ ] Monitor deployment progress
  - [ ] Monitor error logs
  - [ ] Monitor performance metrics
  - [ ] Monitor user feedback

### ☑️ Post-Deployment Verification Checklist (30–60 min)

- [ ] **Production smoke test**
  - [ ] Test critical user journeys
  - [ ] Verify authentication/authorization
  - [ ] Test payment functionality
  - [ ] Verify third-party integrations
  - [ ] Check performance

### ☑️ First 24 Hours Monitoring Checklist

- [ ] **Continuous monitoring**
  - [ ] Monitor error rate
  - [ ] Monitor response time
  - [ ] Monitor traffic
  - [ ] Monitor support tickets

### ☑️ Rollback Conditions Check

- [ ] **Rollback trigger conditions**
  - [ ] Is critical functionality broken
  - [ ] Is there severe performance degradation
  - [ ] Is there data corruption
  - [ ] Are there security vulnerabilities

## T+1 to T+7: Post-Release

### ☑️ Day 1 Checklist

- [ ] **Intensive monitoring**
  - [ ] Intensive system metrics monitoring
  - [ ] Fast issue response
  - [ ] Collect user feedback
  - [ ] Record discovered issues

### ☑️ Week 1 Checklist

- [ ] **Continuous tracking**
  - [ ] Fix post-release defects
  - [ ] Monitor trend changes
  - [ ] Collect user feedback
  - [ ] Prepare hotfix if necessary

### ☑️ Release Retrospective Checklist

- [ ] **Retrospective meeting**
  - [ ] Discuss what went well
  - [ ] Identify improvement opportunities
  - [ ] Analyze testing gaps
  - [ ] Create process improvement plan
  - [ ] Use prompts: test-reporting

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
