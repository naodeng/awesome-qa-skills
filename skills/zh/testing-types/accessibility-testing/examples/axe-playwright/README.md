# axe-core + Playwright 可访问性测试示例

这是一个完整的可访问性自动化测试项目，使用 axe-core 和 Playwright 检测 WCAG 2.1 合规性问题。

## 📋 项目概述

- **测试框架**: Playwright + axe-core
- **测试用例数**: 12 个
- **覆盖标准**: WCAG 2.1 Level A/AA
- **测试类型**: 自动化可访问性扫描
- **代码行数**: ~450 行

## 🎯 测试覆盖

### WCAG 2.1 原则覆盖

1. **Perceivable（可感知）**
   - 图片替代文本
   - 颜色对比度
   - 音频/视频字幕

2. **Operable（可操作）**
   - 键盘可访问性
   - 焦点管理
   - 导航一致性

3. **Understandable（可理解）**
   - 表单标签
   - 错误提示
   - 语言标识

4. **Robust（健壮）**
   - 有效的 HTML
   - ARIA 属性
   - 兼容性

### 测试场景

- ✅ 首页可访问性扫描
- ✅ 登录表单可访问性
- ✅ 导航菜单键盘访问
- ✅ 模态框可访问性
- ✅ 表单验证可访问性
- ✅ 图片替代文本检查
- ✅ 颜色对比度检查
- ✅ 标题层级检查
- ✅ 链接可访问性
- ✅ 按钮可访问性
- ✅ 表格可访问性
- ✅ 动态内容可访问性

## 🚀 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 运行测试

```bash
# 运行所有测试
npm test

# 运行特定测试文件
npm test -- homepage.spec.ts

# 调试模式
npm test -- --debug

# 生成 HTML 报告
npm test -- --reporter=html
```

### 3. 查看报告

```bash
# 打开 HTML 报告
npx playwright show-report

# 查看 JSON 报告
cat a11y-violations.json
```

## 📁 项目结构

```
axe-playwright/
├── tests/
│   ├── homepage.spec.ts          # 首页可访问性测试
│   ├── login.spec.ts              # 登录表单测试
│   ├── navigation.spec.ts         # 导航测试
│   ├── modal.spec.ts              # 模态框测试
│   └── forms.spec.ts              # 表单测试
├── utils/
│   ├── axe-helper.ts              # axe 辅助函数
│   └── report-generator.ts        # 报告生成器
├── playwright.config.ts           # Playwright 配置
├── package.json
└── README.md
```

## 🔧 配置说明

### playwright.config.ts

```typescript
export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 1,
  use: {
    baseURL: 'https://example.com',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
});
```

### axe 配置选项

```typescript
// 只检查 WCAG 2.1 Level A/AA
await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa'])
  .analyze();

// 排除特定规则
await new AxeBuilder({ page })
  .disableRules(['color-contrast'])
  .analyze();

// 只检查特定区域
await new AxeBuilder({ page })
  .include('#main-content')
  .exclude('#ads')
  .analyze();
```

## 📊 测试报告

### 违规项格式

```json
{
  "violations": [
    {
      "id": "color-contrast",
      "impact": "serious",
      "description": "确保前景色和背景色的对比度满足 WCAG 2 AA 标准",
      "help": "元素必须有足够的颜色对比度",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.4/color-contrast",
      "tags": ["wcag2aa", "wcag143"],
      "nodes": [
        {
          "html": "<a href=\"/about\">关于我们</a>",
          "target": ["a[href=\"/about\"]"],
          "failureSummary": "对比度为 2.5:1，需要至少 4.5:1"
        }
      ]
    }
  ]
}
```

### 影响级别

- **critical**: 严重影响可访问性，必须立即修复
- **serious**: 严重问题，应优先修复
- **moderate**: 中等问题，应该修复
- **minor**: 轻微问题，建议修复

## 🧪 测试示例

### 基础可访问性扫描

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('首页可访问性', async ({ page }) => {
  await page.goto('/');
  
  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();
  
  expect(accessibilityScanResults.violations).toEqual([]);
});
```

### 表单可访问性测试

```typescript
test('登录表单可访问性', async ({ page }) => {
  await page.goto('/login');
  
  // 检查表单区域
  const results = await new AxeBuilder({ page })
    .include('form')
    .analyze();
  
  expect(results.violations).toEqual([]);
  
  // 验证表单标签
  const emailLabel = page.locator('label[for="email"]');
  await expect(emailLabel).toBeVisible();
  
  const passwordLabel = page.locator('label[for="password"]');
  await expect(passwordLabel).toBeVisible();
});
```

### 键盘导航测试

```typescript
test('键盘导航', async ({ page }) => {
  await page.goto('/');
  
  // 使用 Tab 键导航
  await page.keyboard.press('Tab');
  
  // 检查焦点可见性
  const focusedElement = await page.locator(':focus');
  await expect(focusedElement).toBeVisible();
  
  // 检查焦点指示器
  const focusOutline = await focusedElement.evaluate((el) => {
    const styles = window.getComputedStyle(el);
    return styles.outline !== 'none';
  });
  
  expect(focusOutline).toBe(true);
});
```

### 动态内容测试

```typescript
test('模态框可访问性', async ({ page }) => {
  await page.goto('/');
  
  // 打开模态框
  await page.click('[data-testid="open-modal"]');
  await page.waitForSelector('[role="dialog"]');
  
  // 检查模态框可访问性
  const results = await new AxeBuilder({ page })
    .include('[role="dialog"]')
    .analyze();
  
  expect(results.violations).toEqual([]);
  
  // 验证焦点管理
  const modalTitle = page.locator('[role="dialog"] h2');
  await expect(modalTitle).toBeFocused();
  
  // 测试 Esc 键关闭
  await page.keyboard.press('Escape');
  await expect(page.locator('[role="dialog"]')).not.toBeVisible();
});
```

## 🎯 最佳实践

### 1. 测试策略

- 在每个页面加载后运行基础扫描
- 针对交互元素进行专项测试
- 测试不同状态下的可访问性
- 结合自动化和手工测试

### 2. 规则配置

```typescript
// 推荐：只检查 WCAG 2.1 A/AA
await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa'])
  .analyze();

// 避免：检查所有规则（可能包含实验性规则）
await new AxeBuilder({ page }).analyze();
```

### 3. 错误处理

```typescript
test('可访问性测试', async ({ page }) => {
  await page.goto('/');
  
  const results = await new AxeBuilder({ page }).analyze();
  
  if (results.violations.length > 0) {
    // 保存详细报告
    await page.screenshot({ path: 'a11y-violations.png' });
    
    // 生成 JSON 报告
    fs.writeFileSync(
      'a11y-violations.json',
      JSON.stringify(results.violations, null, 2)
    );
    
    // 打印摘要
    console.log(`发现 ${results.violations.length} 个违规项`);
    results.violations.forEach((violation) => {
      console.log(`- ${violation.id}: ${violation.description}`);
    });
  }
  
  expect(results.violations).toEqual([]);
});
```

### 4. CI/CD 集成

```yaml
# .github/workflows/a11y-tests.yml
name: Accessibility Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright
        run: npx playwright install --with-deps
      
      - name: Run accessibility tests
        run: npm test
      
      - name: Upload test results
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: a11y-report
          path: |
            playwright-report/
            a11y-violations.json
```

## 🔍 手工测试补充

自动化工具只能检测约 30% 的可访问性问题，还需要手工测试：

### 键盘导航清单

- [ ] 所有交互元素可通过 Tab 键访问
- [ ] Tab 顺序符合逻辑
- [ ] 焦点指示器清晰可见
- [ ] 可使用 Enter/Space 激活按钮
- [ ] 可使用 Esc 关闭模态框
- [ ] 可使用方向键导航菜单

### 屏幕阅读器测试

- [ ] NVDA（Windows）
- [ ] JAWS（Windows）
- [ ] VoiceOver（macOS/iOS）
- [ ] TalkBack（Android）

### 视觉测试

- [ ] 文本缩放至 200%
- [ ] 高对比度模式
- [ ] 深色模式
- [ ] 移动设备视口

## 🚨 常见问题

### 问题1：测试运行缓慢

**解决方案**：
- 使用 `include` 限制扫描范围
- 排除不重要的区域（如广告）
- 并行运行测试

### 问题2：误报过多

**解决方案**：
- 配置规则排除已知误报
- 使用 `withTags` 只检查特定标准
- 手工验证可疑问题

### 问题3：动态内容未检测

**解决方案**：
- 在触发动态内容后再运行扫描
- 使用 `waitForSelector` 等待元素出现
- 针对特定区域进行扫描

## 📚 参考资源

- [WCAG 2.1 官方文档](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe-core 文档](https://github.com/dequelabs/axe-core)
- [Playwright 文档](https://playwright.dev/)
- [WebAIM 资源](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**需要帮助？** 查看 [故障排除](../../SKILL.md#故障排除--troubleshooting) 或提交 Issue
