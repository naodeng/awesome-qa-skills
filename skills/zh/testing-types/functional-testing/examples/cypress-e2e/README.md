# Cypress E2E 测试示例

这是一个使用 Cypress 进行端到端测试的完整示例项目。

## 📋 项目概述

本示例展示了如何使用 Cypress 进行：
- 登录功能测试
- API Mocking 和拦截
- 表单验证测试
- 会话管理测试
- 网络错误处理

## 🚀 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 运行测试

**交互模式（推荐用于开发）**:
```bash
npm run cy:open
```

**无头模式（用于 CI/CD）**:
```bash
npm test
# 或
npm run cy:run
```

**指定浏览器**:
```bash
npm run cy:run:chrome
npm run cy:run:firefox
```

**有头模式（查看测试执行过程）**:
```bash
npm run cy:run:headed
```

## 📁 项目结构

```
cypress-e2e/
├── cypress/
│   ├── e2e/                    # 测试文件
│   │   ├── login.cy.js         # 登录功能测试
│   │   └── api-mocking.cy.js   # API Mocking 测试
│   ├── fixtures/               # 测试数据
│   ├── support/                # 支持文件和自定义命令
│   │   ├── commands.js
│   │   └── e2e.js
│   └── screenshots/            # 失败截图（自动生成）
├── cypress.config.js           # Cypress 配置
├── package.json
└── README.md
```

## 🧪 测试用例

### 登录功能测试 (login.cy.js)

测试场景包括：
- ✅ 成功登录有效用户
- ✅ 无效用户名/密码错误处理
- ✅ 空字段验证
- ✅ "记住我"功能
- ✅ 密码可见性切换
- ✅ 导航到忘记密码/注册页面
- ✅ 账户锁定机制
- ✅ 会话管理和登出

### API Mocking 测试 (api-mocking.cy.js)

测试场景包括：
- ✅ 成功加载数据
- ✅ API 错误处理
- ✅ 网络超时处理
- ✅ CRUD 操作（创建、读取、更新、删除）
- ✅ 搜索功能
- ✅ 分页加载
- ✅ 请求头和请求体验证

## 🔧 配置说明

### cypress.config.js

```javascript
{
  baseUrl: 'https://example.cypress.io',  // 基础 URL
  viewportWidth: 1280,                     // 视口宽度
  viewportHeight: 720,                     // 视口高度
  video: true,                             // 录制视频
  screenshotOnRunFailure: true,            // 失败时截图
  defaultCommandTimeout: 10000,            // 命令超时
  pageLoadTimeout: 30000,                  // 页面加载超时
  retries: {
    runMode: 2,                            // CI 模式重试次数
    openMode: 0                            // 交互模式重试次数
  }
}
```

## 📝 最佳实践

### 1. 使用 data-cy 属性

```html
<!-- 推荐 -->
<button data-cy="login-button">Login</button>

<!-- 不推荐 -->
<button class="btn btn-primary">Login</button>
```

```javascript
// 推荐
cy.get('[data-cy=login-button]').click()

// 不推荐
cy.get('.btn.btn-primary').click()
```

### 2. 使用别名 (Aliases)

```javascript
// 为请求创建别名
cy.intercept('GET', '/api/users').as('getUsers')

// 等待请求完成
cy.wait('@getUsers')

// 访问请求/响应数据
cy.wait('@getUsers').its('response.statusCode').should('eq', 200)
```

### 3. 自定义命令

在 `cypress/support/commands.js` 中定义：

```javascript
Cypress.Commands.add('login', (username, password) => {
  cy.visit('/login')
  cy.get('[data-cy=username]').type(username)
  cy.get('[data-cy=password]').type(password)
  cy.get('[data-cy=login-button]').click()
})
```

使用：

```javascript
cy.login('testuser', 'password123')
```

### 4. 测试隔离

```javascript
beforeEach(() => {
  // 每个测试前清理状态
  cy.clearCookies()
  cy.clearLocalStorage()
  cy.visit('/login')
})
```

### 5. 等待策略

```javascript
// 等待元素出现
cy.get('[data-cy=user-list]').should('be.visible')

// 等待 API 请求
cy.wait('@getUsers')

// 等待特定条件
cy.get('[data-cy=loading]').should('not.exist')
```

## 🎯 API Mocking 技巧

### 基本拦截

```javascript
cy.intercept('GET', '/api/users', {
  statusCode: 200,
  body: [{ id: 1, name: 'John' }]
})
```

### 动态响应

```javascript
cy.intercept('GET', '/api/users', (req) => {
  req.reply({
    statusCode: 200,
    body: generateMockData()
  })
})
```

### 模拟延迟

```javascript
cy.intercept('GET', '/api/users', {
  delay: 2000,  // 2秒延迟
  body: []
})
```

### 模拟错误

```javascript
cy.intercept('GET', '/api/users', {
  statusCode: 500,
  body: { error: 'Internal Server Error' }
})
```

### 验证请求

```javascript
cy.intercept('POST', '/api/users', (req) => {
  expect(req.body).to.have.property('name')
  expect(req.headers).to.have.property('authorization')
  req.reply({ statusCode: 201 })
})
```

## 🐛 调试技巧

### 1. 使用 .debug()

```javascript
cy.get('[data-cy=user-list]')
  .debug()  // 在这里暂停
  .should('have.length', 3)
```

### 2. 使用 .pause()

```javascript
cy.get('[data-cy=login-button]')
  .click()
  .pause()  // 暂停测试执行
```

### 3. 查看网络请求

在 Cypress Test Runner 中查看 Network 标签。

### 4. 截图和视频

```javascript
// 手动截图
cy.screenshot('my-screenshot')

// 视频会自动录制（在 cypress/videos/ 目录）
```

## 📊 测试报告

### 生成 Mochawesome 报告

1. 安装依赖：
```bash
npm install --save-dev mochawesome mochawesome-merge mochawesome-report-generator
```

2. 更新配置：
```javascript
// cypress.config.js
reporter: 'mochawesome',
reporterOptions: {
  reportDir: 'cypress/reports',
  overwrite: false,
  html: false,
  json: true
}
```

3. 生成报告：
```bash
npm run cy:run
npx mochawesome-merge cypress/reports/*.json > report.json
npx marge report.json
```

## 🔗 CI/CD 集成

### GitHub Actions

```yaml
name: Cypress Tests

on: [push]

jobs:
  cypress-run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: cypress-io/github-action@v5
        with:
          build: npm run build
          start: npm start
          wait-on: 'http://localhost:3000'
```

### GitLab CI

```yaml
cypress:
  image: cypress/browsers:node18.12.0-chrome107
  script:
    - npm ci
    - npm run cy:run
  artifacts:
    when: always
    paths:
      - cypress/screenshots
      - cypress/videos
```

## 🚨 常见问题

### 1. 元素未找到

**问题**: `Timed out retrying: Expected to find element`

**解决方案**:
```javascript
// 增加超时时间
cy.get('[data-cy=element]', { timeout: 10000 })

// 等待元素出现
cy.get('[data-cy=element]').should('be.visible')
```

### 2. 测试不稳定 (Flaky)

**解决方案**:
- 使用 `cy.wait('@alias')` 等待 API 请求
- 避免使用固定的 `cy.wait(1000)`
- 使用 `.should()` 断言等待条件满足

### 3. 跨域问题

**解决方案**:
```javascript
// cypress.config.js
{
  chromeWebSecurity: false
}
```

## 📚 参考资源

- [Cypress 官方文档](https://docs.cypress.io/)
- [Cypress 最佳实践](https://docs.cypress.io/guides/references/best-practices)
- [Cypress 示例](https://github.com/cypress-io/cypress-example-recipes)
- [Cypress Real World App](https://github.com/cypress-io/cypress-realworld-app)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT

---

*最后更新: 2026-02-09*
