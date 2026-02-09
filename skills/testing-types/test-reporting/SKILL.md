---
name: test-reporting
version: 2.0.0
last-updated: 2024-02-06
description: 生成专业的测试报告，包含执行摘要、度量指标、缺陷分析、风险评估。支持日报、周报、发布报告等。默认输出 Markdown，可请求 Excel/CSV/JSON/PDF。Use for 测试报告 or test reporting.
category: testing-types
level: intermediate
tags: [reporting, metrics, dashboard, summary, analysis]
dependencies: []
recommended-with: [test-strategy, bug-reporting, test-case-writing]
context-aware: true
context-patterns:
  report-types: [daily, weekly, sprint, release, executive]
  audiences: [team, management, stakeholders]
  formats: [summary, detailed, dashboard]
output-formats: [markdown, excel, csv, json, pdf, html]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
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

## 参考文件

- **[prompts/test-reporting.md](prompts/test-reporting.md)** — 测试报告提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **[测试报告模板](examples/test-report-templates/)** - 各类测试报告模板

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
