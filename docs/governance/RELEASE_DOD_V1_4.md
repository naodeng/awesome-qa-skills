<div align="right"><a href="./RELEASE_DOD_V1_4_EN.md">English</a></div>

# v1.4 Release DoD（治理收口）

本清单验收仓库治理交付，不等同于已发布包或发布批准。

| 门禁 | 状态 | 证据 / 边界 |
| --- | --- | --- |
| 契约与卡片证据 | `VERIFIED` | 35 张 v1.4 收口契约与生成视图 |
| 仓库质量门禁 | `VERIFIED` | `bash scripts/check_skills_quality.sh` |
| 双语/链接/freshness 检查 | `VERIFIED` | Matrix、Inventory 与双语文档检查 |
| 物理 Skill 包变更 | `N/A` | v1.4 治理收口不创建 Skill 目录 |
| 运行时与外部目标执行 | `NOT_RUN` | 未执行真实应用、API、浏览器或生产目标 |
| 模型 Eval 与 Quality Score | `NOT_RUN` / `NOT_SCORED` | 静态结构不证明模型效果或质量分数 |
| 人工发布批准、风险接受、推送与发布 | `N/A` / `NOT_RUN` | 需要明确人工决策和外部交付动作 |

`v1.4` 范围包含 35 条契约记录；每张 Project 卡可因仓库交付物验收而标记 Done，但发布批准仍为 `NOT_RUN`。

## 卡片证据

| 卡片 | 类型 | 验收 | 证据 |
| --- | --- | --- | --- |
| `v1.0｜治理｜16 个虚拟 Domain 分类` | 虚拟 Domain | `VERIFIED_STATIC` | [docs/governance/virtual-domains.yaml](virtual-domains.yaml)<br>[scripts/virtual_domains.py](../../scripts/virtual_domains.py)<br>[scripts/generate_skill_governance_inventory.py](../../scripts/generate_skill_governance_inventory.py)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `v1.0｜治理｜Deprecation 与替代路径规则` | 治理 | `VERIFIED_STATIC` | [docs/SKILL_DEPRECATION_GUIDE.md](../SKILL_DEPRECATION_GUIDE.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/governance/DEPRECATION_DECISION_CONTRACT.md](DEPRECATION_DECISION_CONTRACT.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `v1.0｜治理｜中英文一致性质量契约` | 治理 | `VERIFIED_STATIC` | [docs/governance/DOCUMENTATION_POLICY.md](DOCUMENTATION_POLICY.md)<br>[docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md](BILINGUAL_CONSISTENCY_CONTRACT.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py)<br>[README.md](../../README.md)<br>[README_EN.md](../../README_EN.md) |
| `v1.0｜治理｜Skill Quality Score 与最低 Eval 标准` | 治理 | `VERIFIED_STATIC` | [docs/SKILL_QUALITY_GATE.md](../SKILL_QUALITY_GATE.md)<br>[docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md](QUALITY_SCORE_EVAL_CONTRACT.md)<br>[scripts/validate_skill_eval_rules.py](../../scripts/validate_skill_eval_rules.py)<br>[scripts/validate_skill_evals.sh](../../scripts/validate_skill_evals.sh) |
| `v1.0｜文档｜README 与双语入口治理` | 文档 | `VERIFIED_STATIC` | [README.md](../../README.md)<br>[README_EN.md](../../README_EN.md)<br>[docs/catalog/skills-index.md](../catalog/skills-index.md)<br>[docs/catalog/skills-index_EN.md](../catalog/skills-index_EN.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py) |
| `v1.0｜文档｜Skill Map Graph Catalog 治理` | 文档 | `VERIFIED_STATIC` | [docs/catalog/skills-graph.md](../catalog/skills-graph.md)<br>[docs/catalog/skills-graph_EN.md](../catalog/skills-graph_EN.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md)<br>[docs/SKILL_MATRIX_EN.md](../SKILL_MATRIX_EN.md) |
| `v1.0｜文档｜Workflow Eval 安装文档同步清单` | 文档 | `VERIFIED_STATIC` | [docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md](WORKFLOW_EVAL_INSTALL_SYNC.md)<br>[scripts/INSTALL_SKILLS.md](../../scripts/INSTALL_SKILLS.md)<br>[scripts/install-skills-mac.sh](../../scripts/install-skills-mac.sh)<br>[scripts/install-skills-windows.ps1](../../scripts/install-skills-windows.ps1) |
| `v1.0｜复盘｜Phase 0 Governance Review` | 复盘 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_V1_4_CLOSEOUT.md](PHASE_0_V1_4_CLOSEOUT.md)<br>[docs/governance/SKILL_GOVERNANCE_ROADMAP.md](SKILL_GOVERNANCE_ROADMAP.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `v1.0｜里程碑｜v1.0 Governance 发布准备` | 发布准备 | `VERIFIED_STATIC` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `v1.0｜治理｜典型 Match Merge 映射复核` | 映射 | `VERIFIED_STATIC` | [docs/governance/skill-governance-registry.yaml](skill-governance-registry.yaml)<br>[docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Enhancement Sprint 节奏` | 治理 | `VERIFIED_STATIC` | [docs/governance/ENHANCEMENT_SPRINT.md](ENHANCEMENT_SPRINT.md)<br>[docs/governance/SKILL_GOVERNANCE_ROADMAP.md](SKILL_GOVERNANCE_ROADMAP.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/SKILL_QUALITY_GATE.md](../SKILL_QUALITY_GATE.md) |
| `治理｜候选 Skill 15 步执行模板` | 治理 | `VERIFIED_STATIC` | [docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE.md](CANDIDATE_SKILL_15_STEP_TEMPLATE.md)<br>[docs/SKILL_MATCHING_GUIDE.md](../SKILL_MATCHING_GUIDE.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/SKILL_DESIGN_GUIDE.md](../SKILL_DESIGN_GUIDE.md) |
| `里程碑｜v1.1-v1.4 Shift Left` | 里程碑 | `VERIFIED_STATIC` | [docs/governance/SHIFT_LEFT_MILESTONE.md](SHIFT_LEFT_MILESTONE.md)<br>[docs/catalog/skills-graph.md](../catalog/skills-graph.md)<br>[docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md](QA_SKILLS_EVOLUTION_ROADMAP.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match Enhance｜requirement-change-impact-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Merge｜test-impact-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Merge Enhance｜code-change-risk-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match｜workload-modeling` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match｜capacity-planning` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜performance-bottleneck-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜performance-result-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜performance-regression-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜flaky-test-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜production-verification` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Merge｜regression-scope-selection` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match｜ai-test-case-review` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match Enhance｜ai-log-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match Enhance｜ai-root-cause-analysis` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match｜quality-risk-identification` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match Enhance｜ai-test-data-generation` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match Enhance｜llm-output-quality-testing` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Match｜llm-evaluation` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜prompt-testing` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `治理｜Existing｜agent-tool-testing` | 映射 | `VERIFIED_STATIC` | [docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `Release DoD｜v1.0` | Release DoD | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `Release DoD｜v1.4` | Release DoD | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_4.md](RELEASE_DOD_V1_4.md)<br>[docs/governance/PHASE_0_V1_4_CLOSEOUT.md](PHASE_0_V1_4_CLOSEOUT.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |

## 复现

```bash
python3 scripts/generate_v14_closeout.py --verify-project
python3 scripts/generate_v14_closeout.py --check
bash scripts/check_skills_quality.sh
```

实时 Project 校验覆盖完整 v1.4 卡片集；本 DoD 视图只展示契约中声明的对应版本范围。
