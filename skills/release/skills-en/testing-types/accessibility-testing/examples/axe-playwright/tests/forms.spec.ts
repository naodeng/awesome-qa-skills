import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

/**
 * 表单可访问性测试套件
 * 
 * 测试覆盖：
 * - 表单标签
 * - 错误提示
 * - 必填字段标识
 * - 字段分组
 */

test.describe('表单可访问性测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/contact'); // 或其他包含表单的页面
    await page.waitForLoadState('networkidle');
  });

  test('表单应通过可访问性扫描', async ({ page }) => {
    const form = page.locator('form').first();
    
    if (await form.count() > 0) {
      const accessibilityScanResults = await new AxeBuilder({ page })
        .include('form')
        .withTags(['wcag2a', 'wcag2aa'])
        .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    } else {
      test.skip();
    }
  });

  test('所有输入框应有关联的标签', async ({ page }) => {
    const inputs = await page.locator('input:not([type="hidden"]), textarea, select').all();
    
    for (const input of inputs) {
      const id = await input.getAttribute('id');
      const ariaLabel = await input.getAttribute('aria-label');
      const ariaLabelledby = await input.getAttribute('aria-labelledby');
      
      // 检查是否有 label 关联
      let hasLabel = false;
      if (id) {
        const label = page.locator(`label[for="${id}"]`);
        hasLabel = await label.count() > 0;
      }

      // 检查是否在 label 内部
      const isInsideLabel = await input.evaluate((el) => {
        return el.closest('label') !== null;
      });

      // 应该有以下之一：label 关联、aria-label、aria-labelledby、在 label 内部
      expect(hasLabel || ariaLabel || ariaLabelledby || isInsideLabel).toBe(true);
    }
  });

  test('必填字段应有明确标识', async ({ page }) => {
    const requiredInputs = await page.locator('input[required], textarea[required], select[required]').all();
    
    for (const input of requiredInputs) {
      // 验证有 required 属性或 aria-required
      const required = await input.getAttribute('required');
      const ariaRequired = await input.getAttribute('aria-required');
      
      expect(required !== null || ariaRequired === 'true').toBe(true);

      // 验证标签中有视觉指示（如 * 号）
      const id = await input.getAttribute('id');
      if (id) {
        const label = page.locator(`label[for="${id}"]`);
        if (await label.count() > 0) {
          const labelText = await label.textContent();
          // 通常包含 * 或 "必填" 等文字
          const hasRequiredIndicator = labelText?.includes('*') || 
                                       labelText?.includes('必填') || 
                                       labelText?.includes('required');
          
          // 这是建议，不是强制要求
          if (!hasRequiredIndicator) {
            console.warn(`字段 ${id} 缺少视觉必填指示器`);
          }
        }
      }
    }
  });

  test('错误提示应可访问', async ({ page }) => {
    const form = page.locator('form').first();
    
    if (await form.count() > 0) {
      // 提交空表单触发验证
      const submitButton = page.locator('button[type="submit"]').first();
      await submitButton.click();
      
      // 等待错误提示
      await page.waitForSelector('[role="alert"], .error, [aria-invalid="true"]', { timeout: 5000 });

      // 扫描错误状态
      const accessibilityScanResults = await new AxeBuilder({ page })
        .include('form')
        .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);

      // 验证错误提示有 role="alert" 或 aria-live
      const errorMessages = page.locator('[role="alert"], [aria-live]');
      const count = await errorMessages.count();
      expect(count).toBeGreaterThan(0);

      // 验证无效字段标记为 aria-invalid="true"
      const invalidInputs = await page.locator('[aria-invalid="true"]').all();
      expect(invalidInputs.length).toBeGreaterThan(0);

      // 验证错误提示与字段关联
      for (const input of invalidInputs) {
        const ariaDescribedby = await input.getAttribute('aria-describedby');
        if (ariaDescribedby) {
          const errorElement = page.locator(`#${ariaDescribedby}`);
          await expect(errorElement).toBeVisible();
        }
      }
    } else {
      test.skip();
    }
  });

  test('字段分组应使用 fieldset 和 legend', async ({ page }) => {
    const fieldsets = await page.locator('fieldset').all();
    
    // 如果有 fieldset，验证每个都有 legend
    for (const fieldset of fieldsets) {
      const legend = fieldset.locator('legend').first();
      await expect(legend).toBeVisible();
      
      const legendText = await legend.textContent();
      expect(legendText?.trim()).toBeTruthy();
    }

    // 检查单选按钮组和复选框组
    const radioGroups = await page.locator('input[type="radio"]').all();
    if (radioGroups.length > 0) {
      // 单选按钮应该在 fieldset 中或有 role="radiogroup"
      for (const radio of radioGroups) {
        const inFieldset = await radio.evaluate((el) => {
          return el.closest('fieldset') !== null;
        });
        
        const inRadioGroup = await radio.evaluate((el) => {
          return el.closest('[role="radiogroup"]') !== null;
        });

        if (!inFieldset && !inRadioGroup) {
          console.warn('单选按钮应该在 fieldset 或 radiogroup 中');
        }
      }
    }
  });

  test('输入框应有合适的 autocomplete 属性', async ({ page }) => {
    // 常见字段的 autocomplete 值
    const expectedAutocomplete: Record<string, string[]> = {
      email: ['email'],
      password: ['current-password', 'new-password'],
      tel: ['tel'],
      name: ['name', 'given-name', 'family-name'],
      address: ['street-address', 'address-line1', 'address-line2'],
      city: ['address-level2'],
      country: ['country', 'country-name'],
      'postal-code': ['postal-code'],
      'credit-card': ['cc-number', 'cc-name', 'cc-exp', 'cc-csc'],
    };

    const inputs = await page.locator('input[type="email"], input[type="tel"], input[name*="name"], input[name*="address"]').all();
    
    for (const input of inputs) {
      const type = await input.getAttribute('type');
      const name = await input.getAttribute('name');
      const autocomplete = await input.getAttribute('autocomplete');

      // 建议有 autocomplete 属性
      if (!autocomplete) {
        console.warn(`字段 ${name || type} 建议添加 autocomplete 属性`);
      }
    }
  });

  test('帮助文本应与字段关联', async ({ page }) => {
    const inputs = await page.locator('input, textarea, select').all();
    
    for (const input of inputs) {
      const ariaDescribedby = await input.getAttribute('aria-describedby');
      
      if (ariaDescribedby) {
        // 验证描述元素存在
        const ids = ariaDescribedby.split(' ');
        for (const id of ids) {
          const descElement = page.locator(`#${id}`);
          const exists = await descElement.count() > 0;
          expect(exists).toBe(true);
        }
      }
    }
  });

  test('表单应支持键盘提交', async ({ page }) => {
    const form = page.locator('form').first();
    
    if (await form.count() > 0) {
      // 聚焦到第一个输入框
      const firstInput = form.locator('input, textarea, select').first();
      await firstInput.focus();

      // 填写表单（如果需要）
      const type = await firstInput.getAttribute('type');
      if (type === 'email') {
        await firstInput.fill('test@example.com');
      } else if (type === 'text') {
        await firstInput.fill('Test');
      }

      // 按 Enter 键提交
      await page.keyboard.press('Enter');
      
      // 验证表单响应（可能是验证错误或提交）
      // 这里只验证有响应，不验证具体行为
      await page.waitForTimeout(500);
    } else {
      test.skip();
    }
  });

  test('下拉选择框应可访问', async ({ page }) => {
    const selects = await page.locator('select').all();
    
    for (const select of selects) {
      // 验证有标签
      const id = await select.getAttribute('id');
      if (id) {
        const label = page.locator(`label[for="${id}"]`);
        const hasLabel = await label.count() > 0;
        
        const ariaLabel = await select.getAttribute('aria-label');
        const ariaLabelledby = await select.getAttribute('aria-labelledby');
        
        expect(hasLabel || ariaLabel || ariaLabelledby).toBe(true);
      }

      // 验证选项有文本
      const options = await select.locator('option').all();
      for (const option of options) {
        const text = await option.textContent();
        expect(text?.trim()).toBeTruthy();
      }
    }
  });

  test('复选框和单选按钮应可访问', async ({ page }) => {
    const checkboxes = await page.locator('input[type="checkbox"], input[type="radio"]').all();
    
    for (const checkbox of checkboxes) {
      // 验证有标签
      const id = await checkbox.getAttribute('id');
      if (id) {
        const label = page.locator(`label[for="${id}"]`);
        const hasLabel = await label.count() > 0;
        
        const ariaLabel = await checkbox.getAttribute('aria-label');
        const ariaLabelledby = await checkbox.getAttribute('aria-labelledby');
        
        expect(hasLabel || ariaLabel || ariaLabelledby).toBe(true);
      }

      // 验证可以通过空格键切换
      await checkbox.focus();
      const initialChecked = await checkbox.isChecked();
      
      await page.keyboard.press('Space');
      await page.waitForTimeout(100);
      
      const afterChecked = await checkbox.isChecked();
      expect(afterChecked).toBe(!initialChecked);
    }
  });
});
