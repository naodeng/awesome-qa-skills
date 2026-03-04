---
name: requirements-analysis-en
description: Use this skill when you need to analyze requirements, identify test points, boundaries, dependencies, and risks before test design; triggers include requirements analysis and test point analysis.
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

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/requirements-analysis_EN.md](prompts/requirements-analysis_EN.md)** — Requirements analysis prompt
- **[output-formats.md](output-formats.md)** — Format instructions

## Code Examples

1. **Requirements Analysis Templates (Planned)** - Requirements analysis examples and templates

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

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
