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

