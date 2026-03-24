---
name: test-reporting
description: Use this skill when you need to generate test reports with summary, metrics, defect analysis, and risk assessment; triggers include 测试报告 and test reporting.
---

# 测试报告（中文版）

**英文版：** 见技能 `test-reporting-en`。

提示词见本目录 `prompts/test-reporting.md`。

## 何时使用

- 用户提到「测试报告」「test reporting」「测试总结」
- 需要生成测试报告或测试总结
- **触发示例：**「生成测试报告」「编写 Sprint 测试总结」

## 输出格式选项

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 参考文件

- **[prompts/test-reporting.md](prompts/test-reporting.md)** — 测试报告提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **测试报告模板（计划中）** - 各类测试报告模板

## 常见误区 | Common Pitfalls

- ❌ **只有数据没有分析** → ✅ 提供洞察和建议
- ❌ **报告过于冗长** → ✅ 突出重点，分层展示
- ❌ **缺少可视化** → ✅ 使用图表展示趋势
- ❌ **没有行动项** → ✅ 明确后续行动

## 最佳实践 | Best Practices

### 1. 报告结构

```markdown
# 测试报告

## 1. 执行摘要
- 测试概况
- 主要发现
- 质量评估
- 建议

## 2. 测试执行
- 执行统计
- 覆盖率
- 通过率

## 3. 缺陷分析
- 缺陷统计
- 严重程度分布
- 趋势分析

## 4. 风险与问题
- 当前风险
- 阻塞问题
- 缓解措施

## 5. 后续计划
- 待完成工作
- 改进建议
- 行动项
```

### 2. 关键指标

**执行指标**:
- 用例总数
- 执行数量
- 通过率
- 失败率

**质量指标**:
- 缺陷密度
- 缺陷逃逸率
- 修复时间
- 重开率

**效率指标**:
- 自动化率
- 执行时间
- 生产力

## 故障排除 | Troubleshooting

### 问题1：报告太长没人看

**解决方案**：
使用金字塔结构：
1. 执行摘要（1页）
2. 关键指标（1页）
3. 详细数据（附录）

### 问题2：数据不准确

**解决方案**：
1. 使用测试管理工具
2. 自动化数据收集
3. 定期校验数据

**相关技能：** test-strategy、bug-reporting、test-case-writing。

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
