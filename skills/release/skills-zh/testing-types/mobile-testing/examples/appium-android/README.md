# Appium Android 移动测试示例

使用 Appium + Python 进行 Android 应用自动化测试的完整示例。

## 📋 项目结构

```
appium-android/
├── README.md                    # 本文件
├── requirements.txt             # Python 依赖
├── pytest.ini                   # Pytest 配置
├── conftest.py                  # Pytest fixtures
├── config/
│   └── config.py               # 测试配置
├── pages/                       # Page Object
│   ├── base_page.py
│   ├── login_page.py
│   └── home_page.py
├── tests/                       # 测试用例
│   ├── test_login.py
│   └── test_navigation.py
├── utils/                       # 工具类
│   └── driver_factory.py
└── apps/                        # 测试应用
    └── app-debug.apk
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 安装 Appium
npm install -g appium

# 安装 Appium 驱动
appium driver install uiautomator2

# 验证安装
appium --version
```

### 2. 配置 Android 环境

```bash
# 安装 Android SDK
# 设置环境变量
export ANDROID_HOME=/path/to/android-sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools

# 验证 adb
adb version

# 连接设备或启动模拟器
adb devices
```

### 3. 运行测试

```bash
# 启动 Appium 服务器
appium

# 运行测试（新终端）
pytest

# 运行特定测试
pytest tests/test_login.py

# 生成报告
pytest --html=reports/report.html
```

## 📝 代码示例

### 配置文件 (config.py)

```python
import os

# Appium 服务器配置
APPIUM_SERVER = "http://localhost:4723"

# Android 设备配置
ANDROID_CAPS = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "app": os.path.join(os.path.dirname(__file__), "../apps/app-debug.apk"),
    "appPackage": "com.example.app",
    "appActivity": ".MainActivity",
    "noReset": False,
    "fullReset": False,
}

# 测试配置
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
```

### 基础页面类 (base_page.py)

```python
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def swipe_up(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, 500)
    
    def swipe_down(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, 500)
```

### 登录页面 (login_page.py)

```python
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 元素定位器
    USERNAME_INPUT = (AppiumBy.ID, "com.example.app:id/username")
    PASSWORD_INPUT = (AppiumBy.ID, "com.example.app:id/password")
    LOGIN_BUTTON = (AppiumBy.ID, "com.example.app:id/login_button")
    ERROR_MESSAGE = (AppiumBy.ID, "com.example.app:id/error_message")
    
    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)
```

### 测试用例 (test_login.py)

```python
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
    
    def test_valid_login(self):
        """测试有效登录"""
        self.login_page.login("testuser", "password123")
        assert self.home_page.is_loaded()
    
    def test_invalid_credentials(self):
        """测试无效凭证"""
        self.login_page.login("invalid", "wrong")
        assert self.login_page.is_error_displayed()
    
    def test_empty_username(self):
        """测试空用户名"""
        self.login_page.enter_password("password123")
        self.login_page.click_login()
        assert self.login_page.is_error_displayed()
```

## 🎯 最佳实践

### 1. 元素定位策略

优先级顺序：
1. Resource ID（最稳定）
2. Accessibility ID
3. XPath（最后选择）

### 2. 等待策略

```python
# 显式等待
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "element_id")))

# 隐式等待
driver.implicitly_wait(10)
```

### 3. 手势操作

```python
# 滑动
driver.swipe(start_x, start_y, end_x, end_y, duration)

# 点击坐标
driver.tap([(x, y)])

# 长按
from selenium.webdriver.common.actions import interaction
actions = ActionChains(driver)
actions.click_and_hold(element).perform()
```

## 🐛 常见问题

### 1. Appium 连接失败

**解决方案**:
```bash
# 检查 Appium 服务器
appium --version

# 检查设备连接
adb devices

# 重启 Appium
pkill -f appium
appium
```

### 2. 元素找不到

**解决方案**:
- 使用 Appium Inspector 查看元素
- 增加等待时间
- 检查元素定位器

### 3. 应用安装失败

**解决方案**:
```bash
# 手动安装应用
adb install app-debug.apk

# 卸载应用
adb uninstall com.example.app
```

## 📚 参考资源

- [Appium 官方文档](http://appium.io/docs/)
- [Android UI Automator](https://developer.android.com/training/testing/ui-automator)
- [Appium Python Client](https://github.com/appium/python-client)

---

**难度级别**: 高级  
**预计学习时间**: 60-90 分钟  
**最后更新**: 2026-02-06
