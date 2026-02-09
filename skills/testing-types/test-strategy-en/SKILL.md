---
name: test-strategy-en
version: 2.0.0
last-updated: 2024-02-06
description: Develop comprehensive test strategy including test scope, methods, resources, risks. Supports agile, waterfall, and other development models. Default output: Markdown, can request Excel/CSV/JSON. Use for test strategy.
category: testing-types
level: advanced
tags: [strategy, planning, management, risk, quality]
dependencies: [requirements-analysis-en]
recommended-with: [test-case-writing-en, test-reporting-en, functional-testing-en]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop, api, embedded]
  methodologies: [agile, waterfall, devops, continuous-testing]
  team-sizes: [solo, small, medium, large]
output-formats: [markdown, excel, csv, json, pdf]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# Test Strategy

**中文版：** 见技能 `test-strategy`。

Prompts: see `prompts/test-strategy.md` in this directory.

## When to Use

- User mentions **test strategy**, **test plan**, **quality strategy**, or **test planning**
- Need to develop test strategy or plan for a project
- **Trigger:** e.g. "Develop test strategy for this project" or "Write test plan document"

## Output Format Options

This skill **defaults to Markdown output** (consistent with Standard-version template). For other formats, specify at the **end** of your request:

| Format | Description | How to Request (Example) |
|--------|-------------|--------------------------|
| **Markdown** | Default, easy to read and version control | No need to specify |
| **Excel** | Tab-separated, paste into Excel | "Please output as tab-separated table for Excel" |
| **PDF** | Formal document format | "Please output in PDF format" |
| **JSON** | Easy for program parsing | "Please output in JSON format" |

See **[output-formats.md](output-formats.md)** for detailed specifications and examples.

## How to Use Prompts in This Skill

1. Open `prompts/test-strategy.md` in this directory, copy content below the dashed line to AI conversation.
2. Attach your project information and requirements.
3. For Excel/PDF/JSON, add the request sentence from output-formats.md at the end.

## Reference Files

- **[prompts/test-strategy.md](prompts/test-strategy.md)** — Test strategy Standard-version prompts
- **[output-formats.md](output-formats.md)** — Markdown / Excel / PDF / JSON request instructions

## Code Examples

This skill provides the following real code examples:

1. **[Test Strategy Template Collection](examples/test-strategy-templates/)** - Complete test strategy templates
   - Agile project test strategy
   - Waterfall project test strategy
   - Mobile app test strategy
   - API test strategy
   - Microservices test strategy
   - Risk assessment matrix
   - Resource planning templates

2. **Strategy Generation Tools** (coming soon)
3. **Risk Assessment Tools** (coming soon)

Check [examples/](examples/) directory for more examples.

## Common Pitfalls

- ❌ **Strategy too generic** → ✅ Develop specific strategy for project characteristics
- ❌ **Ignoring risk assessment** → ✅ Identify and assess testing risks
- ❌ **Insufficient resource planning** → ✅ Specify personnel, time, tool requirements
- ❌ **Missing metrics** → ✅ Define clear quality goals and measurements
- ❌ **Strategy never changes** → ✅ Adjust strategy based on project progress
- ❌ **Only focus on functional testing** → ✅ Cover performance, security, compatibility, etc.
- ❌ **No exit criteria** → ✅ Define clear test completion and release criteria

## Best Practices

### 1. Test Strategy Core Elements

**Complete test strategy should include**:

```markdown
# Test Strategy Document

## 1. Project Overview
- Project background
- Project goals
- Project scope

## 2. Test Objectives
- Quality goals
- Coverage goals
- Performance goals

## 3. Test Scope
- Included features
- Excluded features
- Test types

## 4. Test Approach
- Test levels (unit/integration/system/acceptance)
- Test types (functional/performance/security/compatibility)
- Test techniques (black-box/white-box/gray-box)

## 5. Test Environment
- Hardware requirements
- Software requirements
- Network requirements
- Test data

## 6. Test Tools
- Test management tools
- Automation tools
- Performance testing tools
- Defect management tools

## 7. Resource Planning
- Staffing
- Schedule
- Budget estimation

## 8. Risk Management
- Risk identification
- Risk assessment
- Mitigation measures

## 9. Test Deliverables
- Test plan
- Test cases
- Test reports
- Defect reports

## 10. Entry/Exit Criteria
- Test start conditions
- Test completion conditions
- Release criteria
```

### 2. Test Pyramid Strategy

```
        /\
       /  \  E2E Tests (10%)
      /____\
     /      \
    / Integration \ (30%)
   /    Tests     \
  /______________\
 /                \
/  Unit Tests (60%) \
/____________________\
```

**Layered Testing Strategy**:
- **Unit Tests (60%)**: Fast, stable, low cost
- **Integration Tests (30%)**: Verify module interactions
- **End-to-End Tests (10%)**: Verify critical business flows

### 3. Risk-Driven Testing

**Risk Assessment Matrix**:

| Feature Module | Business Impact | Technical Complexity | Change Frequency | Risk Level | Test Priority |
|---------------|-----------------|---------------------|-----------------|------------|---------------|
| Payment | High | High | Low | High | P0 |
| Login | High | Medium | Low | High | P0 |
| Search | Medium | High | Medium | Medium | P1 |
| Recommendation | Medium | High | High | Medium | P1 |
| Comments | Low | Low | Low | Low | P2 |

**Risk Level Calculation**:
```
Risk Level = (Business Impact + Technical Complexity + Change Frequency) / 3
```

### 4. Agile Testing Strategy

**Sprint Testing Activities**:

```markdown
## Sprint Planning (Day 1)
- [ ] Participate in Sprint Planning
- [ ] Understand user stories
- [ ] Identify testing tasks
- [ ] Estimate testing effort

## Sprint Execution (Day 2-9)
- [ ] Write test cases
- [ ] Execute exploratory testing
- [ ] Automate regression tests
- [ ] Track defects

## Sprint Review (Day 10)
- [ ] Demo test results
- [ ] Collect feedback
- [ ] Update test strategy

## Sprint Retrospective (Day 10)
- [ ] Summarize testing experience
- [ ] Identify improvement points
- [ ] Update best practices
```

### 5. Test Type Coverage

**Comprehensive Test Types**:

| Test Type | Goal | Tools | Frequency |
|-----------|------|-------|-----------|
| Unit Testing | Code quality | Jest, Pytest | Every commit |
| Integration Testing | Module interaction | Postman, Pytest | Daily build |
| Functional Testing | Business functionality | Playwright, Selenium | Every Sprint |
| Performance Testing | Response time, throughput | K6, JMeter | Every release |
| Security Testing | Vulnerability scanning | OWASP ZAP | Every release |
| Compatibility Testing | Cross-browser, devices | BrowserStack | Before release |
| Accessibility Testing | WCAG compliance | axe-core | Before release |
| Exploratory Testing | Discover unknown issues | Manual | Continuous |

### 6. Automation Strategy

**Automation Decision Tree**:

```
Is the test repeatedly executed?
  No → Manual testing
  Yes ↓

Is the test stable?
  No → Manual testing
  Yes ↓

Automation cost < Manual cost?
  No → Manual testing
  Yes → Automated testing
```

**Automation Priority**:
1. **High Priority**: Smoke tests, regression tests, API tests
2. **Medium Priority**: Functional tests, integration tests
3. **Low Priority**: Exploratory tests, usability tests

### 7. Test Metrics

**Key Metrics**:

```markdown
## Process Metrics
- Test case count
- Test execution rate
- Automation coverage
- Defect discovery rate

## Quality Metrics
- Defect density (defects/KLOC)
- Defect escape rate
- Defect fix time
- Test pass rate

## Efficiency Metrics
- Test execution time
- Automation time saved
- Test ROI
- Team productivity
```

## Troubleshooting

### Issue 1: Don't know how to start developing strategy

**Symptom**: Facing new project, don't know where to start

**Solution**:

Use **5W2H Analysis**:

```markdown
## Test Strategy Analysis

### What (What to test)
- Functional requirements
- Non-functional requirements
- Business processes
- User experience

### Why (Why test)
- Quality assurance
- Risk control
- User satisfaction
- Compliance requirements

### Who (Who tests)
- Test team
- Development team
- Business team
- End users

### When (When to test)
- Unit testing: Development phase
- Integration testing: Integration phase
- System testing: Testing phase
- Acceptance testing: Before release

### Where (Where to test)
- Development environment
- Test environment
- Pre-production environment
- Production environment

### How (How to test)
- Manual testing
- Automated testing
- Exploratory testing
- Performance testing

### How Much (How much to invest)
- Personnel: X people
- Time: Y weeks
- Budget: Z dollars
- Tools: List
```

### Issue 2: Test scope unclear

**Symptom**: Unsure what needs testing and what doesn't

**Solution**:

Create **Test Scope Matrix**:

```markdown
## Test Scope Definition

### In Scope
| Feature Module | Test Types | Priority | Owner |
|---------------|------------|----------|-------|
| User Login | Functional, Security, Performance | P0 | John |
| Product Search | Functional, Performance | P1 | Jane |
| Order Payment | Functional, Security, Integration | P0 | Bob |

### Out of Scope
| Item | Reason | Notes |
|------|--------|-------|
| Third-party payment internal logic | External system | Only test integration points |
| Historical data migration | One-time task | Handled by DBA |
| Admin backend (old version) | Being deprecated | No longer maintained |

### Assumptions & Dependencies
- Test environment ready before Sprint starts
- Test data provided by development team
- Third-party APIs available in test environment
```

### Issue 3: Insufficient resources, cannot complete all testing

**Symptom**: Limited time, personnel, budget

**Solution**:

Adopt **Risk-Based Testing**:

```markdown
## Risk-Driven Test Priority

### High-Risk Areas (Must Test)
- Payment flow
- User authentication
- Data security
- Core business logic

### Medium-Risk Areas (Should Test)
- Search functionality
- Recommendation algorithm
- Notification system
- Report generation

### Low-Risk Areas (Optional Test)
- UI beautification
- Help documentation
- Statistical analysis
- Logging

### Resource Allocation
- High risk: 60% resources
- Medium risk: 30% resources
- Low risk: 10% resources
```

### Issue 4: Test strategy disconnected from reality

**Symptom**: Strategy document looks good but cannot be executed

**Solution**:

Develop **Executable Strategy**:

```markdown
## Executable Test Strategy

### Daily Activities
- [ ] 09:00 - Standup sync test progress
- [ ] 09:30 - Execute smoke tests
- [ ] 10:00 - Execute new feature tests
- [ ] 14:00 - Defect verification and regression
- [ ] 17:00 - Update test report

### Weekly Activities
- [ ] Monday: Sprint Planning, identify testing tasks
- [ ] Wednesday: Test progress check
- [ ] Friday: Sprint Review, demo test results

### Per Sprint Activities
- [ ] Sprint start: Create test plan
- [ ] Sprint mid: Execute tests, track defects
- [ ] Sprint end: Test summary, retrospective

### Checkpoints
- [ ] Complete smoke test within 30 min after code commit
- [ ] Complete functional test within 2 hours after user story completion
- [ ] Complete regression test 1 day before Sprint end
```

### Issue 5: Test strategy for different environments

**Symptom**: Don't know what testing to do in different environments

**Solution**:

**Environment Testing Matrix**:

```markdown
## Environment Testing Strategy

### Development Environment (Dev)
- **Purpose**: Quick verification of code changes
- **Test Types**: Unit tests, smoke tests
- **Frequency**: Every code commit
- **Automation**: 100%

### Test Environment (QA)
- **Purpose**: Comprehensive functional testing
- **Test Types**: Functional, integration, regression
- **Frequency**: Daily build
- **Automation**: 80%

### Pre-production Environment (Staging)
- **Purpose**: Production environment simulation
- **Test Types**: End-to-end, performance, security
- **Frequency**: Before release
- **Automation**: 60%

### Production Environment (Production)
- **Purpose**: Monitoring and verification
- **Test Types**: Smoke tests, monitoring
- **Frequency**: After release, continuous monitoring
- **Automation**: 100%
```

### Issue 6: How to develop strategy in agile projects

**Symptom**: Agile projects change fast, strategy hard to develop

**Solution**:

Adopt **Lightweight Agile Testing Strategy**:

```markdown
## Agile Testing Strategy

### Testing Quadrants

**Quadrant 1: Technology-facing, Supporting the Team**
- Unit tests
- Component tests
- Automation first

**Quadrant 2: Business-facing, Supporting the Team**
- Functional tests
- User story tests
- Example-driven

**Quadrant 3: Business-facing, Critique Product**
- Exploratory testing
- Usability testing
- User acceptance testing

**Quadrant 4: Technology-facing, Critique Product**
- Performance testing
- Security testing
- Maintainability testing

### Testing Activities in Sprint

**Sprint Planning**:
- Participate in user story discussion
- Identify testing tasks
- Define acceptance criteria

**Daily Standup**:
- Sync test progress
- Identify blocking issues
- Adjust test plan

**Sprint Review**:
- Demo test results
- Collect feedback
- Verify acceptance criteria

**Sprint Retrospective**:
- Review testing process
- Identify improvement points
- Update testing practices
```

### Issue 7: How to measure test strategy effectiveness

**Symptom**: Don't know if strategy is effective

**Solution**:

Define **Test Strategy KPIs**:

```markdown
## Test Strategy Effectiveness Metrics

### Quality Metrics
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Production defects | < 5/month | 3/month | ✅ |
| Defect escape rate | < 5% | 3% | ✅ |
| Critical defects | 0 | 0 | ✅ |
| Customer complaints | < 2/month | 1/month | ✅ |

### Efficiency Metrics
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Test automation rate | > 80% | 85% | ✅ |
| Test execution time | < 2h | 1.5h | ✅ |
| Defect fix time | < 2 days | 1.5 days | ✅ |
| Release frequency | 2 weeks | 2 weeks | ✅ |

### Coverage Metrics
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Requirements coverage | 100% | 100% | ✅ |
| Code coverage | > 80% | 85% | ✅ |
| Automation coverage | > 70% | 75% | ✅ |

### Improvement Suggestions
- ✅ Quality metrics met, continue maintaining
- ⚠️  Consider increasing release frequency to weekly
- 💡 Explore AI-assisted testing to improve efficiency
```

### Get More Help

If the issue is still unresolved:
1. Check [FAQ.md](../../../FAQ.md)
2. Check example README.md files
3. Reference test strategy templates
4. Consult team's test manager

**Related Skills:** requirements-analysis-en, test-case-writing-en, test-reporting-en, functional-testing-en.
