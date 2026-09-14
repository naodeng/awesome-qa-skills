<div align="right"><strong>🇨🇳 中文</strong> | <a href="./PHASE_1_REQUIREMENTS_QUALITY_EN.md">🇬🇧 English</a></div>

# v1.1 Phase 1：需求质量 Skill 开发

## 当前状态

`IN_PROGRESS_WITH_LIMITATIONS`（2026-09-14）。远端 `main` 已快进合入本地 `develop`；v1.1 P0 前五个需求质量 Skill 已建立中英文独立包，并完成包级静态结构检查和 Eval dry-run。真实模型 Eval 尚未执行：当前环境没有可用的 Claude 登录状态，因此 `eval_execution` 保持 `NOT_RUN`。

本阶段只覆盖需求质量分析能力的第一批五个 Skill，不代表 v1.1 发布、运行效果、业务需求闭环或 Go/No-Go 结论。

## 范围

| 顺序 | Skill | 主要职责 | Project 卡片 |
| --- | --- | --- | --- |
| 1 | `requirement-quality-review` | 对完整性、清晰度、可验证性、可行性、范围和证据质量做总览评审，并路由专项分析 | `PVTI_lAHOAHP1as4BjBhVzg6Sbo4` · `v1.1 P0｜候选 Skill｜requirement-quality-review` |
| 2 | `requirement-ambiguity-analysis` | 识别角色、对象、条件、数量、时间、状态和验收语句的歧义 | `PVTI_lAHOAHP1as4BjBhVzg6Sbp0` · `v1.1 P0｜候选 Skill｜requirement-ambiguity-analysis` |
| 3 | `requirement-consistency-analysis` | 比较跨来源术语、标识、格式、状态、规则、行为和版本范围的一致性 | `PVTI_lAHOAHP1as4BjBhVzg6Sbsc` · `v1.1 P0｜候选 Skill｜requirement-consistency-analysis` |
| 4 | `requirement-conflict-detection` | 识别同一适用范围内互斥的规则和约束，保留双方并交给 Human 决策 | `PVTI_lAHOAHP1as4BjBhVzg6Sbuk` · `v1.1 P0｜候选 Skill｜requirement-conflict-detection` |
| 5 | `requirement-traceability-analysis` | 建立需求、验收、设计、代码、测试、缺陷和证据的双向追踪 | `PVTI_lAHOAHP1as4BjBhVzg6Sbxw` · `v1.1 P0｜候选 Skill｜requirement-traceability-analysis` |

五张卡片均为 `In Progress`；本阶段不移动其他 Project 卡片，不创建 Issue，不 push，不发布版本。

## 统一边界

- 每个 Skill 都有独立的中英文 `SKILL.md`、主 Prompt、`agents/openai.yaml`、Eval 配置和三类边界用例。
- 输入审计统一保留 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`，但每个 Skill 的发现 ID 和专业输出不同。
- 静态存在、名称匹配、报告文字和 dry-run 只证明结构或声明；不能升级为模型行为、测试执行、缺陷关闭、审批或发布证据。
- 五个新包不修改 `requirements-analysis` 或 `requirements-analysis-plus` 的既有行为，也不通过相对路径依赖其他 Skill 的内部文件。
- `requirement-quality-review` 负责总览和路由，不产生数字质量分或 Go/No-Go；四个专项 Skill 只报告证据边界内的发现，不代替 Human 决策。

## 交付与验收

1. 两种语言各有 84 个逻辑 Skill 包，合计 168 个物理目录；五个新增包目录名、frontmatter `name` 和 Agent metadata key 一致。
2. 五个包的 Eval YAML 可由 `skill-up validate` 加载，三类 case 可 dry-run；结构门禁、元数据、独立性和完整性检查通过。
3. registry 为每个新 Skill 记录 `Planned-P0`、`P0`、`Engineering QA`、`requirements`、角色、证据路径和 `NOT_SCORED`/`NOT_RUN` 状态，并为五个候选记录六字段匹配证据。
4. 中英文 README、Catalog、Graph、治理矩阵、匹配登记表和库存均由当前仓库内容复现且无漂移。
5. 真实模型 Eval、外部测试目标、业务语义等价、质量评分和版本发布另行安排；未有证据时保持 `NOT_RUN`、`UNASSESSED` 或 `IN_PROGRESS_WITH_LIMITATIONS`。

## 复现

```bash
python3 scripts/validate_agents_metadata.py --report /tmp/v11-final-metadata.md
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-final-independence.md
python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/v11-final-integrity.md
bash scripts/validate_skill_evals.sh
bash scripts/check_skills_quality.sh
```

生成视图：

```bash
python3 scripts/generate_skill_inventory.py
python3 scripts/generate_skill_governance_inventory.py
python3 scripts/generate_skill_governance_matrix.py
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
```
