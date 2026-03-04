---
name: accessibility-testing
description: Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include 可访问性测试 and accessibility testing.
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

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

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

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。
