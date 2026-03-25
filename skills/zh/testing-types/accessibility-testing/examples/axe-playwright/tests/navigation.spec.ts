import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

/**
 * 导航可访问性测试套件
 * 
 * 测试覆盖：
 * - 键盘导航
 * - 焦点管理
 * - Skip links
 * - 导航菜单可访问性
 */

test.describe('导航可访问性测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');
  });

  test('导航菜单应通过可访问性扫描', async ({ page }) => {
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('nav, [role="navigation"]')
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('应有 Skip to main content 链接', async ({ page }) => {
    // 查找跳转链接
    const skipLink = page.locator('a[href="#main"], a[href="#content"]').first();
    
    // 按 Tab 键，跳转链接应该首先获得焦点
    await page.keyboard.press('Tab');
    
    // 检查跳转链接是否可见或可聚焦
    if (await skipLink.count() > 0) {
      await expect(skipLink).toBeFocused();
      
      // 验证链接文本有意义
      const text = await skipLink.textContent();
      expect(text?.toLowerCase()).toMatch(/skip|跳转|跳过/);
      
      // 点击跳转链接
      await skipLink.click();
      
      // 验证焦点移动到主内容区
      const mainContent = page.locator('#main, #content, main, [role="main"]').first();
      await expect(mainContent).toBeFocused();
    }
  });

  test('导航菜单应支持键盘操作', async ({ page }) => {
    // 找到第一个导航链接
    const firstNavLink = page.locator('nav a, [role="navigation"] a').first();
    await firstNavLink.focus();
    await expect(firstNavLink).toBeFocused();

    // 使用 Tab 键在导航项之间移动
    await page.keyboard.press('Tab');
    const secondNavLink = page.locator('nav a, [role="navigation"] a').nth(1);
    await expect(secondNavLink).toBeFocused();

    // 使用 Enter 键激活链接（不实际导航）
    // 只验证焦点状态
  });

  test('下拉菜单应可访问', async ({ page }) => {
    // 查找有子菜单的导航项
    const menuButton = page.locator('[aria-haspopup="true"], [aria-expanded]').first();
    
    if (await menuButton.count() > 0) {
      // 聚焦到菜单按钮
      await menuButton.focus();
      await expect(menuButton).toBeFocused();

      // 检查初始状态
      const initialExpanded = await menuButton.getAttribute('aria-expanded');
      expect(['true', 'false']).toContain(initialExpanded);

      // 使用 Enter 或 Space 打开菜单
      await page.keyboard.press('Enter');
      await page.waitForTimeout(300); // 等待动画

      // 验证菜单打开
      const expandedAfter = await menuButton.getAttribute('aria-expanded');
      expect(expandedAfter).toBe('true');

      // 验证子菜单可访问
      const submenu = page.locator('[role="menu"], [aria-labelledby]').first();
      if (await submenu.count() > 0) {
        const submenuResults = await new AxeBuilder({ page })
          .include('[role="menu"]')
          .analyze();
        
        expect(submenuResults.violations).toEqual([]);
      }

      // 使用 Esc 关闭菜单
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300);

      // 验证菜单关闭
      const expandedFinal = await menuButton.getAttribute('aria-expanded');
      expect(expandedFinal).toBe('false');
    }
  });

  test('移动端菜单按钮应可访问', async ({ page }) => {
    // 设置移动端视口
    await page.setViewportSize({ width: 375, height: 667 });

    // 查找菜单切换按钮
    const menuToggle = page.locator('[aria-label*="menu"], [aria-label*="菜单"], button.menu-toggle').first();
    
    if (await menuToggle.count() > 0) {
      // 验证按钮有可访问的名称
      const ariaLabel = await menuToggle.getAttribute('aria-label');
      expect(ariaLabel).toBeTruthy();

      // 验证按钮可聚焦
      await menuToggle.focus();
      await expect(menuToggle).toBeFocused();

      // 点击打开菜单
      await menuToggle.click();
      await page.waitForTimeout(300);

      // 验证菜单打开
      const expanded = await menuToggle.getAttribute('aria-expanded');
      expect(expanded).toBe('true');

      // 扫描打开的菜单
      const menuResults = await new AxeBuilder({ page })
        .include('nav, [role="navigation"]')
        .analyze();
      
      expect(menuResults.violations).toEqual([]);
    }
  });

  test('面包屑导航应可访问', async ({ page }) => {
    const breadcrumb = page.locator('[aria-label="breadcrumb"], nav.breadcrumb').first();
    
    if (await breadcrumb.count() > 0) {
      // 验证面包屑有正确的 ARIA 标签
      const ariaLabel = await breadcrumb.getAttribute('aria-label');
      expect(ariaLabel?.toLowerCase()).toMatch(/breadcrumb|面包屑/);

      // 扫描面包屑
      const breadcrumbResults = await new AxeBuilder({ page })
        .include('[aria-label="breadcrumb"]')
        .analyze();
      
      expect(breadcrumbResults.violations).toEqual([]);

      // 验证当前页面标记
      const currentPage = page.locator('[aria-current="page"]');
      if (await currentPage.count() > 0) {
        await expect(currentPage).toBeVisible();
      }
    }
  });

  test('焦点指示器应清晰可见', async ({ page }) => {
    // 获取第一个可聚焦元素
    const firstFocusable = page.locator('a, button, input, select, textarea').first();
    await firstFocusable.focus();

    // 检查焦点样式
    const focusOutline = await firstFocusable.evaluate((el) => {
      const styles = window.getComputedStyle(el);
      return {
        outline: styles.outline,
        outlineWidth: styles.outlineWidth,
        outlineStyle: styles.outlineStyle,
        outlineColor: styles.outlineColor,
        boxShadow: styles.boxShadow,
      };
    });

    // 验证有可见的焦点指示器
    const hasVisibleFocus = 
      (focusOutline.outline !== 'none' && focusOutline.outlineWidth !== '0px') ||
      focusOutline.boxShadow !== 'none';

    expect(hasVisibleFocus).toBe(true);
  });

  test('Tab 顺序应符合逻辑', async ({ page }) => {
    // 收集所有可聚焦元素
    const focusableElements = await page.locator('a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])').all();
    
    // 验证没有正数的 tabindex（破坏自然顺序）
    for (const element of focusableElements) {
      const tabindex = await element.getAttribute('tabindex');
      if (tabindex) {
        const tabindexValue = parseInt(tabindex, 10);
        expect(tabindexValue).toBeLessThanOrEqual(0);
      }
    }

    // 模拟 Tab 导航，验证顺序合理
    const tabOrder: string[] = [];
    for (let i = 0; i < Math.min(10, focusableElements.length); i++) {
      await page.keyboard.press('Tab');
      const focused = await page.locator(':focus').first();
      const tagName = await focused.evaluate(el => el.tagName);
      const text = await focused.textContent();
      tabOrder.push(`${tagName}: ${text?.substring(0, 20)}`);
    }

    // 打印 Tab 顺序供人工验证
    console.log('Tab 顺序:', tabOrder);
  });
});
