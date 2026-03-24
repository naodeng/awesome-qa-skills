# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__automation-testing__examples__selenium-pom-python__README.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# Selenium + Page Object Model (POM) 示例

这是一个使用 Python + Selenium + Pytest 实现的 Page Object Model 设计模式示例。

## 📋 项目结构

```
selenium-pom-python/
├── README.md                 # 本文件
├── requirements.txt          # Python 依赖
├── pytest.ini               # Pytest 配置
├── conftest.py              # Pytest fixtures
├── config/
│   └── config.py            # 测试配置
├── pages/                   # Page Object 页面对象
│   ├── __init__.py
│   ├── base_page.py         # 基础页面类
│   ├── login_page.py        # 登录页面
│   ├── home_page.py         # 首页
│   └── product_page.py      # 商品页面
├── tests/                   # 测试用例
│   ├── __init__.py
│   ├── test_login.py        # 登录测试
│   ├── test_product.py      # 商品测试
│   └── test_e2e.py          # 端到端测试
├── utils/                   # 工具类
│   ├── __init__.py
│   ├── driver_factory.py    # WebDriver 工厂
│   └── logger.py            # 日志工具
└── reports/                 # 测试报告（自动生成）
```

## 🎯 设计模式说明

### Page Object Model (POM) 优势

1. **代码复用**：页面元素和操作封装在页面类中，避免重复代码
2. **易于维护**：UI 变更只需修改对应的页面类
3. **提高可读性**：测试用例更接近业务语言
4. **降低耦合**：测试逻辑与页面实现分离

### 架构层次

```
测试用例层 (tests/)
    ↓
页面对象层 (pages/)
    ↓
基础页面层 (base_page.py)
    ↓
WebDriver 层 (driver_factory.py)
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 安装浏览器驱动（自动）
# Selenium 4.x 会自动下载对应的驱动
```

### 2. 配置测试环境

编辑 `config/config.py`：

```python
# 测试环境配置
BASE_URL = "https://www.saucedemo.com"  # 示例网站
BROWSER = "chrome"  # chrome, firefox, edge
HEADLESS = False    # 是否无头模式
IMPLICIT_WAIT = 10  # 隐式等待时间（秒）
```

### 3. 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_login.py

# 运行特定测试用例
pytest tests/test_login.py::TestLogin::test_valid_login

# 生成 HTML 报告
pytest --html=reports/report.html --self-contained-html

# 并行运行（需要 pytest-xdist）
pytest -n 4

# 显示详细输出
pytest -v -s
```

## 📝 代码示例

### 基础页面类 (base_page.py)

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """所有页面对象的基类"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """查找单个元素"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """查找多个元素"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """点击元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator, timeout=10):
        """检查元素是否可见"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
```

### 登录页面类 (login_page.py)

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """登录页面对象"""
    
    # 页面元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{config.BASE_URL}/login"
    
    def open(self):
        """打开登录页面"""
        self.driver.get(self.url)
        return self
    
    def enter_username(self, username):
        """输入用户名"""
        self.input_text(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        """输入密码"""
        self.input_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        """点击登录按钮"""
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, username, password):
        """完整登录流程"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    def get_error_message(self):
        """获取错误消息"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """检查是否显示错误"""
        return self.is_element_visible(self.ERROR_MESSAGE)
```

### 测试用例 (test_login.py)

```python
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestLogin:
    """登录功能测试"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """每个测试前的设置"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
    
    def test_valid_login(self):
        """测试有效登录"""
        # 打开登录页面并登录
        self.login_page.open().login("standard_user", "secret_sauce")
        
        # 验证登录成功
        assert self.home_page.is_loaded(), "首页未加载"
        assert self.home_page.get_title() == "Products", "页面标题不正确"
    
    def test_invalid_username(self):
        """测试无效用户名"""
        self.login_page.open().login("invalid_user", "secret_sauce")
        
        # 验证错误消息
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Username and password do not match" in error_msg
    
    def test_invalid_password(self):
        """测试无效密码"""
        self.login_page.open().login("standard_user", "wrong_password")
        
        assert self.login_page.is_error_displayed()
    
    def test_empty_credentials(self):
        """测试空凭证"""
        self.login_page.open().click_login()
        
        assert self.login_page.is_error_displayed()
        error_msg = self.login_page.get_error_message()
        assert "Username is required" in error_msg
    
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "user has been locked out"),
    ])
    def test_login_scenarios(self, username, password, expected_error):
        """参数化测试多种登录场景"""
        self.login_page.open().login(username, password)
        
        assert self.login_page.is_error_displayed()
        error_msg = self.login_page.get_error_message()
        assert expected_error in error_msg
```

## 🔧 配置文件

### requirements.txt

```txt
selenium==4.16.0
pytest==7.4.3
pytest-html==4.1.1
pytest-xdist==3.5.0
webdriver-manager==4.0.1
```

### pytest.ini

```ini
[pytest]
# 测试文件匹配模式
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# 命令行选项
addopts = 
    -v
    --strict-markers
    --tb=short
    --html=reports/report.html
    --self-contained-html

# 标记定义
markers =
    smoke: 冒烟测试
    regression: 回归测试
    slow: 慢速测试
    skip_in_ci: CI 环境跳过

# 测试目录
testpaths = tests

# 日志配置
log_cli = true
log_cli_level = INFO
```

### conftest.py

```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import config

@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture"""
    # 初始化驱动
    if config.BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    elif config.BROWSER.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"不支持的浏览器: {config.BROWSER}")
    
    # 配置
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    # 清理
    driver.quit()

@pytest.fixture(scope="session")
def test_data():
    """测试数据 fixture"""
    return {
        "valid_user": {
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "locked_user": {
            "username": "locked_out_user",
            "password": "secret_sauce"
        }
    }
```

## 📊 测试报告

运行测试后，查看生成的报告：

```bash
# HTML 报告
open reports/report.html

# Allure 报告（需要安装 allure-pytest）
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 🎯 最佳实践

### 1. 页面对象设计原则

- ✅ 每个页面一个类
- ✅ 元素定位器作为类常量
- ✅ 方法返回 self 支持链式调用
- ✅ 不在页面类中写断言
- ✅ 使用有意义的方法名

### 2. 定位器策略

优先级顺序：
1. `ID` - 最快最稳定
2. `Name` - 次优选择
3. `CSS Selector` - 灵活强大
4. `XPath` - 最后选择（性能较差）

### 3. 等待策略

```python
# ❌ 不推荐：固定等待
time.sleep(5)

# ✅ 推荐：显式等待
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element"))
)

# ✅ 推荐：隐式等待（全局设置）
driver.implicitly_wait(10)
```

### 4. 测试数据管理

```python
# 使用 fixture 管理测试数据
@pytest.fixture
def test_users():
    return {
        "admin": {"username": "admin", "password": "admin123"},
        "user": {"username": "user", "password": "user123"}
    }

# 使用 JSON 文件
import json
with open("test_data.json") as f:
    test_data = json.load(f)
```

## 🐛 常见问题

### 1. 元素找不到

```python
# 问题：NoSuchElementException
# 解决：增加等待时间或检查定位器

# 使用显式等待
wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))
```

### 2. 元素不可点击

```python
# 问题：ElementClickInterceptedException
# 解决：等待元素可点击

wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()

# 或使用 JavaScript 点击
driver.execute_script("arguments[0].click();", element)
```

### 3. StaleElementReferenceException

```python
# 问题：页面刷新后元素引用失效
# 解决：重新查找元素

def safe_click(locator):
    for _ in range(3):
        try:
            element = driver.find_element(*locator)
            element.click()
            break
        except StaleElementReferenceException:
            time.sleep(0.5)
```

## 🚀 进阶功能

### 1. 截图功能

```python
def take_screenshot(driver, name):
    """保存截图"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename

# 在测试失败时自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, item.name)
```

### 2. 数据驱动测试

```python
# 使用 CSV 文件
import csv
import pytest

def load_test_data(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))

@pytest.mark.parametrize("data", load_test_data("test_data.csv"))
def test_with_csv_data(driver, data):
    # 使用 data["username"], data["password"] 等
    pass
```

### 3. 并行执行

```bash
# 安装 pytest-xdist
pip install pytest-xdist

# 并行运行（4 个进程）
pytest -n 4

# 自动检测 CPU 核心数
pytest -n auto
```

## 📚 参考资源

- Selenium 官方文档 (https://www.selenium.dev/documentation/)
- Pytest 官方文档 (https://docs.pytest.org/)
- Page Object Model 设计模式 (https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- 示例网站 (https://www.saucedemo.com) - 用于练习自动化测试

## 📝 练习建议

1. ✅ 运行现有测试，理解 POM 结构
2. ✅ 为 Home Page 添加更多测试用例
3. ✅ 创建新的页面对象（如购物车页面）
4. ✅ 实现端到端测试流程
5. ✅ 添加数据驱动测试
6. ✅ 集成到 CI/CD 流程

---

**难度级别：** 中级  
**预计学习时间：** 30-60 分钟  
**最后更新：** 2026-02-06
