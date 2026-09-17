<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_GOVERNANCE_V1_EN.md">🇬🇧 English</a></div>

# v1.0 Skill 治理基线

## 目的与边界

v1.0 为当前仓库的 162 个逻辑中英文 Skill 对建立可复现的**源代码治理记录**。早期基线曾覆盖 79 个逻辑对；当前树已包含后续 v1.1、v2.0 和 v3-v4 交付，当前数量以生成器实时盘点为准。本文只审查包目录、`SKILL.md`、`agents/openai.yaml` 和 `evals/` 的声明与结构；不运行 Skill 提示词、辅助脚本、模型或真实测试目标。

因此，本基线不提供 Quality Score，也不将静态记录表述为运行效果、测试通过率或能力质量结论。运行行为、语义等价、模型评测与效果均在没有相应执行证据时标为 `UNASSESSED`。

## 字段契约

| 字段 | 含义 | 允许的结论边界 |
| --- | --- | --- |
| Virtual Domain | 使用 [D01–D16 分类源](./virtual-domains.yaml) 为每个逻辑 Skill 指定一个主要 Domain。 | 导航分类，不是安装依赖、执行顺序、语义等价或质量结论。 |
| 状态 | `STRUCTURALLY_RECORDED` 表示双语包、声明元数据与 Eval 文件结构均已被本脚本发现；结构缺口为 `UNASSESSED (structural gap)`。 | 不是功能、质量或执行成功状态。 |
| Scope 边界 | 逐包保留来源描述，并声明静态审查不覆盖的内容。 | 不从描述推断未执行的能力。 |
| 相似/Plus 关系 | 仅记录明确的 Plus、已命名工具族或未评估的语义关系。 | 不把目录命名当作语义等价证明。 |
| Match/Merge 复核 | `match_reviews` 记录典型关系、目标 Skill、证据路径和后续动作。 | 关系复核仍是 `REVIEWED_WITH_LIMITATION`，不授权创建、修改或删除目录。 |
| Eval 结构 | `eval.yaml`、实际 case 数和配置中列出的 case 数。 | 仅为文件结构证据，不代表 Eval 已运行或通过。 |
| Capability Match 证据 | 中英文目录、frontmatter 名称、Agent 元数据和 Eval 结构的可追溯路径。 | 语义及有效性始终保持 `UNASSESSED`，除非另有执行证据。 |

## D01–D16 Virtual Domain

| ID | 中文 | English |
| --- | --- | --- |
| D01 | 需求质量 | Requirement Quality |
| D02 | 工程质量 | Engineering Quality |
| D03 | 测试分析与策略 | Test Analysis & Strategy |
| D04 | 测试设计 | Test Design |
| D05 | 功能与探索式测试 | Functional & Exploratory Testing |
| D06 | API 与集成质量 | API & Integration Quality |
| D07 | UI 与端到端质量 | UI & E2E Quality |
| D08 | 自动化工程 | Automation Engineering |
| D09 | 性能质量 | Performance Quality |
| D10 | 安全质量 | Security Quality |
| D11 | 可靠性与韧性 | Reliability & Resilience |
| D12 | 发布与生产质量 | Release & Production Quality |
| D13 | 可观测性与事故质量 | Observability & Incident Quality |
| D14 | QE 与效能 | Quality Engineering & Productivity |
| D15 | AI 辅助 QA | AI for QA |
| D16 | AI / LLM / Agent 质量 | AI / LLM / Agent Quality |

每个 Skill 只能有一个主要 Domain。混合目录使用 slug 覆盖规则，未映射的新目录必须先补充分类源并通过校验。

## 可复现清单

- [逐项治理清单](../generated/skill-governance-inventory.md)：每个逻辑 Skill 一行，共 162 个逻辑双语对。
- [治理矩阵](../SKILL_MATRIX.md)：显示 D01–D16 标签、优先级和证据边界。
- [典型 Match/Merge 复核](./PHASE_0_MATCH_MERGE_REVIEW.md)：展示 Registry 中 20 条关系及其后续动作。
- [v1.4 Phase 0 收口](./PHASE_0_V1_4_CLOSEOUT.md)：登记 35 张 Project 卡的证据、验收状态和版本边界。
- [分类源](./virtual-domains.yaml)：Domain 定义、目录默认映射和 slug 覆盖规则。
- 生成：`python3 scripts/generate_skill_governance_inventory.py`
- 新鲜度检查：`python3 scripts/generate_skill_governance_inventory.py --check`
- 矩阵生成与检查：`python3 scripts/generate_skill_governance_matrix.py --check`

生成器以当前 `skills/{zh,en}/{testing-workflows,testing-types,skill-engineering}` 为输入，并复用分类源解析目录标题和 slug 覆盖。目录增删、名称变更或 Eval 结构变更后必须重新生成；缺失 Domain 映射或生成物漂移都会由质量门禁拦截。

## Project 卡

| 项目 | 状态 | 验收证据 | 明确不包含 |
| --- | --- | --- | --- |
| v1.0 source-governance closeout | `LOCALLY_VERIFIED` | 当前 162 条逐项记录、D01–D16 分类源、双语入口、Catalog/Graph 链接、可复现生成器、`--check` 和完整本地质量门禁 | Skill/模型/脚本执行、运行质量评分、发布、push |

`LOCALLY_VERIFIED` 仅代表完整质量门禁、生成物新鲜度和 Git 差异检查均有当次证据；它不等同于运行效果或发布状态。
