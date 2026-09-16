<div align="right"><strong>🇨🇳 中文</strong> | <a href="./CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md">🇬🇧 English</a></div>

# 候选 Skill 15 步执行模板

复制本清单处理一个候选能力。每一步都要保留输入、证据、责任边界和未完成状态；先 Match，后决定 Enhance、Merge 或 New。

## Checklist

1. **Identify Quality Gap**：写清质量问题、用户和影响。
2. **Search Existing Skills**：查找当前双语目录、Matrix、Catalog、Workflow 和相似/Plus 包。
3. **Capability Match**：逐项比较 Name、Purpose、Input、Output、Decision Logic、Workflow Role。
4. **Decide**：选择 `EXISTING`、`MATCH`、`ENHANCE`、`MERGE` 或 `NEW`，并写证据。
5. **Define Scope**：规定职责、输入、输出和支持的生命周期阶段。
6. **Define Non-goals**：写明不负责的领域、工具、审批和执行行为。
7. **Design Input / Output**：定义必填信息、不完整输入、结果字段和证据链接。
8. **Define Decision Logic**：定义事实、推断、候选建议和 Human Decision 的分界。
9. **Implement**：只有 `NEW` 且卡片获准后才创建双语独立包；Enhance/Merge 优先改既有包。
10. **Eval**：补齐成功、不完整信息、范围/风险边界三类 case；无环境写 `NOT_RUN`。
11. **Workflow Integration**：确认组合入口、顺序和输出，不把导航箭头当安装依赖。
12. **Documentation**：同步 README、Catalog、Map、Matrix、安装器和双语入口。
13. **Release**：列出版本、质量门禁、迁移、回滚和人工发布决策；未批准写 `NOT_RUN`。
14. **Observe Usage**：收集实际调用、误触发、缺失输入和维护反馈；没有数据写 `UNASSESSED`。
15. **Re-evaluate**：基于新证据重新 Match、评分、Eval、Workflow 和 Deprecation 状态。

## 禁止跳步

目录存在、触发词命中、静态测试通过或 Project 卡 Done 都不能替代语义等价、真实运行、模型效果、业务验收和发布审批。

- [能力匹配指南](../SKILL_MATCHING_GUIDE.md)
- [Skill 生命周期](../SKILL_LIFECYCLE.md)
- [Enhancement Sprint 节奏](./ENHANCEMENT_SPRINT.md)
