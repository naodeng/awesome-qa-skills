---
name: test-case-reviewer-plus
description: 基于需求、策略和测试用例文档生成测试用例评审结果。
---

# test-case-reviewer-plus（中文）

## 适用场景

适合在提测前做用例质量把关，明确漏测风险和优先级修复项。

## 技能目标

基于需求、策略和测试用例文档生成测试用例评审结果。

## 输入

- 必填：需求文档 + 测试用例文档
- 可选：需求分析、技术文档、项目计划、测试策略、其他文档

## 输出

- 输出：评审结果（Markdown 默认，可切换 Word/JSON/Excel）

## 前置准备

- 安装 Python 3
- 准备当前版本用例文档
- 建议同时传入策略文档提升评审准确性

## 快速开始

```bash
python3 scripts/run_review.py --requirement examples/requirement-sample.md --testcase examples/testcase-sample.md --analysis examples/analysis-sample.md --tech examples/tech-sample.md --plan examples/plan-sample.md --strategy examples/strategy-sample.md --output-format markdown --output examples/testcase-sample.review.md
```

## 结果判断

- 成功生成评审结果
- 内容包含总体结论、P0/P1问题、缺失场景、补测建议

## 常见问题

- 若结论过于笼统，增加输入文档完整度
- 若缺少优先级分层，确认输入里是否有风险信息

## 目录说明

- `prompts/`：中文提示词
- `scripts/`：执行脚本
- `examples/`：示例输入输出
- `output-templates/`：输出模板（如目录存在）
- `references/`：规范说明（如目录存在）

## 独立使用声明

- 本技能可脱离英文目录单独使用。
- 运行所需文件全部位于当前技能目录内。
- 文档、提示词、示例均为中文可读版本。

## 审计信息

- 最近验证时间：2026-03-23
- 技能文档版本：1.1.0
