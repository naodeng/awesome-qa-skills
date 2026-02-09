---
name: requirements-analysis-en
version: 2.0.0
last-updated: 2024-02-06
description: Analyze requirement documents, identify test points, boundary conditions, dependencies. Support user stories, use cases, PRD formats. Default output Markdown; can request Excel/CSV/JSON. Use for requirements analysis.
category: testing-types
level: intermediate
tags: [requirements, analysis, test-points, coverage, quality]
dependencies: []
recommended-with: [test-case-writing-en, test-strategy-en, functional-testing-en]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop, api]
  methodologies: [agile, waterfall, user-story, use-case]
  formats: [prd, user-story, brd, frd]
output-formats: [markdown, excel, csv, json, mindmap]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# Requirements Analysis (English)

**中文版：** See skill `requirements-analysis`.

Prompt: this directory's `prompts/requirements-analysis_EN.md`.

## When to Use

- User mentions **requirements analysis**, **test point identification**
- Need to extract test points from requirement documents
- **Trigger examples:** "Analyze test points for this requirement" or "Identify boundary conditions in requirements"

## Output Format Options

This skill **defaults to Markdown**. To get another format, add at the **end** of your request.

## Reference Files

- **[prompts/requirements-analysis_EN.md](prompts/requirements-analysis_EN.md)** — Requirements analysis prompt
- **[output-formats.md](output-formats.md)** — Format instructions

## Code Examples

1. **[Requirements Analysis Templates](examples/requirements-analysis-templates/)** - Requirements analysis examples and templates

## Common Pitfalls

- ❌ **Only looking at surface functionality** → ✅ Deeply analyze implicit requirements and boundary conditions
- ❌ **Ignoring non-functional requirements** → ✅ Focus on performance, security, usability, etc.
- ❌ **Missing exception scenarios** → ✅ Identify all possible exception cases
- ❌ **Lacking priority** → ✅ Mark test point priorities

## Best Practices

### 1. Requirements Analysis Framework (5W1H)

```markdown
## What (What is it)
- Feature description
- Business goals
- User value

## Who (Who uses it)
- Target users
- User roles
- Permission requirements

## When (When)
- Trigger conditions
- Time constraints
- Frequency requirements

## Where (Where)
- Usage scenarios
- Environment requirements
- Platform limitations

## Why (Why)
- Business reasons
- Problem solving
- Value proposition

## How (How to implement)
- Implementation approach
- Technical solution
- Interaction flow
```

### 2. Test Point Identification

**Test Point Types**:
- Functional test points
- UI test points
- Data test points
- Performance test points
- Security test points
- Compatibility test points

**Identification Methods**:
- Equivalence partitioning
- Boundary value analysis
- Decision table
- State transition diagram
- Use case analysis
- User story mapping

### 3. Boundary Condition Analysis

**Boundary Types**:
- Input boundaries (min/max values, length limits)
- Output boundaries (result ranges, data formats)
- Time boundaries (timeout, expiration, scheduling)
- Quantity boundaries (count limits, capacity)
- Permission boundaries (role-based access control)

**Analysis Techniques**:
- On-point testing (exact boundary value)
- Off-point testing (just inside/outside boundary)
- Edge case testing (extreme values)

### 4. Dependency Analysis

**Dependency Types**:
- Data dependencies (input/output relationships)
- Functional dependencies (feature interactions)
- System dependencies (external services, APIs)
- Environmental dependencies (OS, browser, device)

### 5. Risk Assessment

**Risk Categories**:
- High: Critical business impact, high probability
- Medium: Moderate impact or probability
- Low: Minor impact, low probability

**Risk Factors**:
- Complexity of implementation
- Frequency of use
- Business criticality
- Technical uncertainty

## Troubleshooting

### Issue 1: Unclear Requirements

**Symptoms:** Requirements are ambiguous, incomplete, or contradictory

**Solution:**
1. List unclear points with specific questions:
   - What is the expected behavior when...?
   - What are the valid input ranges?
   - What should happen in error cases?
2. Communicate with product manager/stakeholders
3. Document clarification results
4. Update requirement documents
5. Get written confirmation of changes

**Prevention:**
- Use structured requirement templates
- Include acceptance criteria
- Add concrete examples
- Define edge cases explicitly

### Issue 2: Missing Test Points

**Symptoms:** Test coverage is incomplete, important scenarios overlooked

**Solution:**
Use comprehensive checklist:
- [ ] Normal scenarios (happy path)
- [ ] Exception scenarios (error handling)
- [ ] Boundary values (min/max/edge cases)
- [ ] Permission validation (role-based access)
- [ ] Data validation (format, type, range)
- [ ] Performance requirements (response time, throughput)
- [ ] Security requirements (authentication, authorization, encryption)
- [ ] Compatibility (browsers, devices, OS)
- [ ] Usability (accessibility, user experience)
- [ ] Integration points (APIs, external services)

**Techniques:**
- Mind mapping for visual coverage
- Traceability matrix (requirements → test points)
- Peer review of analysis
- Use test design techniques systematically

### Issue 3: Conflicting Requirements

**Symptoms:** Requirements contradict each other or are mutually exclusive

**Solution:**
1. Document all conflicts clearly
2. Analyze impact of each option
3. Present trade-offs to stakeholders
4. Facilitate decision-making meeting
5. Update requirements with final decision
6. Communicate changes to all parties

### Issue 4: Non-Functional Requirements Overlooked

**Symptoms:** Only functional requirements analyzed, missing performance/security/usability

**Solution:**
1. Use NFR checklist:
   - Performance (response time, throughput, scalability)
   - Security (authentication, authorization, data protection)
   - Usability (accessibility, user experience, learnability)
   - Reliability (availability, fault tolerance, recovery)
   - Maintainability (code quality, documentation, testability)
   - Compatibility (browsers, devices, platforms)
2. Ask specific NFR questions for each feature
3. Define measurable NFR criteria
4. Include NFR in test planning

### Issue 5: Inadequate Stakeholder Input

**Symptoms:** Analysis based on assumptions, lacking validation from stakeholders

**Solution:**
1. Schedule requirements review sessions
2. Prepare specific questions and scenarios
3. Use prototypes or mockups for validation
4. Document stakeholder feedback
5. Iterate analysis based on input
6. Get sign-off on final analysis

### Issue 6: Analysis Paralysis

**Symptoms:** Spending too much time on analysis, delaying testing

**Solution:**
1. Set time limits for analysis phase
2. Focus on high-priority requirements first
3. Use iterative approach (analyze → test → refine)
4. Accept that some details will emerge during testing
5. Document assumptions and move forward
6. Schedule follow-up reviews

### Get More Help

If the issue persists:
1. Check [FAQ.md](../../../FAQ.md)
2. Review example templates in examples/ directory
3. Search [GitHub Issues](https://github.com/your-repo/awesome-qa-skills/issues)
4. Submit a new Issue with detailed information

**Related skills:** test-case-writing-en, test-strategy-en, functional-testing-en.
