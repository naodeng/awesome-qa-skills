---
name: requirements-analysis-plus
description: 解析 Word/HTML/JSON/Markdown/Excel 需求文档，并输出结构化需求分析结论。
---

# requirements-analysis-plus（中文）

## 适用场景

适合在测试设计前做需求梳理，先把关键规则、风险点和待确认问题找全。

## 技能目标

解析 Word/HTML/JSON/Markdown/Excel 需求文档，并输出结构化需求分析结论。

## 输入

- 必填：需求文档（Word/HTML/JSON/Markdown/Excel）
- 可选：指定输入格式

## 输出

- 输出：需求分析结论（默认 Markdown）

## 前置准备

- 安装 Python 3
- 准备一份需求文档
- 建议先使用 examples 目录里的样例跑通一次

## 快速开始

```bash
python3 scripts/run_analysis.py --input examples/requirements-sample.md --output examples/requirements-sample.analysis.md
```

## 结果判断

- 结果文件成功生成
- 内容包含：需求摘要、功能点、非功能点、歧义点、测试重点

## 常见问题

- 若解析失败，先确认文件格式与扩展名一致
- 若内容过少，先检查输入文档是否为空或结构过于简单

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
