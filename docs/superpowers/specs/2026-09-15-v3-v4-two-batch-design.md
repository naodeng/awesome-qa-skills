<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-15-v3-v4-two-batch-design_EN.md">🇬🇧 English</a></div>

# v3-v4 Reliability、Security、QE 与 AI Native 两批 Skill 设计

## 状态

“APPROVED_FOR_PLAN”（2026-09-15）。聊天中的两批拆分方案已获确认，本轮复核已修正执行顺序歧义；本文可作为实施计划的规格来源。

本设计记录的是阶段启动快照：develop 在 `15c3804` 时已包含当时的 `origin/main`；本 PR 的审查基线为 `origin/main@7f981931`。本次不 push、不创建 Release，也不把路线图实现自动宣称为版本发布。

设计阶段的 Project #4（Awesome QA Skills — Governance & Roadmap）包含 42 张标题以 v3-v4 P2｜候选 Skill｜ 开头的卡片，初始状态均为 Todo。这里的“拖动卡片”指按实施门禁更新这些 Project 卡片的状态，不是增加仓库 UI。

## 目标

将 Project #4 的 42 张 v3-v4 P2 候选卡片按两个能力域批次推进：

1. Batch 1：Reliability + Security，共 17 张卡片。
2. Batch 2：Quality Engineering + AI Native，共 25 张卡片。

每张卡片先完成 Capability Match，再决定是创建新的双语物理 Skill、增强现有 Skill、合并到现有能力，还是仅登记为已有能力。卡片数量不等于物理目录数量；不得为了清空卡片而复制已有能力。

## 两批范围与卡片

### Batch 1：Reliability + Security（17）

| 分组 | Skill | Project item |
| --- | --- | --- |
| Reliability | reliability-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc5w |
| Reliability | resilience-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc68 |
| Reliability | chaos-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc8M |
| Reliability | failover-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc90 |
| Reliability | recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc_w |
| Reliability | retry-testing | PVTI_lAHOAHP1as4BjBhVzg6SdAw |
| Reliability | timeout-testing | PVTI_lAHOAHP1as4BjBhVzg6SdCU |
| Reliability | circuit-breaker-testing | PVTI_lAHOAHP1as4BjBhVzg6SdEM |
| Reliability | dependency-failure-testing | PVTI_lAHOAHP1as4BjBhVzg6SdFo |
| Reliability | disaster-recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6SdHI |
| Security | authentication-testing | PVTI_lAHOAHP1as4BjBhVzg6SdJA |
| Security | authorization-testing | PVTI_lAHOAHP1as4BjBhVzg6SdLg |
| Security | session-security-testing | PVTI_lAHOAHP1as4BjBhVzg6SdNI |
| Security | api-security-testing | PVTI_lAHOAHP1as4BjBhVzg6SdPY |
| Security | security-requirement-review | PVTI_lAHOAHP1as4BjBhVzg6SdQ0 |
| Security | threat-modeling | PVTI_lAHOAHP1as4BjBhVzg6SdSk |
| Security | secrets-exposure-review | PVTI_lAHOAHP1as4BjBhVzg6SdUg |

Reliability Skill 只分析可靠性目标、故障模式、降级/切换/恢复设计和验证准备；不注入故障、不访问依赖、不运行压测或灾备演练。Security Skill 只基于提供的需求、代码、配置、日志或策略材料提出安全测试/审查候选；不登录系统、不调用真实 API、不读取凭据，也不把静态发现写成安全通过。

### Batch 2：Quality Engineering + AI Native（25）

| 分组 | Skill | Project item |
| --- | --- | --- |
| Quality Engineering | quality-gate-design | PVTI_lAHOAHP1as4BjBhVzg6SdWc |
| Quality Engineering | quality-metrics-design | PVTI_lAHOAHP1as4BjBhVzg6SdY4 |
| Quality Engineering | quality-dashboard-design | PVTI_lAHOAHP1as4BjBhVzg6SdaY |
| Quality Engineering | quality-debt-analysis | PVTI_lAHOAHP1as4BjBhVzg6SdcE |
| Quality Engineering | quality-maturity-assessment | PVTI_lAHOAHP1as4BjBhVzg6Sddo |
| Quality Engineering | test-effectiveness-analysis | PVTI_lAHOAHP1as4BjBhVzg6SdfA |
| Quality Engineering | automation-roi-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdg8 |
| Quality Engineering | testing-bottleneck-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdig |
| Quality Engineering | regression-optimization | PVTI_lAHOAHP1as4BjBhVzg6SdkQ |
| Quality Engineering | ci-test-optimization | PVTI_lAHOAHP1as4BjBhVzg6SdnA |
| Quality Engineering | test-runtime-optimization | PVTI_lAHOAHP1as4BjBhVzg6Sdo4 |
| Quality Engineering | test-maintenance-cost-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdqc |
| Quality Engineering | quality-productivity-metrics | PVTI_lAHOAHP1as4BjBhVzg6SdsA |
| AI Native | prompt-regression-testing | PVTI_lAHOAHP1as4BjBhVzg6SdtI |
| AI Native | rag-quality-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdus |
| AI Native | rag-retrieval-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdwg |
| AI Native | agent-loop-testing | PVTI_lAHOAHP1as4BjBhVzg6SdyQ |
| AI Native | agent-memory-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdzo |
| AI Native | agent-permission-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd1E |
| AI Native | agent-failure-recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd2I |
| AI Native | agent-long-running-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd3w |
| AI Native | multi-agent-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd5g |
| AI Native | llm-hallucination-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd7Q |
| AI Native | llm-consistency-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd8Q |
| AI Native | ai-safety-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd9w |

Quality Engineering Skill 负责定义证据、指标、门禁和效率分析，不虚构数字、不替代发布审批、不进行人员排名。AI Native Skill 负责设计可复核的模型、检索、Agent 和安全验证，不调用模型、Retriever、工具或生产系统。

## Capability Match 门禁

每个候选卡按以下顺序审查，并将结论写入 registry 与 Matching Register：

1. 读取当前中英文 Skill、Prompt、Eval、治理矩阵和相邻 Workflow，建立现有能力证据。
2. 对比候选的名称、目的、主输入、输出、决策逻辑和 Workflow 角色。
3. 记录 EXISTING、ENHANCE、MERGE、MATCH 或 NEW，每个结论必须有具体文件路径和差异说明。
4. 只有结论为 NEW 时创建 skills/{zh,en}/.../<slug>/；ENHANCE 修改被选中的现有包，MERGE 合并能力并保留边界，MATCH 只更新治理/路由证据。

prompt-regression-testing 默认遵循既有四阶段路线图：作为 prompt-testing 的回归模式进行 Match/Enhance 审查，不创建别名目录。只有新证据证明现有 Skill 无法承载独立输入、输出和决策逻辑时，才允许重新评估为 NEW。

本设计不预先把所有候选标为 NEW。Batch 验收可以包含新包、增强包和 Match/Merge 记录，但每张卡都必须有独立、可追溯的交付物。

批次合同测试的目标集合在初始 Match 完成后确定。合同测试只对结论为 NEW 的物理包，以及需要改动的 ENHANCE/MERGE 目标写失败断言；EXISTING/MATCH 只写治理证据，不因没有新目录而被误判为 RED。

## Skill 包与 Prompt 合同

对每个新增或被增强的语言包：

- 保持中英目录名一致；新增包包含 SKILL.md、prompts/<slug>.md、agents/openai.yaml、evals/eval.yaml、三类 case、trigger-prompts.csv 和 local-rules.json。
- SKILL.md 包含何时使用、执行流程、核心约束、按需加载、交付前自检、常见误区和最佳实践。
- 主 Prompt 开头先记录 known、missing、conflicting、stale、out_of_scope 和 assumptions，再分离事实、证据支持的推断、候选建议与 Human 决策。
- 每条领域发现使用稳定的 <PREFIX>-## 编号，并至少记录对象/规则、来源、触发条件或适用范围、预期关注点/理由、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
- 缺少阈值、执行记录、版本关系、基线、凭据边界或业务批准时，保持 unknown、unassessed、blocked 或待确认，不从文件存在、名称或模板推导通过。
- 触发 CSV 覆盖 explicit、implicit、contextual、negative，同时提供应触发和反向控制样本；中文样本使用中文，英文包正文不夹带中文。
- Eval 环境默认是纯文本、无外部目标；三类用例至少覆盖成功路径、信息不完整和近邻/越界误用。边界用例必须拒绝“测试已执行”“全部测试通过”“发布已批准”等无证据结论。

建议使用以下稳定前缀，最终以合同测试中的唯一映射为准：

| Skill | Prefix | Skill | Prefix |
| --- | --- | --- | --- |
| reliability-testing | RLT- | resilience-testing | RES- |
| chaos-testing | CHS- | failover-testing | FOV- |
| recovery-testing | RCV- | retry-testing | RTY- |
| timeout-testing | TMO- | circuit-breaker-testing | CBR- |
| dependency-failure-testing | DPF- | disaster-recovery-testing | DRT- |
| authentication-testing | AUT- | authorization-testing | AZT- |
| session-security-testing | SST- | api-security-testing | AST- |
| security-requirement-review | SRR- | threat-modeling | THM- |
| secrets-exposure-review | SER- | quality-gate-design | QGD- |
| quality-metrics-design | QMD- | quality-dashboard-design | QDD- |
| quality-debt-analysis | QDA- | quality-maturity-assessment | QMA- |
| test-effectiveness-analysis | TEA- | automation-roi-analysis | ARO- |
| testing-bottleneck-analysis | TBA- | regression-optimization | RGO- |
| ci-test-optimization | CTO- | test-runtime-optimization | TRO- |
| test-maintenance-cost-analysis | TMC- | quality-productivity-metrics | QPM- |
| prompt-regression-testing | PRT- | rag-quality-testing | RAGQ- |
| rag-retrieval-testing | RAGT- | agent-loop-testing | ALT- |
| agent-memory-testing | AMT- | agent-permission-testing | AGP- |
| agent-failure-recovery-testing | AFR- | agent-long-running-testing | ALR- |
| multi-agent-testing | MAT- | llm-hallucination-testing | LHT- |
| llm-consistency-testing | LCT- | ai-safety-testing | AIS- |

## 卡片状态与批次流程

卡片状态是执行记录，不是运行质量、业务批准、风险接受或 Release 证据。每批执行：

1. 先完成该批次的初始 Capability Match ledger，再为实际 NEW 物理包和 ENHANCE/MERGE 目标写结构合同测试，并在内容创建前确认相应交付目标为 RED。
2. 只将该批次的精确 item ID 从 Todo 移到 In Progress；用实时 Project 字段和选项 ID，不能猜测或按标题模糊匹配。
3. 完成 Match ledger、Skill 包/增强、Eval、治理同步和目标质量门禁。
4. 重新读取 Project #4，确认只影响本批卡片；证据完整的卡片才移到 Done，其余保持真实状态并登记原因。
5. gh project item-list 只能证明当前状态，不能证明历史上确实经历过 In Progress -> Done；无法获得事件日志时，验收记录必须标记该历史证据为 UNASSESSED。

## 文档与治理同步

每批完成后按实际 Match 结果更新：

- docs/governance/skill-governance-registry.yaml
- 生成的 docs/SKILL_MATRIX.md、docs/SKILL_MATRIX_EN.md、docs/generated/
- docs/SKILL_MATCHING_REGISTER.md、docs/SKILL_MATCHING_REGISTER_EN.md
- docs/catalog/skills-index*、docs/catalog/skills-graph*
- README.md、README_EN.md、对应语言 Skill README
- 必要的 Workflow 路由和阶段说明

不新增跨 Skill 内部 Markdown 链接；推荐关系只写为名称和导航说明，保证单个目录复制后仍可安装。治理记录的 quality_score 保持 NOT_SCORED，eval_execution 保持 NOT_RUN，除非有本批之外的独立证据。

## 验收与非目标

### 验收条件

- 17 张 Batch 1 卡片和 25 张 Batch 2 卡片均有 Match 结论、交付路径、当前 Project 状态和验收证据。
- 所有 NEW 包通过中英结构、metadata、Eval、触发样本、独立性和完整性检查；所有 ENHANCE/MERGE 目标通过同等相关检查。
- 双语 Matrix、Register、Inventory、Catalog、Graph 和 README 可由当前仓库内容复现，无生成文件漂移。
- 批次合同测试、目标 Eval 配置检查、全仓单测、bash scripts/check_skills_quality.sh 和 git diff --check 通过。
- 报告区分静态结构证据、Prompt 文案证据、当前卡片状态，以及未运行的模型/外部目标/业务验证。

### 非目标

- 不创建仓库 Issue，不改变未纳入本批的 Project 卡片，不 push，不创建 Release。
- 不执行真实 API、浏览器、数据库、CI、Chaos、灾备、Retriever、LLM、Agent 或生产系统。
- 不从静态文件存在、Skill 名称、触发 dry-run 或质量门禁推导语义效果、覆盖率、漏洞不存在、质量分、Go/No-Go 或发布完成。
- 不将 v4.1 Existing Enhance Review、v4.0 Workflow、v3.4 Performance Review 或 Release DoD 卡片混入这两个 v3-v4 P2 Skill 批次。

## 计划前置决策

本文确认的实现顺序是：先写规格与实施计划；对 Batch 1 完成初始 Match 后确认实际交付目标 RED，再移动 17 张卡片；完成 Batch 1 验收；再对 Batch 2 完成初始 Match、确认 RED 并移动 25 张卡片。任何 Capability Match 发现的重复能力，都以证据为准改为增强、合并或已有能力记录，不以卡片数量为完成标准。
