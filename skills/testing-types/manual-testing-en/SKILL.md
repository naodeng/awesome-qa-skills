---
name: manual-testing-en
description: Use this skill when you need to plan manual or exploratory testing with charters, heuristics, and session records; triggers include manual testing and exploratory testing.
---

# Manual/Exploratory Testing

**中文版：** 见技能 `manual-testing`。

Prompts: see `prompts/manual-testing_EN.md` in this directory.

## When to Use

- User mentions **manual testing**, **exploratory testing**, or **session-based testing**
- Need to design manual testing approach or exploratory testing charters
- **Trigger:** e.g. "Design exploratory testing charter" or "Create manual testing plan"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/manual-testing_EN.md](prompts/manual-testing_EN.md)** — Manual testing prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **Exploratory Testing Charter Templates (Planned)** - Test charters and session record templates

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
