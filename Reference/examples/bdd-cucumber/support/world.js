const { setWorldConstructor, World } = require('@cucumber/cucumber');
const { simulateLogin } = require('../step-definitions/login-steps');

/**
 * 自定义 World 类
 * 用于在步骤之间共享状态和数据
 */
class CustomWorld extends World {
  constructor(options) {
    super(options);
    
    // 初始化状态
    this.username = null;
    this.password = null;
    this.rememberMe = false;
    this.isLoggedIn = false;
    this.currentUser = null;
    this.currentPage = null;
    this.loginResult = null;
    this.errorMessage = null;
    this.welcomeMessage = null;
    this.session = null;
    this.cookie = null;
    this.accountLocked = false;
    this.loginAttempts = 0;
    
    // 购物车相关
    this.cart = [];
    this.cartMessage = null;
    this.productStock = {};
    this.coupons = {};
    this.appliedCoupon = null;
    this.couponMessage = null;
    
    // 测试数据
    this.testData = {};
    
    // 绑定辅助方法
    this.simulateLogin = simulateLogin.bind(this);
  }
  
  /**
   * 重置状态
   */
  reset() {
    this.username = null;
    this.password = null;
    this.rememberMe = false;
    this.isLoggedIn = false;
    this.currentUser = null;
    this.currentPage = null;
    this.loginResult = null;
    this.errorMessage = null;
    this.welcomeMessage = null;
    this.session = null;
    this.cookie = null;
    this.accountLocked = false;
    this.loginAttempts = 0;
    this.cart = [];
    this.cartMessage = null;
    this.testData = {};
  }
  
  /**
   * 获取购物车总价
   */
  getCartTotal() {
    let total = this.cart.reduce((sum, item) => {
      return sum + (item.price * item.quantity);
    }, 0);
    
    // 应用优惠券
    if (this.appliedCoupon) {
      if (this.appliedCoupon.type === 'fixed') {
        total -= this.appliedCoupon.discount;
      } else if (this.appliedCoupon.type === 'percentage') {
        total *= (1 - this.appliedCoupon.discount / 100);
      }
    }
    
    return total;
  }
  
  /**
   * 获取购物车商品总数
   */
  getCartItemCount() {
    return this.cart.reduce((sum, item) => sum + item.quantity, 0);
  }
  
  /**
   * 查找购物车中的商品
   */
  findCartItem(productName) {
    return this.cart.find(item => item.name === productName);
  }
  
  /**
   * 添加商品到购物车
   */
  addToCart(productName, quantity = 1, price = 0) {
    const existingItem = this.findCartItem(productName);
    
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.cart.push({
        name: productName,
        quantity: quantity,
        price: price
      });
    }
  }
  
  /**
   * 从购物车移除商品
   */
  removeFromCart(productName) {
    this.cart = this.cart.filter(item => item.name !== productName);
  }
  
  /**
   * 更新商品数量
   */
  updateCartItemQuantity(productName, quantity) {
    const item = this.findCartItem(productName);
    if (item) {
      item.quantity = quantity;
    }
  }
  
  /**
   * 清空购物车
   */
  clearCart() {
    this.cart = [];
  }
  
  /**
   * 打印调试信息
   */
  debug() {
    console.log('\n=== World 状态 ===');
    console.log('用户:', this.currentUser);
    console.log('已登录:', this.isLoggedIn);
    console.log('当前页面:', this.currentPage);
    console.log('购物车商品数:', this.cart.length);
    console.log('购物车总价:', this.getCartTotal());
    console.log('==================\n');
  }
}

// 设置自定义 World
setWorldConstructor(CustomWorld);

module.exports = CustomWorld;
