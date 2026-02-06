"""
基础页面类 - 所有页面对象的父类
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """所有页面对象的基类，提供通用方法"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator, timeout=10):
        """
        查找单个元素
        
        Args:
            locator: 元素定位器 (By.ID, "element_id")
            timeout: 超时时间（秒）
        
        Returns:
            WebElement: 找到的元素
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            logger.debug(f"找到元素: {locator}")
            return element
        except TimeoutException:
            logger.error(f"元素未找到: {locator}")
            raise
    
    def find_elements(self, locator, timeout=10):
        """
        查找多个元素
        
        Args:
            locator: 元素定位器
            timeout: 超时时间（秒）
        
        Returns:
            list: 元素列表
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            logger.debug(f"找到 {len(elements)} 个元素: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"元素未找到: {locator}")
            return []
    
    def click(self, locator, timeout=10):
        """
        点击元素
        
        Args:
            locator: 元素定位器
            timeout: 超时时间（秒）
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.debug(f"点击元素: {locator}")
        except Exception as e:
            logger.error(f"点击失败: {locator}, 错误: {str(e)}")
            raise
    
    def input_text(self, locator, text, clear_first=True):
        """
        输入文本
        
        Args:
            locator: 元素定位器
            text: 要输入的文本
            clear_first: 是否先清空
        """
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
        logger.debug(f"输入文本到 {locator}: {text}")
    
    def get_text(self, locator):
        """
        获取元素文本
        
        Args:
            locator: 元素定位器
        
        Returns:
            str: 元素文本
        """
        element = self.find_element(locator)
        text = element.text
        logger.debug(f"获取文本 {locator}: {text}")
        return text
    
    def get_attribute(self, locator, attribute):
        """
        获取元素属性
        
        Args:
            locator: 元素定位器
            attribute: 属性名
        
        Returns:
            str: 属性值
        """
        element = self.find_element(locator)
        value = element.get_attribute(attribute)
        logger.debug(f"获取属性 {locator}.{attribute}: {value}")
        return value
    
    def is_element_visible(self, locator, timeout=10):
        """
        检查元素是否可见
        
        Args:
            locator: 元素定位器
            timeout: 超时时间（秒）
        
        Returns:
            bool: 是否可见
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            logger.debug(f"元素可见: {locator}")
            return True
        except TimeoutException:
            logger.debug(f"元素不可见: {locator}")
            return False
    
    def is_element_present(self, locator):
        """
        检查元素是否存在于 DOM 中
        
        Args:
            locator: 元素定位器
        
        Returns:
            bool: 是否存在
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """
        等待元素消失
        
        Args:
            locator: 元素定位器
            timeout: 超时时间（秒）
        
        Returns:
            bool: 是否消失
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
            logger.debug(f"元素已消失: {locator}")
            return True
        except TimeoutException:
            logger.debug(f"元素未消失: {locator}")
            return False
    
    def scroll_to_element(self, locator):
        """
        滚动到元素
        
        Args:
            locator: 元素定位器
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.debug(f"滚动到元素: {locator}")
    
    def hover_over_element(self, locator):
        """
        鼠标悬停在元素上
        
        Args:
            locator: 元素定位器
        """
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
        logger.debug(f"悬停在元素上: {locator}")
    
    def get_current_url(self):
        """获取当前 URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """获取页面标题"""
        return self.driver.title
    
    def refresh_page(self):
        """刷新页面"""
        self.driver.refresh()
        logger.debug("页面已刷新")
    
    def go_back(self):
        """后退"""
        self.driver.back()
        logger.debug("后退")
    
    def go_forward(self):
        """前进"""
        self.driver.forward()
        logger.debug("前进")
    
    def switch_to_frame(self, locator):
        """切换到 iframe"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
        logger.debug(f"切换到 frame: {locator}")
    
    def switch_to_default_content(self):
        """切换回默认内容"""
        self.driver.switch_to.default_content()
        logger.debug("切换回默认内容")
    
    def accept_alert(self):
        """接受警告框"""
        alert = self.driver.switch_to.alert
        alert.accept()
        logger.debug("接受警告框")
    
    def dismiss_alert(self):
        """取消警告框"""
        alert = self.driver.switch_to.alert
        alert.dismiss()
        logger.debug("取消警告框")
    
    def get_alert_text(self):
        """获取警告框文本"""
        alert = self.driver.switch_to.alert
        return alert.text
    
    def take_screenshot(self, filename):
        """
        截图
        
        Args:
            filename: 文件名
        """
        self.driver.save_screenshot(filename)
        logger.info(f"截图已保存: {filename}")
