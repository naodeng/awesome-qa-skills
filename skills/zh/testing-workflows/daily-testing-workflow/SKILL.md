---
name: daily-testing-workflow
description: Use this skill when you need a day-by-day QA routine including planning, execution, bug reporting, and end-of-day wrap-up; triggers include 日常测试工作流程 and daily testing workflow.
---

# 日常测试工作流程（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要按 daily testing workflow 的节奏推进，而不是只做单个测试任务。
- 需要按步骤使用对应提示词完成一个测试阶段。

## 输出格式选项

默认使用 Markdown，除非需求明确要求其他格式。

## 如何使用

1. 先看 [reference.md](reference.md)，找到当前步骤对应的提示词。
2. 打开 `prompts/` 下对应文件，只补充真正重要的上下文：范围、环境、风险、限制和期望产出。
3. 按步骤推进；遇到阻塞、风险变化或范围变化时，及时调整优先级。

## 工作流步骤

- `accessibility-testing.md`
- `ai-assisted-testing.md`
- `api-testing.md`
- `automation-testing.md`
- `bug-reporting.md`
- `functional-testing.md`
- `manual-testing.md`
- `requirements-analysis.md`
- `test-case-writing.md`
- `test-reporting.md`
- `test-strategy.md`

## 参考文件

- `prompts/`：本技能使用的提示词文件目录。
- `reference.md`：步骤与提示词的对应关系。
- `scripts/`：本技能相关的辅助脚本或转换脚本。

## 常见误区

- 不要在没确认当前步骤前就直接开始执行。
- 不要试图用一个超长提示词跑完整个工作流。
- 不要忽略阻塞项和重新排优先级。

## 最佳实践

- 先从提示词正文出发，再补真正影响结果的上下文。
- 结果要按风险聚焦，而且能直接执行。
- 如果信息不全，先给可用初版，并把缺口标出来。
