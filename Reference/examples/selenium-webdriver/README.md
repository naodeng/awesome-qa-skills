# Selenium WebDriver 示例

这个示例展示了如何使用 Selenium WebDriver 进行 Web 自动化测试，包括等待策略、元素定位和交互操作。

## 📋 功能特性

- ✅ 多种等待策略（显式等待、隐式等待、流畅等待）
- ✅ 8种元素定位方法
- ✅ 常见交互操作（点击、输入、选择、拖拽）
- ✅ 高级操作（鼠标悬停、键盘操作、JavaScript 执行）
- ✅ 截图和日志记录
- ✅ Page Object Model 设计模式

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 下载浏览器驱动

```bash
# ChromeDriver 会自动下载
# 或手动下载: https://chromedriver.chromium.org/
```

### 运行测试

```bash
# 运行所有测试
npm test

# 运行特定测试
npm test -- --grep "等待策略"
```

## 📁 项目结构

```
selenium-webdriver/
├── tests/
│   ├── waits.test.js          # 等待策略测试
│   ├── locators.test.js       # 元素定位测试
│   ├── interactions.test.js   # 交互操作测试
│   └── advanced.test.js       # 高级操作测试
├── pages/
│   ├── BasePage.js            # 基础页面类
│   ├── LoginPage.js           # 登录页面
│   └── DashboardPage.js       # 仪表板页面
├── utils/
│   ├── driver-factory.js      # 驱动工厂
│   └── test-helpers.js        # 测试辅助函数
├── package.json
└── README.md
```

## 📚 测试用例

### 1. 等待策略测试

- 显式等待（Explicit Wait）
- 隐式等待（Implicit Wait）
- 流畅等待（Fluent Wait）
- 等待元素可见
- 等待元素可点击
- 等待元素消失

### 2. 元素定位测试

- ID 定位
- Name 定位
- Class Name 定位
- Tag Name 定位
- Link Text 定位
- Partial Link Text 定位
- CSS Selector 定位
- XPath 定位

### 3. 交互操作测试

- 点击操作
- 文本输入
- 清空输入
- 下拉选择
- 复选框操作
- 单选按钮操作
- 文件上传
- 拖拽操作

### 4. 高级操作测试

- 鼠标悬停
- 右键点击
- 双击
- 键盘操作
- JavaScript 执行
- 窗口切换
- Frame 切换
- Alert 处理

## 🔧 配置说明

### 浏览器配置

```javascript
// Chrome 配置
const chromeOptions = new chrome.Options();
chromeOptions.addArguments('--headless');
chromeOptions.addArguments('--disable-gpu');
chromeOptions.addArguments('--no-sandbox');

// Firefox 配置
const firefoxOptions = new firefox.Options();
firefoxOptions.addArguments('-headless');
```

### 超时配置

```javascript
// 隐式等待
driver.manage().setTimeouts({ implicit: 10000 });

// 页面加载超时
driver.manage().setTimeouts({ pageLoad: 30000 });

// 脚本执行超时
driver.manage().setTimeouts({ script: 30000 });
```

## 📖 使用示例

### 基本用法

```javascript
const { Builder, By, until } = require('selenium-webdriver');

// 创建驱动
const driver = await new Builder().forBrowser('chrome').build();

try {
  // 访问页面
  await driver.get('https://example.com');
  
  // 查找元素
  const element = await driver.findElement(By.id('username'));
  
  // 输入文本
  await element.sendKeys('testuser');
  
  // 点击按钮
  const button = await driver.findElement(By.css('button[type="submit"]'));
  await button.click();
  
  // 等待元素出现
  await driver.wait(until.elementLocated(By.id('welcome')), 5000);
  
} finally {
  await driver.quit();
}
```

### 使用 Page Object

```javascript
const LoginPage = require('./pages/LoginPage');
const DashboardPage = require('./pages/DashboardPage');

describe('登录测试', () => {
  let driver, loginPage, dashboardPage;
  
  before(async () => {
    driver = await new Builder().forBrowser('chrome').build();
    loginPage = new LoginPage(driver);
    dashboardPage = new DashboardPage(driver);
  });
  
  it('应该成功登录', async () => {
    await loginPage.open();
    await loginPage.login('testuser', 'password123');
    
    const welcomeText = await dashboardPage.getWelcomeText();
    assert.include(welcomeText, '欢迎');
  });
  
  after(async () => {
    await driver.quit();
  });
});
```

## 🎯 最佳实践

### 1. 使用显式等待

```javascript
// ❌ 不推荐：使用 sleep
await driver.sleep(5000);

// ✅ 推荐：使用显式等待
await driver.wait(until.elementLocated(By.id('element')), 5000);
```

### 2. 优先使用 ID 和 CSS 选择器

```javascript
// ✅ 最快：ID
await driver.findElement(By.id('username'));

// ✅ 快速：CSS Selector
await driver.findElement(By.css('.login-form input[name="username"]'));

// ⚠️ 较慢：XPath
await driver.findElement(By.xpath('//input[@name="username"]'));
```

### 3. 使用 Page Object 模式

```javascript
// ✅ 推荐：封装页面逻辑
class LoginPage {
  constructor(driver) {
    this.driver = driver;
  }
  
  async login(username, password) {
    await this.driver.findElement(By.id('username')).sendKeys(username);
    await this.driver.findElement(By.id('password')).sendKeys(password);
    await this.driver.findElement(By.css('button[type="submit"]')).click();
  }
}
```

### 4. 异常处理

```javascript
try {
  const element = await driver.findElement(By.id('element'));
  await element.click();
} catch (error) {
  if (error.name === 'NoSuchElementError') {
    console.log('元素未找到');
  } else if (error.name === 'TimeoutError') {
    console.log('操作超时');
  }
  throw error;
}
```

## 🐛 常见问题

### Q: 元素找不到怎么办？

A: 
1. 检查定位器是否正确
2. 添加显式等待
3. 检查元素是否在 iframe 中
4. 使用浏览器开发工具验证

### Q: 测试运行很慢怎么办？

A:
1. 使用无头模式
2. 减少不必要的等待
3. 并行运行测试
4. 优化定位器

### Q: 如何处理动态元素？

A:
1. 使用部分匹配的定位器
2. 使用 XPath 的 contains()
3. 等待元素状态变化
4. 使用 JavaScript 执行

## 📚 相关资源

- [Selenium 官方文档](https://www.selenium.dev/documentation/)
- [WebDriver API](https://www.selenium.dev/selenium/docs/api/javascript/)
- [最佳实践指南](https://www.selenium.dev/documentation/test_practices/)

## 📝 许可证

MIT License
