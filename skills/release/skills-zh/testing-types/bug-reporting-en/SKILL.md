---
name: bug-reporting-en
description: Use this skill when you need to write clear, reproducible bug reports with steps, environment details, and evidence; triggers include bug reporting and defect reporting.
---

# Bug Reporting

**中文版：** 见技能 `bug-reporting`。

Prompts: see `prompts/bug-reporting_EN.md` in this directory.

## When to Use

- User mentions **bug reporting**, **defect reporting**, **bug report**, or **defect report**
- Need to write or optimize defect reports
- **Trigger:** e.g. "Help me write a bug report" or "Optimize this bug description"

## Output Format Options

This skill **defaults to Markdown output** (consistent with Standard-version template). For other formats, specify at the **end** of your request:

| Format | Description | How to Request (Example) |
|--------|-------------|--------------------------|
| **Markdown** | Default, easy to read and version control | No need to specify |
| **Jira** | Jira format with custom fields | "Please output in Jira format" |
| **GitHub Issues** | GitHub Issues format | "Please output in GitHub Issues format" |
| **Excel** | Tab-separated, paste into Excel | "Please output as tab-separated table for Excel" |
| **CSV** | Comma-separated, header row first | "Please output in CSV format" |
| **JSON** | Easy for program parsing | "Please output in JSON format" |

See **[output-formats.md](output-formats.md)** for detailed specifications and examples.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/bug-reporting_EN.md](prompts/bug-reporting_EN.md)** — Bug reporting Standard-version prompts
- **[output-formats.md](output-formats.md)** — Markdown / Jira / GitHub / Excel / CSV / JSON request instructions

## Code Examples

This skill provides the following real code examples:

1. **[Bug Report Templates and Examples](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-bug-reporting-examples-bug-report-templates.md)** - Complete defect report template collection
   - 10+ real bug report examples
   - Multiple format templates (Markdown, Jira, GitHub)
   - Best practices and anti-pattern comparisons
   - Automated report generation scripts

2. **Screenshot and Log Collection Tools** (coming soon)
3. **Bug Report Quality Checker** (coming soon)

Check [examples](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-bug-reporting-examples.md) directory for more examples.

## Common Pitfalls

- ❌ **Unclear title** → ✅ Use concise, clear title with key information
- ❌ **Missing reproduction steps** → ✅ Provide detailed, reproducible steps
- ❌ **No environment info** → ✅ Include OS, browser, version, etc.
- ❌ **Just saying "doesn't work"** → ✅ Describe difference between expected and actual behavior
- ❌ **No attachments** → ✅ Add screenshots, videos, log files
- ❌ **Emotional descriptions** → ✅ Maintain objective, professional tone
- ❌ **Multiple issues in one report** → ✅ Report each defect separately

## Best Practices

### 1. Title Writing

**Good Titles**:
- ✅ `[Login] Login fails with special character password`
- ✅ `[Cart] Total price not updated after deleting item`
- ✅ `[iOS] App crashes on iPhone 12 at startup`

**Bad Titles**:
- ❌ `Login has problem`
- ❌ `Bug`
- ❌ `This doesn't work`

### 2. Reproduction Steps

Use numbered list, clear and specific:

```markdown
## Reproduction Steps

1. Open app and login (username: test@example.com)
2. Click "Cart" icon
3. Add item A to cart (price: $100)
4. Add item B to cart (price: $200)
5. Click "Delete" button next to item A
6. Observe total price display

## Expected Result
Total price should update to $200 (only item B)

## Actual Result
Total price still shows $300 (not updated)
```

### 3. Environment Information

Provide complete environment info:

```markdown
## Test Environment

- **OS**: macOS 13.5
- **Browser**: Chrome 120.0.6099.109
- **App Version**: v2.3.1
- **Test Environment**: Staging (https://staging.example.com)
- **User Role**: Regular user
- **Network**: WiFi
- **Screen Resolution**: 1920x1080
```

### 4. Severity and Priority

**Severity**:
- **Critical**: System crash, data loss, security vulnerability
- **High**: Core functionality unusable
- **Medium**: Functionality works but has obvious issues
- **Low**: UI issues, text errors

**Priority**:
- **P0**: Fix immediately (blocks release)
- **P1**: Fix ASAP (within this week)
- **P2**: Plan to fix (within this iteration)
- **P3**: Can defer (next iteration)

### 5. Attachments and Evidence

- 📸 **Screenshots**: Annotate key areas
- 🎥 **Videos**: Show operation process
- 📄 **Logs**: Console logs, error logs
- 🔗 **Links**: Related docs, similar issues

### 6. Impact Scope

Describe the problem's impact:

```markdown
## Impact Scope

- **Affected Users**: All users using cart
- **Occurrence Rate**: 100% (happens every time item is deleted)
- **Business Impact**: Users may pay wrong amount, leading to complaints
- **Workaround**: Total price displays correctly after page refresh
```

## Troubleshooting

### Issue 1: Defect marked as "Cannot Reproduce"

**Symptom**: Developers cannot reproduce the problem you reported

**Solution**:
1. Provide more detailed reproduction steps
2. Record video showing the problem
3. Provide test data and accounts
4. Check if it's environment-specific
5. Reproduce together with developers

**Improved Example**:
```markdown
## Reproduction Steps (Detailed Version)

**Preconditions**:
- Use test account: test@example.com / Test123!
- Cart already has 2 items
- Browser cache and cookies cleared

**Detailed Steps**:
1. Open Chrome browser (version 120+)
2. Visit https://staging.example.com
3. Click "Login" button in top right
4. Enter email: test@example.com
5. Enter password: Test123!
6. Click "Login" button
7. Wait for page redirect to homepage (about 2 seconds)
8. Click cart icon in top right (shows number 2)
9. On cart page, find first item
10. Click red "Delete" button on right side of that item
11. Observe total price display in top right

**Expected**: Total price changes from $300 to $200
**Actual**: Total price still shows $300

**Attachments**: 
- Video: bug-reproduction.mp4
- Console log: console-log.txt
```

### Issue 2: Defect report considered unclear

**Symptom**: Multiple back-and-forth communications needed to understand the problem

**Solution**:
1. Use 5W1H principle (What, When, Where, Who, Why, How)
2. Add screenshots and annotate key areas
3. Use comparison table to show expected vs actual
4. Provide specific data examples

**Improved Example**:
```markdown
## Problem Description

**What (What problem)**: Users cannot login with special character passwords

**When (When it occurs)**: 
- First discovered: 2024-02-06 14:30
- Occurrence frequency: Every time using password with `@#$%`

**Where (Where)**: 
- Page: Login page (https://example.com/login)
- Component: Password input field

**Who (Who is affected)**: 
- All users with special character passwords
- Estimated 15% of users affected (based on password policy)

**Why (Why it matters)**: 
- Password policy requires special characters
- Users cannot login leads to churn

**How (How it manifests)**:
| Password Type | Example | Can Login |
|--------------|---------|-----------|
| Letters only | `abcdefgh` | ✅ Yes |
| Letters+numbers | `abc12345` | ✅ Yes |
| Contains `@` | `abc@1234` | ❌ No |
| Contains `#` | `abc#1234` | ❌ No |
| Contains `$` | `abc$1234` | ❌ No |
```

### Issue 3: Don't know how to determine severity

**Symptom**: Unsure whether to mark as High or Medium

**Solution**:

Use decision tree:

```
1. Does it cause system crash/data loss/security issue?
   Yes → Critical
   No → Continue

2. Does it affect core business process?
   Yes → High
   No → Continue

3. Is there a workaround?
   No → High
   Yes → Continue

4. Does it affect user experience?
   Severely → Medium
   Slightly → Low
```

### Issue 4: Bug report too long, nobody reads it

**Symptom**: Report is very detailed but developers say it's too long

**Solution**:

Use "inverted pyramid" structure:

```markdown
# [Login] Special character password login fails

## 🔴 Quick Summary (30-second read)
Cannot login with passwords containing `@#$%` special characters.
Affects 15% of users, no workaround.

## 📋 Core Information
- **Severity**: High
- **Impact**: All users with special character passwords
- **Frequency**: 100%
- **Environment**: All browsers

## 🔄 Quick Reproduction (3 steps)
1. Visit login page
2. Enter password `Test@123`
3. Click login → Fails

---

## 📖 Detailed Information (expand when needed)

<details>
<summary>Detailed Reproduction Steps</summary>

1. Open browser...
2. ...(detailed steps)

</details>

<details>
<summary>Environment Information</summary>

- OS: macOS 13.5
- Browser: Chrome 120
- ...

</details>

<details>
<summary>Technical Details</summary>

Console error:
```
Error: Invalid character in password field
```

</details>
```

### Issue 5: Don't know how to describe intermittent issues

**Symptom**: Problem occurs sometimes but not always, hard to describe

**Solution**:

Record multiple observations:

```markdown
## Problem Description
Login functionality fails intermittently

## Observation Log

| Time | Result | Environment | Notes |
|------|--------|-------------|-------|
| 2024-02-06 10:00 | ✅ Success | Chrome | First attempt |
| 2024-02-06 10:05 | ❌ Failed | Chrome | Second attempt |
| 2024-02-06 10:10 | ❌ Failed | Chrome | Third attempt |
| 2024-02-06 10:15 | ✅ Success | Chrome | Fourth attempt |
| 2024-02-06 14:00 | ❌ Failed | Firefox | First attempt |

## Pattern Analysis
- **Failure Rate**: 60% (6/10 attempts)
- **Possible Related Factors**:
  - Time: Higher failure rate in morning
  - Network: More likely to fail on WiFi
  - Load: May be related to server load

## Possible Root Cause Hypotheses
1. Server timeout when load is high
2. Network instability causes request failure
3. Session management issue
```

### Issue 6: Defect marked as "Working as Designed"

**Symptom**: You think it's a bug, but told it's expected behavior

**Solution**:

1. Reference requirements docs or design specs
2. Explain user experience issues
3. Provide competitor comparisons
4. Suggest improvement solutions

```markdown
## Problem Description
Deleting cart item requires double confirmation, affects user experience

## Why This Is a Problem

**User Experience Perspective**:
- User expectation: Direct delete after clicking (with undo)
- Actual experience: Need to click twice, increases operation cost
- Competitor comparison: Taobao, JD all use direct delete + undo

**Data Support**:
- User research: 85% of users think double confirmation is redundant
- Operation data: 60% of users pause over 3 seconds at confirmation dialog

**Suggested Solutions**:
1. Direct delete, provide "Undo" button (recommended)
2. Only confirm when deleting multiple items
3. Add "Don't show again" option

## References
- Requirements doc: PRD-2024-001 Section 3.2
- Design spec: Figma link
- Competitor analysis: attached-competitor-analysis.pdf
```

### Issue 7: Don't know how to report performance issues

**Symptom**: Page is "slow" but don't know how to quantify

**Solution**:

Provide performance metrics:

```markdown
## Problem Description
Homepage loading speed too slow

## Performance Data

**Test Method**: Chrome DevTools Performance panel

**Test Results**:
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| FCP (First Contentful Paint) | 3.2s | <1.8s | ❌ Over |
| LCP (Largest Contentful Paint) | 5.8s | <2.5s | ❌ Over |
| TTI (Time to Interactive) | 7.2s | <3.8s | ❌ Over |
| Total Blocking Time | 850ms | <200ms | ❌ Over |

**Network Conditions**: Fast 3G (simulated)

**Performance Bottlenecks**:
1. Main thread blocked 2.3s (JavaScript execution)
2. Images not optimized (total size 4.5MB)
3. CDN not used
4. Gzip compression not enabled

**Attachments**:
- Performance report: performance-report.json
- Network screenshot: network-waterfall.png
- Lighthouse report: lighthouse-report.html
```

### Get More Help

If the issue is still unresolved:
1. Check [FAQ.md](references/local/FAQ.md)
2. Check example README.md files
3. Reference bug report templates
4. Consult team's test lead

**Related Skills:** manual-testing-en, test-case-writing-en, test-reporting-en, functional-testing-en.

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
