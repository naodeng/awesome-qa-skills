---
name: skill-prose-trim
description: Use this skill when auditing or trimming process residue from Skill、Prompt、注释或文档；触发词包括过程性文案清理、审查残留、当前状态改写。
---

# 过程性文案清理

## 何时使用

需要清理“本次修改”“审查者认为”“之前版本”、未提交设计编号或其他无法在当前仓库语境中解析的文字时使用。

## 执行流程

1. 明确文件范围、语言配对和是否允许修改。
2. 区分当前事实、契约、历史记录、推理过程和审查对话。
3. 删除纯过程性内容；把有价值的事实改写成当前状态表述。
4. 保留负向保证、测量边界、正式引用、归档记录和 fixture fidelity。

## 核心约束

- 不把假设改写成已实现能力。
- 不修改 sealed archive、记录型 fixture 或生成文件，除非用户明确授权。
- 双语文件必须保持语义同步。

产出前阅读 `prompts/skill-prose-trim.md`。
