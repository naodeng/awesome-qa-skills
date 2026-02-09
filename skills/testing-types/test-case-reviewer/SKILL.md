---
name: test-case-reviewer
version: 2.0.0
last-updated: 2024-02-06
description: 对测试用例进行多维度评审，输出评审报告、缺失场景与改进建议。评审覆盖完整性、清晰度、可维护性等。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 测试用例评审 or test case review.
category: testing-types
level: advanced
tags: [review, quality, coverage, improvement, best-practices]
dependencies: [test-case-writing]
recommended-with: [test-strategy, requirements-analysis, functional-testing]
context-aware: true
context-patterns:
  review-types: [completeness, clarity, maintainability, efficiency]
  methodologies: [checklist, peer-review, walkthrough]
output-formats: [markdown, excel, csv, json]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# 测试用例评审（中文版）

**英文版：** 见技能 `test-case-reviewer-en`。

提示词见本目录 `prompts/test-case-reviewer.md`。

## 何时使用

- 用户提到「测试用例评审」「test case review」「用例评审」
- 需要对已有测试用例进行质量评审、缺失场景挖掘与改进建议
- **触发示例：**「请评审以下测试用例」「找出用例中的遗漏与风险」

## 输出格式选项

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明。

## 参考文件

- **[prompts/test-case-reviewer.md](prompts/test-case-reviewer.md)** — 测试用例评审提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **[用例评审标准](examples/test-case-review-standards/)** - 评审检查清单和标准

## 常见误区 | Common Pitfalls

- ❌ **只看表面问题** → ✅ 深入分析覆盖率和质量
- ❌ **批评而不建议** → ✅ 提供具体改进建议
- ❌ **忽略可维护性** → ✅ 评估长期维护成本
- ❌ **缺少优先级** → ✅ 标记问题严重程度

## 最佳实践 | Best Practices

### 1. 评审维度

**完整性（Completeness）**:
- 需求覆盖率
- 场景覆盖率
- 边界值覆盖
- 异常场景覆盖

**清晰度（Clarity）**:
- 步骤明确
- 数据具体
- 结果可验证
- 无歧义

**可维护性（Maintainability）**:
- 用例独立
- 数据分离
- 模块化设计
- 易于更新

**效率（Efficiency）**:
- 执行时间合理
- 无冗余步骤
- 自动化潜力
- ROI 评估

### 2. 评审检查清单

```markdown
## 用例评审检查清单

### 基本信息
- [ ] 用例 ID 唯一
- [ ] 标题清晰
- [ ] 优先级标记
- [ ] 类型标记

### 前置条件
- [ ] 前置条件完整
- [ ] 前置条件可实现
- [ ] 依赖关系明确

### 测试步骤
- [ ] 步骤详细具体
- [ ] 步骤可重复
- [ ] 步骤编号清晰
- [ ] 无遗漏步骤

### 测试数据
- [ ] 数据具体明确
- [ ] 数据可获取
- [ ] 覆盖边界值
- [ ] 包含异常数据

### 预期结果
- [ ] 结果明确
- [ ] 结果可验证
- [ ] 结果完整
- [ ] 无模糊描述

### 覆盖率
- [ ] 正常场景
- [ ] 异常场景
- [ ] 边界条件
- [ ] 权限验证
```

### 3. 评审报告模板

```markdown
## 测试用例评审报告

**评审日期**: 2024-02-06
**评审人**: 张三
**用例数量**: 50
**评审范围**: 登录模块

### 评审总结
- 总体质量：良好
- 主要问题：边界值覆盖不足
- 改进建议：增加异常场景

### 问题统计
| 严重程度 | 数量 | 占比 |
|---------|------|------|
| Critical | 2 | 4% |
| High | 5 | 10% |
| Medium | 10 | 20% |
| Low | 8 | 16% |

### 详细问题

#### Critical 问题
1. **TC-001**: 缺少 SQL 注入测试
   - **影响**: 安全风险
   - **建议**: 添加特殊字符测试

#### High 问题
2. **TC-005**: 边界值测试不完整
   - **影响**: 可能遗漏缺陷
   - **建议**: 补充边界值用例

### 缺失场景
- 并发登录测试
- Session 超时测试
- 密码复杂度验证

### 改进建议
1. 增加边界值测试
2. 补充异常场景
3. 优化用例描述
4. 添加自动化标记
```

## 故障排除 | Troubleshooting

### 问题1：不知道如何评审

**解决方案**：
使用评审检查清单，逐项检查。

### 问题2：评审效率低

**解决方案**：
1. 使用评审工具
2. 批量评审相似用例
3. 重点评审高优先级用例

**相关技能：** test-case-writing、test-strategy、requirements-analysis。
