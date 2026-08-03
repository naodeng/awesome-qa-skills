---
name: release-testing-workflow
description: Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include 发布测试工作流程 and release testing workflow.
---

# 发布测试工作流程（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要按发布窗口推进：T-N 规划 → 专项 → RC → Go/No-Go → 发布后观察。
- 需要发布门禁与放行证据包，并向类型 skill 交接专项执行。

## 执行流程

1. 阅读并遵循 `prompts/release-testing-workflow.md`（时间线、门禁、Go/No-Go、交接）。
2. 补充发布日、范围、冻结规则、候选版本、已知缺陷等上下文。
3. 定位 T 窗口后按需读本目录阶段 `prompts/`；专项执行点名对应类型 skill。
4. 信息不全时仍给门禁看板初版，并标假设；**禁止编造测试通过结果**。

## 核心约束

- 管发布时间线与放行决策；专项报告交给 `performance-testing` / `security-testing` 等。
- 门禁可压缩时间，不可删除判据。
- Go/No-Go 必须基于证据；条件放行必须可验证。
- 禁止相对路径链到其他 skill 文件。

## 按需加载

- 产出前必须阅读并遵循 `prompts/release-testing-workflow.md`。
- 步骤对照：读 `reference.md`。
- 阶段/专项深做：再读本目录对应 `prompts/*.md`。
- 模板：`output-templates/`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 含范围/排除项、T 窗口、门禁看板、证据缺口、下一跳 skill
- [ ] 若到决策点：Go / No-Go / 条件放行有依据
- [ ] 未编造通过结果或未提供的缺陷状态
- [ ] 假设与开放问题已标明

## 常见误区

- 不要删门禁只压缩日程。
- 不要在未冻结时宣称 RC 完成。
- 不要在本 skill 内代写完整专项长报告。
- 不要用空泛「继续观察」代替条件放行条款。
