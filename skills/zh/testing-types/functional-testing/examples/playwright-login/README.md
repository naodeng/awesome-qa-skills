# Playwright 登录功能测试示例

这是一个完整的 Playwright 测试示例，演示如何测试用户登录功能。

## 📋 测试覆盖

### 功能测试
- ✅ 正常登录流程
- ✅ 无效凭据处理
- ✅ 空字段验证
- ✅ 记住我功能
- ✅ 密码可见性切换
- ✅ 加载状态显示
- ✅ 键盘导航

### 可访问性测试
- ✅ ARIA 标签验证
- ✅ 键盘焦点顺序

### 安全性测试
- ✅ 账户锁定机制
- ✅ SQL 注入防护

## 🚀 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 运行测试

```bash
# 无头模式运行所有测试
npm test

# 有头模式运行（可以看到浏览器）
npm run test:headed

# 调试模式
npm run test:debug

# UI 模式（推荐）
npm run test:ui
```

### 3. 查看测试报告

```bash
npm run report
```

## 📁 项目结构

```
playwright-login/
├── package.json           # 项目配置和依赖
├── playwright.config.ts   # Playwright 配置
├── tests/
│   └── login.spec.ts      # 登录测试用例
└── README.md              # 本文档
```

## 🎯 测试用例说明

### TC-001: 使用有效凭据成功登录
**目的**: 验证正常登录流程  
**步骤**:
1. 输入有效用户名
2. 输入有效密码
3. 点击登录按钮

**预期结果**:
- 跳转到仪表板页面
- 显示欢迎消息
- 显示用户头像
- 显示登出按钮

### TC-002: 使用无效用户名登录失败
**目的**: 验证无效用户名的错误处理  
**预期结果**:
- 显示错误消息
- 保持在登录页面
- 输入框保持可编辑

### TC-003: 使用错误密码登录失败
**目的**: 验证错误密码的处理  
**预期结果**:
- 显示错误消息
- 密码框被清空（安全最佳实践）

### TC-004-006: 空字段验证
**目的**: 验证客户端表单验证  
**预期结果**:
- 显示相应的错误提示
- 字段标记为无效状态
- 登录按钮保持禁用

### TC-007: 记住我功能
**目的**: 验证持久化登录  
**预期结果**:
- 设置长期有效的 Cookie
- 下次访问自动登录

### TC-008: 密码可见性切换
**目的**: 验证密码显示/隐藏功能  
**预期结果**:
- 可以切换密码的可见性
- 密码值保持不变

### TC-009: 登录按钮加载状态
**目的**: 验证用户反馈  
**预期结果**:
- 按钮显示加载状态
- 按钮被禁用防止重复提交
- 显示加载动画

### TC-010: 键盘导航
**目的**: 验证键盘可访问性  
**预期结果**:
- Enter 键可以提交表单

### TC-011-012: 可访问性测试
**目的**: 验证 WCAG 合规性  
**预期结果**:
- 所有表单元素有正确的 ARIA 标签
- 键盘焦点顺序符合逻辑

### TC-013: 账户锁定机制
**目的**: 验证安全防护  
**预期结果**:
- 多次失败后锁定账户
- 显示锁定提示

### TC-014: SQL 注入防护
**目的**: 验证安全性  
**预期结果**:
- SQL 注入尝试被阻止
- 返回正常的错误消息

## 🔧 配置说明

### playwright.config.ts

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'https://demo.playwright.dev',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
```

## 📝 最佳实践

### 1. 使用 data-testid 定位元素
```typescript
// ✅ 推荐
await page.click('[data-testid="login-button"]');

// ❌ 不推荐（容易因 UI 变化而失效）
await page.click('.btn-primary');
```

### 2. 使用有意义的测试描述
```typescript
// ✅ 清晰的描述
test('TC-001: 使用有效凭据成功登录', async ({ page }) => {});

// ❌ 模糊的描述
test('test login', async ({ page }) => {});
```

### 3. 独立的测试用例
```typescript
// ✅ 每个测试独立
test.beforeEach(async ({ page }) => {
  await page.goto('/login');
});

// ❌ 测试之间有依赖
```

### 4. 明确的断言
```typescript
// ✅ 多个具体的断言
await expect(page).toHaveURL(/.*dashboard/);
await expect(page.locator('.welcome')).toContainText('欢迎');

// ❌ 单一模糊的断言
await expect(page.locator('.container')).toBeVisible();
```

### 5. 等待策略
```typescript
// ✅ 使用 Playwright 的自动等待
await expect(page.locator('.message')).toBeVisible();

// ❌ 使用固定延迟
await page.waitForTimeout(3000);
```

## 🐛 故障排除

### 问题1: 测试超时

**原因**: 元素加载慢或定位器不正确

**解决方案**:
```typescript
// 增加超时时间
await expect(page.locator('.slow-element')).toBeVisible({ timeout: 10000 });

// 或检查定位器是否正确
```

### 问题2: 测试不稳定

**原因**: 网络延迟或异步操作

**解决方案**:
```typescript
// 等待网络请求完成
await page.waitForResponse(resp => resp.url().includes('/api/login'));

// 等待特定状态
await page.waitForLoadState('networkidle');
```

### 问题3: 无法找到元素

**原因**: 元素在 iframe 中或动态加载

**解决方案**:
```typescript
// 处理 iframe
const frame = page.frameLocator('iframe[name="login-frame"]');
await frame.locator('[data-testid="username"]').fill('user');

// 等待元素出现
await page.waitForSelector('[data-testid="username"]');
```

## 📚 相关资源

- [Playwright 官方文档](https://playwright.dev/)
- [Playwright 最佳实践](https://playwright.dev/docs/best-practices)
- [测试选择器策略](https://playwright.dev/docs/selectors)
- [调试测试](https://playwright.dev/docs/debug)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

[PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0)
