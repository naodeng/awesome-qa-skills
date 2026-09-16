<div align="right"><strong>🇨🇳 中文</strong> | <a href="./DEPRECATION_DECISION_CONTRACT_EN.md">🇬🇧 English</a></div>

# Deprecation 决策契约

本契约把弃用变成可追溯、可逆的治理决定。它补充 [Skill 弃用与归档指南](../SKILL_DEPRECATION_GUIDE.md) 和 [Skill 生命周期](../SKILL_LIFECYCLE.md)，不自动删除目录，也不把弃用当作未经证实的 Match 结论。

## 状态边界

| 状态 | 含义 | 必须发生的动作 |
| --- | --- | --- |
| `Deprecated` | 已确认有替代路径，但仍需兼容历史安装 | 标注替代、保留边界、迁移方式和影响范围 |
| `Archived` | 替代路径稳定，历史使用需求已处理 | 保留历史记录和文档；停止日常维护 |
| `UNASSESSED` | 缺少项目证据，尚不能决定弃用 | 保持现状，补充需求/使用/维护证据 |

## 必填记录

每条弃用提案至少记录：

1. `skill`：物理目录和双语路径。
2. `decision`：`Deprecated`、`Archived` 或 `UNASSESSED`。
3. `replacement`：目标 Skill、mode 或 Workflow；没有替代不得进入 Deprecated。
4. `retained_boundary`：旧 Skill 仍负责什么，以及不再负责什么。
5. `migration`：安装路径、调用方式、文档链接和兼容窗口。
6. `affected_docs`：Matrix、Catalog、Map、README、Workflow 和安装文档。
7. `eval_install_impact`：Eval、触发词、安装器和脚本影响；无证据写 `NOT_RUN` 或 `N/A`。
8. `evidence`：需求、Issue/PR、使用反馈或可复核代码证据。
9. `human_decision`：责任人、时间和风险接受；没有人工决定写 `UNASSESSED`。

## 强制规则

- 先完成 Capability Match，再判断 Enhance、Merge 或 Deprecation；不得用弃用掩盖未复核关系。
- Deprecated 仍保留物理目录、历史路径和双语入口；只有明确迁移影响后才可标记 Archived。
- Matrix、Catalog、Map、README、Workflow 和安装器必须同步替代路径。
- 弃用记录不证明替代 Skill 的语义等价、运行效果、Quality Score 或发布批准。

## 复现与关联

```bash
python3 scripts/generate_skill_governance_matrix.py --check
python3 scripts/check_docs_bilingual.py --repo-root .
```

- [治理 Matrix](../SKILL_MATRIX.md)
- [匹配登记表](../SKILL_MATCHING_REGISTER.md)
- [v1.4 收口](./PHASE_0_V1_4_CLOSEOUT.md)
