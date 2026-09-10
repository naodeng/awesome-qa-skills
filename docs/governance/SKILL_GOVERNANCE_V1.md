<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_GOVERNANCE_V1_EN.md">🇬🇧 English</a></div>

# v1.0 Skill 治理基线

## 目的与边界

v1.0 为当前仓库的 79 个中英文 Skill 对建立可复现的**源代码治理记录**。它只审查包目录、`SKILL.md`、`agents/openai.yaml` 和 `evals/` 的声明与结构；不运行 Skill 提示词、辅助脚本、模型或真实测试目标。

因此，本基线不提供 Quality Score，也不将静态记录表述为运行效果、测试通过率或能力质量结论。运行行为、语义等价、模型评测与效果均在没有相应执行证据时标为 `UNASSESSED`。

## 字段契约

| 字段 | 含义 | 允许的结论边界 |
| --- | --- | --- |
| Virtual Domain | 来自当前目录和全量索引的逻辑归类。 | 导航分类，不是安装依赖或运行顺序。 |
| 状态 | `STRUCTURALLY_RECORDED` 表示双语包、声明元数据与 Eval 文件结构均已被本脚本发现；结构缺口为 `UNASSESSED (structural gap)`。 | 不是功能、质量或执行成功状态。 |
| Scope 边界 | 逐包保留来源描述，并声明静态审查不覆盖的内容。 | 不从描述推断未执行的能力。 |
| 相似/Plus 关系 | 仅记录明确的 Plus、已命名工具族或未评估的语义关系。 | 不把目录命名当作语义等价证明。 |
| Eval 结构 | `eval.yaml`、实际 case 数和配置中列出的 case 数。 | 仅为文件结构证据，不代表 Eval 已运行或通过。 |
| Capability Match 证据 | 中英文目录、frontmatter 名称、Agent 元数据和 Eval 结构的可追溯路径。 | 语义及有效性始终保持 `UNASSESSED`，除非另有执行证据。 |

## 可复现清单

- [逐项治理清单](../generated/skill-governance-inventory.md)：每个逻辑 Skill 一行，共 79 个双语对。
- 生成：`python3 scripts/generate_skill_governance_inventory.py`
- 新鲜度检查：`python3 scripts/generate_skill_governance_inventory.py --check`

生成器以当前 `skills/{zh,en}/{testing-workflows,testing-types,skill-engineering}` 为输入，并用 `docs/catalog/skills-index.md` 的领域标题映射测试类型的 Virtual Domain。目录增删、名称变更或 Eval 结构变更后必须重新生成；`check_skills_quality.sh` 会校验生成物没有漂移。

## Project 卡

| 项目 | 状态 | 验收证据 | 明确不包含 |
| --- | --- | --- | --- |
| v1.0 source-governance closeout | `LOCALLY_VERIFIED` | 79 条逐项记录、双语入口、Catalog/Graph 链接、可复现生成器、`--check` 和完整本地质量门禁 | Skill/模型/脚本执行、运行质量评分、发布、push |

`LOCALLY_VERIFIED` 仅代表完整质量门禁、生成物新鲜度和 Git 差异检查均有当次证据；它不等同于运行效果或发布状态。
