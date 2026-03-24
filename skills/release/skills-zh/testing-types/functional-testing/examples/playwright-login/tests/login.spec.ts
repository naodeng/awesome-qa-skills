import { test, expect } from '@playwright/test';

/**
 * 用户登录功能测试套件
 * 
 * 测试场景：
 * 1. 正常登录流程
 * 2. 无效凭据登录
 * 3. 空字段验证
 * 4. 记住我功能
 * 5. 密码可见性切换
 */

test.describe('用户登录功能', () => {
  // 每个测试前访问登录页面
  test.beforeEach(async ({ page }) => {
    await page.goto('https://demo.playwright.dev/login');
  });

  test('TC-001: 使用有效凭据成功登录', async ({ page }) => {
    // 测试步骤1: 输入用户名
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    
    // 测试步骤2: 输入密码
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    
    // 测试步骤3: 点击登录按钮
    await page.click('[data-testid="login-button"]');
    
    // 验证点1: 跳转到仪表板页面
    await expect(page).toHaveURL(/.*dashboard/);
    
    // 验证点2: 显示欢迎消息
    await expect(page.locator('[data-testid="welcome-message"]'))
      .toContainText('欢迎, testuser');
    
    // 验证点3: 显示用户头像
    await expect(page.locator('[data-testid="user-avatar"]')).toBeVisible();
    
    // 验证点4: 登录按钮消失，显示登出按钮
    await expect(page.locator('[data-testid="logout-button"]')).toBeVisible();
  });

  test('TC-002: 使用无效用户名登录失败', async ({ page }) => {
    // 输入不存在的用户名
    await page.fill('[data-testid="username"]', 'nonexistent@example.com');
    await page.fill('[data-testid="password"]', 'anypassword');
    await page.click('[data-testid="login-button"]');
    
    // 验证错误消息显示
    const errorMessage = page.locator('[data-testid="error-message"]');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText('用户名或密码错误');
    
    // 验证仍在登录页面
    await expect(page).toHaveURL(/.*login/);
    
    // 验证输入框保持可编辑状态
    await expect(page.locator('[data-testid="username"]')).toBeEditable();
  });

  test('TC-003: 使用错误密码登录失败', async ({ page }) => {
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    await page.fill('[data-testid="password"]', 'WrongPassword');
    await page.click('[data-testid="login-button"]');
    
    // 验证错误消息
    await expect(page.locator('[data-testid="error-message"]'))
      .toContainText('用户名或密码错误');
    
    // 验证密码框被清空（安全最佳实践）
    await expect(page.locator('[data-testid="password"]')).toHaveValue('');
  });

  test('TC-004: 空用户名验证', async ({ page }) => {
    // 只输入密码，用户名留空
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    await page.click('[data-testid="login-button"]');
    
    // 验证客户端验证消息
    const usernameInput = page.locator('[data-testid="username"]');
    await expect(usernameInput).toHaveAttribute('aria-invalid', 'true');
    
    // 验证错误提示
    await expect(page.locator('[data-testid="username-error"]'))
      .toContainText('请输入用户名');
  });

  test('TC-005: 空密码验证', async ({ page }) => {
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    // 密码留空
    await page.click('[data-testid="login-button"]');
    
    // 验证密码字段错误状态
    const passwordInput = page.locator('[data-testid="password"]');
    await expect(passwordInput).toHaveAttribute('aria-invalid', 'true');
    
    // 验证错误提示
    await expect(page.locator('[data-testid="password-error"]'))
      .toContainText('请输入密码');
  });

  test('TC-006: 用户名和密码都为空', async ({ page }) => {
    // 直接点击登录按钮
    await page.click('[data-testid="login-button"]');
    
    // 验证两个字段都显示错误
    await expect(page.locator('[data-testid="username-error"]')).toBeVisible();
    await expect(page.locator('[data-testid="password-error"]')).toBeVisible();
    
    // 验证登录按钮保持禁用状态
    await expect(page.locator('[data-testid="login-button"]')).toBeDisabled();
  });

  test('TC-007: 记住我功能', async ({ page, context }) => {
    // 勾选"记住我"
    await page.check('[data-testid="remember-me"]');
    
    // 登录
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    await page.click('[data-testid="login-button"]');
    
    // 等待登录成功
    await expect(page).toHaveURL(/.*dashboard/);
    
    // 验证 Cookie 已设置
    const cookies = await context.cookies();
    const rememberMeCookie = cookies.find(c => c.name === 'remember_token');
    expect(rememberMeCookie).toBeDefined();
    expect(rememberMeCookie?.expires).toBeGreaterThan(Date.now() / 1000 + 86400); // 至少1天
  });

  test('TC-008: 密码可见性切换', async ({ page }) => {
    const passwordInput = page.locator('[data-testid="password"]');
    const toggleButton = page.locator('[data-testid="password-toggle"]');
    
    // 输入密码
    await passwordInput.fill('SecurePass123!');
    
    // 验证初始状态为密码类型
    await expect(passwordInput).toHaveAttribute('type', 'password');
    
    // 点击显示密码
    await toggleButton.click();
    await expect(passwordInput).toHaveAttribute('type', 'text');
    await expect(passwordInput).toHaveValue('SecurePass123!');
    
    // 再次点击隐藏密码
    await toggleButton.click();
    await expect(passwordInput).toHaveAttribute('type', 'password');
  });

  test('TC-009: 登录按钮加载状态', async ({ page }) => {
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    
    // 点击登录按钮
    const loginButton = page.locator('[data-testid="login-button"]');
    await loginButton.click();
    
    // 验证加载状态
    await expect(loginButton).toBeDisabled();
    await expect(loginButton).toContainText('登录中...');
    await expect(page.locator('[data-testid="loading-spinner"]')).toBeVisible();
    
    // 等待登录完成
    await expect(page).toHaveURL(/.*dashboard/, { timeout: 5000 });
  });

  test('TC-010: 键盘导航 - Enter 键提交', async ({ page }) => {
    await page.fill('[data-testid="username"]', 'testuser@example.com');
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    
    // 按 Enter 键提交表单
    await page.locator('[data-testid="password"]').press('Enter');
    
    // 验证登录成功
    await expect(page).toHaveURL(/.*dashboard/);
  });
});

test.describe('登录页面可访问性', () => {
  test('TC-011: 表单元素具有正确的 ARIA 标签', async ({ page }) => {
    await page.goto('https://demo.playwright.dev/login');
    
    // 验证表单可访问性
    const usernameInput = page.locator('[data-testid="username"]');
    await expect(usernameInput).toHaveAttribute('aria-label', '用户名');
    
    const passwordInput = page.locator('[data-testid="password"]');
    await expect(passwordInput).toHaveAttribute('aria-label', '密码');
    
    const loginButton = page.locator('[data-testid="login-button"]');
    await expect(loginButton).toHaveAttribute('aria-label', '登录');
  });

  test('TC-012: 键盘焦点顺序正确', async ({ page }) => {
    await page.goto('https://demo.playwright.dev/login');
    
    // Tab 键导航
    await page.keyboard.press('Tab');
    await expect(page.locator('[data-testid="username"]')).toBeFocused();
    
    await page.keyboard.press('Tab');
    await expect(page.locator('[data-testid="password"]')).toBeFocused();
    
    await page.keyboard.press('Tab');
    await expect(page.locator('[data-testid="remember-me"]')).toBeFocused();
    
    await page.keyboard.press('Tab');
    await expect(page.locator('[data-testid="login-button"]')).toBeFocused();
  });
});

test.describe('登录安全性', () => {
  test('TC-013: 多次失败登录后账户锁定', async ({ page }) => {
    await page.goto('https://demo.playwright.dev/login');
    
    // 尝试5次错误登录
    for (let i = 0; i < 5; i++) {
      await page.fill('[data-testid="username"]', 'testuser@example.com');
      await page.fill('[data-testid="password"]', 'WrongPassword');
      await page.click('[data-testid="login-button"]');
      await page.waitForTimeout(500);
    }
    
    // 验证账户锁定消息
    await expect(page.locator('[data-testid="error-message"]'))
      .toContainText('账户已被锁定，请30分钟后重试');
    
    // 验证登录按钮被禁用
    await expect(page.locator('[data-testid="login-button"]')).toBeDisabled();
  });

  test('TC-014: SQL 注入防护', async ({ page }) => {
    await page.goto('https://demo.playwright.dev/login');
    
    // 尝试 SQL 注入
    await page.fill('[data-testid="username"]', "admin' OR '1'='1");
    await page.fill('[data-testid="password"]', "password' OR '1'='1");
    await page.click('[data-testid="login-button"]');
    
    // 验证登录失败
    await expect(page.locator('[data-testid="error-message"]'))
      .toContainText('用户名或密码错误');
    await expect(page).toHaveURL(/.*login/);
  });
});
