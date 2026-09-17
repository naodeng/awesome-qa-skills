<div align="right"><a href="./RELEASE_DOD_V1_0.md">中文</a></div>

# v1.0 Release DoD (governance closeout)

This checklist evaluates repository governance delivery, not a published package or release approval.

| Gate | State | Evidence / boundary |
| --- | --- | --- |
| Contract and card evidence | `VERIFIED` | 10-card v1.0 closeout contract and generated view |
| Repository quality gate | `VERIFIED` | `bash scripts/check_skills_quality.sh` |
| Bilingual/link/freshness checks | `VERIFIED` | Matrix, inventory, and bilingual documentation checks |
| Physical Skill package changes | `N/A` | v1.0 governance closeout creates no package directories |
| Runtime and external target execution | `NOT_RUN` | No real application, API, browser, or production target was executed |
| Model-backed Eval and Quality Score | `NOT_RUN` / `NOT_SCORED` | Static structure does not prove model effectiveness or quality score |
| Human release approval, risk acceptance, push, and publication | `N/A` / `NOT_RUN` | Requires an explicit human decision and external delivery action |

The `v1.0` scope includes 10 contract records; each Project card may be marked Done for its verified repository deliverable, while release approval remains `NOT_RUN`.

## Card evidence

| Card | Kind | Acceptance | Evidence |
| --- | --- | --- | --- |
| `v1.0｜治理｜16 个虚拟 Domain 分类` | Virtual Domain | `VERIFIED_STATIC` | [docs/governance/virtual-domains.yaml](virtual-domains.yaml)<br>[scripts/virtual_domains.py](../../scripts/virtual_domains.py)<br>[scripts/generate_skill_governance_inventory.py](../../scripts/generate_skill_governance_inventory.py)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `v1.0｜治理｜Deprecation 与替代路径规则` | Governance | `VERIFIED_STATIC` | [docs/SKILL_DEPRECATION_GUIDE.md](../SKILL_DEPRECATION_GUIDE.md)<br>[docs/SKILL_LIFECYCLE.md](../SKILL_LIFECYCLE.md)<br>[docs/governance/DEPRECATION_DECISION_CONTRACT.md](DEPRECATION_DECISION_CONTRACT.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `v1.0｜治理｜中英文一致性质量契约` | Governance | `VERIFIED_STATIC` | [docs/governance/DOCUMENTATION_POLICY.md](DOCUMENTATION_POLICY.md)<br>[docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md](BILINGUAL_CONSISTENCY_CONTRACT.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py)<br>[README.md](../../README.md)<br>[README_EN.md](../../README_EN.md) |
| `v1.0｜治理｜Skill Quality Score 与最低 Eval 标准` | Governance | `VERIFIED_STATIC` | [docs/SKILL_QUALITY_GATE.md](../SKILL_QUALITY_GATE.md)<br>[docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md](QUALITY_SCORE_EVAL_CONTRACT.md)<br>[scripts/validate_skill_eval_rules.py](../../scripts/validate_skill_eval_rules.py)<br>[scripts/validate_skill_evals.sh](../../scripts/validate_skill_evals.sh) |
| `v1.0｜文档｜README 与双语入口治理` | Documentation | `VERIFIED_STATIC` | [README.md](../../README.md)<br>[README_EN.md](../../README_EN.md)<br>[docs/catalog/skills-index.md](../catalog/skills-index.md)<br>[docs/catalog/skills-index_EN.md](../catalog/skills-index_EN.md)<br>[scripts/check_docs_bilingual.py](../../scripts/check_docs_bilingual.py) |
| `v1.0｜文档｜Skill Map Graph Catalog 治理` | Documentation | `VERIFIED_STATIC` | [docs/catalog/skills-graph.md](../catalog/skills-graph.md)<br>[docs/catalog/skills-graph_EN.md](../catalog/skills-graph_EN.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md)<br>[docs/SKILL_MATRIX_EN.md](../SKILL_MATRIX_EN.md) |
| `v1.0｜文档｜Workflow Eval 安装文档同步清单` | Documentation | `VERIFIED_STATIC` | [docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md](WORKFLOW_EVAL_INSTALL_SYNC.md)<br>[scripts/INSTALL_SKILLS.md](../../scripts/INSTALL_SKILLS.md)<br>[scripts/install-skills-mac.sh](../../scripts/install-skills-mac.sh)<br>[scripts/install-skills-windows.ps1](../../scripts/install-skills-windows.ps1) |
| `v1.0｜里程碑｜v1.0 Governance 发布准备` | Release preparation | `VERIFIED_STATIC` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[docs/generated/skill-governance-inventory.md](../generated/skill-governance-inventory.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |
| `v1.0｜治理｜典型 Match Merge 映射复核` | Mapping | `VERIFIED_STATIC` | [docs/governance/skill-governance-registry.yaml](skill-governance-registry.yaml)<br>[docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md](PHASE_0_MATCH_MERGE_REVIEW.md)<br>[docs/SKILL_MATCHING_REGISTER.md](../SKILL_MATCHING_REGISTER.md)<br>[docs/SKILL_MATRIX.md](../SKILL_MATRIX.md) |
| `Release DoD｜v1.0` | Release DoD | `VERIFIED_STATIC_WITH_RELEASE_NOT_RUN` | [docs/governance/RELEASE_DOD_V1_0.md](RELEASE_DOD_V1_0.md)<br>[docs/governance/SKILL_GOVERNANCE_V1.md](SKILL_GOVERNANCE_V1.md)<br>[scripts/check_skills_quality.sh](../../scripts/check_skills_quality.sh) |

## Reproduce

```bash
python3 scripts/generate_v14_closeout.py --verify-project
python3 scripts/generate_v14_closeout.py --check
bash scripts/check_skills_quality.sh
```

The live Project verification covers the full v1.4 card set; this DoD view intentionally shows only its declared version scope.
