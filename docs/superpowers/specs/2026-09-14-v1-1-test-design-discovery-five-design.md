<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-test-design-discovery-five-design_EN.md">🇬🇧 English</a></div>

# v1.1 测试设计发现五张 Skill 卡片设计

## 状态

`APPROVED_FOR_IMPLEMENTATION`（2026-09-14，完成计划 review 修复）。本文覆盖 Project #4 中接下来五张 v1.1 P0 Todo 卡片，只定义能力匹配、目录边界和验证合同，不创建 Skill 包、不修改治理 registry 或生成视图。

## Capability Match 决策

仓库规则是“先匹配，能增强就不新增；只有主输入、输出和决策逻辑确实不同才创建独立目录”。本批五项均有独立交付物，但每项都必须遵守下表边界：

| 候选卡片 | 决策 | 最近能力证据 | 独立边界 |
| --- | --- | --- | --- |
| `test-gap-analysis` | `NEW` | `requirement-traceability-analysis` 做稳定 ID 的双向制品映射；`test-case-reviewer` 评审已有用例；两者都不以“测试义务缺失发现”为独立输入/输出合同 | 新包从需求、风险、变更、缺陷和现有测试资产发现缺失测试义务，输出 `TG-##`；不生成完整追踪矩阵，不把缺口写成覆盖或通过结论 |
| `risk-based-testing` | `NEW` | `quality-risk-analysis` 识别和排序质量风险；`test-strategy` 制定完整策略；`regression-scope-analysis` 聚焦变更/发布后的回归边界 | 新包把已知风险转成测试优先级、深度、方法和时间盒取舍，输出 `RBT-##`；不替代风险登记、完整策略或既有测试集选择 |
| `edge-case-discovery` | `NEW` | `requirements-analysis` 与 `test-case-writing` 要求考虑边界；`test-case-reviewer` 从已有用例找边界漏测，但没有独立的边界发现交付合同 | 新包从输入域、时间、状态、资源、并发、平台和组合维度枚举边界候选，输出 `EC-##`；不做需求质量评审，不写完整测试用例 |
| `negative-scenario-discovery` | `NEW` | `requirements-analysis` 和 `test-case-writing` 可包含异常路径；`test-case-reviewer` 评审已有异常覆盖，但没有独立的失败/拒绝/恢复路径发现合同 | 新包从非法输入、权限拒绝、依赖失败、超时、重试、幂等和数据不一致等角度发现 `NS-##`；不执行故障注入，不写完整测试用例 |
| `test-data-requirement-analysis` | `NEW` | `test-data-generation` 产出数据模型、生成规则和数据集；它把数据需求作为生成输入，而不是独立的先决条件/阻塞分析 | 新包先分析字段、关系、状态、角色、隐私、来源、生命周期、清理和环境前置条件，输出 `TDR-##`；不生成数据、不复制生产数据、不替代数据生成方案 |

### 六字段匹配证据

- **name**：候选卡片名称与现有目标的 `SKILL.md` `name` 不相同；不以名字相似直接新增，以下差异由 purpose、inputs、outputs 和 decision logic 共同证明。
- **purpose**：五项分别面向测试义务缺口、风险到测试决策、边界候选发现、失败路径发现和数据前置需求；现有相邻 Skill 的主要目的不同。
- **inputs**：前四项可消费需求/设计/风险/变更/测试资产，但关注的证据切片和最低输入不同；数据需求分析消费字段关系、生命周期、隐私和环境限制，不要求可生成的数据集。
- **outputs**：五项分别使用 `TG-##`、`RBT-##`、`EC-##`、`NS-##`、`TDR-##` 稳定发现，并包含证据、影响、优先级、缺口动作和验证方法；这些不是现有 Skill 的默认输出合同。
- **decision_logic**：发现类能力必须按来源、触发条件、预期/失败结果和证据状态区分事实、推断与候选；风险类必须解释优先级和深度取舍；数据类必须先判断缺失/冲突/隐私/清理阻塞，不能直接生成。
- **workflow_role**：五项均属于 Engineering QA / Test Design and Preparation，顺序上位于策略或用例执行之前，可被 `discover-testing` 路由为一个主能力；它们不是运行时执行器、生产探针或 Human 放行门。

如果实现阶段发现某项的主输入、输出和决策逻辑已被现有 Skill 完整覆盖，必须在创建目录前改为 `ENHANCE` 或 `MATCH`，并同步修改本设计与计划；不得为了完成卡片数量强行复制能力。

## 共享合同

- 中英文入口、Prompt、metadata、Eval 和本地触发数据结构对等；目录名、frontmatter `name` 和 `agents/openai.yaml` 的 `metadata.key` 使用同一个小写连字符 slug。
- 每个新包必须包含 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml`、成功/信息不足/范围或风险边界三类 `evals/cases/`、`trigger-prompts.csv` 和 `local-rules.json`。
- 每次分析先记录 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`；事实、证据支持的推断、候选建议和 Human 决策分开。
- 每条发现必须有来源和最小证据，并标注影响/优先级、责任角色、关闭条件和验证方法。文件存在、名称匹配、报告文字、静态配置或 Skill 输出模板不等同于执行结果。
- 缺少主材料时交付受限初版并标出 `unassessed`/`blocked` 边界；冲突影响核心判断时保留双方，不静默合并。
- 本批不连接真实项目、数据库、生产观测或外部服务，不执行真实测试、故障注入、数据生成、迁移、发布或审批。
- 本地触发数据必须覆盖 `explicit`、`implicit`、`contextual`、`negative` 四种模式，并同时有应触发和不应触发样本；缺少真实 `skill.selection` 证据时 runner 只能报告 `BLOCKED`。

## 五个 Skill 的最小设计

### `test-gap-analysis`

输入需求/验收标准、风险、变更、缺陷历史、测试资产和执行证据（若提供）。每条 `TG-##` 包含测试义务或行为、来源、缺失类型、影响/优先级、已有控制、证据状态、建议测试意图、责任角色、关闭条件和验证方法。缺口类型至少区分 missing requirement-to-test、orphan test、unverified execution、stale evidence、uncovered risk 和 duplicate/low-value coverage。它不建立完整 RT/TC 矩阵、不宣称覆盖率或通过、不替 Human 接受风险。

### `risk-based-testing`

输入业务关键性、失败模式、变更面、用户/数据影响、历史缺陷、可探测性、环境/资源和时间盒。每条 `RBT-##` 包含风险来源、假设、测试目标、级别/方法、深度、优先级依据、范围取舍、停止条件、扩大范围触发器和所需证据。它不计算伪精确风险分、不生成完整测试策略、不选择具体已有测试 ID、不执行测试，也不把“高风险”自动变成 Human 的发布阻塞决定。

### `edge-case-discovery`

输入需求、数据域、状态模型、时间规则、资源/并发限制、平台差异和已有测试/缺陷证据。每条 `EC-##` 包含维度、边界或组合、触发条件、预期关注点、来源、证据状态、影响/优先级、验证建议和未决问题。至少考虑数值/长度、空值/类型、时间/时区、状态转换、容量/资源、并发/顺序、平台/本地化和组合边界；不把想象的阈值写成事实。

### `negative-scenario-discovery`

输入功能目标、权限/角色、输入约束、依赖和失败契约、幂等/事务规则、历史故障和恢复设计。每条 `NS-##` 包含失败模式、触发刺激、前置条件、预期拒绝/降级/重试/人工接管行为、用户/调用方可见结果、数据一致性影响、证据需求和验证方法。明确区分 invalid input、unauthorized、dependency failure、timeout、retry exhaustion、duplicate request、partial failure 和 unsafe recovery；不执行故障注入或发明错误码。

### `test-data-requirement-analysis`

输入需求/场景、字段 schema、关系与约束、角色/权限、状态、隐私/合规、数据来源、环境、生命周期和清理限制。每条 `TDR-##` 包含场景/测试目标、所需实体和字段、有效/无效/边界/组合条件、关联完整性、状态和角色前置、来源/构造约束、脱敏要求、初始化/清理、阻塞项、责任角色和验证方法。它只分析准备条件和缺口，不生成记录、不调用真实数据源、不承诺数据已经存在。

## 数据流、Eval 和治理交付

统一数据流为：输入材料 → 输入审计 → 结构化发现 → 证据/优先级 → 测试意图或准备行动 → Human 待决问题。每个包至少有一条成功、一条信息不足、一条范围/风险边界 Eval，并覆盖四种本地触发模式。真实模型质量保持 `NOT_SCORED`，模型 Eval 保持 `NOT_RUN`，本地 dry-run 只证明配置可加载。

实现顺序必须是：先写本批合同测试并观察 RED；确认 RED 后，将五张精确 Project 卡片从 `Todo` 移到 `In Progress`；随后每个 Skill 独立完成 RED → 最小 GREEN → REFACTOR；最后更新 registry、Capability Match Register、双语 README/Catalog/Graph 和生成视图。其他 Project 卡片不变。

## 非目标

- 不创建 `test-gap-analysis` 的追踪矩阵替代品，不改变 `requirement-traceability-analysis` 的 `RT-##`/`TC-##` 语义。
- 不把 `risk-based-testing` 变成完整 `test-strategy`、`quality-risk-analysis` 或 `regression-test-selection` 的别名。
- 不把边界/负向发现变成完整用例生成、执行或故障注入。
- 不把数据需求分析变成 `test-data-generation` 的数据集生成器。
- 不提交、不 push、不发布版本；保留现有工作区未提交改动。
