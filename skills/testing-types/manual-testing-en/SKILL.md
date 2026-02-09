---
name: manual-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design manual and exploratory testing approaches with test charters, heuristic methods, session records. Default output: Markdown, can request Excel/CSV/JSON. Use for manual testing or exploratory testing.
category: testing-types
level: intermediate
tags: [manual, exploratory, charter, heuristic, session]
dependencies: []
recommended-with: [functional-testing-en, bug-reporting-en, test-case-writing-en]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop, api]
  approaches: [scripted, exploratory, session-based]
  techniques: [tours, heuristics, personas]
output-formats: [markdown, excel, csv, json]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# Manual/Exploratory Testing

**中文版：** 见技能 `manual-testing`。

Prompts: see `prompts/manual-testing.md` in this directory.

## When to Use

- User mentions **manual testing**, **exploratory testing**, or **session-based testing**
- Need to design manual testing approach or exploratory testing charters
- **Trigger:** e.g. "Design exploratory testing charter" or "Create manual testing plan"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## Reference Files

- **[prompts/manual-testing.md](prompts/manual-testing.md)** — Manual testing prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **[Exploratory Testing Charter Templates](examples/exploratory-testing-charters/)** - Test charters and session record templates

## Common Pitfalls

- ❌ **Random testing without plan** → ✅ Use test charters to guide exploration
- ❌ **Not recording test process** → ✅ Detailed session recording
- ❌ **Ignoring heuristic methods** → ✅ Apply testing heuristics
- ❌ **Missing time-boxing** → ✅ Set clear time limits

## Best Practices

### 1. Exploratory Testing Charter

```markdown
## Test Charter

**Goal**: Explore login functionality security
**Scope**: Login page and authentication flow
**Time**: 90 minutes
**Tester**: John Doe

**Exploration Focus**:
- SQL injection vulnerabilities
- XSS attacks
- Brute force protection
- Session management

**Test Data**:
- Special characters
- SQL statements
- Script code
- Extra-long strings
```

### 2. Testing Heuristics (SFDPOT)

- **Structure**: Test system structure
- **Function**: Test functionality implementation
- **Data**: Test data processing
- **Platform**: Test platform compatibility
- **Operations**: Test operation flow
- **Time**: Test time-related aspects

### 3. Testing Tours

- **Business District Tour**: Test core business features
- **Historical District Tour**: Test legacy features
- **Entertainment District Tour**: Test fun features
- **Tourist District Tour**: Test help and documentation
- **Saboteur Tour**: Try to break the system

## Troubleshooting

### Issue 1: Don't know where to start exploring

**Solution**:
Use test charter template:
```markdown
**Explore**: [Feature/Area]
**Using**: [Tools/Methods]
**To Discover**: [Issues/Risks]
```

### Issue 2: Low exploratory testing efficiency

**Solution**:
1. Set time-box (60-90 minutes)
2. Use heuristic methods
3. Record test notes
4. Regular review and summary

**Related Skills:** functional-testing-en, bug-reporting-en, test-case-writing-en.
