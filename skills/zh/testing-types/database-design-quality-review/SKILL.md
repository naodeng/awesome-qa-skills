---
name: database-design-quality-review
description: Use this skill when an ERD, DDL, ORM schema, or migration plan needs an evidence-bounded database design review before implementation; triggers include 数据库设计质量评审, database design review, and migration readiness review.
---

# 数据库设计质量评审

在实现或迁移前评审 ERD、DDL、ORM schema、数据所有权、生命周期、查询约束、事务并发、迁移兼容和恢复设计。输出 `DB-##` 发现与验证准备，不连接真实数据库、不运行查询，也不替 Human 批准上线。

## 何时使用

- 需要检查模型完整性、约束、索引、生命周期/隐私和数据所有权。
- 需要识别事务隔离、并发、迁移回滚、备份恢复和性能风险。
- 需要在 DDL 或迁移材料不完整时交付受限设计评审。

不适用于执行迁移、连接生产数据库、压测查询或凭表名补造业务规则。

## 输出格式选项

- 默认输出 Markdown；用户要求表格、CSV 或 JSON 时，保留相同的证据、状态、影响、责任角色和验证字段。
- 不把结构化格式或静态清单写成执行、通过、批准或发布证据。

## 如何使用

1. 先读取本 Skill 的主 Prompt，并提供目标、范围、材料、环境和已有证据。
2. 按 Prompt 的输入审计和输出合同执行；缺少信息时交付带边界的初版。
3. 对每条发现保留来源、证据状态、影响、责任角色、关闭条件和验证方法。

## 工作方式

1. 阅读 `prompts/database-design-quality-review.md`，审计目标、版本、数据库边界和证据。
2. 将输入分为 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
3. 按对象、约束、索引、事务/并发、生命周期、迁移和恢复建立覆盖矩阵，使用 `DB-##` 绑定来源与最小证据。
4. 输出事实、证据推断、建议和 Human 决策，给出影响、责任角色、关闭条件和验证方法。
5. 没有执行身份、时间、环境和原始结果时，不写数据库操作已成功。

## 核心约束

- 不连接、写入、迁移或查询真实数据库；不运行基准或恢复演练。
- 不凭表名、字段名或常见模式发明业务规则、阈值、保留期限或隐私分类。
- 每条 `DB-##` 至少包含对象、来源/证据、约束/索引、事务/并发、迁移回滚、影响、责任角色和验证方式。
- 示例必须脱敏；缺少证据时标记 `missing`、`unverified`、`unexecuted` 或 `unassessed`。

## 参考文件

- 每次产出前必须阅读 `prompts/database-design-quality-review.md`。
- 回归时读取 `evals/eval.yaml` 和用例；静态设计检查不证明数据库行为。
- 触发检查使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json`；缺少 selection trace 时报告 `BLOCKED`。

## 最佳实践

- 优先处理高影响且可验证的缺口，使用最小实验或补证动作降低不确定性。
- 将事实、证据支持的推断、建议和 Human 决策分开，避免把假设升级为结论。

## 交付前自检

- [ ] 已审计对象、版本、所有权、范围和证据
- [ ] 已覆盖模型、约束、索引、生命周期/隐私、事务并发、迁移、性能、备份恢复和测试准备度
- [ ] 每条 `DB-##` 有最小证据、影响、责任角色、行动和验证
- [ ] 所有示例使用脱敏数据，未连接真实数据库
- [ ] 未把 DDL 存在或静态检查写成迁移成功或上线批准

## 常见误区

- 只检查表和字段，不检查约束、生命周期、回滚和恢复。
- 把索引存在当成查询性能已验证。
- 把迁移脚本能解析当成向后兼容和可回滚。
