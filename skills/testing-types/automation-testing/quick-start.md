# 自动化测试快速上手指南

5 分钟快速掌握自动化测试技能的使用方法。

## 📋 前置条件

- 了解基本的编程知识（Python/Java/JavaScript）
- 熟悉 Web 应用基础（HTML、CSS、DOM）
- 安装 Python 3.7+ 或其他编程语言环境

## 🚀 快速开始

### 步骤 1：选择自动化工具

根据你的项目需求选择合适的工具：

| 工具 | 语言 | 适用场景 | 学习曲线 |
|------|------|---------|---------|
| Selenium | 多语言 | Web UI 自动化 | 中等 |
| Playwright | JS/Python | 现代 Web 应用 | 低 |
| Cypress | JavaScript | 前端开发 | 低 |
| Appium | 多语言 | 移动应用 | 高 |
| Robot Framework | Python | 关键字驱动 | 低 |

**推荐新手：** Selenium + Python（生态成熟、资料丰富）

### 步骤 2：运行示例项目

我们提供了一个完整的 Selenium + POM 示例：

```bash
# 1. 进入示例目录
cd skills/testing-types/automation-testing/examples/selenium-pom-python

# 2. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行测试
pytest

# 5. 生成 HTML 报告
pytest --html=reports/report.html --self-contained-html
```

**预期输出：**
```
======================== test session starts =========================
collected 20 items

tests/test_login.py ............                              [ 60%]
tests/test_product.py ........                                [100%]

======================== 20 passed in 45.23s =========================
```

### 步骤 3：理解 Page Object Model

查看示例代码理解 POM 设计模式：

**1. 基础页面类** (`pages/base_page.py`)
```python
class BasePage:
    """所有页面对象的基类"""
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
```

**2. 页面对象** (`pages/login_page.py`)
```python
class LoginPage(BasePage):
    # 元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
```

**3. 测试用例** (`tests/test_login.py`)
```python
def test_valid_login(self):
    # 业务逻辑清晰，无需关心页面实现
    self.login_page.open().login("standard_user", "secret_sauce")
    assert self.home_page.is_loaded()
```

### 步骤 4：使用 AI 生成测试用例

1. **打开提示词文件**
   ```bash
   cat prompts/automation-testing.md
   ```

2. **复制虚线以下的内容到 AI 对话**

3. **附加你的需求**，例如：
   ```
   为以下登录页面生成自动化测试用例：
   
   页面元素：
   - 用户名输入框：id="username"
   - 密码输入框：id="password"
   - 登录按钮：id="login-btn"
   - 错误消息：class="error-message"
   
   测试场景：
   - 有效登录
   - 无效用户名
   - 无效密码
   - 空凭证
   
   使用 Selenium + Python + Pytest
   ```

4. **AI 将生成**：
   - 完整的测试用例代码
   - Page Object 类
   - Pytest fixtures
   - 断言语句

## 📝 实战示例

### 示例 1：创建登录测试

**需求：**
```
为电商网站登录功能创建自动化测试

URL: https://example.com/login
元素：
- 用户名：#username
- 密码：#password
- 登录按钮：#login-button
- 记住我：#remember-me

测试场景：
1. 有效登录
2. 无效凭证
3. 记住我功能
4. 密码可见性切换

使用 Page Object Model 设计模式
```

**AI 输出：** 完整的 POM 实现 + 测试用例

### 示例 2：创建表单填写测试

**需求：**
```
为用户注册表单创建自动化测试

表单字段：
- 姓名、邮箱、密码、确认密码、手机号
- 性别（单选）、兴趣（多选）
- 同意条款（复选框）

验证规则：
- 邮箱格式验证
- 密码强度验证
- 两次密码一致性
- 必填字段验证

使用数据驱动测试
```

**AI 输出：** 包含数据驱动、参数化测试的完整代码

## 🎯 核心概念

### 1. 元素定位策略

优先级顺序：
```python
# 1. ID（最优）
element = driver.find_element(By.ID, "username")

# 2. Name
element = driver.find_element(By.NAME, "email")

# 3. CSS Selector
element = driver.find_element(By.CSS_SELECTOR, ".login-button")

# 4. XPath（最后选择）
element = driver.find_element(By.XPATH, "//button[@id='login']")
```

### 2. 等待策略

```python
# ❌ 不推荐：固定等待
import time
time.sleep(5)

# ✅ 推荐：显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))

# ✅ 推荐：隐式等待（全局设置）
driver.implicitly_wait(10)
```

### 3. Page Object Model 原则

```python
# ✅ 好的实践
class LoginPage(BasePage):
    # 1. 元素定位器作为类常量
    USERNAME_INPUT = (By.ID, "username")
    
    # 2. 方法返回 self 支持链式调用
    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)
        return self
    
    # 3. 不在页面类中写断言
    def is_error_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)

# ❌ 不好的实践
class LoginPage:
    def login(self, username, password):
        # 硬编码定位器
        driver.find_element(By.ID, "username").send_keys(username)
        # 在页面类中写断言
        assert driver.find_element(By.ID, "welcome").is_displayed()
```

## 🔧 常用命令速查

### Pytest 命令

```bash
# 运行所有测试
pytest

# 运行特定文件
pytest tests/test_login.py

# 运行特定测试
pytest tests/test_login.py::TestLogin::test_valid_login

# 显示详细输出
pytest -v -s

# 生成 HTML 报告
pytest --html=reports/report.html --self-contained-html

# 并行运行（需要 pytest-xdist）
pytest -n 4

# 运行标记的测试
pytest -m smoke

# 失败时停止
pytest -x

# 重新运行失败的测试
pytest --lf
```

### Selenium 常用操作

```python
# 浏览器操作
driver.get("https://example.com")
driver.refresh()
driver.back()
driver.forward()
driver.maximize_window()

# 元素操作
element.click()
element.send_keys("text")
element.clear()
element.submit()

# 获取信息
element.text
element.get_attribute("value")
element.is_displayed()
element.is_enabled()
element.is_selected()

# 截图
driver.save_screenshot("screenshot.png")

# 切换
driver.switch_to.frame(frame_element)
driver.switch_to.default_content()
driver.switch_to.alert.accept()
```

## 📊 测试报告

### HTML 报告

```bash
# 生成报告
pytest --html=reports/report.html --self-contained-html

# 查看报告
open reports/report.html
```

### Allure 报告（推荐）

```bash
# 安装
pip install allure-pytest

# 生成数据
pytest --alluredir=reports/allure-results

# 查看报告
allure serve reports/allure-results
```

## 🎓 进阶学习

### 1. 数据驱动测试

```python
import pytest

@pytest.mark.parametrize("username,password,expected", [
    ("valid_user", "valid_pass", True),
    ("invalid_user", "invalid_pass", False),
    ("", "", False),
])
def test_login(username, password, expected):
    result = login_page.login(username, password)
    assert result == expected
```

### 2. 使用 Fixtures

```python
@pytest.fixture(scope="function")
def logged_in_user(driver):
    """自动登录的用户"""
    login_page = LoginPage(driver)
    login_page.open().login("user", "pass")
    return HomePage(driver)

def test_with_logged_in_user(logged_in_user):
    # 测试已登录状态的功能
    assert logged_in_user.is_loaded()
```

### 3. 失败时自动截图

```python
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")
```

### 4. 并行执行

```bash
# 安装
pip install pytest-xdist

# 并行运行
pytest -n 4  # 4 个进程
pytest -n auto  # 自动检测 CPU 核心数
```

## ❓ 遇到问题？

1. **查看故障排除章节**：[SKILL.md#故障排除](SKILL.md#故障排除)
2. **查看示例代码**：[examples/selenium-pom-python/](examples/selenium-pom-python/)
3. **参考官方文档**：
   - [Selenium 文档](https://www.selenium.dev/documentation/)
   - [Pytest 文档](https://docs.pytest.org/)
   - [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## 🎯 下一步

- ✅ 完成快速上手
- 📖 阅读完整的 [SKILL.md](SKILL.md)
- 🔨 运行示例项目
- 🚀 为你的项目创建自动化测试
- 🤖 使用 AI 提示词生成更多测试用例
- 📚 学习进阶主题（数据驱动、并行执行、CI/CD 集成）

## 📚 推荐资源

- [Selenium 官方文档](https://www.selenium.dev/documentation/)
- [Pytest 官方文档](https://docs.pytest.org/)
- [Page Object Model 设计模式](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [测试练习网站](https://www.saucedemo.com) - 用于练习自动化测试

---

**预计学习时间：** 5-10 分钟  
**难度级别：** 初级到中级  
**最后更新：** 2026-02-06
