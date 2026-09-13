<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_LIFECYCLE_EN.md">🇬🇧 English</a></div>

# Skill 生命周期

`Idea → Candidate → Capability Match → Design → Implementation → Eval → Review → Stable`

候选在匹配后进入 Existing、Enhance、Merge、Match 或 New 分支。Stable Skill 可因证据或使用反馈回到 Enhance/Merge；Deprecated 必须提供替代路径，Archived 不再维护但保留历史可追溯性。

| 状态 | 进入条件 | 退出条件 |
| --- | --- | --- |
| Candidate | 质量缺口或候选名称已登记 | 完成六步 Capability Match |
| Existing / Match | 现有能力已覆盖，证据已记录 | 新证据触发 Enhance 或 Merge Review |
| Enhance / Merge | 已确认既有能力需要调整或收敛 | 改动、Eval 与重新评分完成 |
| Planned-P0/P1/P2 | Match 结论为 New，按优先级排期 | 进入 Design |
| Experimental | Scope 或证据尚不足以 Stable | 达到评分与 Eval 门槛，或 Redesign |
| Deprecated / Archived | 替代路径和迁移影响已记录 | Archived 后仅保留可追溯历史 |

每次状态转换都应记录：输入证据、决定、责任范围、受影响双语目录、Eval 状态、Matrix 和文档同步项。任何状态均不得暗示人工审批、发布或风险接受已自动完成。
