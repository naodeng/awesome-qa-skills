<div align="right"><a href="./PHASE_0_PROMPT_BASELINE_SOURCES_EN.md">English</a></div>

# Phase 0 候选 Prompt Baseline 来源登记

## 来源锁定

Phase 0 的候选能力参考源是相邻仓库 `naodeng/awesome-qa-prompt`。本次审查固定在
`develop` 提交 `554178fe9b93d851ec01388597ceb7996d22bd1c`，仓库地址为
`https://github.com/naodeng/awesome-qa-prompt`。

这些文件是只读的内容质量与主题覆盖基线，不是 `awesome-qa-skills` 的运行时依赖。Skill
包不得复制 `Standard-version/`、框架变体目录或跨仓库相对链接；本登记只保存来源定位和
匹配证据。

## 六项证据的取法

| 字段 | Baseline 证据位置 |
| --- | --- |
| name | 中英文 `README.md` 标题与 Prompt 的角色/标题 |
| purpose | `README.md` 的用途说明与 Prompt purpose 注释 |
| inputs | `Standard-version/*.md` 的 `必要输入` / `Required inputs` |
| outputs | `Standard-version/*.md` 的 `执行指令` / `Execution instructions` |
| decision_logic | `分析方法` / `分析与设计方法`、专项聚焦与降级规则 |
| workflow_role | 本仓库 `QA_SKILLS_EVOLUTION_ROADMAP.md` 的阶段边界与 Baseline 的专项输出角色 |

## Registry 关联

候选名称、Target、Conclusion 和适配边界只在
`docs/governance/skill-governance-registry.yaml` 维护；该 Registry 是唯一事实源。
本文件只定义固定 Prompt Baseline 提交和取证规则，避免形成第二份候选决策表。

Registry 的每个 `candidate_source` 直接列出对应 Baseline 的 `README.md` 与
`Standard-version/*.md` 路径；六项 `evidence` 同时列出候选 Baseline 与当前 Target 的
具体文件和章节。下列路径均相对于固定提交，`zh` 与 `en` 目录成对存在。

## 限制

上述来源足以支持候选名称、目的、输入、输出、决策逻辑和 Workflow 角色的结构化审查。
它们不提供具体项目的业务需求、Issue/PR 约束、模型运行结果或真实质量分数；因此候选
`decision_state` 使用 `REVIEWED_WITH_LIMITATION`，Quality Score 与 Eval 执行仍保持
`NOT_SCORED` / `NOT_RUN`，Prompt 语义等价与运行有效性仍为 `UNASSESSED`。
