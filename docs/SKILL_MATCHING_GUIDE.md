<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_MATCHING_GUIDE_EN.md">🇬🇧 English</a></div>

# Skill 能力匹配指南

## 目的

逐项匹配决定记录在 `governance/skill-governance-registry.yaml`，Matching Register 是生成视图；修改 registry 后必须重新生成并运行 `--check`。

所有候选能力在创建目录前必须完成能力匹配。结论只能是 `EXISTING`、`ENHANCE`、`MERGE`、`MATCH` 或 `NEW`。

## 六步核对

1. 名称：是否只是同义名称或工具名差异。
2. 目的：是否解决相同质量问题。
3. 输入：是否依赖同类证据、约束和上下文。
4. 输出：是否产生相同决策、建议或工件。
5. 决策逻辑：是否采用相同的判断规则与风险模型。
6. Workflow 角色：是否处在相同组合位置。

## 结论与动作

| 结论 | 动作 |
| --- | --- |
| EXISTING | 记录映射，不创建目录。 |
| MATCH | 记录同义映射，不创建目录。 |
| ENHANCE | 为既有 Skill 建卡，补齐边界、证据、输出或 Eval。 |
| MERGE | 将候选作为既有 Skill 的 mode、规则或子流程。 |
| NEW | 定义独立 Scope/Non-goals 后，创建中英双语独立 Skill。 |

`NEW` 必须证明输入、分析逻辑、输出和决策价值均不能由已有能力合理承担。匹配结论必须写入 Matrix 和 GitHub Project 卡；静态审查不能代替运行效果证明。

## 受限审查状态

`REVIEWED_WITH_LIMITATION` 表示六项证据已定位并完成结构化比较，但仍缺少项目上下文、语义等价、运行结果或 Eval 证据。它不是批准或可执行状态；其中的 `MATCH`、`MERGE`、`ENHANCE`、`NEW` 只能作为 Phase 1 复核前的候选结论，不能仅凭 Registry 创建、修改或删除 Skill。

## Phase 0 典型映射复核

[20 条典型映射复核记录](./governance/PHASE_0_MATCH_MERGE_REVIEW.md)由 Registry 生成，覆盖 13 条候选映射和 7 条 Existing 自映射。Matrix 的 `Related / Workflow` 列会展示目标 Skill 的关系摘要；候选的六项证据仍以 [Matching Register](./SKILL_MATCHING_REGISTER.md) 为准。

复核只固化导航和后续动作：`EXISTING` / `MATCH` 不创建重复目录，`MERGE` 进入 mode、规则或子流程评估，`ENHANCE` 进入既有 Skill 增强复核。所有结论仍是 `REVIEWED_WITH_LIMITATION`，不能替代项目语义复核、运行评测或人工审批。

复现：`python3 scripts/generate_skill_governance_matrix.py --check`，并运行 `python3 scripts/check_docs_bilingual.py --repo-root .`。
