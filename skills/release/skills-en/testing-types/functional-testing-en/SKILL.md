---
name: functional-testing-en
description: Use this skill when you need to design functional test plans or cases for business flows, UI, data, and integrations; triggers include functional testing and functional test cases.
---

# Functional Testing (English)

**中文版：** See skill `functional-testing`.

Prompt: this directory’s `prompts/functional-testing_EN.md`.

## When to Use

- User mentions **functional testing**, **functional test cases**, **functional test plan**
- Need to design functional test strategy, cases, or plan from requirements/specs
- **Trigger:** e.g. “Design functional test cases for the following requirements” or “Create a functional test plan”

## Output Format Options

This skill **defaults to Markdown** (Standard-version template). To get another format, add one of the following at the **end** of your request:

| Format | Description | How to request (example) |
|--------|-------------|--------------------------|
| **Markdown** | Default; good for reading and version control | No extra instruction |
| **Excel** | Tab-separated, paste into Excel | “Please output as tab-separated table for pasting into Excel” |
| **CSV** | Comma-separated, header row first | “Please output as CSV” |
| **JSON** | For tooling/parsing | “Please output as JSON” |

Details and examples: **[output-formats.md](output-formats.md)** in this directory.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/functional-testing_EN.md](prompts/functional-testing_EN.md)** — Functional testing Standard-version prompt
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON request instructions

## Code Examples

This skill provides the following real-world code examples:

1. **[Playwright Login Testing](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-functional-testing-examples-playwright-login.md)** - Complete login functionality test suite
   - 14 test cases
   - Coverage: functionality, accessibility, security
   - Includes best practices and troubleshooting

2. **Cypress Form Testing** (Coming soon)
3. **Selenium Navigation Testing** (Coming soon)

See [examples](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-functional-testing-examples.md) directory for more examples.

## Common Pitfalls

- ❌ **Skip requirements analysis and write cases directly** → ✅ Use requirements-analysis skill first to analyze requirements and identify test points
- ❌ **Only test normal scenarios** → ✅ Cover exception scenarios, boundary values, and error handling
- ❌ **Unclear case descriptions** → ✅ Use clear steps and expected results to ensure reproducibility
- ❌ **Ignore accessibility testing** → ✅ Include keyboard navigation, screen reader validation
- ❌ **Hardcode test data** → ✅ Use test data management strategy for maintainability

## Best Practices

1. **Test Design**
   - Use equivalence partitioning and boundary value analysis
   - Follow AAA pattern (Arrange-Act-Assert)
   - Keep tests independent, avoid dependencies

2. **Element Location**
   - Prioritize data-testid attributes
   - Avoid volatile CSS class names
   - Use semantic locators

3. **Assertion Strategy**
   - Use multiple specific assertions rather than single vague assertion
   - Verify key business logic
   - Include user experience validation

4. **Maintainability**
   - Use Page Object Model design pattern
   - Extract reusable test utility functions
   - Keep test code clean

5. **Execution Efficiency**
   - Run independent tests in parallel
   - Use appropriate wait strategies
   - Avoid unnecessary delays

## Troubleshooting

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.

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
