"""
Pytest 配置和 fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import config
from datetime import datetime
import os
import logging

# 配置日志
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver(request):
    """
    WebDriver fixture
    每个测试函数都会创建新的浏览器实例
    """
    logger.info(f"初始化 {config.BROWSER} 浏览器")
    
    # 初始化驱动
    if config.BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif config.BROWSER.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    elif config.BROWSER.lower() == "edge":
        options = webdriver.EdgeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"不支持的浏览器: {config.BROWSER}")
    
    # 配置
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
    driver.maximize_window()
    
    logger.info("浏览器初始化完成")
    
    yield driver
    
    # 清理
    logger.info("关闭浏览器")
    driver.quit()


@pytest.fixture(scope="session")
def test_data():
    """
    测试数据 fixture
    """
    return {
        "valid_user": config.TEST_USERS["standard"],
        "locked_user": config.TEST_USERS["locked"],
        "problem_user": config.TEST_USERS["problem"],
        "performance_user": config.TEST_USERS["performance"],
        "invalid_user": {
            "username": "invalid_user",
            "password": "invalid_password"
        }
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    在测试失败时自动截图
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        if config.SCREENSHOT_ON_FAILURE:
            driver = item.funcargs.get("driver")
            if driver:
                # 创建截图目录
                os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
                
                # 生成截图文件名
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name.replace(" ", "_").replace("[", "_").replace("]", "_")
                filename = f"{config.SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
                
                # 保存截图
                driver.save_screenshot(filename)
                logger.info(f"测试失败，截图已保存: {filename}")
                
                # 添加截图到报告
                if hasattr(rep, "extra"):
                    rep.extra.append(pytest_html.extras.image(filename))


def pytest_configure(config):
    """
    Pytest 配置钩子
    """
    # 创建必要的目录
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


def pytest_html_report_title(report):
    """
    自定义 HTML 报告标题
    """
    report.title = "Selenium POM 测试报告"


@pytest.fixture(scope="function")
def login_page(driver):
    """
    登录页面 fixture
    """
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture(scope="function")
def home_page(driver):
    """
    首页 fixture
    """
    from pages.home_page import HomePage
    return HomePage(driver)


@pytest.fixture(scope="function")
def logged_in_user(driver, login_page, home_page):
    """
    已登录用户 fixture
    自动登录并返回首页对象
    """
    login_page.open().login_with_user_type("standard")
    assert home_page.is_loaded(), "登录失败"
    return home_page
