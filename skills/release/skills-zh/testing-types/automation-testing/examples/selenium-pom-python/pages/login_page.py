"""
登录页面对象
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import config
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """登录页面对象"""
    
    # 页面元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CSS_SELECTOR, ".error-button")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.BASE_URL
    
    def open(self):
        """
        打开登录页面
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        self.driver.get(self.url)
        logger.info(f"打开登录页面: {self.url}")
        return self
    
    def enter_username(self, username):
        """
        输入用户名
        
        Args:
            username: 用户名
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        self.input_text(self.USERNAME_INPUT, username)
        logger.info(f"输入用户名: {username}")
        return self
    
    def enter_password(self, password):
        """
        输入密码
        
        Args:
            password: 密码
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        self.input_text(self.PASSWORD_INPUT, password)
        logger.info("输入密码")
        return self
    
    def click_login(self):
        """
        点击登录按钮
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        self.click(self.LOGIN_BUTTON)
        logger.info("点击登录按钮")
        return self
    
    def login(self, username, password):
        """
        完整登录流程
        
        Args:
            username: 用户名
            password: 密码
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        logger.info(f"执行登录: {username}")
        return self
    
    def login_with_user_type(self, user_type):
        """
        使用预定义的用户类型登录
        
        Args:
            user_type: 用户类型 (standard, locked, problem, performance)
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        user = config.TEST_USERS.get(user_type)
        if not user:
            raise ValueError(f"未知的用户类型: {user_type}")
        
        return self.login(user["username"], user["password"])
    
    def get_error_message(self):
        """
        获取错误消息
        
        Returns:
            str: 错误消息文本
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """
        检查是否显示错误消息
        
        Returns:
            bool: 是否显示错误
        """
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=3)
    
    def close_error_message(self):
        """
        关闭错误消息
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        if self.is_element_visible(self.ERROR_BUTTON, timeout=2):
            self.click(self.ERROR_BUTTON)
            logger.info("关闭错误消息")
        return self
    
    def clear_username(self):
        """
        清空用户名
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        element = self.find_element(self.USERNAME_INPUT)
        element.clear()
        logger.info("清空用户名")
        return self
    
    def clear_password(self):
        """
        清空密码
        
        Returns:
            LoginPage: 返回自身支持链式调用
        """
        element = self.find_element(self.PASSWORD_INPUT)
        element.clear()
        logger.info("清空密码")
        return self
    
    def is_login_button_enabled(self):
        """
        检查登录按钮是否可用
        
        Returns:
            bool: 是否可用
        """
        element = self.find_element(self.LOGIN_BUTTON)
        return element.is_enabled()
    
    def get_username_placeholder(self):
        """
        获取用户名输入框的占位符
        
        Returns:
            str: 占位符文本
        """
        return self.get_attribute(self.USERNAME_INPUT, "placeholder")
    
    def get_password_placeholder(self):
        """
        获取密码输入框的占位符
        
        Returns:
            str: 占位符文本
        """
        return self.get_attribute(self.PASSWORD_INPUT, "placeholder")
