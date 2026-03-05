---
name: test-case-reviewer-en
description: Use this skill when you need to review test cases for completeness, clarity, maintainability, and missing scenarios; triggers include test case review and test case QA.
---

# Test Case Review

**中文版：** 见技能 `test-case-reviewer`。

Prompts: see `prompts/test-case-reviewer_EN.md` in this directory.

## When to Use

- User mentions **test case review**, **case review**, or **test case quality**
- Need to review existing test cases for quality, identify missing scenarios, and provide improvement suggestions
- **Trigger:** e.g. "Please review these test cases" or "Find gaps and risks in the cases"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/test-case-reviewer_EN.md](prompts/test-case-reviewer_EN.md)** — Test case review prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **Test Case Review Standards (Planned)** - Review checklists and standards

## Common Pitfalls

- ❌ **Only surface-level issues** → ✅ Deep analysis of coverage and quality
- ❌ **Criticism without suggestions** → ✅ Provide specific improvement recommendations
- ❌ **Ignoring maintainability** → ✅ Assess long-term maintenance costs
- ❌ **Missing priorities** → ✅ Mark issue severity levels

## Best Practices

### 1. Review Dimensions

**Completeness**:
- Requirements coverage
- Scenario coverage
- Boundary value coverage
- Exception scenario coverage

**Clarity**:
- Clear steps
- Specific data
- Verifiable results
- No ambiguity

**Maintainability**:
- Independent test cases
- Separated data
- Modular design
- Easy to update

**Efficiency**:
- Reasonable execution time
- No redundant steps
- Automation potential
- ROI assessment

### 2. Review Checklist

```markdown
## Test Case Review Checklist

### Basic Information
- [ ] Unique test case ID
- [ ] Clear title
- [ ] Priority marked
- [ ] Type marked

### Preconditions
- [ ] Complete preconditions
- [ ] Achievable preconditions
- [ ] Clear dependencies

### Test Steps
- [ ] Detailed and specific steps
- [ ] Repeatable steps
- [ ] Clear step numbering
- [ ] No missing steps

### Test Data
- [ ] Specific and clear data
- [ ] Obtainable data
- [ ] Boundary values covered
- [ ] Exception data included

### Expected Results
- [ ] Clear results
- [ ] Verifiable results
- [ ] Complete results
- [ ] No vague descriptions

### Coverage
- [ ] Normal scenarios
- [ ] Exception scenarios
- [ ] Boundary conditions
- [ ] Permission validation
```

### 3. Review Report Template

```markdown
## Test Case Review Report

**Review Date**: 2024-02-06
**Reviewer**: John Doe
**Case Count**: 50
**Review Scope**: Login Module

### Review Summary
- Overall Quality: Good
- Main Issues: Insufficient boundary value coverage
- Improvement Suggestions: Add exception scenarios

### Issue Statistics
| Severity | Count | Percentage |
|----------|-------|------------|
| Critical | 2 | 4% |
| High | 5 | 10% |
| Medium | 10 | 20% |
| Low | 8 | 16% |

### Detailed Issues

#### Critical Issues
1. **TC-001**: Missing SQL injection test
   - **Impact**: Security risk
   - **Suggestion**: Add special character tests

#### High Issues
2. **TC-005**: Incomplete boundary value testing
   - **Impact**: May miss defects
   - **Suggestion**: Add boundary value cases

### Missing Scenarios
- Concurrent login testing
- Session timeout testing
- Password complexity validation

### Improvement Suggestions
1. Add boundary value tests
2. Supplement exception scenarios
3. Optimize case descriptions
4. Add automation markers
```

## Troubleshooting

### Issue 1: Don't know how to review

**Solution**:
Use the review checklist and check item by item.

### Issue 2: Low review efficiency

**Solution**:
1. Use review tools
2. Batch review similar cases
3. Focus on high-priority cases

**Related Skills:** test-case-writing-en, test-strategy-en, requirements-analysis-en.

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
