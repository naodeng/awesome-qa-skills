---
name: test-strategy
description: Use this skill when you need to define a test strategy covering scope, methods, resources, risks, and quality gates; triggers include 测试策略 and test strategy.
---

# 测试策略（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要在真实项目里处理 test strategy 相关任务。
- 需要一份可以直接用于执行、评审或跟进的结果。

## 输出格式选项

默认使用 Markdown。若需要 Excel、CSV、JSON、Word 等支持格式，请在需求末尾补充格式要求，并查看 [output-formats.md](output-formats.md)。

## 如何使用

1. 打开 `prompts/test-strategy.md`，把它作为主提示词使用。
2. 补充真实项目上下文：范围、环境、限制、风险、依赖和期望产出。
3. 如果输入不完整，先给出可用初版，并标出信息缺口和假设。

## 参考文件

- `prompts/test-strategy.md`：本技能的主提示词。
- `output-formats.md`：可选输出格式说明。
- `quick-start.md`：快速上手说明。
- `references/`：按需查看的补充说明。
- `examples/`：示例输入或输出。
- `scripts/`：本技能相关的辅助脚本或转换脚本。

## 常见误区

- 不要在范围和上下文都不清楚时直接使用。
- 不要把所有内容都当成同等重要。
- 不要跳过假设和信息缺口。

## 最佳实践

- 先从提示词正文出发，再补真正影响结果的上下文。
- 结果要按风险聚焦，而且能直接执行。
- 如果信息不全，先给可用初版，并把缺口标出来。
