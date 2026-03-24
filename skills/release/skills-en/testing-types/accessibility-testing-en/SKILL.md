---
name: accessibility-testing-en
description: Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include accessibility testing and a11y testing.
---

# Accessibility Testing (English)

**中文版:** See skill `accessibility-testing`.

Prompt: this directory's `prompts/accessibility-testing_EN.md`.

## When to Use

- User mentions **accessibility testing**, **a11y**, **WCAG**
- Need to design accessibility test strategy, cases, or plan based on WCAG standards
- **Trigger examples:** "Design accessibility test cases for the following requirements" or "Create WCAG 2.1 compliance test plan"

## Output Format Options

This skill **defaults to Markdown** (Standard-version template). To get another format, add one of the following at the **end** of your request:

| Format | Description | How to request (example) |
|--------|-------------|--------------------------|
| **Markdown** | Default; good for reading and version control | No extra instruction |
| **Excel** | Tab-separated, paste into Excel | "Please output as tab-separated table for pasting into Excel" |
| **CSV** | Comma-separated, header row first | "Please output as CSV" |
| **JSON** | For tooling/parsing | "Please output as JSON" |

Details and examples: **[output-formats.md](output-formats.md)** in this directory.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/accessibility-testing_EN.md](prompts/accessibility-testing_EN.md)** — Accessibility testing Standard-version prompt
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON request instructions

## Code Examples

This skill provides the following real-world code examples:

1. **[axe-core + Playwright Automation Testing](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-accessibility-testing-examples-axe-playwright.md)** - Complete accessibility automation test suite
   - 12 test cases
   - Covers WCAG 2.1 Level A/AA
   - Includes automation and manual testing guides
   - Detailed violation reports

2. **WCAG 2.1 Manual Testing Checklist** (Coming soon)
3. **Screen Reader Testing Guide** (Coming soon)

See [examples/](references/local/Users-nao.deng-awsomeCode-awesome-qa-skills-skills-testing-types-accessibility-testing-examples.md) directory for more examples.

## Common Pitfalls

- ❌ **Only relying on automation tools** → ✅ Combine automation tools (30% coverage) with manual testing (70% coverage)
- ❌ **Ignoring keyboard navigation** → ✅ Ensure all functionality is accessible via keyboard
- ❌ **Insufficient color contrast** → ✅ Use tools to check contrast, ensure at least 4.5:1 (normal text)
- ❌ **Missing alternative text** → ✅ Provide meaningful alt text for all images and icons
- ❌ **Missing form labels** → ✅ Ensure all form controls have associated labels
- ❌ **Only testing after development** → ✅ Consider accessibility during design and development phases

## Best Practices

1. **WCAG Compliance**
   - Follow WCAG 2.1 Level AA standards (minimum requirement)
   - Use automation tools to detect common issues
   - Conduct manual testing for complex interactions
   - Test with real assistive technologies

2. **Testing Strategy**
   - Integrate automated accessibility testing in CI/CD
   - Conduct regular manual testing and user testing
   - Use multiple tools for cross-validation
   - Track and monitor accessibility issues

3. **Key Test Points**
   - Keyboard navigation (Tab, Enter, Esc, Arrow keys)
   - Screen reader compatibility (NVDA, JAWS, VoiceOver)
   - Color contrast and visual design
   - Form accessibility
   - Semantic HTML
   - Correct ARIA attribute usage

4. **Tool Selection**
   - axe-core: Automated testing (most comprehensive)
   - Lighthouse: Quick audit
   - WAVE: Visual issue identification
   - Screen readers: Real user experience

5. **Documentation and Reporting**
   - Clearly document violations and severity
   - Provide fix suggestions and code examples
   - Track fix progress
   - Generate regular compliance reports

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
