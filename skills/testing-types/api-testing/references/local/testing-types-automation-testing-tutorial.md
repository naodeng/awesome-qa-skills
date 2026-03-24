# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__automation-testing__tutorial.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# 自动化测试教程

## 📚 学习目标

完成本教程后，你将能够：
- 理解自动化测试的核心概念和设计模式
- 掌握 Page Object Model (POM) 设计模式
- 实现数据驱动测试和关键字驱动测试
- 构建可维护的自动化测试框架
- 集成测试到 CI/CD 流程

## 🎯 前置要求

- 掌握至少一门编程语言（JavaScript/Python/Java）
- 了解 Web 技术基础（HTML、CSS、JavaScript）
- 熟悉测试基础概念
- 完成 功能测试教程 (references/_external/testing-types__functional-testing__tutorial__bf70f7da4c.md)

## 📖 教程内容

### 第1步：自动化测试基础（15分钟）

#### 1.1 什么是自动化测试？

自动化测试是使用工具和脚本自动执行测试用例的过程。

**适合自动化的场景：**
- ✅ 重复执行的测试（回归测试）
- ✅ 数据驱动的测试
- ✅ 跨浏览器/跨平台测试
- ✅ 性能和负载测试
- ✅ API 测试

**不适合自动化的场景：**
- ❌ 一次性测试
- ❌ 需要人工判断的测试（视觉测试）
- ❌ 频繁变化的功能
- ❌ 探索性测试

#### 1.2 自动化测试金字塔

```
       /\
      /  \     E2E Tests (10%)
     /____\    
    /      \   Integration Tests (30%)
   /________\  
  /          \ Unit Tests (60%)
 /____________\
```

### 第2步：Page Object Model 模式（30分钟）

#### 2.1 理解 POM 模式

POM 是一种设计模式，将页面元素和操作封装到类中，提高代码复用性和可维护性。

**优势：**
- 🔄 代码复用
- 🛠️ 易于维护
- 📖 提高可读性
- 🧪 降低测试脆弱性

#### 2.2 创建 Page Object

创建 `pages/BasePage.ts`：

```typescript
import { Page, Locator } from '@playwright/test';

export class BasePage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async goto(url: string) {
    await this.page.goto(url);
  }

  async waitForPageLoad() {
    await this.page.waitForLoadState('networkidle');
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ path: `screenshots/${name}.png` });
  }

  async getTitle(): Promise<string> {
    return await this.page.title();
  }
}
```

创建 `pages/LoginPage.ts`：

```typescript
import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  // 定位器
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;
  readonly rememberMeCheckbox: Locator;

  constructor(page: Page) {
    super(page);
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.error-message');
    this.rememberMeCheckbox = page.locator('#remember-me');
  }

  // 页面操作
  async goto() {
    await super.goto('/login');
  }

  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async loginWithRememberMe(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.rememberMeCheckbox.check();
    await this.loginButton.click();
  }

  async getErrorMessage(): Promise<string | null> {
    return await this.errorMessage.textContent();
  }

  async isLoginButtonEnabled(): Promise<boolean> {
    return await this.loginButton.isEnabled();
  }
}
```

创建 `pages/DashboardPage.ts`：

```typescript
import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class DashboardPage extends BasePage {
  readonly welcomeMessage: Locator;
  readonly logoutButton: Locator;
  readonly userMenu: Locator;

  constructor(page: Page) {
    super(page);
    this.welcomeMessage = page.locator('.welcome-message');
    this.logoutButton = page.locator('button.logout');
    this.userMenu = page.locator('.user-menu');
  }

  async getWelcomeMessage(): Promise<string | null> {
    return await this.welcomeMessage.textContent();
  }

  async logout() {
    await this.userMenu.click();
    await this.logoutButton.click();
  }

  async isLoggedIn(): Promise<boolean> {
    return await this.welcomeMessage.isVisible();
  }
}
```

#### 2.3 使用 Page Objects

创建 `tests/login.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { DashboardPage } from '../pages/DashboardPage';

test.describe('登录功能测试', () => {
  let loginPage: LoginPage;
  let dashboardPage: DashboardPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    dashboardPage = new DashboardPage(page);
    await loginPage.goto();
  });

  test('成功登录', async ({ page }) => {
    await loginPage.login('testuser', 'password123');
    
    await expect(page).toHaveURL('/dashboard');
    const welcome = await dashboardPage.getWelcomeMessage();
    expect(welcome).toContain('欢迎');
  });

  test('登录失败显示错误', async () => {
    await loginPage.login('invalid', 'wrong');
    
    const error = await loginPage.getErrorMessage();
    expect(error).toContain('用户名或密码错误');
  });

  test('记住我功能', async ({ page, context }) => {
    await loginPage.loginWithRememberMe('testuser', 'password123');
    
    // 验证 cookie 已设置
    const cookies = await context.cookies();
    const rememberCookie = cookies.find(c => c.name === 'remember_token');
    expect(rememberCookie).toBeDefined();
  });
});
```

### 第3步：数据驱动测试（25分钟）

#### 3.1 使用 JSON 文件

创建 `data/users.json`：

```json
{
  "validUsers": [
    { "username": "admin", "password": "admin123", "role": "管理员" },
    { "username": "user1", "password": "user123", "role": "普通用户" }
  ],
  "invalidUsers": [
    { "username": "", "password": "pass", "error": "请输入用户名" },
    { "username": "user", "password": "", "error": "请输入密码" },
    { "username": "invalid", "password": "wrong", "error": "用户名或密码错误" }
  ]
}
```

创建 `tests/login-data-driven.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { DashboardPage } from '../pages/DashboardPage';
import testData from '../data/users.json';

test.describe('数据驱动登录测试', () => {
  testData.validUsers.forEach(({ username, password, role }) => {
    test(`${role}登录成功`, async ({ page }) => {
      const loginPage = new LoginPage(page);
      const dashboardPage = new DashboardPage(page);

      await loginPage.goto();
      await loginPage.login(username, password);

      await expect(page).toHaveURL('/dashboard');
      const welcome = await dashboardPage.getWelcomeMessage();
      expect(welcome).toContain(role);
    });
  });

  testData.invalidUsers.forEach(({ username, password, error }) => {
    test(`登录失败: ${error}`, async ({ page }) => {
      const loginPage = new LoginPage(page);

      await loginPage.goto();
      await loginPage.login(username, password);

      const errorMsg = await loginPage.getErrorMessage();
      expect(errorMsg).toContain(error);
    });
  });
});
```

#### 3.2 使用 CSV 文件

创建 `data/test-data.csv`：

```csv
username,password,expected
admin,admin123,success
user1,user123,success
,password,请输入用户名
username,,请输入密码
invalid,wrong,用户名或密码错误
```

创建 `utils/csv-reader.ts`：

```typescript
import * as fs from 'fs';
import * as path from 'path';

export function readCSV(filename: string): any[] {
  const filePath = path.join(__dirname, '../data', filename);
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.trim().split('\n');
  const headers = lines[0].split(',');
  
  return lines.slice(1).map(line => {
    const values = line.split(',');
    return headers.reduce((obj, header, index) => {
      obj[header] = values[index];
      return obj;
    }, {} as any);
  });
}
```

使用 CSV 数据：

```typescript
import { readCSV } from '../utils/csv-reader';

const testData = readCSV('test-data.csv');

testData.forEach(({ username, password, expected }) => {
  test(`测试: ${username} / ${password}`, async ({ page }) => {
    // 测试逻辑
  });
});
```

### 第4步：关键字驱动测试（30分钟）

#### 4.1 创建关键字库

创建 `keywords/WebKeywords.ts`：

```typescript
import { Page } from '@playwright/test';

export class WebKeywords {
  constructor(private page: Page) {}

  async navigateTo(url: string) {
    await this.page.goto(url);
  }

  async clickElement(selector: string) {
    await this.page.click(selector);
  }

  async inputText(selector: string, text: string) {
    await this.page.fill(selector, text);
  }

  async verifyText(selector: string, expectedText: string): Promise<boolean> {
    const text = await this.page.textContent(selector);
    return text?.includes(expectedText) || false;
  }

  async verifyElementVisible(selector: string): Promise<boolean> {
    return await this.page.isVisible(selector);
  }

  async selectDropdown(selector: string, value: string) {
    await this.page.selectOption(selector, value);
  }

  async checkCheckbox(selector: string) {
    await this.page.check(selector);
  }

  async waitForElement(selector: string, timeout: number = 5000) {
    await this.page.waitForSelector(selector, { timeout });
  }
}
```

#### 4.2 创建测试步骤文件

创建 `data/login-steps.json`：

```json
{
  "testCases": [
    {
      "name": "成功登录测试",
      "steps": [
        { "keyword": "navigateTo", "args": ["/login"] },
        { "keyword": "inputText", "args": ["#username", "testuser"] },
        { "keyword": "inputText", "args": ["#password", "password123"] },
        { "keyword": "clickElement", "args": ["button[type='submit']"] },
        { "keyword": "verifyText", "args": [".welcome-message", "欢迎"] }
      ]
    },
    {
      "name": "登录失败测试",
      "steps": [
        { "keyword": "navigateTo", "args": ["/login"] },
        { "keyword": "inputText", "args": ["#username", "invalid"] },
        { "keyword": "inputText", "args": ["#password", "wrong"] },
        { "keyword": "clickElement", "args": ["button[type='submit']"] },
        { "keyword": "verifyText", "args": [".error-message", "错误"] }
      ]
    }
  ]
}
```

#### 4.3 执行关键字驱动测试

创建 `tests/keyword-driven.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import { WebKeywords } from '../keywords/WebKeywords';
import testSteps from '../data/login-steps.json';

test.describe('关键字驱动测试', () => {
  testSteps.testCases.forEach(({ name, steps }) => {
    test(name, async ({ page }) => {
      const keywords = new WebKeywords(page);

      for (const step of steps) {
        const { keyword, args } = step;
        const method = (keywords as any)[keyword];
        
        if (typeof method === 'function') {
          const result = await method.apply(keywords, args);
          
          // 如果是验证关键字，检查结果
          if (keyword.startsWith('verify')) {
            expect(result).toBe(true);
          }
        } else {
          throw new Error(`关键字 "${keyword}" 不存在`);
        }
      }
    });
  });
});
```

### 第5步：测试框架组织（20分钟）

#### 5.1 项目结构

```
automation-framework/
├── pages/              # Page Objects
│   ├── BasePage.ts
│   ├── LoginPage.ts
│   └── DashboardPage.ts
├── tests/              # 测试用例
│   ├── login.spec.ts
│   └── dashboard.spec.ts
├── data/               # 测试数据
│   ├── users.json
│   └── test-data.csv
├── keywords/           # 关键字库
│   └── WebKeywords.ts
├── utils/              # 工具函数
│   ├── csv-reader.ts
│   └── test-helpers.ts
├── fixtures/           # 测试 Fixtures
│   └── test-fixtures.ts
├── config/             # 配置文件
│   └── test-config.ts
└── playwright.config.ts
```

#### 5.2 创建测试 Fixtures

创建 `fixtures/test-fixtures.ts`：

```typescript
import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { DashboardPage } from '../pages/DashboardPage';

type MyFixtures = {
  loginPage: LoginPage;
  dashboardPage: DashboardPage;
  authenticatedPage: Page;
};

export const test = base.extend<MyFixtures>({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await use(loginPage);
  },

  dashboardPage: async ({ page }, use) => {
    const dashboardPage = new DashboardPage(page);
    await use(dashboardPage);
  },

  authenticatedPage: async ({ page }, use) => {
    // 自动登录
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('testuser', 'password123');
    await page.waitForURL('/dashboard');
    await use(page);
  },
});

export { expect } from '@playwright/test';
```

使用 Fixtures：

```typescript
import { test, expect } from '../fixtures/test-fixtures';

test('使用认证 fixture', async ({ authenticatedPage, dashboardPage }) => {
  // 页面已经登录，直接测试
  const welcome = await dashboardPage.getWelcomeMessage();
  expect(welcome).toContain('欢迎');
});
```

#### 5.3 配置管理

创建 `config/test-config.ts`：

```typescript
export const config = {
  baseURL: process.env.BASE_URL || 'http://localhost:3000',
  timeout: parseInt(process.env.TIMEOUT || '30000'),
  retries: parseInt(process.env.RETRIES || '2'),
  
  users: {
    admin: {
      username: process.env.ADMIN_USER || 'admin',
      password: process.env.ADMIN_PASS || 'admin123',
    },
    regular: {
      username: process.env.USER || 'user1',
      password: process.env.USER_PASS || 'user123',
    },
  },
  
  screenshots: {
    onFailure: true,
    onSuccess: false,
  },
};
```

### 第6步：CI/CD 集成（15分钟）

#### 6.1 GitHub Actions 配置

创建 `.github/workflows/test.yml`：

```yaml
name: Automated Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨2点运行

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright browsers
        run: npx playwright install --with-deps
      
      - name: Run tests
        run: npx playwright test --project=${{ matrix.browser }}
        env:
          BASE_URL: ${{ secrets.BASE_URL }}
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results-${{ matrix.browser }}
          path: test-results/
      
      - name: Upload HTML report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report-${{ matrix.browser }}
          path: playwright-report/
```

#### 6.2 Docker 支持

创建 `Dockerfile`：

```dockerfile
FROM mcr.microsoft.com/playwright:v1.40.0-focal

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

CMD ["npx", "playwright", "test"]
```

创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  tests:
    build: .
    environment:
      - BASE_URL=http://app:3000
      - CI=true
    volumes:
      - ./test-results:/app/test-results
      - ./playwright-report:/app/playwright-report
    depends_on:
      - app
  
  app:
    image: your-app-image
    ports:
      - "3000:3000"
```

运行测试：

```bash
docker-compose up --abort-on-container-exit
```

## 🎓 练习任务

### 初级练习
1. 为一个简单的表单创建 Page Object
2. 实现基本的数据驱动测试
3. 添加测试报告生成

### 中级练习
1. 构建完整的 POM 框架
2. 实现关键字驱动测试
3. 集成测试到 CI/CD

### 高级练习
1. 实现混合测试框架（POM + 数据驱动 + 关键字驱动）
2. 添加并行测试和测试分片
3. 实现自定义测试报告和仪表板

## 📚 延伸阅读

- 测试自动化金字塔 (https://martinfowler.com/articles/practical-test-pyramid.html)
- Page Object Model 模式 (https://martinfowler.com/bliki/PageObject.html)
- 测试框架设计 (https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- CI/CD 最佳实践 (https://docs.github.com/en/actions/automating-builds-and-tests)

## 🔗 相关资源

- Selenium POM 示例 (examples/)
- 自动化测试 Skill (./SKILL.md)
- 快速开始指南 (./quick-start.md)

## ❓ 常见问题

### Q: 何时使用 POM 模式？
A: 当你有多个测试用例需要操作同一个页面时，使用 POM 可以提高代码复用性和可维护性。

### Q: 数据驱动和关键字驱动有什么区别？
A: 
- 数据驱动：相同的测试逻辑，不同的测试数据
- 关键字驱动：将测试步骤抽象为关键字，非技术人员也能编写测试

### Q: 如何提高测试执行速度？
A: 
- 使用并行执行
- 优化等待策略
- 使用测试分片
- 减少不必要的 UI 交互

## 🎉 下一步

完成本教程后，你可以：
- 学习 性能测试教程 (references/_external/testing-types__performance-testing__tutorial__3e9ccbfe14.md)
- 探索 安全测试教程 (references/_external/testing-types__security-testing__SKILL__3a2ebb5198.md)
- 查看 移动测试教程 (references/_external/testing-types__mobile-testing__tutorial__0d1f5d019c.md)

---

*预计完成时间: 3-4 小时*  
*难度级别: 中级到高级*
