---
name: ai-assisted-testing
version: 2.0.0
last-updated: 2024-02-06
description: 利用 AI 辅助测试活动，包括测试数据生成、缺陷根因分析、测试优先级排序、智能测试推荐。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for AI 辅助测试 or AI assisted testing.
category: testing-types
level: advanced
tags: [ai, ml, automation, intelligence, optimization]
dependencies: []
recommended-with: [test-case-writing, bug-reporting, test-strategy]
context-aware: true
context-patterns:
  ai-capabilities: [generation, analysis, prediction, optimization]
  use-cases: [test-data, root-cause, prioritization, recommendation]
  tools: [gpt, copilot, ml-models]
output-formats: [markdown, excel, csv, json]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# AI 辅助测试（中文版）

**英文版：** 见技能 `ai-assisted-testing-en`。

提示词见本目录 `prompts/ai-assisted-testing.md`。

## 何时使用

- 用户提到「AI 辅助测试」「AI assisted testing」「智能测试」
- 需要利用 AI 提升测试效率和质量
- **触发示例：**「用 AI 生成测试数据」「AI 分析缺陷根因」

## 输出格式选项

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明。

## 参考文件

- **[prompts/ai-assisted-testing.md](prompts/ai-assisted-testing.md)** — AI 辅助测试提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **[AI 测试工具集](examples/ai-testing-tools/)** - AI 辅助测试工具和脚本

## 常见误区 | Common Pitfalls

- ❌ **完全依赖 AI** → ✅ AI 辅助，人工决策
- ❌ **不验证 AI 输出** → ✅ 验证和审查 AI 结果
- ❌ **忽略数据质量** → ✅ 确保训练数据质量
- ❌ **缺少反馈循环** → ✅ 持续优化 AI 模型

## 最佳实践 | Best Practices

### 1. AI 辅助测试场景

**测试数据生成**:
- 边界值生成
- 异常数据生成
- 大规模数据生成
- 个性化数据生成

**缺陷分析**:
- 根因分析
- 相似缺陷识别
- 缺陷预测
- 影响分析

**测试优化**:
- 用例优先级排序
- 测试套件优化
- 回归测试选择
- 资源分配优化

**智能推荐**:
- 测试用例推荐
- 测试工具推荐
- 测试策略推荐
- 改进建议

### 2. AI 工具选择

| 工具类型 | 用途 | 示例工具 |
|---------|------|---------|
| 代码生成 | 生成测试代码 | GitHub Copilot, ChatGPT |
| 数据生成 | 生成测试数据 | Faker, GPT |
| 缺陷分析 | 分析缺陷模式 | ML 模型 |
| 测试优化 | 优化测试策略 | AI 算法 |

### 3. AI 辅助工作流

```markdown
## AI 辅助测试流程

1. **需求分析**
   - AI 提取测试点
   - 人工审查确认

2. **用例设计**
   - AI 生成用例草稿
   - 人工优化完善

3. **数据准备**
   - AI 生成测试数据
   - 人工验证数据

4. **执行测试**
   - 自动化执行
   - AI 分析结果

5. **缺陷分析**
   - AI 分析根因
   - 人工确认修复

6. **持续改进**
   - 收集反馈
   - 优化 AI 模型
```

## 故障排除 | Troubleshooting

### 问题1：AI 生成的内容不准确

**解决方案**：
1. 提供更详细的上下文
2. 使用示例引导 AI
3. 迭代优化提示词
4. 人工审查和修正

### 问题2：AI 工具成本高

**解决方案**：
1. 优先使用开源工具
2. 只在关键场景使用 AI
3. 批量处理降低成本
4. 评估 ROI

**相关技能：** test-case-writing、bug-reporting、test-strategy。
