# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__functional-testing__tutorial.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# 功能测试教程

## 📚 学习目标

完成本教程后，你将能够：
- 理解功能测试的核心概念和最佳实践
- 使用 Playwright 编写端到端测试
- 实现 Page Object Model 设计模式
- 编写可维护的测试用例
- 调试和优化测试脚本

## 🎯 前置要求

- 基本的 JavaScript/TypeScript 知识
- 了解 HTML 和 CSS 选择器
- 安装 Node.js (v16+)
- 熟悉命令行操作

## 📖 教程内容

### 第1步：环境搭建（10分钟）

#### 1.1 创建项目

```bash
mkdir my-functional-tests
cd my-functional-tests
npm init -y
```

#### 1.2 安装 Playwright

```bash
npm install -D @playwright/test
npx playwright install
```

#### 1.3 创建配置文件

创建 `playwright.config.ts`：

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
  ],
});
```

### 第2步：编写第一个测试（15分钟）

#### 2.1 创建简单测试

创建 `tests/login.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';

test('用户登录', async ({ page }) => {
  // 1. 访问登录页面
  await page.goto('/login');
  
  // 2. 填写表单
  await page.fill('#username', 'testuser');
  await page.fill('#password', 'password123');
  
  // 3. 点击登录按钮
  await page.click('button[type="submit"]');
  
  // 4. 验证登录成功
  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('.welcome-message')).toContainText('欢迎');
});
```

#### 2.2 运行测试

```bash
npx playwright test
```

### 第3步：使用 Page Object Model（20分钟）

#### 3.1 创建 Page Object

创建 `pages/LoginPage.ts`：

```typescript
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.submitButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.error-message');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async getErrorMessage() {
    return await this.errorMessage.textContent();
  }
}
```

#### 3.2 使用 Page Object

更新 `tests/login.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('使用 POM 登录', async ({ page }) => {
  const loginPage = new LoginPage(page);
  
  await loginPage.goto();
  await loginPage.login('testuser', 'password123');
  
  await expect(page).toHaveURL('/dashboard');
});

test('登录失败显示错误', async ({ page }) => {
  const loginPage = new LoginPage(page);
  
  await loginPage.goto();
  await loginPage.login('invalid', 'wrong');
  
  const error = await loginPage.getErrorMessage();
  expect(error).toContain('用户名或密码错误');
});
```

### 第4步：数据驱动测试（15分钟）

#### 4.1 使用测试数据

创建 `tests/login-data-driven.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

const testData = [
  { username: '', password: 'pass', error: '请输入用户名' },
  { username: 'user', password: '', error: '请输入密码' },
  { username: 'invalid', password: 'wrong', error: '用户名或密码错误' },
];

testData.forEach(({ username, password, error }) => {
  test(`登录验证: ${username || '空'} / ${password || '空'}`, async ({ page }) => {
    const loginPage = new LoginPage(page);
    
    await loginPage.goto();
    await loginPage.login(username, password);
    
    const errorMsg = await loginPage.getErrorMessage();
    expect(errorMsg).toContain(error);
  });
});
```

### 第5步：高级技巧（20分钟）

#### 5.1 等待策略

```typescript
// 等待元素可见
await page.waitForSelector('.loading', { state: 'hidden' });

// 等待网络请求
await page.waitForResponse(response => 
  response.url().includes('/api/user') && response.status() === 200
);

// 等待导航
await Promise.all([
  page.waitForNavigation(),
  page.click('a.logout')
]);
```

#### 5.2 处理弹窗

```typescript
// 处理 alert
page.on('dialog', async dialog => {
  console.log(dialog.message());
  await dialog.accept();
});

// 处理新窗口
const [newPage] = await Promise.all([
  page.waitForEvent('popup'),
  page.click('a[target="_blank"]')
]);
await newPage.waitForLoadState();
```

#### 5.3 文件上传

```typescript
// 上传文件
await page.setInputFiles('input[type="file"]', 'path/to/file.pdf');

// 上传多个文件
await page.setInputFiles('input[type="file"]', [
  'file1.pdf',
  'file2.pdf'
]);
```

#### 5.4 截图和视频

```typescript
// 截图
await page.screenshot({ path: 'screenshot.png' });

// 元素截图
await page.locator('.chart').screenshot({ path: 'chart.png' });

// 全页截图
await page.screenshot({ path: 'fullpage.png', fullPage: true });
```

### 第6步：测试组织（15分钟）

#### 6.1 使用 Fixtures

创建 `fixtures/test-fixtures.ts`：

```typescript
import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

type MyFixtures = {
  loginPage: LoginPage;
};

export const test = base.extend<MyFixtures>({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await use(loginPage);
  },
});

export { expect } from '@playwright/test';
```

使用 Fixtures：

```typescript
import { test, expect } from '../fixtures/test-fixtures';

test('使用 fixture 登录', async ({ loginPage, page }) => {
  await loginPage.login('testuser', 'password123');
  await expect(page).toHaveURL('/dashboard');
});
```

#### 6.2 测试钩子

```typescript
import { test, expect } from '@playwright/test';

test.describe('用户管理', () => {
  test.beforeEach(async ({ page }) => {
    // 每个测试前执行
    await page.goto('/admin/users');
  });

  test.afterEach(async ({ page }) => {
    // 每个测试后执行
    await page.evaluate(() => localStorage.clear());
  });

  test('创建用户', async ({ page }) => {
    // 测试逻辑
  });

  test('删除用户', async ({ page }) => {
    // 测试逻辑
  });
});
```

### 第7步：调试技巧（10分钟）

#### 7.1 调试模式

```bash
# 使用调试模式
npx playwright test --debug

# 使用 UI 模式
npx playwright test --ui
```

#### 7.2 代码中暂停

```typescript
test('调试测试', async ({ page }) => {
  await page.goto('/login');
  
  // 暂停执行，打开调试器
  await page.pause();
  
  await page.fill('#username', 'test');
});
```

#### 7.3 查看测试报告

```bash
# 生成 HTML 报告
npx playwright test --reporter=html

# 查看报告
npx playwright show-report
```

## 🎓 练习任务

### 初级练习
1. 创建一个注册页面的测试
2. 测试表单验证（必填字段、邮箱格式等）
3. 测试导航菜单的所有链接

### 中级练习
1. 为购物车功能创建 Page Object
2. 实现数据驱动的搜索测试
3. 测试文件上传和下载功能

### 高级练习
1. 实现跨页面的用户流程测试
2. 创建可复用的测试 Fixtures
3. 实现并行测试和测试分片

## 📚 延伸阅读

- Playwright 官方文档 (https://playwright.dev/)
- 测试最佳实践 (https://playwright.dev/docs/best-practices)
- Page Object Model 模式 (https://martinfowler.com/bliki/PageObject.html)
- 测试金字塔理论 (https://martinfowler.com/articles/practical-test-pyramid.html)

## 🔗 相关资源

- Playwright 示例代码 (examples/)
- 功能测试 Skill (./SKILL.md)
- 快速开始指南 (./quick-start.md)
- 输出格式说明 (./output-formats.md)

## ❓ 常见问题

### Q: 测试运行很慢怎么办？
A: 
- 使用 `test.describe.parallel()` 并行运行测试
- 减少不必要的等待时间
- 使用 `--workers` 参数控制并发数

### Q: 如何处理动态内容？
A: 
- 使用 `waitForSelector` 等待元素出现
- 使用 `waitForResponse` 等待 API 响应
- 使用 `toHaveText` 等自动重试的断言

### Q: 如何在 CI/CD 中运行测试？
A: 
- 使用 Docker 容器运行测试
- 配置无头模式：`use: { headless: true }`
- 保存测试报告和截图作为构建产物

## 🎉 下一步

完成本教程后，你可以：
- 学习 API 测试教程 (../api-testing/tutorial.md)
- 探索 自动化测试教程 (../automation-testing/tutorial.md)
- 查看 性能测试教程 (../performance-testing/tutorial.md)

---

*预计完成时间: 2-3 小时*  
*难度级别: 初级到中级*
