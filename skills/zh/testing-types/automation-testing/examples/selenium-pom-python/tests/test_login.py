"""
登录功能测试
"""
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLogin:
    """登录功能测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """每个测试前的设置"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
    
    @pytest.mark.smoke
    def test_valid_login(self, test_data):
        """测试有效登录"""
        # 打开登录页面并登录
        user = test_data["valid_user"]
        self.login_page.open().login(user["username"], user["password"])
        
        # 验证登录成功
        assert self.home_page.is_loaded(), "首页未加载"
        assert self.home_page.get_title() == "Products", "页面标题不正确"
        assert "inventory.html" in self.driver.current_url, "URL 不正确"
    
    @pytest.mark.smoke
    def test_valid_login_with_user_type(self):
        """测试使用预定义用户类型登录"""
        self.login_page.open().login_with_user_type("standard")
        
        assert self.home_page.is_loaded(), "首页未加载"
        assert self.home_page.get_title() == "Products"
    
    def test_invalid_username(self, test_data):
        """测试无效用户名"""
        invalid_user = test_data["invalid_user"]
        self.login_page.open().login(invalid_user["username"], invalid_user["password"])
        
        # 验证错误消息
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Username and password do not match" in error_msg, f"错误消息不正确: {error_msg}"
    
    def test_invalid_password(self, test_data):
        """测试无效密码"""
        user = test_data["valid_user"]
        self.login_page.open().login(user["username"], "wrong_password")
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Username and password do not match" in error_msg
    
    def test_empty_username(self):
        """测试空用户名"""
        self.login_page.open().enter_password("secret_sauce").click_login()
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Username is required" in error_msg, f"错误消息不正确: {error_msg}"
    
    def test_empty_password(self):
        """测试空密码"""
        self.login_page.open().enter_username("standard_user").click_login()
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Password is required" in error_msg, f"错误消息不正确: {error_msg}"
    
    def test_empty_credentials(self):
        """测试空凭证"""
        self.login_page.open().click_login()
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "Username is required" in error_msg
    
    def test_locked_out_user(self, test_data):
        """测试被锁定的用户"""
        user = test_data["locked_user"]
        self.login_page.open().login(user["username"], user["password"])
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        error_msg = self.login_page.get_error_message()
        assert "user has been locked out" in error_msg, f"错误消息不正确: {error_msg}"
    
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "user has been locked out"),
        ("invalid_user", "invalid_pass", "Username and password do not match"),
    ])
    def test_login_scenarios(self, username, password, expected_error):
        """参数化测试多种登录场景"""
        self.login_page.open().login(username, password)
        
        assert self.login_page.is_error_displayed(), f"未显示错误消息: {username}/{password}"
        error_msg = self.login_page.get_error_message()
        assert expected_error in error_msg, f"错误消息不匹配。期望: {expected_error}, 实际: {error_msg}"
    
    def test_close_error_message(self):
        """测试关闭错误消息"""
        self.login_page.open().click_login()
        
        assert self.login_page.is_error_displayed(), "未显示错误消息"
        
        self.login_page.close_error_message()
        
        # 错误消息应该消失
        assert not self.login_page.is_error_displayed(), "错误消息未关闭"
    
    def test_login_button_enabled(self):
        """测试登录按钮是否可用"""
        self.login_page.open()
        
        assert self.login_page.is_login_button_enabled(), "登录按钮不可用"
    
    def test_clear_credentials(self):
        """测试清空凭证"""
        self.login_page.open()
        self.login_page.enter_username("test_user")
        self.login_page.enter_password("test_pass")
        
        self.login_page.clear_username()
        self.login_page.clear_password()
        
        self.login_page.click_login()
        
        # 应该显示用户名必填错误
        assert self.login_page.is_error_displayed()
        error_msg = self.login_page.get_error_message()
        assert "Username is required" in error_msg
    
    @pytest.mark.regression
    def test_logout(self, test_data):
        """测试登出功能"""
        # 先登录
        user = test_data["valid_user"]
        self.login_page.open().login(user["username"], user["password"])
        
        assert self.home_page.is_loaded(), "登录失败"
        
        # 登出
        self.home_page.logout()
        
        # 验证返回登录页面
        assert self.driver.current_url == self.login_page.url, "未返回登录页面"
