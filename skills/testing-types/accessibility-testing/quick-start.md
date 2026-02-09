# 可访问性测试 - 5分钟快速上手

本指南帮助你在 5 分钟内开始使用可访问性测试技能。

## 📋 前置条件

- Node.js >= 16
- 基本的 Web 开发知识
- 了解 WCAG 基础概念（可选）

## 🚀 快速开始

### 步骤 1: 安装依赖（1分钟）

```bash
cd skills/testing-types/accessibility-testing/examples/axe-playwright
npm install
```

### 步骤 2: 运行示例测试（2分钟）

```bash
# 运行所有可访问性测试
npm test

# 运行特定测试
npm test -- login.spec.ts

# 生成 HTML 报告
npm test -- --reporter=html
```

### 步骤 3: 查看测试报告（1分钟）

测试完成后，查看：
- 终端输出：违规项摘要
- `playwright-report/index.html`：详细的 HTML 报告
- `a11y-violations.json`：JSON 格式的违规详情

### 步骤 4: 理解测试结果（1分钟）

测试报告包含：
- **Violations（违规）**：必须修复的问题
- **Impact（影响）**：critical、serious、moderate、minor
- **WCAG 标准**：违反的具体标准（如 WCAG 2.1 Level A）
- **修复建议**：如何修复问题

## 📖 核心概念

### WCAG 2.1 四大原则（POUR）

1. **Perceivable（可感知）**
   - 提供替代文本
   - 确保颜色对比度
   - 支持文本缩放

2. **Operable（可操作）**
   - 键盘可访问
   - 足够的操作时间
   - 避免癫痫触发

3. **Understandable（可理解）**
   - 清晰的文本
   - 可预测的行为
   - 输入帮助

4. **Robust（健壮）**
   - 兼容辅助技术
   - 有效的 HTML
   - 正确的 ARIA

### 合规级别

- **Level A**：最基本的可访问性（必须满足）
- **Level AA**：推荐的可访问性级别（大多数法规要求）
- **Level AAA**：最高级别的可访问性（可选）

## 🔧 常用命令

```bash
# 运行所有测试
npm test

# 运行特定文件
npm test -- login.spec.ts

# 调试模式
npm test -- --debug

# 生成报告
npm test -- --reporter=html

# 只检查特定 WCAG 级别
npm test -- --grep "WCAG 2.1 Level A"
```

## 📝 编写你的第一个测试

创建 `my-test.spec.ts`：

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('首页可访问性测试', async ({ page }) => {
  // 1. 访问页面
  await page.goto('https://your-website.com');
  
  // 2. 运行 axe 扫描
  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa']) // 只检查 WCAG 2.1 A/AA
    .analyze();
  
  // 3. 断言没有违规
  expect(accessibilityScanResults.violations).toEqual([]);
});
```

## 🎯 测试关键区域

### 1. 表单可访问性

```typescript
test('表单可访问性', async ({ page }) => {
  await page.goto('/form');
  
  // 检查表单区域
  const results = await new AxeBuilder({ page })
    .include('form')
    .analyze();
  
  expect(results.violations).toEqual([]);
});
```

### 2. 键盘导航

```typescript
test('键盘导航', async ({ page }) => {
  await page.goto('/');
  
  // 使用 Tab 键导航
  await page.keyboard.press('Tab');
  
  // 检查焦点可见性
  const focusedElement = await page.locator(':focus');
  await expect(focusedElement).toBeVisible();
});
```

### 3. 颜色对比度

```typescript
test('颜色对比度', async ({ page }) => {
  await page.goto('/');
  
  // 只检查颜色对比度
  const results = await new AxeBuilder({ page })
    .withTags(['color-contrast'])
    .analyze();
  
  expect(results.violations).toEqual([]);
});
```

## 🛠️ 配置选项

### 排除特定规则

```typescript
await new AxeBuilder({ page })
  .disableRules(['color-contrast']) // 排除颜色对比度检查
  .analyze();
```

### 只检查特定区域

```typescript
await new AxeBuilder({ page })
  .include('#main-content') // 只检查主内容区
  .exclude('#ads') // 排除广告区
  .analyze();
```

### 自定义规则配置

```typescript
await new AxeBuilder({ page })
  .configure({
    rules: [
      { id: 'color-contrast', enabled: false },
      { id: 'image-alt', enabled: true }
    ]
  })
  .analyze();
```

## 📊 理解测试报告

### 违规项结构

```json
{
  "id": "color-contrast",
  "impact": "serious",
  "description": "确保前景色和背景色的对比度满足 WCAG 2 AA 标准",
  "help": "元素必须有足够的颜色对比度",
  "helpUrl": "https://dequeuniversity.com/rules/axe/4.4/color-contrast",
  "nodes": [
    {
      "html": "<a href=\"/about\">关于我们</a>",
      "target": ["a[href=\"/about\"]"],
      "failureSummary": "对比度为 2.5:1，需要至少 4.5:1"
    }
  ]
}
```

### 影响级别

- **critical**：严重影响可访问性，必须立即修复
- **serious**：严重问题，应优先修复
- **moderate**：中等问题，应该修复
- **minor**：轻微问题，建议修复

## 🔍 手工测试清单

自动化工具只能检测约 30% 的可访问性问题，还需要手工测试：

### 键盘导航
- [ ] 所有交互元素可通过 Tab 键访问
- [ ] Tab 顺序符合逻辑
- [ ] 焦点指示器清晰可见
- [ ] 可使用 Enter/Space 激活按钮
- [ ] 可使用 Esc 关闭模态框

### 屏幕阅读器
- [ ] 使用 NVDA/JAWS（Windows）测试
- [ ] 使用 VoiceOver（macOS/iOS）测试
- [ ] 使用 TalkBack（Android）测试
- [ ] 所有内容可被正确读取
- [ ] 交互元素有清晰的标签

### 视觉
- [ ] 文本可缩放至 200% 而不丢失内容
- [ ] 颜色不是传达信息的唯一方式
- [ ] 动画可以暂停或禁用
- [ ] 没有闪烁内容（避免癫痫触发）

## 🚨 常见问题快速修复

### 问题：图片缺少 alt 文本

```html
<!-- ❌ 错误 -->
<img src="logo.png">

<!-- ✅ 正确 -->
<img src="logo.png" alt="公司 Logo">

<!-- ✅ 装饰性图片 -->
<img src="decoration.png" alt="">
```

### 问题：按钮缺少可访问名称

```html
<!-- ❌ 错误 -->
<button><i class="icon-close"></i></button>

<!-- ✅ 正确 -->
<button aria-label="关闭">
  <i class="icon-close"></i>
</button>
```

### 问题：表单控件缺少标签

```html
<!-- ❌ 错误 -->
<input type="email" placeholder="邮箱">

<!-- ✅ 正确 -->
<label for="email">邮箱</label>
<input id="email" type="email">
```

### 问题：颜色对比度不足

```css
/* ❌ 错误：对比度 2.5:1 */
color: #999;
background: #fff;

/* ✅ 正确：对比度 7:1 */
color: #595959;
background: #fff;
```

## 📚 下一步

1. **深入学习**
   - 阅读 [SKILL.md](SKILL.md) 了解完整功能
   - 查看 [examples/axe-playwright/](examples/axe-playwright/) 的完整示例
   - 学习 WCAG 2.1 标准

2. **集成到项目**
   - 在 CI/CD 中运行可访问性测试
   - 设置测试覆盖率目标
   - 建立可访问性审查流程

3. **扩展测试**
   - 添加更多测试场景
   - 测试不同设备和浏览器
   - 进行真实用户测试

## 🔗 有用资源

- [WCAG 2.1 官方文档](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe-core 文档](https://github.com/dequelabs/axe-core)
- [WebAIM 资源](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)
- [MDN 可访问性指南](https://developer.mozilla.org/zh-CN/docs/Web/Accessibility)

## 💡 提示

- 从一开始就考虑可访问性，而不是事后补救
- 使用语义化 HTML，减少对 ARIA 的依赖
- 定期进行可访问性审计
- 邀请残障用户参与测试
- 将可访问性纳入团队文化

---

**需要帮助？** 查看 [故障排除](SKILL.md#故障排除--troubleshooting) 或 [FAQ](../../../FAQ.md)
