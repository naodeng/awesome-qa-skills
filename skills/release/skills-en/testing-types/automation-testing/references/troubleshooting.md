## 故障排除

### 常见问题

#### 1. 元素找不到 (NoSuchElementException)

**问题：** 测试运行时找不到页面元素

**解决方案：**
```python
# 使用显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))

# 或增加隐式等待时间
driver.implicitly_wait(10)
```

#### 2. 元素不可点击 (ElementClickInterceptedException)

**问题：** 元素被其他元素遮挡

**解决方案：**
```python
# 等待元素可点击
wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()

# 或使用 JavaScript 点击
driver.execute_script("arguments[0].click();", element)

# 或滚动到元素
driver.execute_script("arguments[0].scrollIntoView(true);", element)
```

#### 3. StaleElementReferenceException

**问题：** 页面刷新后元素引用失效

**解决方案：**
```python
# 重新查找元素
def safe_click(locator):
    for _ in range(3):
        try:
            element = driver.find_element(*locator)
            element.click()
            break
        except StaleElementReferenceException:
            time.sleep(0.5)
```

#### 4. 浏览器驱动版本不匹配

**问题：** `SessionNotCreatedException: session not created`

**解决方案：**
```bash
# 使用 webdriver-manager 自动管理驱动
pip install webdriver-manager

# 在代码中使用
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

#### 5. 测试运行缓慢

**问题：** 测试执行时间过长

**解决方案：**
- 使用无头模式：`options.add_argument("--headless")`
- 并行运行测试：`pytest -n 4`
- 减少不必要的等待时间
- 优化定位器（优先使用 ID、Name）

#### 6. 测试不稳定（Flaky Tests）

**问题：** 测试有时通过有时失败

**解决方案：**
- 增加等待时间
- 使用显式等待替代隐式等待
- 检查测试数据依赖
- 确保测试独立性
- 添加重试机制：`@pytest.mark.flaky(reruns=3)`

#### 7. 截图功能不工作

**问题：** 测试失败时没有生成截图

**解决方案：**
```python
# 在 conftest.py 中添加钩子
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")
```

