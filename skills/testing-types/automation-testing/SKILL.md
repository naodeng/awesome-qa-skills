---
name: automation-testing
version: 2.0.0
description: 默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 自动化测试 or automation-testing.
tags: [automation, testing, selenium, pom, page-object-model, pytest]
difficulty: intermediate
last_updated: 2026-02-06
---

# 自动化测试（中文版）

**英文版：** 见技能 `automation-testing-en`。

提示词见本目录 `prompts/automation-testing.md`。

## 何时使用

- 用户提到「自动化测试」「automation-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/automation-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的具体需求。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 代码示例

### 1. Selenium + Page Object Model (Python)

完整的 POM 设计模式实现，包含登录、产品管理等功能测试。

**位置：** `examples/selenium-pom-python/`

**包含内容：**
- 完整的 Page Object Model 架构
- 基础页面类（BasePage）
- 登录页面、首页页面对象
- 15+ 个测试用例
- Pytest 配置和 fixtures
- 自动截图功能
- HTML 测试报告

**快速开始：**
```bash
cd examples/selenium-pom-python
pip install -r requirements.txt
pytest
```

**测试覆盖：**
- 登录功能（有效/无效凭证、锁定用户）
- 产品列表显示
- 购物车操作（添加/移除商品）
- 产品排序功能
- 参数化测试

详见：[examples/selenium-pom-python/README.md](examples/selenium-pom-python/README.md)

## 最佳实践

### 自动化测试设计原则

1. **测试金字塔**
   - 单元测试（70%）：快速、稳定、低成本
   - 集成测试（20%）：测试模块间交互
   - UI 测试（10%）：端到端业务流程

2. **Page Object Model (POM)**
   - 页面元素和操作封装在页面类中
   - 测试用例只关注业务逻辑
   - 提高代码复用和可维护性

3. **等待策略**
   - 避免使用固定等待（time.sleep）
   - 使用显式等待（WebDriverWait）
   - 合理设置隐式等待时间

4. **测试数据管理**
   - 使用配置文件管理测试数据
   - 使用 fixtures 提供测试数据
   - 测试后清理数据

5. **测试独立性**
   - 每个测试应该独立运行
   - 不依赖其他测试的执行顺序
   - 使用 setup/teardown 管理测试环境

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| Selenium | Web UI 自动化 | 跨浏览器、多语言支持 |
| Playwright | 现代 Web 应用 | 快速、稳定、多浏览器 |
| Cypress | 前端开发者 | 易用、实时重载、调试友好 |
| Appium | 移动应用 | 跨平台、原生/混合应用 |
| Robot Framework | 关键字驱动 | 易读、非技术人员友好 |

### POM 设计模式最佳实践

```python
# ✅ 好的实践
class LoginPage(BasePage):
    # 元素定位器作为类常量
    USERNAME_INPUT = (By.ID, "username")
    
    def login(self, username, password):
        # 方法返回 self 支持链式调用
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

# ❌ 不好的实践
class LoginPage:
    def login(self, username, password):
        # 硬编码定位器
        driver.find_element(By.ID, "username").send_keys(username)
        # 在页面类中写断言
        assert driver.find_element(By.ID, "welcome").is_displayed()
```

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

## 参考文件

- **prompts/automation-testing.md** — 自动化测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/selenium-pom-python/** — Selenium + POM 完整示例
- **quick-start.md** — 5 分钟快速上手指南
