---
name: testcase-writer-plus
description: 解析需求文档和需求分析结果，生成高质量测试用例。
---

# testcase-writer-plus（中文）

## 适用场景

适合在需求评审后快速产出首版测试用例，并统一用例字段格式。

## 技能目标

解析需求文档和需求分析结果，生成高质量测试用例。

## 输入

- 必填：需求文档 + 需求分析结果
- 支持：Word/HTML/JSON/Markdown/Excel

## 输出

- 输出：测试用例（Markdown 默认，可切换 Word/JSON/Excel）

## 前置准备

- 安装 Python 3
- 准备需求文档与分析文档
- 输出格式不填时默认 Markdown

## 快速开始

```bash
python3 scripts/run_writer.py --requirement examples/requirement-sample.md --analysis examples/analysis-sample.md --output-format markdown --output examples/requirement-sample.testcases.md
```

## 结果判断

- 成功生成用例文件
- 每条用例包含标题、优先级、类型、前置条件、步骤、测试数据、预期结果

## 常见问题

- 若格式不对，检查 --output-format 参数
- 若用例数量偏少，检查输入文档是否提供了足够规则信息

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
