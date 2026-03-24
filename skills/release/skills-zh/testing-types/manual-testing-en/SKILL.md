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
