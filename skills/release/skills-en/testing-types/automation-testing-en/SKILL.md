---
name: automation-testing-en
description: Use this skill when you need to design automation testing approaches using patterns like POM, data-driven testing, or BDD; triggers include automation testing and test automation strategy.
---

# Automation Testing (English)

**中文版：** See skill `automation-testing`.

Prompt: this directory's `prompts/automation-testing_EN.md`.

## When to Use

- User mentions **automation testing**, **automation-testing**
- Need to execute this testing type or produce deliverables per Standard-version
- **Trigger examples:** "Generate/design/write automation test cases for the following"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Code Examples

### 1. Selenium + Page Object Model (Python)

Complete POM design pattern implementation with login, product management functionality tests.

**Location:** `../automation-testing/examples/selenium-pom-python/`

**Includes:**
- Complete Page Object Model architecture
- Base page class (BasePage)
- Login page, home page objects
- 15+ test cases
- Pytest configuration and fixtures
- Auto-screenshot functionality
- HTML test reports

**Quick Start:**
```bash
cd examples/selenium-pom-python
pip install -r requirements.txt
pytest
```

**Test Coverage:**
- Login functionality (valid/invalid credentials, locked users)
- Product list display
- Shopping cart operations (add/remove items)
- Product sorting functionality
- Parameterized tests

See: [examples/selenium-pom-python/README.md](references/local/testing-types-automation-testing-examples-selenium-pom-python-README.md)

### 2. Playwright (TypeScript)

Coming soon - Modern web automation with Playwright framework.

### 3. Cypress (JavaScript)

Coming soon - Frontend-focused E2E testing with Cypress.

## Best Practices

### Automation Test Design Principles

1. **Test Pyramid**
   - Unit tests (70%): Fast, stable, low cost
   - Integration tests (20%): Test module interactions
   - UI tests (10%): End-to-end business workflows

2. **Page Object Model (POM)**
   - Encapsulate page elements and operations in page classes
   - Test cases focus only on business logic
   - Improve code reuse and maintainability

3. **Wait Strategies**
   - Avoid fixed waits (time.sleep)
   - Use explicit waits (WebDriverWait)
   - Set reasonable implicit wait times

4. **Test Data Management**
   - Use configuration files for test data
   - Use fixtures to provide test data
   - Clean up data after tests

5. **Test Independence**
   - Each test should run independently
   - Don't depend on other tests' execution order
   - Use setup/teardown to manage test environment

### Tool Selection Guide

| Tool | Use Case | Advantages |
|------|----------|------------|
| Selenium | Web UI automation | Cross-browser, multi-language support |
| Playwright | Modern web apps | Fast, stable, multi-browser |
| Cypress | Frontend developers | Easy to use, live reload, debug-friendly |
| Appium | Mobile apps | Cross-platform, native/hybrid apps |
| Robot Framework | Keyword-driven | Readable, non-technical friendly |

### POM Design Pattern Best Practices

```python
# ✅ Good practice
class LoginPage(BasePage):
    # Element locators as class constants
    USERNAME_INPUT = (By.ID, "username")
    
    def login(self, username, password):
        # Method returns self for method chaining
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

# ❌ Bad practice
class LoginPage:
    def login(self, username, password):
        # Hardcoded locators
        driver.find_element(By.ID, "username").send_keys(username)
        # Assertions in page class
        assert driver.find_element(By.ID, "welcome").is_displayed()
```

## Common Pitfalls

- ❌ Automating unstable or unclear requirements first → ✅ Prioritize stable, high-value workflows for automation
- ❌ Overusing brittle UI selectors → ✅ Prefer resilient locators and shared selector conventions
- ❌ Mixing test logic with environment setup everywhere → ✅ Centralize setup/teardown and reusable fixtures
- ❌ Ignoring flaky-test tracking → ✅ Record flaky patterns and fix root causes before scaling coverage

## Troubleshooting

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
## Reference Files

- **prompts/automation-testing_EN.md** — Automation testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/selenium-pom-python/** — Complete Selenium + POM example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, functional-testing-en, test-case-writing-en, performance-testing-en.

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
