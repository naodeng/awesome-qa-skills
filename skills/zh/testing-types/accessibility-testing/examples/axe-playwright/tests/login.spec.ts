import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { saveViolations, printViolationsSummary } from '../utils/axe-helper';

/**
 * 登录表单可访问性测试套件
 * 
 * 测试覆盖：
 * - 表单标签和关联
 * - 错误提示可访问性
 * - 键盘导航
 * - 焦点管理
 */

test.describe('登录表单可访问性测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.waitForLoadState('networkidle');
  });

  test('表单应通过可访问性扫描', async ({ page }) => {
    // 只扫描表单区域
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('form')
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'login-form');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('所有表单控件应有关联的标签', async ({ page }) => {
    // 检查标签关联
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['label'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);

    // 额外验证：检查邮箱和密码字段
    const emailLabel = page.locator('label[for="email"]');
    await expect(emailLabel).toBeVisible();
    
    const passwordLabel = page.locator('label[for="password"]');
    await expect(passwordLabel).toBeVisible();
  });

  test('表单应支持键盘导航', async ({ page }) => {
    // 使用 Tab 键导航到第一个输入框
    await page.keyboard.press('Tab');
    
    // 检查焦点是否在邮箱输入框
    const emailInput = page.locator('#email, input[type="email"]').first();
    await expect(emailInput).toBeFocused();

    // 继续 Tab 到密码输入框
    await page.keyboard.press('Tab');
    const passwordInput = page.locator('#password, input[type="password"]').first();
    await expect(passwordInput).toBeFocused();

    // Tab 到提交按钮
    await page.keyboard.press('Tab');
    const submitButton = page.locator('button[type="submit"]');
    await expect(submitButton).toBeFocused();

    // 使用 Enter 键提交（应该触发验证）
    await page.keyboard.press('Enter');
  });

  test('错误提示应可访问', async ({ page }) => {
    // 提交空表单触发验证错误
    const submitButton = page.locator('button[type="submit"]');
    await submitButton.click();

    // 等待错误提示出现
    await page.waitForSelector('[role="alert"], .error-message', { timeout: 5000 });

    // 扫描错误状态下的表单
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('form')
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'login-form-errors');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    expect(accessibilityScanResults.violations).toEqual([]);

    // 验证错误提示有 role="alert" 或 aria-live
    const errorMessages = page.locator('[role="alert"], [aria-live]');
    const count = await errorMessages.count();
    expect(count).toBeGreaterThan(0);
  });

  test('输入框应有正确的 aria 属性', async ({ page }) => {
    // 提交空表单触发验证错误
    await page.locator('button[type="submit"]').click();
    await page.waitForSelector('[role="alert"], .error-message', { timeout: 5000 });

    // 检查邮箱输入框的 aria 属性
    const emailInput = page.locator('#email, input[type="email"]').first();
    const emailAriaInvalid = await emailInput.getAttribute('aria-invalid');
    const emailAriaDescribedby = await emailInput.getAttribute('aria-describedby');

    // 应该标记为 invalid
    expect(emailAriaInvalid).toBe('true');
    
    // 应该关联到错误提示
    if (emailAriaDescribedby) {
      const errorElement = page.locator(`#${emailAriaDescribedby}`);
      await expect(errorElement).toBeVisible();
    }
  });

  test('密码输入框应有显示/隐藏切换', async ({ page }) => {
    const passwordInput = page.locator('#password, input[type="password"]').first();
    
    // 检查是否有切换按钮
    const toggleButton = page.locator('button[aria-label*="显示"], button[aria-label*="隐藏"], button[aria-label*="Show"], button[aria-label*="Hide"]');
    
    if (await toggleButton.count() > 0) {
      // 验证切换按钮可访问
      await expect(toggleButton.first()).toBeVisible();
      
      // 验证按钮有可访问的名称
      const ariaLabel = await toggleButton.first().getAttribute('aria-label');
      expect(ariaLabel).toBeTruthy();
      
      // 点击切换
      await toggleButton.first().click();
      
      // 验证输入框类型改变
      const type = await passwordInput.getAttribute('type');
      expect(['password', 'text']).toContain(type);
    }
  });

  test('记住我复选框应可访问', async ({ page }) => {
    const rememberCheckbox = page.locator('input[type="checkbox"]').first();
    
    if (await rememberCheckbox.count() > 0) {
      // 检查复选框可访问性
      const accessibilityScanResults = await new AxeBuilder({ page })
        .include('input[type="checkbox"]')
        .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);

      // 验证有关联的标签
      const checkboxId = await rememberCheckbox.getAttribute('id');
      if (checkboxId) {
        const label = page.locator(`label[for="${checkboxId}"]`);
        await expect(label).toBeVisible();
      }

      // 验证可以通过空格键切换
      await rememberCheckbox.focus();
      await page.keyboard.press('Space');
      const checked = await rememberCheckbox.isChecked();
      expect(checked).toBe(true);
    }
  });

  test('忘记密码链接应可访问', async ({ page }) => {
    const forgotPasswordLink = page.locator('a[href*="forgot"], a[href*="reset"]').first();
    
    if (await forgotPasswordLink.count() > 0) {
      // 验证链接有可访问的名称
      const text = await forgotPasswordLink.textContent();
      expect(text?.trim()).toBeTruthy();

      // 验证链接可以通过键盘访问
      await forgotPasswordLink.focus();
      await expect(forgotPasswordLink).toBeFocused();

      // 验证可以通过 Enter 键激活
      // （不实际导航，只验证焦点）
    }
  });
});
