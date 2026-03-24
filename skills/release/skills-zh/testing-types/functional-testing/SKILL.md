---
name: functional-testing
description: Use this skill when you need to design functional test plans or cases for business flows, UI, data, and integrations; triggers include 功能测试 and functional testing.
---

# 功能测试（中文版）

**英文版：** 见技能 `functional-testing-en`。

提示词见本目录 `prompts/functional-testing.md`。

## 何时使用

- 用户提到「功能测试」「functional testing」「功能测试用例」「功能测试方案」
- 需要根据需求或规格设计功能测试策略、测试用例、测试方案
- **触发示例：**「根据以下需求设计功能测试用例」「做一份功能测试方案」

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

- **[prompts/functional-testing.md](prompts/functional-testing.md)** — 功能测试 Standard-version 提示词
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON 请求说明

## 代码示例 | Code Examples

本技能提供以下真实代码示例：

1. **[Playwright 登录测试](examples/playwright-login/)** - 完整的登录功能测试套件
   - 14个测试用例
   - 覆盖功能、可访问性、安全性
   - 包含最佳实践和故障排除

2. **Cypress 表单测试**（即将推出）
3. **Selenium 导航测试**（即将推出）

查看 [examples/](examples/) 目录获取更多示例。

## 常见误区 | Common Pitfalls

- ❌ **跳过需求分析直接写用例** → ✅ 先使用 requirements-analysis skill 分析需求，识别测试点
- ❌ **只测试正常场景** → ✅ 同时覆盖异常场景、边界值和错误处理
- ❌ **用例描述不清晰** → ✅ 使用明确的步骤和预期结果，确保可重现
- ❌ **忽略可访问性测试** → ✅ 包含键盘导航、屏幕阅读器等可访问性验证
- ❌ **测试数据硬编码** → ✅ 使用测试数据管理策略，便于维护

## 最佳实践 | Best Practices

1. **测试设计**
   - 使用等价类划分和边界值分析
   - 遵循 AAA 模式（Arrange-Act-Assert）
   - 保持测试独立性，避免依赖

2. **元素定位**
   - 优先使用 data-testid 属性
   - 避免使用易变的 CSS 类名
   - 使用语义化的定位器

3. **断言策略**
   - 使用多个具体的断言而非单一模糊断言
   - 验证关键业务逻辑
   - 包含用户体验验证

4. **维护性**
   - 使用 Page Object Model 设计模式
   - 提取可复用的测试工具函数
   - 保持测试代码整洁

5. **执行效率**
   - 并行运行独立测试
   - 使用合适的等待策略
   - 避免不必要的延迟

## 故障排除 | Troubleshooting

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。

## 目标受众

- 在真实项目中执行该测试域工作的 QA 与开发人员
- 需要结构化、可复用测试交付物的测试负责人
- 需要快速生成可落地测试产出的 AI 使用者

## 不适用场景

- 无测试范围上下文的纯线上应急处置
- 需要法律/合规最终裁定但缺少专家复核的决策
- 缺少最小输入（范围、环境、期望行为）的请求

## 关键成功因素

- 先明确范围、环境与验收标准，再生成测试内容
- 生成结果必须结合真实系统约束做二次校验
- 保持产物可追踪（需求 -> 测试点 -> 缺陷 -> 决策）

## 输出模板与解析脚本

- 模板目录：`output-templates/`
  - `template-word.md`（Word 友好结构）
  - `template-excel.tsv`（Excel 可直接粘贴）
  - `template-xmind.md`（XMind 结构化大纲）
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- 解析脚本目录：`scripts/`
  - 解析通用：`parse_output_formats.py`
  - 解析按格式：`parse_word.py`、`parse_excel.py`、`parse_xmind.py`、`parse_json.py`、`parse_csv.py`、`parse_markdown.py`
  - 转换通用：`convert_output_formats.py`
  - 转换按格式：`convert_to_word.py`、`convert_to_excel.py`、`convert_to_xmind.py`、`convert_to_json.py`、`convert_to_csv.py`、`convert_to_markdown.py`
  - 批量转换：`batch_convert_templates.py`（批量输出到 `artifacts/`）

示例：
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
