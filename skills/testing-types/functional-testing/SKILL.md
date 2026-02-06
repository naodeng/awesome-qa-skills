---
name: functional-testing
description: 设计功能测试方案与用例，覆盖业务功能、UI、数据、集成。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 功能测试 or functional testing.
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

## 如何使用本技能中的提示词

1. 打开本目录 `prompts/functional-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的功能需求或系统规格。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 参考文件

- **[prompts/functional-testing.md](prompts/functional-testing.md)** — 功能测试 Standard-version 提示词
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON 请求说明

**相关技能：** api-testing、test-case-writing、test-strategy。
