<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_LIFECYCLE_EN.md">🇬🇧 English</a></div>

# Skill 生命周期

`Idea → Candidate → Capability Match → Design → Implementation → Eval → Review → Stable`

Phase 0 的逐项治理事实源是 `governance/skill-governance-registry.yaml`（JSON 兼容 YAML）；`SKILL_MATRIX.md` 与 `SKILL_MATCHING_REGISTER.md` 均由生成器产出，不应手工编辑。`Candidate` 只表示等待匹配证据，不表示能力缺失或质量失败。

候选在匹配后进入 Existing、Enhance、Merge、Match 或 New 分支。Stable Skill 可因证据或使用反馈回到 Enhance/Merge；Deprecated 必须提供替代路径，Archived 不再维护但保留历史可追溯性。

| 状态 | 进入条件 | 退出条件 |
| --- | --- | --- |
| Candidate | 质量缺口或候选名称已登记 | 完成六步 Capability Match |
| Existing / Match | 现有能力已覆盖，证据已记录 | 新证据触发 Enhance 或 Merge Review |
| Enhance / Merge | 已确认既有能力需要调整或收敛 | 改动、Eval 与重新评分完成 |
| Planned-P0/P1/P2 | Match 结论为 New，按优先级排期 | 进入 Design |
| Experimental | Scope 或证据尚不足以 Stable | 达到评分与 Eval 门槛，或 Redesign |
| Deprecated / Archived | 替代路径和迁移影响已记录 | Archived 后仅保留可追溯历史 |

### `REVIEWED_WITH_LIMITATION`

这是 Registry 中的受限审查状态：六项证据已经逐项定位并完成结构化比较，但项目业务上下文、语义等价、运行结果或 Eval 证据仍不完整。该状态不是人工批准、发布、风险接受或可直接执行的信号；其中的 `MATCH`、`MERGE`、`ENHANCE` 或 `NEW` 仍是候选结论，必须在 Phase 1 结合需求和真实资产复核后，才能转入实施或继续保留限制。

每次状态转换都应记录：输入证据、决定、责任范围、受影响双语目录、Eval 状态、Matrix 和文档同步项。任何状态均不得暗示人工审批、发布或风险接受已自动完成。
