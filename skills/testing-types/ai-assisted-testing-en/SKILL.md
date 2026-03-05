---
name: ai-assisted-testing-en
description: Use this skill when you need AI-assisted testing workflows such as test data generation, root-cause analysis, and prioritization; triggers include AI-assisted testing and AI for QA.
---

# AI-Assisted Testing

**中文版：** 见技能 `ai-assisted-testing`。

Prompts: see `prompts/ai-assisted-testing_EN.md` in this directory.

## When to Use

- User mentions **AI-assisted testing**, **intelligent testing**, or **AI testing**
- Need to leverage AI to improve testing efficiency and quality
- **Trigger:** e.g. "Use AI to generate test data" or "AI analyze defect root cause"

## Output Format Options

This skill **defaults to Markdown output**. For other formats, specify at the **end** of your request.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/ai-assisted-testing_EN.md](prompts/ai-assisted-testing_EN.md)** — AI-assisted testing prompts
- **[output-formats.md](output-formats.md)** — Format specifications

## Code Examples

1. **AI Testing Toolkit (Planned)** - AI-assisted testing tools and scripts

## Common Pitfalls

- ❌ **Completely relying on AI** → ✅ AI assists, human decides
- ❌ **Not validating AI output** → ✅ Verify and review AI results
- ❌ **Ignoring data quality** → ✅ Ensure training data quality
- ❌ **Missing feedback loop** → ✅ Continuously optimize AI models

## Best Practices

### 1. AI-Assisted Testing Scenarios

**Test Data Generation**:
- Boundary value generation
- Exception data generation
- Large-scale data generation
- Personalized data generation

**Defect Analysis**:
- Root cause analysis
- Similar defect identification
- Defect prediction
- Impact analysis

**Test Optimization**:
- Test case prioritization
- Test suite optimization
- Regression test selection
- Resource allocation optimization

**Intelligent Recommendations**:
- Test case recommendations
- Test tool recommendations
- Test strategy recommendations
- Improvement suggestions

### 2. AI Tool Selection

| Tool Type | Purpose | Example Tools |
|-----------|---------|---------------|
| Code Generation | Generate test code | GitHub Copilot, ChatGPT |
| Data Generation | Generate test data | Faker, GPT |
| Defect Analysis | Analyze defect patterns | ML models |
| Test Optimization | Optimize test strategy | AI algorithms |

### 3. AI-Assisted Workflow

```markdown
## AI-Assisted Testing Process

1. **Requirements Analysis**
   - AI extracts test points
   - Human review and confirmation

2. **Test Case Design**
   - AI generates case drafts
   - Human optimizes and refines

3. **Data Preparation**
   - AI generates test data
   - Human validates data

4. **Execute Tests**
   - Automated execution
   - AI analyzes results

5. **Defect Analysis**
   - AI analyzes root cause
   - Human confirms fix

6. **Continuous Improvement**
   - Collect feedback
   - Optimize AI models
```

## Troubleshooting

### Issue 1: AI-generated content inaccurate

**Solution**:
1. Provide more detailed context
2. Use examples to guide AI
3. Iteratively optimize prompts
4. Human review and correction

### Issue 2: High AI tool costs

**Solution**:
1. Prioritize open-source tools
2. Use AI only in critical scenarios
3. Batch processing to reduce costs
4. Evaluate ROI

**Related Skills:** test-case-writing-en, bug-reporting-en, test-strategy-en.

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
