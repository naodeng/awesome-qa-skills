<div align="right"><strong>🇨🇳 中文</strong> | <a href="./ENHANCEMENT_SPRINT_EN.md">🇬🇧 English</a></div>

# Enhancement Sprint 节奏

每 2–3 个 New Sprint 后安排 1 个 Enhancement / Merge / Eval Sprint，避免只增加目录而不维护既有能力。v1.4 的治理收口是第一批可复用的 Enhancement Sprint 规则。

## 节奏与输入

| 节奏 | 目标 | 必查证据 |
| --- | --- | --- |
| New Sprint × 2–3 | 交付经 Match 证明为 NEW 的独立能力 | Scope、Non-goals、双语包、Eval、Workflow、安装 |
| Enhancement Sprint × 1 | 收敛边界、输出和维护成本 | Prompt、旧/新 Eval、Quality Score、Matrix、README |
| Release Review | 汇总变更和剩余风险 | 质量门禁、运行证据、人工审批、迁移/回滚 |

## Enhancement 清单

1. 精简 Prompt，保留输入审计、证据边界和 Human Decision。
2. 收敛 Scope，补足 Non-goals 和信息不足路径。
3. 增强 Eval：成功、不完整信息、范围/风险边界；变更后重新评估。
4. 检查中英文、触发词、Workflow 引用、Matrix、README 和安装入口。
5. 复核相似 Skill 的 Match/Merge，必要时建立 Deprecation 提案。
6. 记录变更前后证据和未评估项；没有运行结果写 `NOT_RUN`，没有评分写 `NOT_SCORED`。

## Exit criteria

Enhancement Sprint 只有在文档、结构、Eval 工件和质量门禁完成后才能收口；`Done` 表示该 Sprint 交付物完成，不等于运行效果、发布批准或风险接受。

- [候选 Skill 15 步模板](./CANDIDATE_SKILL_15_STEP_TEMPLATE.md)
- [Quality Score 与最低 Eval 契约](./QUALITY_SCORE_EVAL_CONTRACT.md)
- [v1.4 收口](./PHASE_0_V1_4_CLOSEOUT.md)
