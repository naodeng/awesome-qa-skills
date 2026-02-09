---
name: accessibility-testing
version: 2.0.0
last-updated: 2024-02-06
description: 设计可访问性测试方案与用例，覆盖 WCAG 2.1 标准、屏幕阅读器、键盘导航。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 可访问性测试 or accessibility testing.
category: testing-types
level: intermediate
tags: [accessibility, a11y, wcag, inclusive, compliance]
dependencies: []
recommended-with: [functional-testing, manual-testing, automation-testing]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop]
  frameworks: [react, vue, angular, flutter]
  test-frameworks: [axe-core, pa11y, lighthouse, jest-axe]
output-formats: [markdown, excel, csv, json, jira, testrail]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# 可访问性测试（中文版）

**英文版：** 见技能 `accessibility-testing-en`。

提示词见本目录 `prompts/accessibility-testing.md`。

## 何时使用

- 用户提到「可访问性测试」「accessibility testing」「a11y」「WCAG」
- 需要根据 WCAG 标准设计可访问性测试策略、测试用例、测试方案
- **触发示例：**「根据以下需求设计可访问性测试用例」「做一份 WCAG 2.1 合规性测试方案」

## 输出格式选项

本技能**默认输出为 Markdown**（与 Standard-version 模板一致）。若需其他格式，请在需求**末尾**明确说明：

| 格式 | 说明 | 如何请求（示例） |
|------|------|------------------|
| **Markdown** | 默认，便于阅读与版本管理 | 无需额外说明 |
| **Excel** | 制表符分隔，可粘贴到 Excel | 「请以 Excel 可粘贴的制表符分隔表格输出」 |
| **CSV** | 逗号分隔，首行为表头 | 「请以 CSV 格式输出」 |
| **JSON** | 便于程序解析 | 「请以 JSON 形式输出」 |

详细说明与示例见本目录 **[output-formats.md](output-formats.md)**。

## 如何使用本技能中的提示词

1. 打开本目录 `prompts/accessibility-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的功能需求或系统规格。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 参考文件

- **[prompts/accessibility-testing.md](prompts/accessibility-testing.md)** — 可访问性测试 Standard-version 提示词
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON 请求说明

## 代码示例 | Code Examples

本技能提供以下真实代码示例：

1. **[axe-core + Playwright 自动化测试](examples/axe-playwright/)** - 完整的可访问性自动化测试套件
   - 12个测试用例
   - 覆盖 WCAG 2.1 Level A/AA
   - 包含自动化和手工测试指南
   - 详细的违规报告

2. **WCAG 2.1 手工测试清单**（即将推出）
3. **屏幕阅读器测试指南**（即将推出）

查看 [examples/](examples/) 目录获取更多示例。

## 常见误区 | Common Pitfalls

- ❌ **只依赖自动化工具** → ✅ 结合自动化工具（30%覆盖）和手工测试（70%覆盖）
- ❌ **忽略键盘导航** → ✅ 确保所有功能可通过键盘访问
- ❌ **颜色对比度不足** → ✅ 使用工具检查对比度，确保至少 4.5:1（正常文本）
- ❌ **缺少替代文本** → ✅ 为所有图片、图标提供有意义的 alt 文本
- ❌ **表单标签缺失** → ✅ 确保所有表单控件有关联的 label
- ❌ **只在开发完成后测试** → ✅ 在设计和开发阶段就考虑可访问性

## 最佳实践 | Best Practices

1. **WCAG 合规性**
   - 遵循 WCAG 2.1 Level AA 标准（最低要求）
   - 使用自动化工具检测常见问题
   - 进行手工测试验证复杂交互
   - 使用真实的辅助技术测试

2. **测试策略**
   - 在 CI/CD 中集成自动化可访问性测试
   - 定期进行手工测试和用户测试
   - 使用多种工具交叉验证
   - 记录和追踪可访问性问题

3. **关键测试点**
   - 键盘导航（Tab、Enter、Esc、方向键）
   - 屏幕阅读器兼容性（NVDA、JAWS、VoiceOver）
   - 颜色对比度和视觉设计
   - 表单可访问性
   - 语义化 HTML
   - ARIA 属性正确使用

4. **工具选择**
   - axe-core：自动化测试（最全面）
   - Lighthouse：快速审计
   - WAVE：可视化问题
   - 屏幕阅读器：真实用户体验

5. **文档和报告**
   - 清晰记录违规项和严重程度
   - 提供修复建议和代码示例
   - 追踪修复进度
   - 定期生成合规性报告

## 故障排除 | Troubleshooting

### 问题1：axe-core 报告过多误报

**症状**：自动化测试报告大量问题，但实际上是误报

**解决方案**：
1. 配置规则排除已知误报：
   ```typescript
   await new AxeBuilder({ page })
     .disableRules(['color-contrast']) // 排除特定规则
     .analyze();
   ```
2. 使用标签过滤：
   ```typescript
   await new AxeBuilder({ page })
     .withTags(['wcag2a', 'wcag2aa']) // 只检查 WCAG 2.1 A/AA
     .analyze();
   ```
3. 手工验证可疑问题
4. 更新到最新版本的 axe-core

### 问题2：无法检测动态内容的可访问性问题

**症状**：模态框、下拉菜单等动态内容的问题未被检测

**解决方案**：
1. 在触发动态内容后再运行测试：
   ```typescript
   await page.click('[data-testid="open-modal"]');
   await page.waitForSelector('[role="dialog"]');
   const results = await new AxeBuilder({ page }).analyze();
   ```
2. 针对特定区域测试：
   ```typescript
   await new AxeBuilder({ page })
     .include('[role="dialog"]')
     .analyze();
   ```
3. 测试不同状态下的可访问性

### 问题3：键盘导航测试不通过

**症状**：某些元素无法通过键盘访问

**解决方案**：
1. 检查 tabindex 属性：
   ```html
   <!-- ✅ 推荐：使用 tabindex="0" 使元素可聚焦 -->
   <div role="button" tabindex="0">Click me</div>
   
   <!-- ❌ 避免：tabindex > 0 会破坏自然的 Tab 顺序 -->
   <div tabindex="5">Bad practice</div>
   ```
2. 使用语义化 HTML：
   ```html
   <!-- ✅ 推荐：原生按钮自动可聚焦 -->
   <button>Click me</button>
   
   <!-- ❌ 不推荐：需要额外的可访问性属性 -->
   <div onclick="...">Click me</div>
   ```
3. 添加键盘事件处理：
   ```typescript
   element.addEventListener('keydown', (e) => {
     if (e.key === 'Enter' || e.key === ' ') {
       // 处理激活
     }
   });
   ```

### 问题4：颜色对比度不足

**症状**：axe-core 报告颜色对比度问题

**解决方案**：
1. 使用对比度检查工具：
   - Chrome DevTools Lighthouse
   - WebAIM Contrast Checker
   - Colour Contrast Analyser
2. 确保对比度至少：
   - 正常文本：4.5:1
   - 大文本（18pt+）：3:1
   - UI 组件：3:1
3. 调整颜色方案：
   ```css
   /* ❌ 对比度不足 */
   color: #999; /* 灰色文本 */
   background: #fff; /* 白色背景 */
   
   /* ✅ 对比度充足 */
   color: #595959; /* 深灰色文本 */
   background: #fff; /* 白色背景 */
   ```

### 问题5：屏幕阅读器无法正确读取内容

**症状**：使用屏幕阅读器时内容混乱或缺失

**解决方案**：
1. 使用语义化 HTML：
   ```html
   <!-- ✅ 推荐 -->
   <nav>
     <ul>
       <li><a href="/">Home</a></li>
     </ul>
   </nav>
   
   <!-- ❌ 不推荐 -->
   <div class="nav">
     <div class="item">Home</div>
   </div>
   ```
2. 正确使用 ARIA 属性：
   ```html
   <!-- ✅ 推荐：提供有意义的标签 -->
   <button aria-label="关闭对话框">×</button>
   
   <!-- ❌ 不推荐：屏幕阅读器只会读"乘号" -->
   <button>×</button>
   ```
3. 使用 aria-live 通知动态变化：
   ```html
   <div aria-live="polite" aria-atomic="true">
     <!-- 动态内容 -->
   </div>
   ```

### 问题6：表单可访问性问题

**症状**：表单控件缺少标签或错误提示不清晰

**解决方案**：
1. 关联 label 和 input：
   ```html
   <!-- ✅ 推荐：显式关联 -->
   <label for="email">邮箱</label>
   <input id="email" type="email" />
   
   <!-- ✅ 推荐：隐式关联 -->
   <label>
     邮箱
     <input type="email" />
   </label>
   ```
2. 提供清晰的错误提示：
   ```html
   <input
     id="email"
     type="email"
     aria-invalid="true"
     aria-describedby="email-error"
   />
   <span id="email-error" role="alert">
     请输入有效的邮箱地址
   </span>
   ```
3. 使用 fieldset 和 legend 分组：
   ```html
   <fieldset>
     <legend>联系方式</legend>
     <!-- 表单控件 -->
   </fieldset>
   ```

### 问题7：CI 环境中测试失败

**症状**：本地通过但 CI 环境中可访问性测试失败

**解决方案**：
1. 确保 CI 环境安装了浏览器：
   ```yaml
   - name: Install Playwright
     run: npx playwright install --with-deps
   ```
2. 检查环境差异（字体、渲染）
3. 保存失败时的截图和报告：
   ```typescript
   if (violations.length > 0) {
     await page.screenshot({ path: 'a11y-violations.png' });
     fs.writeFileSync('a11y-report.json', JSON.stringify(violations));
   }
   ```
4. 使用 Docker 容器保证环境一致性

### 获取更多帮助

如果问题仍未解决：
1. 查看 [FAQ.md](../../../FAQ.md)
2. 查看示例的 README.md 文件
3. 参考 WCAG 2.1 官方文档
4. 使用 WebAIM 资源
5. 提交新的 Issue 并附上详细信息

**相关技能：** functional-testing、manual-testing、automation-testing、test-case-writing。
