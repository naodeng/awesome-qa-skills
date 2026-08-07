const { Given, When, Then } = require('@cucumber/cucumber');
const { expect } = require('chai');

// 前置条件
Given('用户在商品页面', function() {
  this.currentPage = 'products';
  console.log('用户在商品页面');
});

Given('购物车中有以下商品:', function(dataTable) {
  this.cart = this.cart || [];
  
  const items = dataTable.hashes();
  items.forEach(item => {
    this.cart.push({
      name: item['商品名称'],
      quantity: parseInt(item['数量']),
      price: parseInt(item['单价'] || 0)
    });
  });
  
  console.log(`购物车中有 ${this.cart.length} 种商品`);
});

Given('购物车中有商品 {string} 数量为 {int}', function(productName, quantity) {
  this.cart = this.cart || [];
  this.cart.push({
    name: productName,
    quantity: quantity,
    price: 5999
  });
  
  console.log(`添加 ${productName} x${quantity} 到购物车`);
});

Given('购物车中有 {int} 个商品', function(count) {
  this.cart = [];
  
  for (let i = 1; i <= count; i++) {
    this.cart.push({
      name: `商品${i}`,
      quantity: 1,
      price: 100
    });
  }
  
  console.log(`购物车中有 ${count} 个商品`);
});

Given('商品 {string} 的库存只有 {int} 件', function(productName, stock) {
  this.productStock = this.productStock || {};
  this.productStock[productName] = stock;
  
  console.log(`${productName} 库存: ${stock}`);
});

Given('购物车中有商品总价 {int} 元', function(totalPrice) {
  this.cart = [{
    name: '测试商品',
    quantity: 1,
    price: totalPrice
  }];
  
  console.log(`购物车总价: ${totalPrice} 元`);
});

Given('用户有优惠券 {string} 可以减免 {int} 元', function(couponCode, discount) {
  this.coupons = this.coupons || {};
  this.coupons[couponCode] = {
    code: couponCode,
    discount: discount,
    type: 'fixed'
  };
  
  console.log(`添加优惠券: ${couponCode}, 减免 ${discount} 元`);
});

// 操作
When('用户添加商品 {string} 到购物车', function(productName) {
  this.cart = this.cart || [];
  
  this.cart.push({
    name: productName,
    quantity: 1,
    price: 5999
  });
  
  console.log(`添加 ${productName} 到购物车`);
});

When('用户添加以下商品到购物车:', function(dataTable) {
  this.cart = this.cart || [];
  
  const items = dataTable.hashes();
  items.forEach(item => {
    this.cart.push({
      name: item['商品名称'],
      quantity: parseInt(item['数量']),
      price: 5999
    });
  });
  
  console.log(`添加 ${items.length} 种商品到购物车`);
});

When('用户从购物车移除 {string}', function(productName) {
  this.cart = this.cart.filter(item => item.name !== productName);
  console.log(`从购物车移除 ${productName}`);
});

When('用户将 {string} 的数量更新为 {int}', function(productName, newQuantity) {
  const item = this.cart.find(item => item.name === productName);
  
  if (item) {
    item.quantity = newQuantity;
    console.log(`更新 ${productName} 数量为 ${newQuantity}`);
  }
});

When('用户清空购物车', function() {
  this.cart = [];
  this.cartMessage = '购物车是空的';
  console.log('清空购物车');
});

When('用户尝试添加 {int} 件 {string} 到购物车', function(quantity, productName) {
  const stock = this.productStock[productName] || 0;
  
  if (quantity > stock) {
    this.errorMessage = '库存不足';
    console.log(`库存不足: 尝试添加 ${quantity} 件，但只有 ${stock} 件`);
  } else {
    this.cart = this.cart || [];
    this.cart.push({
      name: productName,
      quantity: quantity,
      price: 5999
    });
  }
});

When('用户应用优惠券 {string}', function(couponCode) {
  const coupon = this.coupons[couponCode];
  
  if (coupon) {
    this.appliedCoupon = coupon;
    this.couponMessage = '优惠券已应用';
    console.log(`应用优惠券: ${couponCode}`);
  }
});

When('用户点击结账按钮', function() {
  this.currentPage = 'checkout';
  console.log('跳转到结账页面');
});

When('用户登出并重新登录', function() {
  // 保存购物车
  const savedCart = [...this.cart];
  
  // 模拟登出
  this.isLoggedIn = false;
  
  // 模拟重新登录
  this.isLoggedIn = true;
  
  // 恢复购物车
  this.cart = savedCart;
  
  console.log('用户登出并重新登录');
});

// 断言
Then('购物车应该有 {int} 个商品', function(expectedCount) {
  const actualCount = this.cart.length;
  console.log(`购物车商品数: ${actualCount}`);
  expect(actualCount).to.equal(expectedCount);
});

Then('购物车中应该包含 {string}', function(productName) {
  const hasProduct = this.cart.some(item => item.name === productName);
  console.log(`购物车包含 ${productName}: ${hasProduct}`);
  expect(hasProduct).to.be.true;
});

Then('购物车应该有 {int} 种商品', function(expectedTypes) {
  const actualTypes = this.cart.length;
  console.log(`购物车商品种类: ${actualTypes}`);
  expect(actualTypes).to.equal(expectedTypes);
});

Then('购物车总数量应该是 {int}', function(expectedTotal) {
  const actualTotal = this.cart.reduce((sum, item) => sum + item.quantity, 0);
  console.log(`购物车总数量: ${actualTotal}`);
  expect(actualTotal).to.equal(expectedTotal);
});

Then('购物车中不应该包含 {string}', function(productName) {
  const hasProduct = this.cart.some(item => item.name === productName);
  console.log(`购物车包含 ${productName}: ${hasProduct}`);
  expect(hasProduct).to.be.false;
});

Then('购物车中 {string} 的数量应该是 {int}', function(productName, expectedQuantity) {
  const item = this.cart.find(item => item.name === productName);
  console.log(`${productName} 数量: ${item ? item.quantity : 0}`);
  expect(item.quantity).to.equal(expectedQuantity);
});

Then('购物车总价应该更新', function() {
  const totalPrice = this.cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  console.log(`购物车总价: ${totalPrice} 元`);
  expect(totalPrice).to.be.greaterThan(0);
});

Then('购物车应该是空的', function() {
  console.log(`购物车商品数: ${this.cart.length}`);
  expect(this.cart).to.be.empty;
});

Then('应该显示 {string} 消息', function(expectedMessage) {
  const message = this.cartMessage || this.couponMessage || this.errorMessage;
  console.log(`消息: ${message}`);
  expect(message).to.include(expectedMessage);
});

Then('购物车总价应该是 {int} 元', function(expectedPrice) {
  let totalPrice = this.cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  
  // 应用优惠券
  if (this.appliedCoupon) {
    totalPrice -= this.appliedCoupon.discount;
  }
  
  console.log(`购物车总价: ${totalPrice} 元`);
  expect(totalPrice).to.equal(expectedPrice);
});

Then('应该显示错误消息 {string}', function(expectedError) {
  console.log(`错误消息: ${this.errorMessage}`);
  expect(this.errorMessage).to.include(expectedError);
});

Then('用户应该跳转到支付页面', function() {
  console.log(`当前页面: ${this.currentPage}`);
  expect(this.currentPage).to.equal('checkout');
});

Then('订单摘要应该显示所有商品', function() {
  console.log(`订单包含 ${this.cart.length} 种商品`);
  expect(this.cart.length).to.be.greaterThan(0);
});

Then('购物车中应该仍然有 {string}', function(productName) {
  const hasProduct = this.cart.some(item => item.name === productName);
  console.log(`购物车持久化验证: ${hasProduct}`);
  expect(hasProduct).to.be.true;
});
