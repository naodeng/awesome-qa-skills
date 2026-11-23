<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-11-23-ai-native-qa-skill-gap-review_EN.md">🇬🇧 English</a></div>

# AI Native QA 背景下的全仓 Skill 缺口评审

**评审日期：2026-11-23**
**评审时基线：** `skills/zh` 与 `skills/en` 共 171 个逻辑 Skill（342 个目录），重点检查 AI Native QA、AI for QA 与 AI 原生研发质量相关能力。
**本报告建议：** 新增 4 个 Skill、条件新增 1 个 Workflow、完善 15 项既有 Skill、修复 3 个 P0 阻塞项。此数只表示缺口评审直接建议；A–D 全量迭代合并后的实际实施范围见文末。
**证据边界：** 本报告基于静态文件检查、`grep` 统计、仓库质量门禁与单元测试结果，以及带日期的外部公开资料快照；未运行任何 AI 相关 Skill，未调用模型，不构成行为评测、业务验收或发布批准。

## 结论摘要

1. **不缺 Skill 数量，缺的是三类纵深。** Testing for AI 已形成 18 个专项，但 AI for QA 只有 2 个入口；AI 原生研发质量（AI 生成代码、Agent PR、Skill/插件供应链）基本空白；AI 协议、成本、轨迹证据三条硬边没有 Skill 承接。
2. **AI for QA 结构性偏薄。** `ai-assisted-testing` 的 Prompt 只有 64 行，领域操作仅 4 条通用句；相比之下 `prompt-testing` 有 116 行和 8 个 Eval 用例。它却是路由中 AI 辅助任务的默认出口。
3. **Testing for AI 的覆盖是“场景多、证据浅”。** 20 个 AI 相关 Prompt 中，5 个没有领域操作与判定步骤，8 个没有稳定的 `XX-##` 发现合同；评测用例多为“必须包含标题/状态码”的文本检查，不是轨迹或行为断言。
4. **工作流层没有 AI 闭环。** 唯一 AI Composition 路线 `ai-feature-validation` 止于“评测规划”，没有评测门禁、灰度、线上监控和回滚；也没有 Bugfix 验证、AI 代码验证两条已被 2026-10-16 评审提出的路线。
5. **评审时的基线工作树是红灯。** `bash scripts/check_skills_quality.sh` 在 `[3/11]` 因 `stale_governance_inventory=zh,en` 失败；`discover-testing` 的能力快照仍是 169 个，路由器单测因缺 `test-case-importer`、`test-case-retrieval` 而失败。后续实施状态见文末记录。

## 评审方法与证据边界

- 读取全部 Skill 的 frontmatter、主 Prompt、`evals/` 与可选 `references/`，统计 Prompt 行数、领域判定章节、发现合同与用例数量。
- 用 `grep` 检查 MCP、结构化输出、token 成本、TTFT、上下文压缩、模型迁移、多模态、在线评测等关键词在两个语言树中的覆盖情况。
- 运行 `bash scripts/check_skills_quality.sh` 与 `python3 -m unittest scripts.tests.test_review_standalone_helpers.StandaloneHelperTests.test_router_snapshot_is_complete_and_availability_is_unknown`，记录当前结果，不修复。
- 对照 `docs/catalog/`、`docs/governance/`、`docs/SKILL_MATCHING_REGISTER.md` 与历史评审，避免把已完成或被判 `MERGE` 的能力再当成新方向。
- 外部资料仅用于解释“为什么现在补”，不作为本仓库能力、效果或市场规模的证据；具体链接和快照日期见文末。

## 现状盘点：20 个 AI 相关 Skill

按能力域拆分为两组：D15（AI for QA）与 D16（AI / LLM / Agent 质量）。治理 registry 中 D15 只有 2 个 Skill、D16 有 18 个；这个比例本身就说明投入偏向了“测 AI”，而不是“用 AI 做 QA”和“AI 参与研发的质量控制”。

| Skill | 域 | 现有证据 | 主要缺口 |
| --- | --- | --- | --- |
| `ai-assisted-testing` | D15 | 64 行 Prompt、4 条通用领域操作、1 条 provenance、1 条 ROI | 缺分派矩阵、AI 草稿验收协议、虚假信心清单、成本核算 |
| `ai-generated-test-review` | D15 | 分层 references、7 个用例、领域执行要点 | 只覆盖测试代码，不覆盖 AI 生成的需求/方案/报告 |
| `ai-feature-testing` | D16 | 4 步领域判定、切片与 rubric | 缺流式、多模态、成本与线上闭环 |
| `llm-testing` | D16 | 通用骨架 + 覆盖清单 | 无领域判定、无 `XX-##`、与 feature/prompt/eval 边界模糊 |
| `prompt-testing` | D16 | `PRT-##`、8 个用例、回归模式 | 无领域判定；无模型/供应商迁移语义 |
| `llm-evaluation-design` | D16 | 指标/数据/评分清单 | 无数据集卫生、统计量、judge 校准细节 |
| `llm-hallucination-testing` | D16 | 领域判定 + `LHT-##` | 与 RAG grounding 的交接边界可更清晰 |
| `llm-consistency-testing` | D16 | 领域判定 + `LCT-##` | 缺模型迁移、弃用截止与影子/金丝雀 |
| `rag-quality-testing` | D16 | 领域判定 + `RAGQ-##` | 缺检索依赖变化对答案的归因 |
| `rag-retrieval-testing` | D16 | 领域判定 + `RAGT-##` | 缺 embedding/索引迁移、hybrid、reranker |
| `ai-agent-testing` | D16 | 通用骨架 + 覆盖清单 | 无 `XX-##`；缺轨迹证据模式 |
| `agent-tool-testing` | D16 | 通用骨架 + 10 项覆盖 | 无领域判定、无 MCP、无 schema 演进 |
| `agent-loop-testing` | D16 | 领域判定 + `ALT-##` | 缺与超时/预算/取消的联动 |
| `agent-memory-testing` | D16 | 领域判定 + `AMT-##` | 缺上下文装配与压缩摘要保真 |
| `agent-permission-testing` | D16 | 领域判定 + `AGP-##` | 缺 MCP 授权透传与 confused deputy |
| `agent-failure-recovery-testing` | D16 | 领域判定 + `AFR-##` | 恢复证据与事故分诊的交接可加强 |
| `agent-long-running-testing` | D16 | 领域判定 + `ALR-##` | 缺长任务成本与 token 预算 |
| `multi-agent-testing` | D16 | 领域判定 + `MAT-##` | 缺跨 Agent 轨迹合并与归因 |
| `ai-safety-testing` | D16 | 领域判定 + `AIS-##`、政策矩阵 | 无红队程序、过度拒答校准、披露流程 |
| `prompt-injection-testing` | D16 | 覆盖清单完整 | 无领域判定；缺 MCP/资源/工具描述投毒、外泄通道 |

**可以确认的强项：** 2026 年 v3-v4 批次新增的 11 个 AI 包已经具备“领域操作与判定 + `XX-##` 合同”，例如 agent 家族、RAG 两个包、幻觉与一致性测试。这说明“写深一个领域”在本仓库已被验证可行，缺的是把同一标准回补到 9 个存量 AI 包和新增能力域。

## 四类缺口

### A. AI for QA：只有一个薄入口

现状：D15 只有 `ai-assisted-testing` 与 `ai-generated-test-review`。前者覆盖“用 AI 提效”的通用建议，后者只评审 AI 生成的测试代码。缺少的是 AI 作为 QA 协作者时的运营协议。

- **分派矩阵缺失。** 没有说明需求分析、用例生成、数据准备、失败分流、报告撰写分别适合 AI 做什么、必须人工做什么。
- **AI 草稿验收缺失。** 没有“输入快照 → 模型/Prompt 版本 → 草稿 → 人工复核 → 采纳版本 → 证据”的可执行字段；现有一句 provenance 不足以支撑审计。
- **虚假信心缺失。** 没有“生成全绿但断言无效”“AI 改写测试以消除失败”“引用不存在的接口/字段”等失效模式清单。
- **成本与收益缺失。** 只有一句“测量人工基线工时”，没有 token 成本、复核工时、返工率的口径。
- **AI 生成的非测试产物缺少验收。** 需求、测试方案、缺陷单、发布说明由 AI 起草时，没有对应的评审规则。

判断：不新增“泛 AI QA”Skill，直接重写 `ai-assisted-testing` 为 v2；把“非测试产物验收”作为 `ai-generated-test-review` 的可选模式，先登记边界，再决定是否独立。

### B. Testing for AI：场景多，硬边少

已覆盖：AI 功能、LLM 行为、Prompt、评测设计、幻觉、一致性、RAG 答案与检索、8 个 Agent 专项、安全与注入。真正的空白是以下几条：

| 缺口 | 当前证据 | 为什么现在必须补 |
| --- | --- | --- |
| **MCP 协议与安全** | 两个语言树的 Skill 中 `MCP`/`Model Context Protocol` **0 命中** | MCP 2026-07-28 改为无状态协议、`server/discover`、MRTR、`subscriptions/listen`、OAuth 2.1 + `iss` 校验；工具描述/资源投毒、token passthrough、confused deputy 成为独立测试面。`agent-tool-testing` 只覆盖 Agent 侧工具选择与副作用。 |
| **结构化输出** | 所有 Skill Markdown 中 `structured output` **0 命中**，`prompt-testing` 只有“格式”一项 | JSON mode、schema 校验、非法 JSON 恢复、流式半成品、schema 演进是产品级高频失败模式；`api-schema-validation` 只覆盖 HTTP 契约。 |
| **成本与时延** | `TTFT`、`token cost`、`缓存命中` **0 命中**；`llm-testing` 只有“成本延迟”一项 | 上下文增长、重试放大、缓存读价、流式首字节直接决定 AI 功能是否可上线；通用性能 Skill 关注的是基础设施负载。 |
| **轨迹证据** | `OTel`/`GenAI` 语义约定 **0 命中**；`ai-agent-testing` 有 run/step ID 顺序核对，但不解析轨迹 | Agent 测试的结论若只看最终答案，会漏掉错误工具选择、错误顺序和无效重试；轨迹是 Agent 质量的第一手证据。 |
| **Judge 校准** | `LLM-as-judge` 仅出现在 `llm-evaluation-design` 的一行规则 | 位置/冗长/自我偏好偏差、评分者间一致性、judge 版本化决定评测结论是否可信。 |
| **模型迁移** | AI 相关 Skill 中 `弃用`/`deprecat` **0 命中** | 模型退役窗口从两周到六个月不等，未固定别名会静默漂移；迁移需要再基线、双跑、能力与成本双回归。 |
| **上下文装配** | `上下文压缩`/`compaction`/`lost in the middle` **0 命中** | Agent 的截断、压缩、排序与缓存命中失败，常表现为“看起来像模型能力问题”的缺陷。 |
| **线上 AI 质量** | 通用 `production-verification` 无 drift/在线评测/护栏拦截率 | 发布后仍需判断模型漂移、拒答率、反馈信号与成本异常。 |
| **红队** | AI 安全 Skill 中 `红队`/`red team` **0 命中** | 安全测试有计划性覆盖，但缺少攻击面组织、攻击库、披露与过度拒答校准。 |
| **多模态/语音** | `多模态`/`语音`/`OCR`/`vision` **0 命中** | 视觉与语音输入已进入产品，但缺少跨模态一致性与语音质量验收。 |

判断：不要新增“大而全的 LLM 测试”。按“协议 / 证据 / 成本 / 迁移 / 线上”五个方向补，其中只有 MCP 与结构化输出值得独立成包，其余优先做既有 Skill 的模式。

### C. AI 原生研发质量：只覆盖了“测试”，没覆盖“代码与资产”

- `ai-generated-test-review` 已经能问“测试被破坏后是否仍然通过”，但没有 Skill 问“Agent 写的生产代码是否可信”。
- `code-review` 的覆盖清单是通用代码风险（逻辑、并发、资损、契约），没有“虚构依赖/API、静默兜底、超宽 diff、只在测试上改绿、生成来源”这些 AI 代码高发问题。
- 没有 Agent PR 的评审约定：意图/范围/证据/归属、CI 完整性 diff、未受信输入进入工作流。
- 没有第三方 Skill / 插件 / MCP Server 的供应链审查：不可信指令、捆绑脚本、工具权限、数据外泄、版本与来源。
- AI 参与需求/方案撰写后，`requirement-quality-review` 没有“AI 生成 spec”模式（虚构范围、缺失约束、不可验收表述）。
- `quality-productivity-metrics` 与 `automation-roi-analysis` 没有 AI 成本分母（token、复核工时、返工率、假绿率）。

判断：新增 `ai-generated-code-review` 与 `skill-security-review` 两个包；其余通过既有 Skill 的模式与字段补齐，不拆目录。

### D. 工作流与路由：没有 AI 闭环，而且当前红灯

- **没有 AI 原生工作流。** 14 个工作流里没有“AI 功能从评测设计到发布门禁与线上监控”的路线；`ai-feature-validation` 只把用户送到 `ai-feature-testing` + `llm-testing`，止于评测规划。
- **缺少验证路线。** 2026-10-16 评审已提出 `bugfix-verification` 与 `ai-code-verification` 两条组合路由，但 `discover-testing/reference.md` 仍只有 8 条路线，二者都没有。
- **路由器对 AI 覆盖不足。** 20 个 AI Skill 中只有 5 个被路由 Prompt 点名（`ai-agent-testing`、`ai-assisted-testing`、`ai-feature-testing`、`llm-testing`、`prompt-testing`）；`llm-evaluation-design`、RAG、安全、注入、6 个 agent 专项都没有进入选择表。
- **快照过期。** `references/skill-capability-inventory.json` 仍是 169 个 ID，缺 `test-case-importer`、`test-case-retrieval`；单测失败。
- **质量标准红灯。** `bash scripts/check_skills_quality.sh` 在 Step 3 因治理清单未重新生成而退出 1。
- **报告字段不足。** `test-reporting` 与 `test-report-review` 没有模型、Prompt、数据集、judge、run ID、token 成本字段，AI 证据无法被下游复核。
- **Eval 覆盖偏文本。** AI 包的 4–8 个用例多数检查标题、状态码和“必须包含”，没有轨迹 fixture、no-skill baseline、缺证据阻断的行为断言。

## 建议新增的 Skill

只建议 4 个独立新包，另 1 个条件新增。理由统一为：现有相邻 Skill 的**输入、产物与证据模型**无法容纳该能力，而不是“名字听起来新”。

| 候选 | 优先级 | 决策 | 负责什么 | 不负责什么 |
| --- | --- | --- | --- | --- |
| `mcp-server-testing` | P0 | NEW | MCP 2026-07-28 无状态协议、`server/discover`、stdio/Streamable HTTP、MRTR、`subscriptions/listen`、OAuth 2.1 与 `iss`/audience、工具 schema 完整性、描述/资源投毒、dual-era 兼容 | 不负责 Agent 侧工具选择与副作用（`agent-tool-testing`）；不负责 HTTP API 契约（`api-contract-testing`）；不负责通用注入行为（`prompt-injection-testing`） |
| `ai-generated-code-review` | P0 | NEW | 审查 Agent 写的生产代码：意图/范围/证据/归属、CI 完整性 diff、虚构依赖/API、静默兜底、复制粘贴、缺测试、生成来源、停止规则 | 不负责 AI 写的测试（`ai-generated-test-review`）；不负责通用代码风险（`code-review`）；不代替 `pr-quality-review` 的完整 PR 流程 |
| `structured-output-testing` | P1 | NEW | JSON/schema 一致性、非法 JSON 恢复、流式部分输出、schema 演进、工具参数结构、拒绝与修复循环 | 不负责 HTTP API schema（`api-schema-validation`）；不负责 Prompt 行为回归（`prompt-testing`） |
| `skill-security-review` | P1 | NEW（`skill-engineering`） | 第三方 Skill/插件/MCP 供应链：不可信指令、捆绑脚本执行、工具权限、数据外泄、来源与完整性、安装期风险 | 不负责自有包的契约完整性（`skill-quality-review`）；不负责产品运行时安全（`ai-safety-testing`） |
| `ai-feature-release-workflow` | P2 | 条件 NEW（先定阶段契约） | AI 特性的 eval 资产链（数据集/judge/eval run）→ 门禁 → 灰度/影子 → 线上监控 → 回滚，输出可复核证据包 | 不重写 `release-testing-workflow` 的通用发布门禁；不实现评测引擎或 CI Runner |

### 为什么是这 4 个

- **MCP 是唯一“全仓 0 命中且已成为集成面”的协议。** 2026-07-28 规范把会话、初始化握手和订阅模型全部改掉，旧的“工具调用契约”无法覆盖版本协商、传输、授权与投毒。`agent-tool-testing` 的 10 项覆盖清单里没有任何一项是协议级。
- **AI 生成代码与 AI 生成测试的风险不同。** 现有 `code-review` 不检查依赖真实性与生成来源；`ai-generated-test-review` 明确只审测试。两者之间的“实现是否真的满足验收条件、是否在 CI 上作弊”无人负责。
- **结构化输出是高频失败面，而非 Prompt 细节。** 产品级 JSON mode、函数调用参数、流式半成品和 schema 演进都有自己的失败模式；把它塞进 `prompt-testing` 会让回归模式与结构校验混在一起。
- **Skill/插件/MCP 供应链是 AI 原生研发的新攻击面。** 本仓库自己分发可执行指令，CI 也已有插件扫描动作；但 `skill-engineering` 只有质量、评测、文案、变更验证，没有任何安全审查。
- **工作流只在能定义阶段交接时才新增。** 既往 `ai-native-quality-workflow` 曾因“未给出端到端阶段/输入输出契约”被判 `MERGE`；这次先要求写出阶段、产物、退出状态和证据清单，再决定是否建目录。

## 建议完善的 Skill（不新增目录）

| 目标 | 优先级 | 改动 | 验收 |
| --- | --- | --- | --- |
| `discover-testing` | P0 | 重新生成 169→171 能力快照；增加 AI 子领域路由表（eval 设计 vs LLM 行为 vs Prompt vs RAG vs Agent 家族）；新增 `bugfix-verification`、`ai-code-verification`、`ai-eval-gate` 三条路线 | 单测通过；AI 专项命中率可核对；路线只给主+辅各一个 |
| `ai-assisted-testing` | P0 | 重写为 v2：分派矩阵（按产物类型）、AI 草稿验收协议、provenance 字段、虚假信心与假绿清单、token/复核/返工成本口径、人工门禁 | 覆盖三类 Eval：完整输入、信息不足、越权/高风险；Prompt 不再只有通用 4 条 |
| `test-reporting` + `test-report-review` | P0 | 增加 AI 证据字段：模型/Prompt/数据集/judge 版本、run ID、token 成本、评测者身份、执行状态 | 报告评审能定位版本不一致与未执行证据 |
| `agent-tool-testing` | P1 | 补领域判定与 `ATT-##`；MCP 交接、schema 演进、工具描述投毒、幂等键、副作用分级 | 与 `mcp-server-testing` 边界清晰，无重复覆盖 |
| `prompt-injection-testing` | P1 | 补领域判定；间接注入扩展至 RAG、工具描述、MCP 资源、UI 内容；外泄通道、防御纵深、多轮持久化 | 覆盖清单每一项都有可观察断言与证据要求 |
| `llm-evaluation-design` | P1 | 补数据集卫生（污染/泄漏/标注）、样本量与置信、judge 校准交接、CI 门槛、领域判定 | 能输出可执行的评测协议，而不是指标清单 |
| `llm-testing` | P1 | 明确与 feature/prompt/eval 的边界；补领域判定、采样与预算、轨迹与成本 | 不再作为“什么都管”的模糊入口 |
| `ai-safety-testing` | P1 | 增加红队程序模式：攻击面组织、攻击库、过度拒答校准、披露与升级 | 安全结论区分“无已知失败”与“已通过” |
| `ai-agent-testing` | P1 | 增加轨迹证据模式：span 模型、步级归因、pass^k、失败定位；与 `distributed-trace-analysis` 交接 | 无轨迹证据时不得声称行为已验证 |
| `quality-gate-design` | P1 | 增加 AI eval 门禁模式：样本量/置信、flake 预算、judge 版本、成本预算、证据来源 | 门禁能阻断“绿但证据不足” |
| `release-testing-workflow` | P1 | 增加 AI 特性门禁交接：eval 回归、护栏、灰度/影子、回滚、线上指标 | 不在通用发布流程里硬编码 AI 细节 |
| AI 包 `evals/` | P1 | 增加轨迹 fixture、no-skill baseline、缺证据阻断、跨语言对照；减少纯标题断言 | 至少一个用例能在“证据缺失”时拒绝给通过 |
| `llm-consistency-testing` | P2 | 增加模型/供应商迁移模式：再基线、弃用截止、双跑、能力+成本回归 | 迁移结论必须绑定两个版本 |
| `production-verification` | P2 | 增加 AI 线上质量模式：在线 eval、漂移、护栏拦截率、拒答/反馈、成本异常 | 不把一次性发布验证写成持续监控 |
| `rag-retrieval-testing` | P2 | 增加 embedding/索引迁移、hybrid、reranker、重建与新鲜度 | 检索变化对答案的影响可归因 |
| `test-data-generation` | P2 | 增加合成评测集、许可与 PII、污染控制 | 数据集来源与限制可追溯 |
| `ci-test-optimization` | P2 | 增加 eval 作业的成本/分片/缓存/失败重跑策略 | 不把 LLM 调用当普通单测 |
| `code-review` + `pr-quality-review` | P2 | 增加 Agent PR 信号：范围漂移、CI 完整性、依赖真实性、未受信输入；与 `ai-generated-code-review` 交接 | 通用 PR 流程能识别“AI 生成的超宽 diff” |
| `requirement-quality-review` | P2 | 增加 AI 生成 spec 模式：虚构范围、缺失约束、不可验收表述 | 不把“写得像需求”当可测试 |
| `quality-productivity-metrics` + `automation-roi-analysis` | P2 | 增加 AI 成本分母与假绿/返工指标 | 不用生成速度代替交付收益 |

## 明确不建议新增或延后

- **不新增“AI 测试总览”**：`llm-testing` 已是总入口，再建会制造第二套路由。
- **不把 `prompt-regression` 拆成新目录**：现行 `prompt-testing` 模式已经承载基线、候选、数据集身份和 `PRT-##`。
- **不重造 Eval Engine / Runner / 排行榜**：仓库已明确 `skill-up` 为唯一通用评测引擎；promptfoo/DeepEval 只适合以后做薄适配，且要保留原始报告与成本边界。
- **不现在新增多模态 Skill**：语音/视觉验收尚无统一一致性标准（ITU-T P.808 只覆盖语音质量，多模态 Agent 仍在演进）。触发条件：目标产品确有图像/语音输入，且有可复核的验收样本。
- **不新增上下文工程独立包**：先并入 `agent-memory-testing` 与 `prompt-testing`；当“装配/压缩/缓存”出现独立产物与证据模型时再拆。
- **不新增 Prompt 发布管理包**：并入 `prompt-testing` 的版本回归与 `quality-gate-design` 的 AI 门禁模式。
- **不新增 AI 质量视角角色**：`multi-role-quality-synthesis` 与现有五视角已能承载；AI 问题优先由专项 Skill 提出，避免角色层膨胀。
- **不新增插件专属 Skill**（如质量工作台看板/雷达操作）：Host 行为不属于 leaf Skill；可复用本仓库的证据状态字段，但不把插件路径写进 Skill。

## 迭代路线与验收

### 迭代 A（P0，1 个短迭代）：先清红灯，再补 AI for QA 主干

1. 重新生成治理清单与 `skill-capability-inventory.json`，修复路由器单测与质量门禁。
2. 升级 `discover-testing`：AI 子领域路由表 + `bugfix-verification` / `ai-code-verification` / `ai-eval-gate` 三条路线。
3. 重写 `ai-assisted-testing` v2，并在 `test-reporting` / `test-report-review` 落 AI 证据字段。
4. 同步 README、索引、Composition、注册表与路线图计数（当前 README/索引 171，路线图仍 169/338）。

**验收：** `bash scripts/check_skills_quality.sh` 退出 0；路由器单测通过；三条路线各有一个正向与一个“信息不足不通过”用例。

### 迭代 B（P1，1–2 个迭代）：协议与生成代码

1. 新增 `mcp-server-testing`、`ai-generated-code-review`（双语、`agents/openai.yaml`、`evals/` 三类用例、索引与 README 标记）。
2. 升级 `agent-tool-testing`、`prompt-injection-testing`、`llm-evaluation-design`、`llm-testing`。
3. 为 AI 包补轨迹 fixture 与“缺证据阻断”用例。

**验收：** 两个新包可独立复制安装；MCP 用例覆盖版本协商、传输、授权、投毒、dual-era；AI 代码评审用例至少包含一个“测试全绿但实现错误”的样例。

### 迭代 C（P1/P2，1–2 个迭代）：评测可信与发布闭环

1. 新增 `structured-output-testing`、`skill-security-review`。
2. 升级 `quality-gate-design`、`release-testing-workflow`、`ai-safety-testing`、`ai-agent-testing`、`llm-consistency-testing`、`production-verification`。
3. 视契约成熟度决定 `ai-feature-release-workflow` 是否建包；未成熟则先扩 `ai-feature-validation` 路线。

**验收：** 评测门禁能区分“通过”“证据不足”“未执行”；迁移模式绑定两个版本；供应链审查有威胁模型与阻断规则。

### 迭代 D（P2/观察）：数据、CI、多模态与指标

`rag-retrieval-testing`、`test-data-generation`、`ci-test-optimization`、`code-review`/`pr-quality-review`、`requirement-quality-review`、`quality-productivity-metrics` 按真实项目反馈排期；多模态保持观察，达到触发条件再立项。

## 与质量工作台等 Host 的关系

- 本仓库的 Skill 应保持 Host 无关；质量工作台、Codex、Claude Code、Cursor 只是调用方。
- 工作台已有的看板、门禁与项目会话可以直接消费本仓库的状态词（`PASS`/`FAIL`/`BLOCKED`/`NOT_RUN`/`UNKNOWN`/`STALE`）与证据包字段；但不要把工作台路径、项目 ID、数据库结构写入 leaf Skill。
- 若需要自动串阶段，优先做 Host 侧适配器或一条可复制的 workflow recipe，而不是把多步编排塞进 `discover-testing` 的“一次只选一个主 Skill”契约。
- 项目级 AI 会话适合为每个 Skill 提供稳定的工作目录与证据落盘位置；这属于 Host 责任，不是 Skill 的安装依赖。

## 外部观察（2026-11-23 快照）

以下仅用于说明“为什么是现在”，不代表本仓库已验证这些结论：

- **MCP 2026-07-28** 移除协议级会话与 `initialize` 握手，新增 `server/discover`、MRTR、`subscriptions/listen`，并弃用 sampling/roots/logging/DCR；测试面因此从“工具参数”扩展到协议、传输、授权与兼容代际。[MCP changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- **MCP 安全最佳实践**明确 token passthrough、confused deputy、SSRF 与 state-handle 绑定等风险，适合转成可执行用例。[MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- **OpenTelemetry GenAI 语义约定**仍在 Development 且已迁出核心仓库；Agent、工具、`load_skill` 等 span 可作为可选证据层，但需固定版本并默认关闭内容采集。[semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
- **LLM-as-judge 不能默认可信**：MT-Bench 报告与人类偏好约 80% 一致，同时指出位置、冗长、自我增强偏差；JudgeBench 显示在客观难题上强模型 judge 可能仅略优于随机。校准应看评分者间一致性与偏差探测，而不是单次分数。[MT-Bench](https://arxiv.org/abs/2306.05685) · [JudgeBench](https://arxiv.org/abs/2410.12784)
- **模型退役是常态**：官方通知窗口从数周到数月不等，未固定的别名会静默漂移；迁移前需要在两个模型上跑代表性请求并比较输出、时延与成本。[OpenAI deprecations](https://developers.openai.com/api/docs/deprecations) · [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **AI 生成代码有可量化的特定风险**：Copilot 早期研究显示约 40% 的安全相关生成片段存在漏洞；使用助手的人更容易高估自己代码的安全性；生成包名约 19.7% 为虚构，带来“slopsquatting”。[Pearce et al.](https://cacm.acm.org/research-highlights/asleep-at-the-keyboard-assessing-the-security-of-github-copilots-code-contributions/) · [Perry et al.](https://arxiv.org/abs/2211.03622) · [USENIX 2025](https://par.nsf.gov/biblio/10686032/media/xml)
- **Agent PR 评审已形成具体检查项**：CI 作弊（删除/跳过测试、降低覆盖）、代码复用盲区、“幻觉正确性”、工作流中的未受信输入，以及“超过 5 个无关文件就要求拆小”的停止规则。[GitHub Blog](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)
- **Agent 评测从最终答案转向轨迹**：LangSmith 区分最终响应、轨迹、单步；DeepEval 提供轨迹指标；τ-bench 用 `pass^k` 暴露“能力够但稳定性不足”。[LangSmith](https://docs.langchain.com/langsmith/evaluate-complex-agent) · [DeepEval](https://deepeval.com/docs/metrics-introduction) · [τ-bench](https://arxiv.org/abs/2406.12045)
- **语音/多模态仍缺统一验收标准**：ITU-T P.808 覆盖众包语音质量，语音 Agent 指标仍在演进；这支持“观察、不急于独立成包”。[ITU-T P.808](https://www.itu.int/rec/T-REC-P.808-202106-I/en)

## 主要来源

- 仓库内：[README](../../README.md)、[Skills 索引](../catalog/skills-index.md)、[演进路线图](../governance/QA_SKILLS_EVOLUTION_ROADMAP.md)、[治理路线图](../governance/SKILL_GOVERNANCE_ROADMAP.md)、[匹配登记表](../SKILL_MATCHING_REGISTER.md)
- 历史评审：[AI Native QA 扩展空间（2026-10-16）](./2026-10-16-ai-native-qa-development-landscape.md)、[GitHub 相邻项目调研（2026-10-25）](./2026-10-25-github-qa-skills-iteration-research.md)
- 关键文件：[`ai-assisted-testing`](../../skills/zh/testing-types/ai-assisted-testing/)、[`agent-tool-testing`](../../skills/zh/testing-types/agent-tool-testing/)、[`llm-evaluation-design`](../../skills/zh/testing-types/llm-evaluation-design/)、[`discover-testing` 路由参考](../../skills/zh/testing-workflows/discover-testing/reference.md)、[质量门禁脚本](../../scripts/check_skills_quality.sh)
- 外部链接见上一节；所有外部内容均为 2026-11-23 的公开快照，未独立复测。

## 迭代 A（P0）实施状态快照（2026-11-23）

以下状态是迭代 A 单独验收时的历史快照；当时的 171 项路由快照和 171 个 Skill CLI 发现数，不代表随后完成 B–D 后的当前目录总数。它记录仓库内改动与检查，不代表 Skill 行为评测、业务验收或发布批准。

| 项目 | 状态 | 证据 / 未完成项 |
| --- | --- | --- |
| A1 质量门禁与路由快照 | **完成** | `check_skills_quality.sh` 最终 PASS（414 项测试）；双语路由快照为 171 项，生成清单/矩阵已更新。 |
| A2 路由与 AI 子领域 | **执行计划范围内完成** | 新增 `bugfix-verification`、`ai-eval-gate` 两条路线；Prompt 覆盖 20 个 AI Skill，4 个双语路由 Eval；Composition 为 10 条路线、16 个目标 Skill。缺口评审提出的 `ai-code-verification` 本轮未实现，保留为后续项。 |
| A3 `ai-assisted-testing` v2 | **完成** | 中英版本 2.0.0；分派矩阵、来源链、假信心清单、成本字段、人工门禁和 6 个 Eval 用例/语言均已补齐。 |
| A4 AI 报告证据字段 | **完成** | `test-reporting`、`test-report-review` 中英版本 1.1.0；评审增加 AI 版本/run 一致性第 8 项；每个 Skill 新增 1 个双语 Eval。 |
| 最终只读复核 | **完成** | 补强双语 Eval：假全绿要求 `release_gate_status: BLOCKED` / `human_release_decision: PENDING`；缺基线提效要求 `productivity_claim_status: UNSUPPORTED`；bugfix 路由要求 `verification_state: NOT_RUN`。这些是字面字段断言，不能识别换字段或自然语言中的矛盾表述；对应 Prompt 已将字段规定为唯一结论来源。 |
| AI 行为评测 | **NOT_RUN** | 未运行真实模型评测；本轮无模型调用、凭据使用或费用。静态 Eval YAML 校验不是行为评测。 |
| 提交与发布 | **未执行** | 未创建提交或推送；等待后续授权。 |

迭代 A 快照验证：`bash scripts/check_skills_quality.sh` PASS（414 tests）；`SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh` PASS（当时 `skills@1.7.0` 从本地目录发现 171 个 Skill，并完成 English `functional-testing` 隔离安装 smoke）；`bash scripts/validate_skill_evals.sh` PASS（当时 352 OK / 0 fail）；双语文档检查 PASS（0 findings）。

## 全部迭代的范围复核（2026-11-23）

本节把该缺口评审与用户给出的 A–D 迭代范围合并计数；它覆盖报告上方的建议项和 20 个 AI Skill 的 Eval 要求，避免把同一个 Skill 重复计算。

- **新增 4 个独立 Skill：** `mcp-server-testing`、`ai-generated-code-review`、`structured-output-testing`、`skill-security-review`。另有 **1 个条件 Workflow：** `ai-feature-release-workflow`；阶段输入/输出、退出状态与证据交接契约已经定义，因此本轮纳入创建。
- **改动 33 个既有逻辑 Skill：** 迭代 B–D 明列 18 个；迭代 A 的 4 个条目包括 `discover-testing`、`ai-assisted-testing`、`test-reporting`、`test-report-review`；再加 20 个 AI Skill Eval 中尚未被前述目标覆盖的 11 个。20 个 AI Skill 的评测要求已并入此数，不能再额外加 20。
- 以上“逻辑 Skill”按 canonical name 计数：33 个既有包对应 66 个语言目录；新增 4 个独立 Skill 和 1 个 Workflow，对应 10 个语言目录。合计影响 38 个 canonical package、76 个双语目录。
- `ai-code-verification` 是 `discover-testing` 的路线，不新增 Skill。多模态继续观察；达到目标产品确有图像/语音输入且具备可复核验收样本的触发条件后再立项。
- 完成目录同步后，仓库应为每种语言 176 个 Skill（15 个 Workflow、155 个测试类型、6 个 Skill Engineering），中英双语合计 352 个目录。

### A–D 计划最终收口（2026-11-23）

- **范围已落地：** 4 个新增独立 Skill、1 个条件 Workflow、33 个既有逻辑 Skill；共 38 个 canonical package / 76 个双语目录。Iteration A 的 `ai-code-verification` 路线、`ai-eval-gate` 与报告证据项均已实现；Iteration B/C 的协议、生成代码、结构化输出、安全、Eval 门禁、发布闭环和迁移项均已实现。Iteration D 列出的 RAG、测试数据、CI、代码评审、需求评审、生产力指标与 ROI 项均已纳入对应 Skill。
- **评测资产补齐：** 为 B/C 与 20 个 AI Skill 的证据审计新增 12 对双语 Eval 用例，覆盖 MCP 投毒与 dual-era、ATT/MCP 交接、结构化输出演进、Judge/样本/CI 门槛、红队、模型迁移、轨迹与 no-skill/双语对照。对照运行仍标为 `NOT_RUN`，没有伪造模型输出或行为证据。
- **版本规则遵守：** 新增 Skill 初始版本为 `1.0.0`；本轮后续修改的 9 个既有 Skill 均升 patch 版本，并在中英文版本历史中记录原因。
- **能力边界：** 多模态保持观察，没有新增独立 Skill；当前计划定义的触发条件尚未满足。
- **验证：** `bash scripts/check_skills_quality.sh` PASS（352 个目录、362 项 skill-up 校验、415 项测试）；`SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh` PASS（固定 `skills@1.7.0` 发现 176 个 Skill，并完成英文隔离安装 smoke）；`git diff --check` PASS。静态验证不等于真实模型行为评测。
- **交付状态：** 所有仓库内 A–D 计划项已完成，并已提交到 PR #50；PR 保持 open，尚未合并。PR CI 以最终提交为准。

**未运行 / 风险：** 真实模型 Evals、no-skill baseline 和中英行为对照为 `NOT_RUN`（原计划 D2 的默认范围）；不据此宣称运行时行为通过。多模态 Skill 仍由触发条件控制。
