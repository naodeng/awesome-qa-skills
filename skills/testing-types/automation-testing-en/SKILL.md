---
name: automation-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design automation test plans including POM, data-driven, BDD patterns. Default output Markdown; can request Excel/CSV/JSON. Use for automation testing.
category: testing-types
level: intermediate
tags: [automation, selenium, playwright, cypress, pom, bdd, data-driven]
dependencies: [functional-testing-en]
recommended-with: [api-testing-en, functional-testing-en, test-case-writing-en]
context-aware: true
context-patterns:
  project-types: [web, mobile, api]
  frameworks: [selenium, playwright, cypress, appium, webdriverio]
  test-frameworks: [pytest, junit, testng, jest, mocha]
  patterns: [page-object-model, data-driven, bdd, keyword-driven]
output-formats: [markdown, excel, csv, json, code]
examples-count: 3
has-tutorial: false
has-troubleshooting: true
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

1. Open `prompts/automation-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your specific input.
3. For Excel/CSV/JSON, append the request line from output-formats.md.

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

See: [examples/selenium-pom-python/README.md](../automation-testing/examples/selenium-pom-python/README.md)

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

## Troubleshooting

### Common Issues

#### 1. Element Not Found (NoSuchElementException)

**Problem:** Cannot find page element during test execution

**Solution:**
```python
# Use explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))

# Or increase implicit wait time
driver.implicitly_wait(10)
```

#### 2. Element Not Clickable (ElementClickInterceptedException)

**Problem:** Element is obscured by other elements

**Solution:**
```python
# Wait for element to be clickable
wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()

# Or use JavaScript click
driver.execute_script("arguments[0].click();", element)

# Or scroll to element
driver.execute_script("arguments[0].scrollIntoView(true);", element)
```

#### 3. StaleElementReferenceException

**Problem:** Element reference becomes stale after page refresh

**Solution:**
```python
# Re-find the element
def safe_click(locator):
    for _ in range(3):
        try:
            element = driver.find_element(*locator)
            element.click()
            break
        except StaleElementReferenceException:
            time.sleep(0.5)
```

#### 4. Browser Driver Version Mismatch

**Problem:** `SessionNotCreatedException: session not created`

**Solution:**
```bash
# Use webdriver-manager to auto-manage drivers
pip install webdriver-manager

# Use in code
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

#### 5. Slow Test Execution

**Problem:** Tests take too long to execute

**Solution:**
- Use headless mode: `options.add_argument("--headless")`
- Run tests in parallel: `pytest -n 4`
- Reduce unnecessary wait times
- Optimize locators (prioritize ID, Name)

#### 6. Flaky Tests

**Problem:** Tests sometimes pass, sometimes fail

**Solution:**
- Increase wait times
- Use explicit waits instead of implicit waits
- Check test data dependencies
- Ensure test independence
- Add retry mechanism: `@pytest.mark.flaky(reruns=3)`

#### 7. Screenshot Functionality Not Working

**Problem:** No screenshots generated when tests fail

**Solution:**
```python
# Add hook in conftest.py
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")
```

## Reference Files

- **prompts/automation-testing_EN.md** — Automation testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/selenium-pom-python/** — Complete Selenium + POM example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, functional-testing-en, test-case-writing-en, performance-testing-en.
