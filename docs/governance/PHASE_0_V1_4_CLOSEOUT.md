<div align="right"><a href="./PHASE_0_V1_4_CLOSEOUT_EN.md">English</a></div>

# v1.4 Phase 0 治理收口

本文由 v1.4 收口契约生成。Project 卡片可以在仓库交付物验收后标记 Done；这不代表 v1.4 版本本身已获发布批准。

**Theme:** `Requirement / Strategy Existing Skill Cleanup`
**Project:** `#4` — Awesome QA Skills — Governance & Roadmap

契约覆盖 35 张 P0 卡片：2 张原已 Done，33 张完成本批转移；2026-09-16 复核结果为 v1.4：Done 35、In Progress 0、Todo 0。
仓库/静态证据：`VERIFIED`；运行时：`NOT_RUN`；模型 Eval：`NOT_RUN`；发布批准：`NOT_RUN`。
Static repository and documentation checks are verified. Runtime behavior and real-target execution are NOT_RUN; model evaluation and Quality Score remain NOT_SCORED; semantic equivalence, business acceptance, risk acceptance, release approval, and external publication remain UNASSESSED or NOT_RUN.

| Project item ID | Project 卡片 | 类型 | 前置 → 目标 | 验收 | 证据 |
| --- | --- | --- | --- | --- | --- |
| `PVTI_lAHOAHP1as4BjBhVzg6SrHw` | `v1.0｜治理｜16 个虚拟 Domain 分类` | 虚拟 Domain | `Done` → `Done` | `VERIFIED_STATIC` | [docs/governance/virtual-domains.yaml](virtual-domains.yaml)<br>[scripts/virtual_domains.py](../../scripts/virtual_domains.py)<br>[scripts/generate_skill_governance_inventory.py](../../scripts/generate_skill_governance_inventory.py)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrMU` | `v1.0｜治理｜Deprecation 与替代路径规则` | 治理 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/SKILL_DEPRECATION_GUIDE.md](../SKILL_DEPRECATION_GUIDE.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/governance/DEPRECATION_DECISION_CONTRACT.md](DEPRECATION_DECISION_CONTRACT.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrNg` | `v1.0｜治理｜中英文一致性质量契约` | 治理 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/DOCUMENTATION_POLICY.md](DOCUMENTATION_POLICY.md)<br>[docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md](BILINGUAL_CONSISTENCY_CONTRACT.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py)<br>[README.md](../../README.md)<br>[README_EN.md](../../README_EN.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrPk` | `v1.0｜治理｜Skill Quality Score 与最低 Eval 标准` | 治理 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/SKILL_QUALITY_GATE.md](../SKILL_QUALITY_GATE.md)<br>[docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md](QUALITY_SCORE_EVAL_CONTRACT.md)<br>[scripts/validate_skill_eval_rules.py](../../scripts/validate_skill_eval_rules.py)<br>[scripts/validate_skill_evals.sh](../../scripts/validate_skill_evals.sh) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrYc` | `v1.0｜文档｜README 与双语入口治理` | 文档 | `In Progress` → `Done` | `VERIFIED_STATIC` | [README.md](../../README.md)<br>[README_EN.md](../../README_EN.md)<br>[docs/catalog/skills-index.md](../catalog/skills-index.md)<br>[docs/catalog/skills-index_EN.md](../catalog/skills-index_EN.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrZ4` | `v1.0｜文档｜Skill Map Graph Catalog 治理` | 文档 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/catalog/skills-graph.md](../catalog/skills-graph.md)<br>[docs/catalog/skills-graph_EN.md](../catalog/skills-graph_EN.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md)<br>[docs/SKILL_MATRIX_EN.md](../SKILL_MATRIX_EN.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6Srck` | `v1.0｜文档｜Workflow Eval 安装文档同步清单` | 文档 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md](WORKFLOW_EVAL_INSTALL_SYNC.md)<br>[scripts/INSTALL_SKILLS.md](../../scripts/INSTALL_SKILLS.md)<br>[scripts/install-skills-mac.sh](../../scripts/install-skills-mac.sh)<br>[scripts/install-skills-windows.ps1](../../scripts/install-skills-windows.ps1) |
| `PVTI_lAHOAHP1as4BjBhVzg6Srds` | `v1.0｜复盘｜Phase 0 Governance Review` | 复盘 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_V1_4_CLOSEOUT.md](PHASE_0_V1_4_CLOSEOUT.md)<br>[docs/governance/SKILL_GOVERNANCE_ROADMAP.md](SKILL_GOVERNANCE_ROADMAP.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `PVTI_lAHOAHP1as4BjBhVzg6SrfA` | `v1.0｜里程碑｜v1.0 Governance 发布准备` | 发布准备 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `PVTI_lAHOAHP1as4BjBhVzg6S3dk` | `v1.0｜治理｜典型 Match Merge 映射复核` | 映射 | `Done` → `Done` | `VERIFIED_STATIC` | [docs/governance/skill-governance-registry.yaml](skill-governance-registry.yaml)<br>[docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6S30Y` | `治理｜Enhancement Sprint 节奏` | 治理 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/ENHANCEMENT_SPRINT.md](ENHANCEMENT_SPRINT.md)<br>[docs/governance/SKILL_GOVERNANCE_ROADMAP.md](SKILL_GOVERNANCE_ROADMAP.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/SKILL_QUALITY_GATE.md](../SKILL_QUALITY_GATE.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6S32E` | `治理｜候选 Skill 15 步执行模板` | 治理 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE.md](CANDIDATE_SKILL_15_STEP_TEMPLATE.md)<br>[docs/SKILL_MATCHING_GUIDE.md](../SKILL_MATCHING_GUIDE.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/SKILL_DESIGN_GUIDE.md](../SKILL_DESIGN_GUIDE.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6S38Q` | `里程碑｜v1.1-v1.4 Shift Left` | 里程碑 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/SHIFT_LEFT_MILESTONE.md](SHIFT_LEFT_MILESTONE.md)<br>[docs/catalog/skills-graph.md](../catalog/skills-graph.md)<br>[docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md](QA_SKILLS_EVOLUTION_ROADMAP.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TITI` | `治理｜Match Enhance｜requirement-change-impact-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIVU` | `治理｜Merge｜test-impact-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIWg` | `治理｜Merge Enhance｜code-change-risk-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIYs` | `治理｜Match｜workload-modeling` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIaM` | `治理｜Match｜capacity-planning` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIcE` | `治理｜Existing｜performance-bottleneck-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIeE` | `治理｜Existing｜performance-result-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIf8` | `治理｜Existing｜performance-regression-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIiA` | `治理｜Existing｜flaky-test-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIjI` | `治理｜Existing｜production-verification` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIlI` | `治理｜Merge｜regression-scope-selection` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIno` | `治理｜Match｜ai-test-case-review` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIpg` | `治理｜Match Enhance｜ai-log-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIrY` | `治理｜Match Enhance｜ai-root-cause-analysis` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIs8` | `治理｜Match｜quality-risk-identification` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIvo` | `治理｜Match Enhance｜ai-test-data-generation` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIw8` | `治理｜Match Enhance｜llm-output-quality-testing` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TIyo` | `治理｜Match｜llm-evaluation` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TI0E` | `治理｜Existing｜prompt-testing` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TI2M` | `治理｜Existing｜agent-tool-testing` | 映射 | `In Progress` → `Done` | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `PVTI_lAHOAHP1as4BjBhVzg6TaoM` | `Release DoD｜v1.0` | Release DoD | `In Progress` → `Done` | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `PVTI_lAHOAHP1as4BjBhVzg6TarQ` | `Release DoD｜v1.4` | Release DoD | `In Progress` → `Done` | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_4.md](RELEASE_DOD_V1_4.md)<br>[docs/governance/PHASE_0_V1_4_CLOSEOUT.md](PHASE_0_V1_4_CLOSEOUT.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |

## 版本规划

| 优先级 | 版本 | 范围 |
| --- | --- | --- |
| `P1` | `v1.5` | Test Engineering and existing Skill enhancement |
| `P2` | `v1.6` | Performance, AI Native, and quality-engineering follow-up |
| `Backlog` | `v1.7` | Deferred governance and composition work |
| `Backlog` | `v1.8` | Deferred ecosystem and release improvements |

## 证据边界

- 没有九维评分证据前，Quality Score 保持 `NOT_SCORED`。
- 未执行真实目标、模型或外部环境时，Eval/运行状态保持 `NOT_RUN`。
- 语义等价、业务验收、风险接受和外部索引/发布状态保持 `UNASSESSED`。
- 本次 v1.4 收口不创建、删除、重命名物理 Skill 目录，也不把目录当作别名。

## 复现

```bash
python3 scripts/generate_v14_closeout.py --verify-project
python3 scripts/generate_v14_closeout.py --check
python3 scripts/generate_skill_governance_matrix.py --check
python3 scripts/check_docs_bilingual.py --repo-root .
```

`--check` 只离线校验仓库中的契约和生成视图；`--verify-project` 会按 ID、标题、状态和内容类型复核实时 Project 条目。
