---
name: test-case-reviewer
description: 对测试用例进行多维度评审，输出评审报告、缺失场景与改进建议。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 测试用例评审 or test case review.
---

# 测试用例评审（中文版）

**英文版：** 见技能 `test-case-reviewer-en`。

提示词见本目录 `prompts/test-case-reviewer.md`。

## 何时使用

- 用户提到「测试用例评审」「test case review」「用例评审」
- 需要对已有测试用例进行质量评审、缺失场景挖掘与改进建议
- **触发示例：**「请评审以下测试用例」「找出用例中的遗漏与风险」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/test-case-reviewer.md`，将虚线以下内容复制到 AI 对话。
2. 附加待评审的测试用例。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 参考文件

- **prompts/test-case-reviewer.md** — 测试用例评审 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
