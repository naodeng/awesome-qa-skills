# 研发质量流程角色与阶段 Skill 设计

> 日期：2026-08-11<br>
> 状态：已实施<br>
> 适用范围：`awesome-qa-skills` 中英文 Skill 设计，以及 AI 研发质量分析 MVP 的能力映射

## 1. 目标

为 AI 研发质量分析 MVP 的八个阶段和五个角色补齐可复用 Skill，同时满足以下约束：

- `AI-Quality-Workforce` 与 `awesome-qa-skills` 双向独立；
- 每个 Skill 复制或单独安装后可以独立使用；
- 阶段能力、角色判断和多角色汇总职责分离；
- 同一角色在不同阶段使用独立、可单独执行的 Prompt；
- 中文和英文 Skill 功能、结构和 Evals 对齐；
- 复用现有 Skill，不为八阶段五角色机械创建 40 个 Skill；
- 本设计只覆盖第一期 MVP，不提前加入第二期专项能力。

## 2. 方案选择

### 2.1 不采用：每个阶段角色组合一个 Skill

为每个单元格创建 `product-requirements-analysis`、`qa-code-review` 等 Skill，绑定关系直观，但最多形成 40 个 Skill，中英文合计 80 套目录。输入契约、输出结构和评审规则会大量重复，Evals 和长期维护成本过高。

### 2.2 不采用：每个阶段一个 Skill，角色只作为自由参数

该方案新增 Skill 最少，但阶段 Prompt 会逐渐包含五套角色逻辑。角色边界分散在八个阶段中，容易漂移，也不便于独立复用角色能力。

### 2.3 采用：阶段 Skill + 角色视角 Skill + 汇总 Skill

每个 AI 分析单元由阶段 Skill 和角色视角 Skill 组合。阶段 Skill 决定输入、阶段方法和 Artifact 契约；角色视角 Skill 决定该角色的关注点、判断标准和越权边界。多角色阶段完成后，由统一汇总 Skill 生成阶段汇总报告。

组合是增强机制，不是硬依赖：

- 阶段 Skill 单独安装后仍能完成完整阶段任务；
- 角色视角 Skill 单独安装后仍能针对材料完成该角色分析；
- 组合运行时必须遵守项目定义的 Artifact Schema；
- 可选角色 Skill 缺失时记录降级，不伪装为已经执行；
- 必需阶段 Skill 缺失时 Task 明确阻塞；
- 汇总 Skill 缺失时保留各角色 Artifact，允许人工汇总。

## 3. 能力边界

### 3.1 项目负责

- Workflow 和 Task 编排；
- Task 状态、重试、审批和审计；
- 输入输出契约与 Artifact Schema；
- Skill key、版本、参数和阶段绑定；
- `TaskRun`、`ArtifactVersion` 与来源追踪；
- Skill 缺失、输出不合约和降级处理。

### 3.2 Skill 负责

- 分析方法和执行步骤；
- 阶段或角色判断规则；
- Prompt 和按需参考材料；
- Markdown 输出要求；
- 信息不足、证据不足和职责越界处理；
- Skill 自身的 Evals。

### 3.3 禁止耦合

- 项目不得通过本机路径读取 `awesome-qa-skills`；
- Skill 不得写入项目数据库模型、内部 Task ID 或平台实现细节；
- Skill 之间不得用 Markdown 相对链接访问其他 Skill 的内部文件；
- 中文 Skill 不依赖英文 Prompt，英文 Skill 不依赖中文 Prompt；
- 项目只通过 `skill_key + skill_version + schema_version` 解析能力。

## 4. Skill 分层

### 4.1 阶段 Skill

阶段 Skill 定义：

- 当前阶段允许读取的输入；
- 阶段分析或评审流程；
- 阶段特有质量规则；
- 信息缺失与阻塞条件；
- 独立输出结构；
- 项目 Artifact Schema 的字段映射。

### 4.2 角色视角 Skill

角色 Skill 定义：

- 角色关注点和风险判断标准；
- 角色在不同阶段应回答的问题；
- 角色不得修改或替代的结论；
- 阶段不适用和输入不足的处理；
- 独立角色分析报告格式。

### 4.3 多角色汇总 Skill

`multi-role-quality-synthesis` 负责：

- 合并角色独立报告；
- 去重并保留所有来源；
- 区分共识、分歧、阻塞项和待确认项；
- 保留少数角色提出的高风险意见；
- 禁止生成任何输入角色均未提出的新事实；
- 禁止 PM 输入覆盖质量事实；
- 输出可追溯的阶段汇总报告。

## 5. 角色 Skill

| 角色 | Skill key | 核心责任 | 禁止越权 |
|---|---|---|---|
| 全能产品专家 | `product-quality-perspective` | 用户价值、业务目标、流程、规则、范围、验收标准和产品风险 | 不替代 QA 给出测试通过结论；不判断代码实现正确 |
| 全能 QA 专家 | `qa-quality-perspective` | 可测性、覆盖、测试方法、用例、证据、缺陷和质量风险 | 不虚构执行结果；证据不足时不得判定通过 |
| 全能 UI/UX 专家 | `ux-quality-perspective` | 信息架构、用户路径、交互、视觉一致性、跨端和可访问性 | 无原型时不虚构界面；不判断后端实现细节 |
| 全能技术专家 | `technical-quality-perspective` | 架构、接口、数据、兼容性、安全、性能、可观测性和代码风险 | 无代码或技术方案时不输出确定性实现结论 |
| 全能 PM 专家 | `project-delivery-perspective` | 排期、资源、依赖、里程碑、风险责任人和行动跟踪 | 不修改测试事实、缺陷状态、质量证据或质量结论 |

每个角色报告至少包含：角色结论摘要、已确认事实、风险与问题、分析依据、信息缺口与影响、待确认事项和建议行动。

## 6. 同一角色的阶段 Prompt 设计

角色 Skill 内不同阶段的 Prompt 相互独立，不通过一个大 Prompt 猜测阶段。调用方必须显式提供 `stage`；不支持的阶段返回“不适用”，不得静默套用相近 Prompt。

以 `product-quality-perspective` 为例：

```text
product-quality-perspective/
├── SKILL.md
├── prompts/
│   ├── requirements-analysis.md
│   ├── test-strategy.md
│   ├── test-strategy-review.md
│   ├── code-review.md
│   ├── test-case-writing.md
│   ├── test-case-review.md
│   ├── test-reporting.md
│   └── test-report-review.md
├── agents/openai.yaml
└── evals/
    ├── eval.yaml
    └── cases/
```

每个阶段 Prompt 必须完整定义：允许输入、分析目标、最低检查维度、职责边界、缺失信息处理、输出结构和风险标准。Prompt 之间不互相引用。

各角色配置的阶段 Prompt：

| 角色 Skill | 独立阶段 Prompt |
|---|---|
| `product-quality-perspective` | 八个阶段；代码评审、用例编写和测试报告按条件启用 |
| `qa-quality-perspective` | 八个阶段 |
| `ux-quality-perspective` | 八个阶段；测试策略、策略评审、代码评审、用例编写和测试报告按条件启用 |
| `technical-quality-perspective` | 八个阶段 |
| `project-delivery-perspective` | 测试策略、测试策略评审、测试报告 Review |

条件参与的 Prompt 仍是完整 Prompt，但执行前必须先判断本阶段材料是否涉及该角色关注范围。判断为不适用时输出原因，不生成空泛报告。

## 7. 阶段 × 角色 × Skill 映射

### 7.1 需求分析

阶段 Skill：默认 `requirements-analysis-plus`；简单材料可降级为 `requirements-analysis`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 默认 | 阶段 Skill + `product-quality-perspective` | 价值、流程、规则、范围、验收标准、产品风险 |
| QA | 默认 | 阶段 Skill + `qa-quality-perspective` | 可测性、测试点、边界、异常、依赖、质量风险 |
| UI/UX | 默认 | 阶段 Skill + `ux-quality-perspective` | 用户路径、交互状态、原型缺口、跨端、可访问性 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 可行性、接口、数据、安全、性能、实现风险 |
| PM | 不参与 | — | — |

角色报告完成后调用 `multi-role-quality-synthesis`，输出四份角色报告和一份需求分析汇总报告。

### 7.2 测试策略

阶段 Skill：默认 `test-strategy-plus`；简单场景可使用 `test-strategy`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 默认 | 阶段 Skill + `product-quality-perspective` | 业务优先级、核心用户路径、不可接受风险 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 范围、方法、深度、环境、数据、准入与退出 |
| UI/UX | 条件 | 阶段 Skill + `ux-quality-perspective` | UI、跨端、可访问性和体验验证策略 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 接口、数据、性能、安全、可观测性和依赖 |
| PM | 仅输入 | `project-delivery-perspective` | 时间、人力、依赖、里程碑和约束 |

PM 产物标记为项目约束输入，不是质量结论。最后调用 `multi-role-quality-synthesis`。

### 7.3 测试策略评审

新增阶段 Skill：`test-strategy-review`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 默认 | 阶段 Skill + `product-quality-perspective` | 核心业务和用户价值是否得到保障 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 覆盖、方法、深度和门槛是否充分可执行 |
| UI/UX | 条件 | 阶段 Skill + `ux-quality-perspective` | 体验、跨端和可访问性是否遗漏 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 技术风险、环境、数据和系统约束是否覆盖 |
| PM | 仅输入 | `project-delivery-perspective` | 计划是否现实、依赖是否明确 |

AI 角色分析和汇总完成后，由 Human Task 最终选择通过、有条件通过或驳回。

### 7.4 代码评审

阶段 Skill：`code-review`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 条件 | 阶段 Skill + `product-quality-perspective` | 业务规则、状态流和验收语义 |
| QA | 默认 | 阶段 Skill + `qa-quality-perspective` | 可测性、回归、异常、测试遗漏和可观测性 |
| UI/UX | 条件 | 阶段 Skill + `ux-quality-perspective` | UI 状态、反馈、响应式和可访问性实现 |
| 技术 | 默认、主责 | 阶段 Skill + `technical-quality-perspective` | 逻辑、架构、接口、数据、安全、性能和维护风险 |
| PM | 不参与 | — | — |

必须提供代码版本、Diff 或可访问仓库；缺失时阶段 Task 阻塞。最后调用 `multi-role-quality-synthesis`。

### 7.5 测试用例编写

阶段 Skill：`test-case-writing`；复杂项目可评估 `testcase-writer-plus`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 条件 | 阶段 Skill + `product-quality-perspective` | 核心业务路径、规则和验收场景 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 正向、异常、边界、状态、数据和回归用例 |
| UI/UX | 条件 | 阶段 Skill + `ux-quality-perspective` | 交互、视觉状态、跨端和可访问性用例 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 接口、数据、安全、性能和技术异常用例 |
| PM | 不参与 | — | — |

角色先提供场景候选与风险标签，QA 主责形成统一测试用例。每条用例保留 `source_role` 和需求追溯信息，避免生成四套重复用例。

### 7.6 测试用例 Review

阶段 Skill：默认 `test-case-reviewer-plus`；快速检查可使用 `test-case-reviewer`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 默认 | 阶段 Skill + `product-quality-perspective` | 业务规则、用户价值和验收覆盖 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 覆盖、优先级、步骤、预期、数据和可执行性 |
| UI/UX | 默认 | 阶段 Skill + `ux-quality-perspective` | 用户旅程、交互状态、跨端和可访问性 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 接口、数据、异常、安全、性能和技术风险 |
| PM | 不参与 | — | — |

AI 汇总必须区分阻塞缺口、高风险补测、可维护性问题和低价值用例；Human Task 做最终决策。

### 7.7 测试报告

阶段 Skill：`test-reporting`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 条件 | 阶段 Skill + `product-quality-perspective` | 业务目标完成度和关键路径残余风险 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 覆盖、执行、缺陷、证据、质量状态和置信度 |
| UI/UX | 条件 | 阶段 Skill + `ux-quality-perspective` | 体验、跨端和可访问性验证结果 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 技术缺陷、稳定性、安全、性能和可观测性风险 |
| PM | 不参与 | — | — |

执行报告和缺陷报告同时缺失时只能输出“未执行或证据不足”，不得推断测试通过。最后调用 `multi-role-quality-synthesis`。

### 7.8 测试报告 Review

新增阶段 Skill：`test-report-review`。

| 角色 | 参与 | Skill 组合 | 重点 |
|---|---|---|---|
| 产品 | 默认 | 阶段 Skill + `product-quality-perspective` | 业务目标、关键路径和产品风险表达 |
| QA | 默认、主责 | 阶段 Skill + `qa-quality-perspective` | 数据、证据、覆盖、缺陷和结论一致性 |
| UI/UX | 默认 | 阶段 Skill + `ux-quality-perspective` | 体验验证结果和残余风险完整性 |
| 技术 | 默认 | 阶段 Skill + `technical-quality-perspective` | 技术风险、限制和未解决问题准确性 |
| PM | 仅输入 | `project-delivery-perspective` | 责任人、期限、依赖和后续行动 |

AI 汇总不得把证据不足改写为通过，不得隐藏未测范围，也不得让 PM 输入覆盖 QA 或技术事实。Human Task 做最终决策。

## 8. Human Review 内部结构

测试策略评审、测试用例 Review 和测试报告 Review 在看板上仍是三个独立 Human Task 阶段，但阶段内部采用以下顺序：

```mermaid
flowchart LR
    A[AI 角色评审分析] --> B[多角色评审汇总]
    B --> C[Human 最终决定]
```

Human 最终决定不能被 AI 汇总结论替代。驳回后由上游负责人修订 Artifact 并创建新版本，再生成新的角色分析、汇总和人工评审记录。

## 9. 新增与增强范围

### 9.1 P0 新增 Skill

| Skill | 目录类别 | 用途 |
|---|---|---|
| `product-quality-perspective` | `testing-workflows` | 产品跨阶段质量视角 |
| `qa-quality-perspective` | `testing-workflows` | QA 跨阶段质量视角 |
| `ux-quality-perspective` | `testing-workflows` | UI/UX 跨阶段质量视角 |
| `technical-quality-perspective` | `testing-workflows` | 技术跨阶段质量视角 |
| `project-delivery-perspective` | `testing-workflows` | PM 项目约束与行动视角 |
| `multi-role-quality-synthesis` | `testing-workflows` | 多角色报告汇总与追溯 |
| `test-strategy-review` | `testing-types` | 测试策略评审 |
| `test-report-review` | `testing-types` | 测试报告评审 |

八个 Skill 均在 `skills/zh/` 和 `skills/en/` 下创建同名目录，共 16 个语言目录。

### 9.2 P1 增强现有 Skill

| Skill | 增强内容 |
|---|---|
| `requirements-analysis-plus` | 角色组合输入；事实、假设、来源、风险和待确认项字段 |
| `test-strategy-plus` | 角色来源与 PM 约束输入；项目限制不覆盖质量结论 |
| `code-review` | 条件角色启动；代码版本缺失时明确阻塞 |
| `test-case-writing` | `source_role`、需求追溯和角色场景去重 |
| `test-case-reviewer-plus` | 多角色评审输入和 Human 决策接口 |
| `test-reporting` | 证据等级、证据不足状态和禁止虚假通过规则 |

在修改前先确认 `test-case-writing` 与 `testcase-writer-plus` 的实际边界，不扩大重复能力。

### 9.3 P2 延后

风险分析、架构评审、发布准入、缺陷分析、证据验证、安全、性能和可访问性专项不进入第一期新增范围。

## 10. 项目组合契约

项目声明示例：

```yaml
stage_skill:
  key: requirements-analysis-plus
  version: 1.0.0
  required: true
perspective_skill:
  key: product-quality-perspective
  version: 1.0.0
  required: false
parameters:
  stage: requirements-analysis
output:
  artifact_type: role_analysis_report
  schema_version: 1
  source_role: product
```

角色 Artifact 至少记录：

- `stage`
- `source_role`
- `skill_version`
- `prompt_version`
- `input_versions`
- `summary`
- `facts`
- `assumptions`
- `findings`
- `evidence`
- `risks`
- `missing_information`
- `questions`
- `recommended_actions`
- `confidence`

Artifact Schema 属于项目契约，不属于某个 Skill 的私有格式。符合相同 Schema 的企业内部 Skill、用户自定义 Skill或其他实现可以替换 `awesome-qa-skills` 中的实现。

## 11. Evals 与独立性验收

### 11.1 每个角色 Skill

至少覆盖：正常参与、信息不完整、角色越权、不适用阶段、条件参与不命中、角色结论冲突。每个阶段 Prompt 至少有一条有效用例；高风险阶段增加证据不足和诱导越权用例。

### 11.2 两个评审 Skill

至少覆盖：通过、有条件通过、阻塞驳回、输入不完整、上游结论冲突、证据不足但被要求给出通过结论。

### 11.3 汇总 Skill

至少覆盖：正常汇总、去重保留来源、角色冲突、条件角色缺席、禁止创造新事实、PM 尝试覆盖质量事实。

### 11.4 独立安装验收

1. 将单个语言 Skill 复制到临时空目录；
2. 检查没有跨 Skill 相对链接；
3. 检查没有 `AI-Quality-Workforce` 本机路径或内部对象 ID；
4. 单独执行成功、信息不足和职责边界 Evals；
5. 中文与英文分别验证；
6. 模拟可选角色 Skill 缺失时的降级；
7. 模拟阶段 Skill 缺失时的明确阻塞；
8. 模拟汇总 Skill 缺失时保留角色 Artifact；
9. 运行 `bash scripts/check_skills_quality.sh`；
10. 单独报告 `skill-up validate` 和实际 eval run 是否执行成功，不用完整性检查代替运行证据。

## 12. 完成标准

- 八个新增 Skill 中英文结构和能力对齐；
- 六个现有 Skill 的增强不破坏其原有独立使用方式；
- 角色 Skill 的参与阶段均有独立 Prompt；
- 不适用阶段不会套用通用空泛分析；
- 阶段 Skill、角色 Skill 和汇总 Skill 均可独立安装和执行；
- 项目只通过稳定 key、版本和 Schema 引用能力；
- 多角色汇总可以追溯到角色原始 Artifact；
- 三个 Review 阶段保留 Human 最终决定；
- 所有相关 Evals、元数据、完整性和独立性检查通过；
- 未经单独验证，不宣称运行时 Evals 已通过。
