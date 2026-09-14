<div align="right"><strong>🇨🇳 中文</strong> | <a href="./PHASE_1_REQUIREMENTS_QUALITY_EN.md">🇬🇧 English</a></div>

# v1.1 Phase 1：需求质量 Skill 开发

## 当前状态

`ACCEPTED_WITH_DEFERRED_EVAL`（2026-09-14）。远端 `main` 已快进合入本地 `develop`；v1.1 P0 前五个需求质量 Skill、后续十个质量 Skill 卡片以及本批五个测试设计发现 Skill 已完成中英文包开发、增强模式实现、包级静态结构检查、触发样本本地 runner dry-run 和范围边界语义评测配置。用户明确同意暂时跳过真实模型 Eval，因此 registry 的 `eval_execution` 继续保持 `NOT_RUN`。

本状态表示 v1.1 **实现范围已统一验收**，不表示真实模型运行效果、业务语义等价、质量评分、Go/No-Go 或版本发布完成。真实模型 Eval 作为后续统一处理项保留。

## 统一验收结论

| 验收项 | 当前证据 | 状态 |
| --- | --- | --- |
| 双语包、元数据、独立性、完整性、文档和治理视图 | `bash scripts/check_skills_quality.sh`：192 个 Skill，`skill-up validate` 192/192，20 条本地规则，全部通过 | `verified` |
| 合同测试和全仓单测 | `python3 -m unittest discover -s scripts/tests -v`：40/40 通过 | `verified` |
| 本地触发数据 dry-run | 18 个目标 × 中英文两种语言 = 36 个数据集，36/36 退出 0 | `verified` |
| 真实模型 Eval | 用户明确延期；registry 保持 `eval_execution: NOT_RUN` | `deferred` |
| 外部目标、业务语义等价、质量评分、版本发布 | 不在本次实现范围内 | `UNASSESSED` |

结论：本次验收只关闭 v1.1 实现范围；20 张对应 Project 卡片移至 `Done`，其他卡片保持原状态。

## 范围

| 顺序 | Skill | 主要职责 | Project 卡片 |
| --- | --- | --- | --- |
| 1 | `requirement-quality-review` | 对完整性、清晰度、可验证性、可行性、范围和证据质量做总览评审，并路由专项分析 | `PVTI_lAHOAHP1as4BjBhVzg6Sbo4` · `v1.1 P0｜候选 Skill｜requirement-quality-review` |
| 2 | `requirement-ambiguity-analysis` | 识别角色、对象、条件、数量、时间、状态和验收语句的歧义 | `PVTI_lAHOAHP1as4BjBhVzg6Sbp0` · `v1.1 P0｜候选 Skill｜requirement-ambiguity-analysis` |
| 3 | `requirement-consistency-analysis` | 比较跨来源术语、标识、格式、状态、规则、行为和版本范围的一致性 | `PVTI_lAHOAHP1as4BjBhVzg6Sbsc` · `v1.1 P0｜候选 Skill｜requirement-consistency-analysis` |
| 4 | `requirement-conflict-detection` | 识别同一适用范围内互斥的规则和约束，保留双方并交给 Human 决策 | `PVTI_lAHOAHP1as4BjBhVzg6Sbuk` · `v1.1 P0｜候选 Skill｜requirement-conflict-detection` |
| 5 | `requirement-traceability-analysis` | 建立需求、验收、设计、代码、测试、缺陷和证据的双向追踪 | `PVTI_lAHOAHP1as4BjBhVzg6Sbxw` · `v1.1 P0｜候选 Skill｜requirement-traceability-analysis` |

五张卡片在实现期间为 `In Progress`；统一验收后移至 `Done`。不移动其他 Project 卡片，不创建 Issue，不 push，不发布版本。

## 后续十个 P0 卡片

| 顺序 | 卡片名 | 交付形态 | Project 卡片 |
| --- | --- | --- | --- |
| 1 | `business-rule-extraction` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb0o` |
| 2 | `business-rule-consistency-review` | 增强 `requirement-consistency-analysis` 的 business-rule mode | `PVTI_lAHOAHP1as4BjBhVzg6Sb2Q` |
| 3 | `technical-design-quality-review` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb3A` |
| 4 | `architecture-testability-review` | 增强 `testability-analysis` 的 architecture mode | `PVTI_lAHOAHP1as4BjBhVzg6Sb4I` |
| 5 | `api-design-quality-review` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb5U` |
| 6 | `database-design-quality-review` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb6o` |
| 7 | `observability-design-review` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb7Y` |
| 8 | `error-handling-design-review` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb8Y` |
| 9 | `test-scope-analysis` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb_M` |
| 10 | `test-coverage-analysis` | 增强 `requirement-traceability-analysis` 的 coverage_analysis mode | `PVTI_lAHOAHP1as4BjBhVzg6ScAY` |

上述十张卡片在实现期间均为 `In Progress`；统一验收后移至 `Done`。增强卡片不创建重复目录，不移动其他 Project 卡片，不创建 Issue，不 push，不发布版本。

## 当前五个测试设计发现卡片

| 顺序 | 卡片名 | 交付形态 | Project 卡片 |
| --- | --- | --- | --- |
| 1 | `test-gap-analysis` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScBw` |
| 2 | `risk-based-testing` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScEE` |
| 3 | `edge-case-discovery` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScGA` |
| 4 | `negative-scenario-discovery` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScIs` |
| 5 | `test-data-requirement-analysis` | 新增双语物理 Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScKk` |

上述五张卡片在实现期间均为 `In Progress`；统一验收后移至 `Done`。本批不移动其他 Project 卡片，不创建 Issue，不 push，不发布版本。

## 统一边界

- 每个 Skill 都有独立的中英文 `SKILL.md`、主 Prompt、`agents/openai.yaml`、Eval 配置、三类边界用例、`trigger-prompts.csv` 和 `local-rules.json`；触发数据覆盖显式、隐式、上下文和反向控制。
- 输入审计统一保留 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`，但每个 Skill 的发现 ID 和专业输出不同。
- 静态存在、名称匹配、报告文字和 dry-run 只证明结构或声明；不能升级为模型行为、测试执行、缺陷关闭、审批或发布证据。
- 五个新包不修改 `requirements-analysis` 或 `requirements-analysis-plus` 的既有行为，也不通过相对路径依赖其他 Skill 的内部文件。
- 后续十个卡片交付七个新增物理 Skill 和三个现有 Skill 的增强模式；候选卡片名与物理目录名分离登记，不通过别名目录制造重复能力。
- `requirement-quality-review` 负责总览和路由，不产生数字质量分或 Go/No-Go；四个专项 Skill 只报告证据边界内的发现，不代替 Human 决策。

## 交付与验收

1. 两种语言各有 96 个逻辑 Skill 包，合计 192 个物理目录；七个上一批新增包和五个本批新增包的目录名、frontmatter `name` 和 Agent metadata key 一致，三个增强候选不产生别名目录。
2. 七个上一批新增包、五个本批新增包和三个增强目标的 Eval YAML 可由 `skill-up validate` 加载，新增/增强 case 可 dry-run；本地触发 runner 可读取 36 个中英文目标数据集（18 个目标 × 2 种语言）；结构门禁、元数据、独立性和完整性检查通过。
3. registry 为十二个新 Skill 记录 `Planned-P0`、`P0`、`Engineering QA`、阶段、角色、证据路径和 `NOT_SCORED`/`NOT_RUN` 状态，并为三个增强候选记录六字段匹配证据。
4. 中英文 README、Catalog、Graph、治理矩阵、匹配登记表和库存均由当前仓库内容复现且无漂移。
5. 真实模型 Eval、外部测试目标、业务语义等价、质量评分和版本发布另行安排；本次明确不将真实模型 Eval 作为实现范围验收阻塞项，未有证据时保持 `NOT_RUN` 或 `UNASSESSED`。

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

本地触发样本预览（十八个目标 Skill，各语言分别执行；无 `--run` 时只产生 dry-run 结构预览）：

```bash
python3 scripts/run_skill_trace_eval.py \
  --prompts skills/zh/testing-types/requirement-quality-review/evals/trigger-prompts.csv \
  --config skills/zh/testing-types/requirement-quality-review/evals/local-rules.json \
  --project-root /tmp/v11-requirement-quality-projects \
  --output-dir /tmp/v11-requirement-quality-reports
```
