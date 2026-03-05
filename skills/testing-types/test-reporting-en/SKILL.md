---
name: test-reporting-en
description: Use this skill when you need to generate test reports with summary, metrics, defect analysis, and risk assessment; triggers include test reporting and QA status report.
---

# Test Reporting

**中文版：** 见技能 `test-reporting`。

Prompts: see `prompts/test-reporting_EN.md` in this directory.

## When to Use

- User mentions **test reporting**, **test summary**, or **test report**
- Need to generate test reports or test summaries
- **Trigger:** e.g. "Generate test report" or "Write Sprint test summary"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/test-reporting_EN.md](prompts/test-reporting_EN.md)** — Test reporting prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **Test Report Templates (Planned)** - Various test report templates

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
