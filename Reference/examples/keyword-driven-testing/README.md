# 关键字驱动测试示例

这个示例展示了如何实现关键字驱动测试（Keyword-Driven Testing），使非技术人员也能编写和维护测试用例。

## 📋 功能特性

- ✅ 关键字库设计
- ✅ Excel/CSV 测试用例
- ✅ JSON 测试用例
- ✅ 关键字执行引擎
- ✅ 测试报告生成
- ✅ 可扩展的关键字系统
- ✅ 错误处理和日志

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 运行测试

```bash
# 运行所有测试
npm test

# 运行特定测试套件
npm run test:login
npm run test:shopping

# 生成报告
npm run test:report
```

## 📁 项目结构

```
keyword-driven-testing/
├── keywords/
│   ├── WebKeywords.js          # Web 操作关键字
│   ├── ApiKeywords.js           # API 操作关键字
│   ├── DatabaseKeywords.js      # 数据库操作关键字
│   └── ValidationKeywords.js    # 验证关键字
├── test-cases/
│   ├── login-tests.json         # 登录测试用例
│   ├── shopping-tests.json      # 购物测试用例
│   └── api-tests.json           # API 测试用例
├── engine/
│   ├── KeywordEngine.js         # 关键字执行引擎
│   ├── TestRunner.js            # 测试运行器
│   └── Reporter.js              # 报告生成器
├── utils/
│   ├── logger.js                # 日志工具
│   └── helpers.js               # 辅助函数
├── package.json
└── README.md
```

## 📚 关键字设计

### 关键字分类

1. **导航关键字**
   - `navigateTo` - 导航到URL
   - `clickLink` - 点击链接
   - `goBack` - 后退
   - `refresh` - 刷新页面

2. **输入关键字**
   - `inputText` - 输入文本
   - `clearText` - 清空文本
   - `selectDropdown` - 选择下拉框
   - `checkCheckbox` - 勾选复选框

3. **验证关键字**
   - `verifyText` - 验证文本
   - `verifyElementVisible` - 验证元素可见
   - `verifyElementEnabled` - 验证元素启用
   - `verifyUrl` - 验证URL

4. **等待关键字**
   - `waitForElement` - 等待元素
   - `waitForText` - 等待文本
   - `sleep` - 等待指定时间

5. **API 关键字**
   - `sendGetRequest` - 发送GET请求
   - `sendPostRequest` - 发送POST请求
   - `verifyStatusCode` - 验证状态码
   - `verifyResponseBody` - 验证响应体

## 🎯 测试用例格式

### JSON 格式

```json
{
  "testSuite": "登录功能测试",
  "testCases": [
    {
      "id": "TC001",
      "name": "成功登录",
      "steps": [
        {
          "keyword": "navigateTo",
          "args": ["https://example.com/login"]
        },
        {
          "keyword": "inputText",
          "args": ["#username", "admin"]
        },
        {
          "keyword": "inputText",
          "args": ["#password", "admin123"]
        },
        {
          "keyword": "clickElement",
          "args": ["#loginButton"]
        },
        {
          "keyword": "verifyText",
          "args": [".welcome-message", "欢迎"]
        }
      ]
    }
  ]
}
```

### Excel/CSV 格式

```csv
TestCase,Step,Keyword,Arg1,Arg2,Arg3,Expected
TC001,1,navigateTo,https://example.com/login,,,
TC001,2,inputText,#username,admin,,
TC001,3,inputText,#password,admin123,,
TC001,4,clickElement,#loginButton,,,
TC001,5,verifyText,.welcome-message,欢迎,,success
```

## 🔧 使用方法

### 1. 定义关键字

```javascript
// keywords/WebKeywords.js
class WebKeywords {
  constructor(driver) {
    this.driver = driver;
  }

  async navigateTo(url) {
    await this.driver.get(url);
    return { status: 'pass', message: `导航到 ${url}` };
  }

  async inputText(selector, text) {
    const element = await this.driver.findElement(By.css(selector));
    await element.sendKeys(text);
    return { status: 'pass', message: `输入文本: ${text}` };
  }

  async clickElement(selector) {
    const element = await this.driver.findElement(By.css(selector));
    await element.click();
    return { status: 'pass', message: `点击元素: ${selector}` };
  }

  async verifyText(selector, expectedText) {
    const element = await this.driver.findElement(By.css(selector));
    const actualText = await element.getText();
    
    if (actualText.includes(expectedText)) {
      return { status: 'pass', message: `文本验证通过: ${expectedText}` };
    } else {
      return { 
        status: 'fail', 
        message: `文本验证失败: 期望 "${expectedText}", 实际 "${actualText}"` 
      };
    }
  }
}
```

### 2. 编写测试用例

```json
{
  "testSuite": "购物车测试",
  "testCases": [
    {
      "id": "TC002",
      "name": "添加商品到购物车",
      "steps": [
        {
          "keyword": "navigateTo",
          "args": ["https://example.com/products"]
        },
        {
          "keyword": "clickElement",
          "args": [".product:first-child .add-to-cart"]
        },
        {
          "keyword": "verifyText",
          "args": [".cart-count", "1"]
        },
        {
          "keyword": "navigateTo",
          "args": ["https://example.com/cart"]
        },
        {
          "keyword": "verifyElementVisible",
          "args": [".cart-item"]
        }
      ]
    }
  ]
}
```

### 3. 运行测试

```javascript
const KeywordEngine = require('./engine/KeywordEngine');
const testCases = require('./test-cases/shopping-tests.json');

const engine = new KeywordEngine();
await engine.runTestSuite(testCases);
```

## 📊 测试报告

测试完成后会生成详细的报告：

```
测试套件: 登录功能测试
执行时间: 2024-02-09 10:30:00
总用例数: 5
通过: 4
失败: 1
跳过: 0

TC001 - 成功登录: PASS (2.5s)
  ✓ navigateTo: https://example.com/login
  ✓ inputText: #username = admin
  ✓ inputText: #password = admin123
  ✓ clickElement: #loginButton
  ✓ verifyText: .welcome-message contains "欢迎"

TC002 - 登录失败: FAIL (1.8s)
  ✓ navigateTo: https://example.com/login
  ✓ inputText: #username = invalid
  ✓ inputText: #password = wrong
  ✓ clickElement: #loginButton
  ✗ verifyText: .error-message contains "错误"
    期望: "错误", 实际: "用户名或密码错误"
```

## 🎯 最佳实践

### 1. 关键字命名规范

```javascript
// ✅ 好的命名：清晰、动词开头
navigateTo()
inputText()
clickElement()
verifyText()

// ❌ 不好的命名：模糊、不一致
goto()
type()
press()
check()
```

### 2. 关键字粒度

```javascript
// ✅ 好的粒度：原子操作
inputText(selector, text)
clickElement(selector)

// ❌ 不好的粒度：复合操作
loginUser(username, password)  // 应该拆分为多个关键字
```

### 3. 错误处理

```javascript
async clickElement(selector) {
  try {
    const element = await this.driver.findElement(By.css(selector));
    await element.click();
    return { status: 'pass', message: `点击元素: ${selector}` };
  } catch (error) {
    return { 
      status: 'fail', 
      message: `点击元素失败: ${selector}`,
      error: error.message 
    };
  }
}
```

### 4. 参数化

```json
{
  "testCase": "参数化登录",
  "parameters": {
    "username": "admin",
    "password": "admin123",
    "loginUrl": "https://example.com/login"
  },
  "steps": [
    {
      "keyword": "navigateTo",
      "args": ["${loginUrl}"]
    },
    {
      "keyword": "inputText",
      "args": ["#username", "${username}"]
    },
    {
      "keyword": "inputText",
      "args": ["#password", "${password}"]
    }
  ]
}
```

### 5. 可复用的测试片段

```json
{
  "fragments": {
    "login": [
      { "keyword": "navigateTo", "args": ["${loginUrl}"] },
      { "keyword": "inputText", "args": ["#username", "${username}"] },
      { "keyword": "inputText", "args": ["#password", "${password}"] },
      { "keyword": "clickElement", "args": ["#loginButton"] }
    ]
  },
  "testCases": [
    {
      "name": "测试1",
      "steps": [
        { "fragment": "login" },
        { "keyword": "verifyText", "args": [".welcome", "欢迎"] }
      ]
    }
  ]
}
```

## 🔄 与其他测试方法对比

| 特性 | 关键字驱动 | 数据驱动 | BDD |
|------|-----------|---------|-----|
| 技术门槛 | 低 | 中 | 低 |
| 可维护性 | 高 | 中 | 高 |
| 灵活性 | 中 | 高 | 中 |
| 可读性 | 高 | 中 | 高 |
| 适用场景 | 重复性测试 | 参数化测试 | 需求驱动 |

## 🐛 常见问题

### Q: 如何添加新的关键字？

A: 在关键字类中添加新方法：

```javascript
async customKeyword(arg1, arg2) {
  // 实现逻辑
  return { status: 'pass', message: '执行成功' };
}
```

### Q: 如何处理动态数据？

A: 使用变量和参数：

```json
{
  "parameters": {
    "timestamp": "${Date.now()}"
  },
  "steps": [
    {
      "keyword": "inputText",
      "args": ["#email", "user_${timestamp}@example.com"]
    }
  ]
}
```

### Q: 如何实现条件执行？

A: 添加条件关键字：

```javascript
async executeIf(condition, keyword, args) {
  if (this.evaluateCondition(condition)) {
    return await this[keyword](...args);
  }
  return { status: 'skip', message: '条件不满足，跳过' };
}
```

### Q: 如何集成到 CI/CD？

A: 使用命令行运行并生成报告：

```bash
node run-tests.js --suite login --format junit --output reports/
```

## 📚 相关资源

- [关键字驱动测试最佳实践](https://www.guru99.com/keyword-driven-testing.html)
- [Robot Framework](https://robotframework.org/) - 流行的关键字驱动框架
- [测试自动化金字塔](https://martinfowler.com/articles/practical-test-pyramid.html)

## 📝 许可证

MIT License
