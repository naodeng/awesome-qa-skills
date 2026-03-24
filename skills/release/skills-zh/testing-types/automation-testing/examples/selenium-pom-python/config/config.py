"""
测试配置文件
"""
import os

# 基础配置
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
BROWSER = os.getenv("BROWSER", "chrome")  # chrome, firefox, edge
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# 等待时间配置
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))

# 测试数据
TEST_USERS = {
    "standard": {
        "username": "standard_user",
        "password": "secret_sauce"
    },
    "locked": {
        "username": "locked_out_user",
        "password": "secret_sauce"
    },
    "problem": {
        "username": "problem_user",
        "password": "secret_sauce"
    },
    "performance": {
        "username": "performance_glitch_user",
        "password": "secret_sauce"
    }
}

# 报告配置
SCREENSHOT_ON_FAILURE = True
SCREENSHOT_DIR = "screenshots"
REPORT_DIR = "reports"

# 日志配置
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "test_execution.log"
