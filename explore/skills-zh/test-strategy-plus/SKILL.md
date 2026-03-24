---
name: test-strategy-plus
description: 基于需求、分析、技术文档、计划文档等输入生成测试策略。
---

# test-strategy-plus（中文）

## 适用场景

适合在版本开始或里程碑前形成可落地的测试策略和质量门禁。

## 技能目标

基于需求、分析、技术文档、计划文档等输入生成测试策略。

## 输入

- 必填：需求文档
- 可选：需求分析、技术文档、项目计划、其他补充文档

## 输出

- 输出：测试策略（Markdown 默认，可切换 Word/JSON/Excel）

## 前置准备

- 安装 Python 3
- 至少准备需求文档
- 建议补充技术与计划文档提升策略完整度

## 快速开始

```bash
python3 scripts/run_strategy.py --requirement examples/requirement-sample.md --analysis examples/analysis-sample.md --tech examples/tech-sample.md --plan examples/plan-sample.md --output-format markdown --output examples/requirement-sample.strategy.md
```

## 结果判断

- 成功生成策略文件
- 内容包含范围、方法、准入准出、风险和里程碑

## 常见问题

- 若策略过泛，补充更具体的技术和计划文档
- 若输出格式不符，确认 --output-format 参数

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
