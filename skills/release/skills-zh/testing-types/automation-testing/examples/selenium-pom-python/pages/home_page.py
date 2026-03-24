"""
首页（产品列表页）对象
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """首页页面对象"""
    
    # 页面元素定位器
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_loaded(self):
        """
        检查页面是否加载完成
        
        Returns:
            bool: 是否加载完成
        """
        return self.is_element_visible(self.PAGE_TITLE, timeout=5)
    
    def get_title(self):
        """
        获取页面标题
        
        Returns:
            str: 页面标题
        """
        return self.get_text(self.PAGE_TITLE)
    
    def open_menu(self):
        """
        打开侧边菜单
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        self.click(self.MENU_BUTTON)
        logger.info("打开侧边菜单")
        return self
    
    def logout(self):
        """
        登出
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        self.open_menu()
        self.click(self.LOGOUT_LINK)
        logger.info("执行登出")
        return self
    
    def get_product_count(self):
        """
        获取产品数量
        
        Returns:
            int: 产品数量
        """
        products = self.find_elements(self.PRODUCT_ITEMS)
        count = len(products)
        logger.info(f"产品数量: {count}")
        return count
    
    def get_product_names(self):
        """
        获取所有产品名称
        
        Returns:
            list: 产品名称列表
        """
        elements = self.find_elements(self.PRODUCT_NAMES)
        names = [element.text for element in elements]
        logger.info(f"产品名称: {names}")
        return names
    
    def get_product_prices(self):
        """
        获取所有产品价格
        
        Returns:
            list: 产品价格列表
        """
        elements = self.find_elements(self.PRODUCT_PRICES)
        prices = [element.text for element in elements]
        logger.info(f"产品价格: {prices}")
        return prices
    
    def add_product_to_cart_by_index(self, index):
        """
        通过索引添加产品到购物车
        
        Args:
            index: 产品索引（从 0 开始）
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
            logger.info(f"添加产品到购物车: 索引 {index}")
        else:
            raise IndexError(f"产品索引 {index} 超出范围")
        return self
    
    def add_product_to_cart_by_name(self, product_name):
        """
        通过名称添加产品到购物车
        
        Args:
            product_name: 产品名称
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        # 将产品名称转换为按钮 ID
        button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        button_locator = (By.ID, button_id)
        self.click(button_locator)
        logger.info(f"添加产品到购物车: {product_name}")
        return self
    
    def remove_product_from_cart_by_index(self, index):
        """
        通过索引从购物车移除产品
        
        Args:
            index: 产品索引（从 0 开始）
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
            logger.info(f"从购物车移除产品: 索引 {index}")
        else:
            raise IndexError(f"产品索引 {index} 超出范围")
        return self
    
    def get_cart_item_count(self):
        """
        获取购物车商品数量
        
        Returns:
            int: 购物车商品数量，如果购物车为空返回 0
        """
        if self.is_element_visible(self.CART_BADGE, timeout=2):
            count = int(self.get_text(self.CART_BADGE))
            logger.info(f"购物车商品数量: {count}")
            return count
        logger.info("购物车为空")
        return 0
    
    def click_cart(self):
        """
        点击购物车图标
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        self.click(self.CART_LINK)
        logger.info("点击购物车")
        return self
    
    def select_sort_option(self, option):
        """
        选择排序选项
        
        Args:
            option: 排序选项值 (az, za, lohi, hilo)
        
        Returns:
            HomePage: 返回自身支持链式调用
        """
        from selenium.webdriver.support.ui import Select
        dropdown = self.find_element(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(option)
        logger.info(f"选择排序选项: {option}")
        return self
    
    def get_current_sort_option(self):
        """
        获取当前排序选项
        
        Returns:
            str: 当前排序选项值
        """
        from selenium.webdriver.support.ui import Select
        dropdown = self.find_element(self.SORT_DROPDOWN)
        select = Select(dropdown)
        option = select.first_selected_option.get_attribute("value")
        logger.info(f"当前排序选项: {option}")
        return option
    
    def is_product_in_cart(self, product_name):
        """
        检查产品是否在购物车中（通过检查是否有 Remove 按钮）
        
        Args:
            product_name: 产品名称
        
        Returns:
            bool: 是否在购物车中
        """
        button_id = f"remove-{product_name.lower().replace(' ', '-')}"
        button_locator = (By.ID, button_id)
        return self.is_element_present(button_locator)
