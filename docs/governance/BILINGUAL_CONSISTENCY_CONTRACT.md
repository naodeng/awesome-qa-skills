<div align="right"><strong>🇨🇳 中文</strong> | <a href="./BILINGUAL_CONSISTENCY_CONTRACT_EN.md">🇬🇧 English</a></div>

# 中英文一致性质量契约

本契约定义当前有效文档和 Skill 包的结构一致性。它检查可复现的路径、入口和链接，不把字面相似当作语义等价，也不证明运行效果。

## 一致性要求

| 范围 | 契约 |
| --- | --- |
| 项目文档 | `NAME.md` 与 `NAME_EN.md` 成对存在，顶部互有语言切换链接 |
| Skill 目录 | `skills/zh` 与 `skills/en` 使用相同物理 slug 和相同维护文件结构 |
| Skill 内容 | `SKILL.md`、主 Prompt、README、quick-start、tutorial、output-formats、reference 和 Workflow reference 按相对路径镜像 |
| Catalog | 中文/英文索引列出同一组 Skill；根 README 的 `data-skill` marker 不重复、不缺失、不引入未知项 |
| Generated | Matrix、Inventory、Register 等生成物由事实源重建；生成产物不要求逐文件翻译，但必须有双语入口 |
| Links | 当前入口中的相对链接必须可解析；跨 Skill 只使用导航链接，不链接另一个 Skill 的内部文件 |

## 当前覆盖

- 每种语言 164 个 Skill 包，中英文合计 328 个物理目录。
- `testing-workflows` 当前 10 个工作流必须在双语安装/Eval 清单中逐项出现。
- 生成治理视图由 Registry、虚拟 Domain manifest 和生成器共同决定；任何源变更都必须重新生成并执行 `--check`。

## 质量门禁

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
bash scripts/check_skills_quality.sh
```

检查通过只说明结构、镜像和链接证据可复现；语义、模型 Eval、运行时和发布状态仍按 `UNASSESSED`、`NOT_RUN` 或 `N/A` 记录。

## 导航

- [双语文档维护策略](./DOCUMENTATION_POLICY.md)
- [Workflow/Eval 安装同步清单](./WORKFLOW_EVAL_INSTALL_SYNC.md)
- [v1.4 收口](./PHASE_0_V1_4_CLOSEOUT.md)
