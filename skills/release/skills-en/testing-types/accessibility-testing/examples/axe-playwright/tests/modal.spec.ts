import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

/**
 * 模态框可访问性测试套件
 * 
 * 测试覆盖：
 * - 焦点管理
 * - 键盘陷阱
 * - ARIA 属性
 * - Esc 键关闭
 */

test.describe('模态框可访问性测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');
  });

  test('模态框应通过可访问性扫描', async ({ page }) => {
    // 打开模态框
    const openButton = page.locator('[data-testid="open-modal"], button:has-text("打开")').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]', { timeout: 5000 });

      // 扫描模态框
      const accessibilityScanResults = await new AxeBuilder({ page })
        .include('[role="dialog"]')
        .withTags(['wcag2a', 'wcag2aa'])
        .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    } else {
      test.skip();
    }
  });

  test('模态框应有正确的 ARIA 属性', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      const modal = page.locator('[role="dialog"]').first();

      // 验证 role="dialog"
      const role = await modal.getAttribute('role');
      expect(role).toBe('dialog');

      // 验证 aria-modal="true"
      const ariaModal = await modal.getAttribute('aria-modal');
      expect(ariaModal).toBe('true');

      // 验证 aria-labelledby 或 aria-label
      const ariaLabelledby = await modal.getAttribute('aria-labelledby');
      const ariaLabel = await modal.getAttribute('aria-label');
      expect(ariaLabelledby || ariaLabel).toBeTruthy();

      // 如果有 aria-labelledby，验证对应元素存在
      if (ariaLabelledby) {
        const labelElement = page.locator(`#${ariaLabelledby}`);
        await expect(labelElement).toBeVisible();
      }
    } else {
      test.skip();
    }
  });

  test('打开模态框时焦点应移动到模态框', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');
      await page.waitForTimeout(300); // 等待焦点移动

      // 验证焦点在模态框内
      const focusedElement = page.locator(':focus');
      const modal = page.locator('[role="dialog"]').first();
      
      // 焦点应该在模态框内的某个元素上
      const isFocusInModal = await focusedElement.evaluate((el, modalEl) => {
        return modalEl.contains(el);
      }, await modal.elementHandle());

      expect(isFocusInModal).toBe(true);
    } else {
      test.skip();
    }
  });

  test('焦点应被困在模态框内（焦点陷阱）', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      const modal = page.locator('[role="dialog"]').first();
      
      // 获取模态框内所有可聚焦元素
      const focusableElements = await modal.locator('a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])').all();
      
      if (focusableElements.length > 0) {
        // 聚焦到第一个元素
        await focusableElements[0].focus();

        // 按 Tab 键循环
        for (let i = 0; i < focusableElements.length + 2; i++) {
          await page.keyboard.press('Tab');
          
          // 验证焦点仍在模态框内
          const focusedElement = page.locator(':focus');
          const isFocusInModal = await focusedElement.evaluate((el, modalEl) => {
            return modalEl.contains(el);
          }, await modal.elementHandle());

          expect(isFocusInModal).toBe(true);
        }

        // 按 Shift+Tab 反向循环
        for (let i = 0; i < focusableElements.length + 2; i++) {
          await page.keyboard.press('Shift+Tab');
          
          const focusedElement = page.locator(':focus');
          const isFocusInModal = await focusedElement.evaluate((el, modalEl) => {
            return modalEl.contains(el);
          }, await modal.elementHandle());

          expect(isFocusInModal).toBe(true);
        }
      }
    } else {
      test.skip();
    }
  });

  test('按 Esc 键应关闭模态框', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      // 按 Esc 键
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300); // 等待关闭动画

      // 验证模态框已关闭
      const modal = page.locator('[role="dialog"]');
      await expect(modal).not.toBeVisible();
    } else {
      test.skip();
    }
  });

  test('关闭模态框后焦点应返回触发元素', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      // 聚焦并点击打开按钮
      await openButton.focus();
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      // 关闭模态框
      const closeButton = page.locator('[data-testid="close-modal"], [aria-label*="关闭"], [aria-label*="Close"]').first();
      if (await closeButton.count() > 0) {
        await closeButton.click();
      } else {
        await page.keyboard.press('Escape');
      }
      
      await page.waitForTimeout(300);

      // 验证焦点返回到打开按钮
      await expect(openButton).toBeFocused();
    } else {
      test.skip();
    }
  });

  test('点击遮罩层应关闭模态框', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      // 查找遮罩层
      const overlay = page.locator('.modal-overlay, .backdrop, [data-testid="modal-overlay"]').first();
      
      if (await overlay.count() > 0) {
        // 点击遮罩层（不是模态框内容）
        const box = await overlay.boundingBox();
        if (box) {
          await page.mouse.click(box.x + 10, box.y + 10);
          await page.waitForTimeout(300);

          // 验证模态框已关闭
          const modal = page.locator('[role="dialog"]');
          await expect(modal).not.toBeVisible();
        }
      }
    } else {
      test.skip();
    }
  });

  test('关闭按钮应有可访问的名称', async ({ page }) => {
    const openButton = page.locator('[data-testid="open-modal"]').first();
    
    if (await openButton.count() > 0) {
      await openButton.click();
      await page.waitForSelector('[role="dialog"]');

      // 查找关闭按钮
      const closeButton = page.locator('[data-testid="close-modal"], [aria-label*="关闭"], [aria-label*="Close"]').first();
      
      if (await closeButton.count() > 0) {
        // 验证有可访问的名称
        const ariaLabel = await closeButton.getAttribute('aria-label');
        const text = await closeButton.textContent();
        const title = await closeButton.getAttribute('title');

        expect(ariaLabel || text?.trim() || title).toBeTruthy();
      }
    } else {
      test.skip();
    }
  });
});
