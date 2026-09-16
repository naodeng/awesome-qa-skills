<div align="right"><a href="./RELEASE_DOD_V1_0_EN.md">English</a></div>

# v1.0 Release DoD（治理收口）

本清单验收仓库治理交付，不等同于已发布包或发布批准。

| 门禁 | 状态 | 证据 / 边界 |
| --- | --- | --- |
| 契约与卡片证据 | `VERIFIED` | 10 张 v1.0 收口契约与生成视图 |
| 仓库质量门禁 | `VERIFIED` | `bash scripts/check_skills_quality.sh` |
| 双语/链接/freshness 检查 | `VERIFIED` | Matrix、Inventory 与双语文档检查 |
| 物理 Skill 包变更 | `N/A` | v1.0 治理收口不创建 Skill 目录 |
| 运行时与外部目标执行 | `NOT_RUN` | 未执行真实应用、API、浏览器或生产目标 |
| 模型 Eval 与 Quality Score | `NOT_RUN` / `NOT_SCORED` | 静态结构不证明模型效果或质量分数 |
| 人工发布批准、风险接受、推送与发布 | `N/A` / `NOT_RUN` | 需要明确人工决策和外部交付动作 |

`v1.0` 范围包含 10 条契约记录；每张 Project 卡可因仓库交付物验收而标记 Done，但发布批准仍为 `NOT_RUN`。

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
| `v1.0｜里程碑｜v1.0 Governance 发布准备` | 发布准备 | `VERIFIED_STATIC` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `v1.0｜治理｜典型 Match Merge 映射复核` | 映射 | `VERIFIED_STATIC` | [docs/governance/skill-governance-registry.yaml](skill-governance-registry.yaml)<br>[docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `Release DoD｜v1.0` | Release DoD | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |

## 复现

```bash
python3 scripts/generate_v14_closeout.py --verify-project
python3 scripts/generate_v14_closeout.py --check
bash scripts/check_skills_quality.sh
```

实时 Project 校验覆盖完整 v1.4 卡片集；本 DoD 视图只展示契约中声明的对应版本范围。
