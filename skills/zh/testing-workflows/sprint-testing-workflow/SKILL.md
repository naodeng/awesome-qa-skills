---
name: sprint-testing-workflow
description: Use this skill when you need a sprint-based QA workflow from planning through review and retrospective; triggers include 迭代测试工作流程 and sprint testing workflow.
---

# 迭代测试工作流程（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要按冲刺/迭代节奏推进：规划 → 设置 → 执行 → 回归 → 稳定 → 评审。
- 需要迭代门禁与 DoD，并向类型 skill 交接，而不是只做单次测试任务。

## 执行流程

1. 阅读并遵循 `prompts/sprint-testing-workflow.md`（阶段、门禁、DoD、交接）。
2. 补充迭代目标、故事范围、容量、遗留缺陷等关键上下文。
3. 定位阶段后按 `reference.md` 点名交接类型 skill；禁止相对路径链到其他 skill 内部文件。
4. 信息不全时先给可用迭代测试计划，并标假设与缺口。

## 核心约束

- 管迭代阶段与退出证据；完整产物交给类型 skill。
- 门禁与 DoD 必须可检查。
- 范围变更时重算优先级并写明对门禁的影响。
- 禁止相对路径链到其他 skill 文件。

## 按需加载

- 产出前必须阅读并遵循 `prompts/sprint-testing-workflow.md`。
- 步骤与交接对照：读 `reference.md`。
- 阶段深做：调用对应类型 skill，不要在本 skill 内展开完整产物。
- 模板：`output-templates/`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 含阶段定位、门禁看板、退出标准对照、下一跳 skill
- [ ] 高风险项有明确优先级与 Owner
- [ ] 未编造用户未提供的细节
- [ ] 假设、取舍与遗留已标明

## 常见误区

- 不要写成无门禁的逐日流水账。
- 不要在规划阶段倾倒全量用例正文。
- 不要在开发未收敛时宣称回归已通过。
- 不要用「测了很多」代替退出证据。
