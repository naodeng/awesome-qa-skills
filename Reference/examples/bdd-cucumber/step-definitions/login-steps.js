const { Given, When, Then } = require('@cucumber/cucumber');
const { expect } = require('chai');

// 前置条件
Given('用户在登录页面', async function() {
  this.currentPage = 'login';
  console.log('用户导航到登录页面');
});

Given('用户名是 {string}', function(username) {
  this.username = username;
  console.log(`设置用户名: ${username}`);
});

Given('密码是 {string}', function(password) {
  this.password = password;
  console.log(`设置密码: ${password}`);
});

Given('用户勾选了"记住我"选项', function() {
  this.rememberMe = true;
  console.log('勾选记住我选项');
});

Given('用户已登录', function() {
  this.isLoggedIn = true;
  this.currentUser = 'testuser';
  this.currentPage = 'home';
  console.log('用户已登录');
});

// 操作
When('用户点击登录按钮', function() {
  console.log(`尝试登录: ${this.username} / ${this.password}`);
  
  // 模拟登录逻辑
  const result = this.simulateLogin(this.username, this.password, this.rememberMe);
  
  this.loginResult = result.status;
  this.errorMessage = result.error;
  this.welcomeMessage = result.welcome;
  this.currentPage = result.page;
  this.isLoggedIn = result.isLoggedIn;
  this.cookie = result.cookie;
});

When('用户尝试使用错误密码登录 {int} 次', function(attempts) {
  console.log(`尝试使用错误密码登录 ${attempts} 次`);
  
  this.loginAttempts = attempts;
  
  for (let i = 0; i < attempts; i++) {
    const result = this.simulateLogin(this.username, 'wrongpassword');
    this.loginResult = result.status;
    this.errorMessage = result.error;
  }
  
  // 第3次失败后锁定账户
  if (attempts >= 3) {
    this.accountLocked = true;
    this.errorMessage = '账户已被锁定';
  }
});

When('用户点击登出按钮', function() {
  console.log('用户点击登出');
  
  this.isLoggedIn = false;
  this.currentUser = null;
  this.currentPage = 'login';
  this.session = null;
  
  console.log('用户已登出');
});

// 断言
Then('用户应该看到欢迎消息 {string}', function(expectedMessage) {
  console.log(`验证欢迎消息: ${this.welcomeMessage}`);
  expect(this.welcomeMessage).to.include(expectedMessage);
});

Then('用户应该在首页', function() {
  console.log(`当前页面: ${this.currentPage}`);
  expect(this.currentPage).to.equal('home');
});

Then('用户应该看到错误消息 {string}', function(expectedError) {
  console.log(`验证错误消息: ${this.errorMessage}`);
  expect(this.errorMessage).to.include(expectedError);
});

Then('用户应该仍在登录页面', function() {
  console.log(`当前页面: ${this.currentPage}`);
  expect(this.currentPage).to.equal('login');
});

Then('登录结果应该是 {string}', function(expectedResult) {
  console.log(`验证登录结果: ${this.loginResult}`);
  
  if (expectedResult === 'success') {
    expect(this.loginResult).to.equal('success');
    expect(this.isLoggedIn).to.be.true;
  } else {
    expect(this.loginResult).to.equal('error');
    expect(this.isLoggedIn).to.be.false;
  }
});

Then('用户应该无法登录', function() {
  console.log('验证用户无法登录');
  expect(this.accountLocked).to.be.true;
  expect(this.isLoggedIn).to.be.false;
});

Then('应该设置记住我的 Cookie', function() {
  console.log('验证记住我 Cookie');
  expect(this.cookie).to.exist;
  expect(this.cookie.name).to.equal('remember_token');
});

Then('用户应该成功登录', function() {
  console.log('验证登录成功');
  expect(this.isLoggedIn).to.be.true;
  expect(this.currentPage).to.equal('home');
});

Then('用户应该返回登录页面', function() {
  console.log('验证返回登录页面');
  expect(this.currentPage).to.equal('login');
});

Then('用户会话应该被清除', function() {
  console.log('验证会话已清除');
  expect(this.session).to.be.null;
  expect(this.isLoggedIn).to.be.false;
});

// 辅助方法（添加到 World）
function simulateLogin(username, password, rememberMe = false) {
  // 验证用户名
  if (!username || username.trim() === '') {
    return {
      status: 'error',
      error: '请输入用户名',
      page: 'login',
      isLoggedIn: false
    };
  }
  
  // 验证密码
  if (!password || password.trim() === '') {
    return {
      status: 'error',
      error: '请输入密码',
      page: 'login',
      isLoggedIn: false
    };
  }
  
  // 验证凭证
  const validCredentials = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'pass456'
  };
  
  if (validCredentials[username] === password) {
    const result = {
      status: 'success',
      welcome: `欢迎, ${username === 'admin' ? '管理员' : username}`,
      page: 'home',
      isLoggedIn: true
    };
    
    if (rememberMe) {
      result.cookie = {
        name: 'remember_token',
        value: 'mock-token-123',
        expires: Date.now() + 30 * 24 * 60 * 60 * 1000 // 30 days
      };
    }
    
    return result;
  }
  
  return {
    status: 'error',
    error: '用户名或密码错误',
    page: 'login',
    isLoggedIn: false
  };
}

// 导出辅助方法供 World 使用
module.exports = { simulateLogin };
