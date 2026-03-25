import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { saveViolations, printViolationsSummary } from '../utils/axe-helper';

/**
 * 首页可访问性测试套件
 * 
 * 测试覆盖：
 * - WCAG 2.1 Level A/AA 合规性
 * - 页面结构和语义
 * - 图片替代文本
 * - 颜色对比度
 */

test.describe('首页可访问性测试', () => {
  test.beforeEach(async ({ page }) => {
    // 访问首页
    await page.goto('/');
    await page.waitForLoadState('networkidle');
  });

  test('应通过 WCAG 2.1 Level A 标准', async ({ page }) => {
    // 运行 axe 扫描，只检查 Level A
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a'])
      .analyze();

    // 如果有违规，保存详细报告
    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'homepage-wcag2a');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    // 断言没有违规
    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('应通过 WCAG 2.1 Level AA 标准', async ({ page }) => {
    // 运行 axe 扫描，检查 Level A 和 AA
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    // 如果有违规，保存详细报告
    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'homepage-wcag2aa');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    // 断言没有违规
    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('所有图片应有替代文本', async ({ page }) => {
    // 只检查图片替代文本规则
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['image-alt'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);

    // 额外验证：检查所有图片
    const images = await page.locator('img').all();
    
    for (const img of images) {
      const alt = await img.getAttribute('alt');
      const role = await img.getAttribute('role');
      
      // 图片应该有 alt 属性（可以为空字符串表示装饰性图片）
      // 或者有 role="presentation"
      expect(alt !== null || role === 'presentation').toBe(true);
    }
  });

  test('颜色对比度应符合标准', async ({ page }) => {
    // 只检查颜色对比度
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['color-contrast'])
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'homepage-color-contrast');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('标题层级应正确', async ({ page }) => {
    // 检查标题层级
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['heading-order'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);

    // 额外验证：应该有 h1 标题
    const h1Count = await page.locator('h1').count();
    expect(h1Count).toBeGreaterThan(0);
    expect(h1Count).toBeLessThanOrEqual(1); // 每页只应有一个 h1
  });

  test('页面应有有效的语言属性', async ({ page }) => {
    // 检查 HTML lang 属性
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['html-has-lang', 'html-lang-valid'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);

    // 额外验证
    const lang = await page.locator('html').getAttribute('lang');
    expect(lang).toBeTruthy();
    expect(lang).toMatch(/^[a-z]{2}(-[A-Z]{2})?$/); // 如 'zh' 或 'zh-CN'
  });

  test('链接应有可访问的名称', async ({ page }) => {
    // 检查链接可访问性
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['link-name'])
      .analyze();

    if (accessibilityScanResults.violations.length > 0) {
      await saveViolations(page, accessibilityScanResults.violations, 'homepage-link-name');
      printViolationsSummary(accessibilityScanResults.violations);
    }

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('页面应有有效的地标区域', async ({ page }) => {
    // 检查地标区域
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withRules(['region'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);

    // 验证关键地标存在
    const main = await page.locator('main, [role="main"]').count();
    expect(main).toBeGreaterThan(0);
  });
});
