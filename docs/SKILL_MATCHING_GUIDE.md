<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_MATCHING_GUIDE_EN.md">🇬🇧 English</a></div>

# Skill 能力匹配指南

## 目的

逐项匹配决定记录在 `governance/skill-governance-registry.yaml`，Matching Register 是生成视图；修改 registry 后必须重新生成并运行 `--check`。

所有候选能力在创建目录前必须完成能力匹配。结论只能是 `EXISTING`、`ENHANCE`、`MERGE`、`MATCH` 或 `NEW`。

## 六步核对

1. 名称：是否只是同义名称或工具名差异。
2. 目的：是否解决相同质量问题。
3. 输入：是否依赖同类证据、约束和上下文。
4. 输出：是否产生相同决策、建议或工件。
5. 决策逻辑：是否采用相同的判断规则与风险模型。
6. Workflow 角色：是否处在相同组合位置。

## 结论与动作

| 结论 | 动作 |
| --- | --- |
| EXISTING | 记录映射，不创建目录。 |
| MATCH | 记录同义映射，不创建目录。 |
| ENHANCE | 为既有 Skill 建卡，补齐边界、证据、输出或 Eval。 |
| MERGE | 将候选作为既有 Skill 的 mode、规则或子流程。 |
| NEW | 定义独立 Scope/Non-goals 后，创建中英双语独立 Skill。 |

`NEW` 必须证明输入、分析逻辑、输出和决策价值均不能由已有能力合理承担。匹配结论必须写入 Matrix 和 GitHub Project 卡；静态审查不能代替运行效果证明。
