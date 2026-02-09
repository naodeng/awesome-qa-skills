---
name: test-reporting-en
version: 2.0.0
last-updated: 2024-02-06
description: Generate professional test reports with executive summary, metrics, defect analysis, risk assessment. Supports daily, weekly, release reports. Default output: Markdown, can request Excel/CSV/JSON/PDF. Use for test reporting.
category: testing-types
level: intermediate
tags: [reporting, metrics, dashboard, summary, analysis]
dependencies: []
recommended-with: [test-strategy-en, bug-reporting-en, test-case-writing-en]
context-aware: true
context-patterns:
  report-types: [daily, weekly, sprint, release, executive]
  audiences: [team, management, stakeholders]
  formats: [summary, detailed, dashboard]
output-formats: [markdown, excel, csv, json, pdf, html]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# Test Reporting

**中文版：** 见技能 `test-reporting`。

Prompts: see `prompts/test-reporting.md` in this directory.

## When to Use

- User mentions **test reporting**, **test summary**, or **test report**
- Need to generate test reports or test summaries
- **Trigger:** e.g. "Generate test report" or "Write Sprint test summary"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## Reference Files

- **[prompts/test-reporting.md](prompts/test-reporting.md)** — Test reporting prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **[Test Report Templates](examples/test-report-templates/)** - Various test report templates

## Common Pitfalls

- ❌ **Only data without analysis** → ✅ Provide insights and recommendations
- ❌ **Report too lengthy** → ✅ Highlight key points, layered presentation
- ❌ **Missing visualizations** → ✅ Use charts to show trends
- ❌ **No action items** → ✅ Specify follow-up actions

## Best Practices

### 1. Report Structure

```markdown
# Test Report

## 1. Executive Summary
- Test overview
- Key findings
- Quality assessment
- Recommendations

## 2. Test Execution
- Execution statistics
- Coverage
- Pass rate

## 3. Defect Analysis
- Defect statistics
- Severity distribution
- Trend analysis

## 4. Risks and Issues
- Current risks
- Blocking issues
- Mitigation measures

## 5. Next Steps
- Pending work
- Improvement suggestions
- Action items
```

### 2. Key Metrics

**Execution Metrics**:
- Total test cases
- Executed count
- Pass rate
- Failure rate

**Quality Metrics**:
- Defect density
- Defect escape rate
- Fix time
- Reopen rate

**Efficiency Metrics**:
- Automation rate
- Execution time
- Productivity

## Troubleshooting

### Issue 1: Report too long, nobody reads it

**Solution**:
Use pyramid structure:
1. Executive summary (1 page)
2. Key metrics (1 page)
3. Detailed data (appendix)

### Issue 2: Data inaccurate

**Solution**:
1. Use test management tools
2. Automate data collection
3. Regularly validate data

**Related Skills:** test-strategy-en, bug-reporting-en, test-case-writing-en.
