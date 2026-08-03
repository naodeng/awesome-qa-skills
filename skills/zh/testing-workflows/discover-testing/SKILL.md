---
name: discover-testing
description: Use this skill when you need to route a request to the right testing skill before execution; triggers include 测试技能路由、discover testing and which testing skill.
---

# 测试技能路由（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要在执行前先判断应该用哪个测试 skill。
- 一个请求同时涉及多个测试方向或多个阶段。

## 执行流程

1. 先读用户请求，识别主要测试目标与阶段。
2. 阅读并遵循 `prompts/` 路由规范：先选 1 个主 skill；仅必要时再补 1 个辅助 skill。
3. 输出路由结论后，把请求交给目标 skill；不要在本 skill 内把整件事执行完。

## 核心约束

- 一次只推荐少量 skill，避免菜单式罗列。
- 目标 skill 已经很明显时，直接指出，不要无效绕路。
- 路由结果要可执行：写清推荐 skill 名与理由。

## 按需加载

- 产出前必须阅读并遵循 `prompts/discover-testing.md`（最低覆盖清单、输出结构、质量要求）。
- 需要 Excel/CSV/JSON/Word 等格式时：读 `output-formats.md`，并按用户格式要求输出。
- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。
- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。
- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。
- 需要步骤与提示词映射时：读 `reference.md`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 最低覆盖关注：主要目标、最适合的主 skill、可选辅助 skill、为什么这么选、下一步怎么接着做（细节以主提示词为准）
- [ ] 已覆盖最低清单，或标明为何省略
- [ ] 高风险项有明确优先级
- [ ] 未编造用户未提供的细节
- [ ] 假设与信息缺口已标明

## 常见误区

- 不要一次推荐很多 skill。
- 不要把技能选择写成具体测试执行。
- 不要在信息不足时假装已经选定且可落地。
