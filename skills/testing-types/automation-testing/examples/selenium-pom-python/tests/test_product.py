"""
产品功能测试
"""
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestProduct:
    """产品功能测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logged_in_user):
        """每个测试前的设置 - 使用已登录用户"""
        self.driver = driver
        self.home_page = logged_in_user
    
    @pytest.mark.smoke
    def test_product_list_displayed(self):
        """测试产品列表显示"""
        assert self.home_page.get_product_count() > 0, "没有产品显示"
        assert self.home_page.get_title() == "Products", "页面标题不正确"
    
    def test_product_count(self):
        """测试产品数量"""
        count = self.home_page.get_product_count()
        assert count == 6, f"产品数量不正确，期望 6，实际 {count}"
    
    def test_product_names_displayed(self):
        """测试产品名称显示"""
        names = self.home_page.get_product_names()
        
        assert len(names) > 0, "没有产品名称"
        assert all(name for name in names), "存在空的产品名称"
    
    def test_product_prices_displayed(self):
        """测试产品价格显示"""
        prices = self.home_page.get_product_prices()
        
        assert len(prices) > 0, "没有产品价格"
        assert all(price.startswith("$") for price in prices), "价格格式不正确"
    
    @pytest.mark.smoke
    def test_add_product_to_cart_by_index(self):
        """测试通过索引添加产品到购物车"""
        initial_count = self.home_page.get_cart_item_count()
        
        self.home_page.add_product_to_cart_by_index(0)
        
        new_count = self.home_page.get_cart_item_count()
        assert new_count == initial_count + 1, "购物车数量未增加"
    
    @pytest.mark.smoke
    def test_add_product_to_cart_by_name(self):
        """测试通过名称添加产品到购物车"""
        initial_count = self.home_page.get_cart_item_count()
        
        self.home_page.add_product_to_cart_by_name("sauce-labs-backpack")
        
        new_count = self.home_page.get_cart_item_count()
        assert new_count == initial_count + 1, "购物车数量未增加"
    
    def test_add_multiple_products(self):
        """测试添加多个产品"""
        self.home_page.add_product_to_cart_by_index(0)
        self.home_page.add_product_to_cart_by_index(1)
        self.home_page.add_product_to_cart_by_index(2)
        
        count = self.home_page.get_cart_item_count()
        assert count == 3, f"购物车数量不正确，期望 3，实际 {count}"
    
    def test_remove_product_from_cart(self):
        """测试从购物车移除产品"""
        # 先添加产品
        self.home_page.add_product_to_cart_by_index(0)
        initial_count = self.home_page.get_cart_item_count()
        
        # 移除产品
        self.home_page.remove_product_from_cart_by_index(0)
        
        new_count = self.home_page.get_cart_item_count()
        assert new_count == initial_count - 1, "购物车数量未减少"
    
    def test_cart_badge_not_displayed_when_empty(self):
        """测试购物车为空时不显示徽章"""
        count = self.home_page.get_cart_item_count()
        assert count == 0, "购物车应该为空"
    
    @pytest.mark.parametrize("sort_option,expected_first", [
        ("az", "Sauce Labs Backpack"),
        ("za", "Test.allTheThings() T-Shirt (Red)"),
    ])
    def test_sort_products(self, sort_option, expected_first):
        """测试产品排序"""
        self.home_page.select_sort_option(sort_option)
        
        names = self.home_page.get_product_names()
        assert names[0] == expected_first, f"排序不正确，期望第一个是 {expected_first}，实际是 {names[0]}"
    
    def test_sort_by_price_low_to_high(self):
        """测试按价格从低到高排序"""
        self.home_page.select_sort_option("lohi")
        
        prices = self.home_page.get_product_prices()
        # 提取数字价格
        price_values = [float(price.replace("$", "")) for price in prices]
        
        # 验证是升序
        assert price_values == sorted(price_values), "价格排序不正确"
    
    def test_sort_by_price_high_to_low(self):
        """测试按价格从高到低排序"""
        self.home_page.select_sort_option("hilo")
        
        prices = self.home_page.get_product_prices()
        price_values = [float(price.replace("$", "")) for price in prices]
        
        # 验证是降序
        assert price_values == sorted(price_values, reverse=True), "价格排序不正确"
    
    def test_click_cart_icon(self):
        """测试点击购物车图标"""
        self.home_page.click_cart()
        
        # 验证跳转到购物车页面
        assert "cart.html" in self.driver.current_url, "未跳转到购物车页面"
    
    @pytest.mark.regression
    def test_add_all_products_to_cart(self):
        """测试添加所有产品到购物车"""
        product_count = self.home_page.get_product_count()
        
        for i in range(product_count):
            self.home_page.add_product_to_cart_by_index(i)
        
        cart_count = self.home_page.get_cart_item_count()
        assert cart_count == product_count, f"购物车数量不正确，期望 {product_count}，实际 {cart_count}"
