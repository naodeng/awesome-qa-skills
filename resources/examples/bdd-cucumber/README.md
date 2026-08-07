# BDD 测试示例 (Cucumber)

这个示例展示了如何使用 Cucumber 进行行为驱动开发（BDD）测试，使用 Gherkin 语言编写可读的测试场景。

## 📋 功能特性

- ✅ Gherkin 语法编写测试场景
- ✅ Given-When-Then 模式
- ✅ 场景大纲（Scenario Outline）
- ✅ 数据表（Data Tables）
- ✅ 标签（Tags）管理
- ✅ 钩子函数（Hooks）
- ✅ 自定义报告

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 运行测试

```bash
# 运行所有测试
npm test

# 运行特定标签的测试
npm run test:smoke
npm run test:regression

# 生成 HTML 报告
npm run test:report
```

## 📁 项目结构

```
bdd-cucumber/
├── features/
│   ├── login.feature           # 登录功能场景
│   ├── search.feature          # 搜索功能场景
│   ├── shopping-cart.feature   # 购物车功能场景
│   └── user-registration.feature # 用户注册场景
├── step-definitions/
│   ├── login-steps.js          # 登录步骤定义
│   ├── search-steps.js         # 搜索步骤定义
│   ├── cart-steps.js           # 购物车步骤定义
│   └── common-steps.js         # 通用步骤定义
├── support/
│   ├── hooks.js                # 钩子函数
│   ├── world.js                # 世界对象
│   └── helpers.js              # 辅助函数
├── pages/
│   ├── LoginPage.js            # 登录页面对象
│   ├── SearchPage.js           # 搜索页面对象
│   └── CartPage.js             # 购物车页面对象
├── cucumber.js                 # Cucumber 配置
├── package.json
└── README.md
```

## 📚 Gherkin 语法

### 基本结构

```gherkin
Feature: 功能名称
  功能描述

  Background: 背景（每个场景前执行）
    Given 前置条件

  Scenario: 场景名称
    Given 给定前置条件
    When 当执行某个操作
    Then 那么应该得到某个结果
    And 并且还有其他结果
    But 但是不应该有某个结果
```

### 场景大纲

```gherkin
Scenario Outline: 参数化场景
  Given 用户名是 "<username>"
  When 密码是 "<password>"
  Then 登录结果是 "<result>"

  Examples:
    | username | password | result  |
    | admin    | admin123 | success |
    | user1    | user123  | success |
    | invalid  | wrong    | error   |
```

### 数据表

```gherkin
Scenario: 创建多个用户
  Given 以下用户:
    | name  | email              | role  |
    | Alice | alice@example.com  | admin |
    | Bob   | bob@example.com    | user  |
  When 创建这些用户
  Then 所有用户应该创建成功
```

### 标签

```gherkin
@smoke @login
Feature: 登录功能

@critical
Scenario: 管理员登录
  Given 用户是管理员
  When 登录系统
  Then 应该看到管理员面板

@skip
Scenario: 暂时跳过的场景
  Given 某个条件
  When 某个操作
  Then 某个结果
```

## 🎯 最佳实践

### 1. 编写清晰的场景

```gherkin
# ✅ 好的场景：清晰、具体
Scenario: 用户成功登录
  Given 用户在登录页面
  And 用户名是 "admin"
  And 密码是 "admin123"
  When 用户点击登录按钮
  Then 用户应该看到欢迎消息
  And 用户应该在首页

# ❌ 不好的场景：模糊、不具体
Scenario: 登录
  Given 在页面上
  When 输入信息
  Then 成功
```

### 2. 使用业务语言

```gherkin
# ✅ 好的：使用业务术语
Scenario: 客户下单购买商品
  Given 客户已登录
  When 客户将商品添加到购物车
  And 客户完成结账
  Then 订单应该创建成功

# ❌ 不好的：使用技术术语
Scenario: POST /api/orders
  Given token is valid
  When send POST request
  Then response code is 201
```

### 3. 保持场景独立

```gherkin
# ✅ 好的：每个场景独立
Scenario: 添加商品到购物车
  Given 用户已登录
  And 购物车是空的
  When 用户添加商品 "iPhone"
  Then 购物车应该有 1 个商品

# ❌ 不好的：依赖其他场景
Scenario: 结账
  # 假设购物车已经有商品（依赖上一个场景）
  When 用户点击结账
  Then 应该跳转到支付页面
```

### 4. 使用 Background 减少重复

```gherkin
Feature: 购物车功能

  Background:
    Given 用户已登录
    And 用户在商品页面

  Scenario: 添加商品
    When 用户添加商品到购物车
    Then 购物车应该有 1 个商品

  Scenario: 移除商品
    Given 购物车有 1 个商品
    When 用户移除商品
    Then 购物车应该是空的
```

## 🔧 配置说明

### cucumber.js 配置

```javascript
module.exports = {
  default: {
    require: ['step-definitions/**/*.js', 'support/**/*.js'],
    format: ['progress', 'html:reports/cucumber-report.html'],
    publishQuiet: true,
  },
  smoke: {
    require: ['step-definitions/**/*.js', 'support/**/*.js'],
    format: ['progress'],
    tags: '@smoke',
  },
  regression: {
    require: ['step-definitions/**/*.js', 'support/**/*.js'],
    format: ['progress'],
    tags: 'not @skip',
  },
};
```

### 钩子函数

```javascript
const { Before, After, BeforeAll, AfterAll } = require('@cucumber/cucumber');

BeforeAll(async function() {
  // 所有测试前执行一次
  console.log('开始测试');
});

Before(async function() {
  // 每个场景前执行
  this.startTime = Date.now();
});

After(async function(scenario) {
  // 每个场景后执行
  const duration = Date.now() - this.startTime;
  console.log(`场景 "${scenario.pickle.name}" 耗时: ${duration}ms`);
  
  if (scenario.result.status === 'FAILED') {
    // 截图
    const screenshot = await this.driver.takeScreenshot();
    this.attach(screenshot, 'image/png');
  }
});

AfterAll(async function() {
  // 所有测试后执行一次
  console.log('测试完成');
});
```

## 📊 报告

### HTML 报告

运行测试后会生成 HTML 报告：

```bash
npm run test:report
```

报告包含：
- 场景执行结果
- 步骤详情
- 失败截图
- 执行时间统计

### JSON 报告

生成 JSON 格式报告用于 CI/CD 集成：

```bash
npm run test:json
```

## 🐛 常见问题

### Q: 如何跳过某些场景？

A: 使用 `@skip` 标签：

```gherkin
@skip
Scenario: 暂时跳过
  Given 某个条件
  When 某个操作
  Then 某个结果
```

### Q: 如何运行特定标签的测试？

A: 使用 `--tags` 参数：

```bash
# 运行 @smoke 标签的测试
npx cucumber-js --tags "@smoke"

# 运行 @smoke 或 @regression 标签的测试
npx cucumber-js --tags "@smoke or @regression"

# 运行 @smoke 但不包括 @skip 的测试
npx cucumber-js --tags "@smoke and not @skip"
```

### Q: 如何处理异步操作？

A: 使用 async/await：

```javascript
When('用户点击登录按钮', async function() {
  await this.loginPage.clickLoginButton();
  await this.driver.wait(until.urlContains('/dashboard'), 5000);
});
```

### Q: 如何共享数据？

A: 使用 World 对象：

```javascript
// world.js
class CustomWorld {
  constructor() {
    this.testData = {};
  }
}

// step-definitions
Given('用户名是 {string}', function(username) {
  this.testData.username = username;
});

When('用户登录', async function() {
  await this.loginPage.login(this.testData.username, this.testData.password);
});
```

## 📚 相关资源

- [Cucumber 官方文档](https://cucumber.io/docs/cucumber/)
- [Gherkin 语法参考](https://cucumber.io/docs/gherkin/reference/)
- [BDD 最佳实践](https://cucumber.io/docs/bdd/)

## 📝 许可证

MIT License
