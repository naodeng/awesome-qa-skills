<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-requirements-quality-skills-design_EN.md">🇬🇧 English</a></div>

# v1.1 前五个需求质量 Skill 设计

## 目标

在 `develop` 已同步远端 `main` 的基线上，启动 Project #4 中 v1.1 P0 的前五个候选 Skill：

1. `requirement-quality-review`
2. `requirement-ambiguity-analysis`
3. `requirement-consistency-analysis`
4. `requirement-conflict-detection`
5. `requirement-traceability-analysis`

每个 Skill 都必须是可独立复制安装的中英双语包，能够在需求、验收标准、变更说明或相关证据不完整时给出有边界的初版分析；不得把推断、建议、映射或静态检查写成已执行测试、已批准决策或发布结论。

## 基线与范围

- 当前代码基线：`develop` 已快进至远端 `main` 的 `afe51cd`。
- Project #4 中上述五张卡片已从 `Todo` 移至 `In Progress`；卡片状态表示开发阶段，不表示发布或风险接受。
- 现有 `requirements-analysis` 负责通用需求理解、测试点、边界、依赖和风险；`requirements-analysis-plus` 负责多格式、多来源需求的综合分析。
- 新 Skill 只处理清晰、可复核的专项问题，不复制现有综合 Skill 的完整流程，也不互相读取对方内部文件。
- `awesome-qa-prompt` 中的 `requirement-traceability-analysis` 是可参考的 Prompt Baseline；其余四项没有同名 Baseline，使用现有仓库的需求分析约束和项目卡片边界重新设计，不复制外部目录结构。

## Capability Match 边界

五项候选均按 `NEW` 方向实施，但登记为 `PROPOSED`，因为当前证据只能证明目录、Prompt 契约和导航边界，不能证明业务语义等价、模型效果或真实项目有效性。每项都必须在 registry 中记录六个匹配字段：名称、目的、输入、输出、决策逻辑和 Workflow 角色，并明确 Scope 与 Non-goals。

如果实现过程中发现某项能力与现有 Skill 语义重叠，必须停止创建该项的独立行为，更新 Matching Register 为 `ENHANCE` / `MERGE` / `MATCH`，并保留差异证据；不能为了完成五张卡片而强行维持重复能力。

## 专项边界

| Skill | 负责的问题 | 不负责的问题 |
| --- | --- | --- |
| `requirement-quality-review` | 以完整性、清晰度、可验证性、可行性、范围和证据质量做总览评审，并指出应进入哪个专项分析 | 不替代四个专项分析；不输出数值质量分或放行决定 |
| `requirement-ambiguity-analysis` | 找出指代不明、角色/范围/量词/条件不清、不可判定措辞和缺失上下文 | 不把不同来源的明确冲突当作普通歧义；不替用户选择解释 |
| `requirement-consistency-analysis` | 比较多份材料中的术语、标识、格式、状态、规则和行为描述是否一致 | 不把互斥约束静默合并；明确冲突转给冲突检测和人工裁决 |
| `requirement-conflict-detection` | 识别有来源证据的互斥规则、约束或验收条件，保留冲突双方、适用范围和裁决问题 | 不自行决定优先级、责任、豁免或最终业务规则 |
| `requirement-traceability-analysis` | 建立需求、验收标准、设计/实现、测试资产、缺陷和证据之间的双向关系，识别孤立项和未覆盖项 | 不把名称相同当作真实链接；不宣称测试已执行或通过 |

专项枚举必须保持不同维度：一致性分析使用关系 `aligned`/`inconsistent`/`conflict`，并单独使用证据状态 `assessed`/`missing`/`stale`/`unassessed`；可追踪性分析使用关系类型 `direct`/`derived`/`indirect`/`contradictory`/`missing`，并单独使用覆盖状态 `complete`/`partial`/`unverified`/`stale`/`unexecuted`/`unassessed`。

## 统一输出契约

每个 Prompt 都要求先做输入审计，再给专项结果。最低共享字段如下：

1. 输入审计：`known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
2. 事实分层：直接材料事实、证据支持的推断、建议、人工决策项必须分开。
3. Findings：每条尽量包含 `ID`、`Topic`、`Sources`、`Status`、`Impact`、`Priority`、`Evidence`、`Question or decision needed`、`Suggested owner`、`Suggested next action` 和 `Validation method`。
4. 专项结果表：根据 Skill 增加领域字段，但不删除来源、状态、证据和行动字段。
5. 风险与依赖：区分缺口、冲突、不可测、未覆盖和待确认项；P0/P1 必须有责任角色和可关闭的下一步。
6. 自检：检查无依据结论、事实与推断混淆、越界判断、未标注假设和伪造的执行/审批结论。

不采用统一数值评分，不在没有输入依据时补造 SLA、阈值、字段、接口、责任人、环境或根因。信息不足时输出最小可用初版并列出 3–5 个高价值问题；若无法安全继续，明确阻塞原因和所需证据。

## 包结构与文档同步

每个语言包创建以下最小结构：

```text
skills/{zh,en}/testing-types/<skill-name>/
├── SKILL.md
├── prompts/<skill-name>.md
├── agents/openai.yaml
└── evals/
    ├── eval.yaml
    ├── trigger-prompts.csv
    ├── local-rules.json
    └── cases/
        ├── basic-success.yaml
        ├── edge-incomplete-input.yaml
        └── edge-scope-boundary.yaml
```

每个 Skill 至少包含成功路径、信息不足、范围/风险边界三类 Eval；专项需要时在同一包中增加冲突、孤立项或多来源用例。中英文目录、frontmatter `name`、Agent metadata key、Prompt 文件名和 Eval 结构必须对齐。

目录完成后同步：

- `skills/zh/README.md` 与 `skills/en/README.md`；
- `docs/catalog/skills-index.md` 与 `_EN.md`；
- 根 `README.md` 与 `README_EN.md`；
- `docs/catalog/skills-graph.md` 与 `_EN.md`；
- Phase 1 需求质量治理说明及其英文镜像；
- `docs/governance/skill-governance-registry.yaml`，再由生成器刷新 Matrix、Matching Register 和治理库存。

这些入口只提供导航和能力边界，不创建跨 Skill 的相对内部链接，不把流程推荐写成安装依赖。

## 开发与验证顺序

按 Project 卡片顺序逐个完成，每个 Skill 独立经过：

1. 先写并运行该 Skill 的压力/边界 Eval 或等价失败基线，记录会暴露的错误行为；
2. 写最小 `SKILL.md`、Prompt、metadata 和三类 Eval，使失败场景有明确约束；
3. 运行 Skill-up 结构校验与可用 Eval，检查输出是否保持来源、状态和人工边界；
4. 复核新暴露的推断、静默合并或越界结论，补充最小修正；
5. 执行该包的完整静态校验后，才进入下一个 Skill。

最终执行仓库级 `bash scripts/check_skills_quality.sh`、治理生成器 `--check`、`git diff --check`，并检查 Git 状态和五张 Project 卡片。静态门禁通过只证明结构、文档、元数据和 Eval 文件符合约定；模型输出质量、运行效果和实际项目覆盖仍保持 `UNASSESSED`，除非有独立执行证据。

## 非目标

- 不修改或删除现有 `requirements-analysis`、`requirements-analysis-plus` 的行为。
- 不引入共享运行时代码、第三方依赖、外部服务或真实测试目标。
- 不自动创建 GitHub Issue、发布版本、推送远端或改变非本批次 Project 卡片状态。
- 不用一个通用模板掩盖五项专项之间的语义差异。
