<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_VERSION_HISTORY_EN.md">🇬🇧 English</a></div>

# Skill 版本与更新记录

本记录跟踪各 Skill 包独立的 `metadata.version`，不代表仓库整体发布版本。新增 Skill 记录初始版本；修改 Skill 记录旧/新版本和本次更新摘要。

## 2026-11-23

### 新增 Skill / Workflow

| Skill | 初始版本（zh/en） | 更新说明 |
| --- | --- | --- |
| `mcp-server-testing` | `1.0.0` / `1.0.0` | 新增 MCP 协议、传输、授权、资源投毒与代际兼容测试。 |
| `ai-generated-code-review` | `1.0.0` / `1.0.0` | 新增 AI/Agent 生成代码评审，覆盖依赖真实性、CI 完整性、测试有效性与来源证据。 |
| `structured-output-testing` | `1.0.0` / `1.0.0` | 新增 JSON/Schema 演进、流式输出与结构化结果失败测试。 |
| `skill-security-review` | `1.0.0` / `1.0.0` | 新增 Skill、插件与 MCP 供应链安全审查。 |
| `ai-feature-release-workflow` | `1.0.0` / `1.0.0` | 新增从评测设计、发布门禁到灰度监控与回滚的阶段交接。 |

### 更新既有 Skill

| Skill | 版本（zh/en） | 更新说明 |
| --- | --- | --- |
| `agent-failure-recovery-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加故障轨迹与缺执行证据评测。 |
| `agent-long-running-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充长任务轨迹、检查点和缺证据检查。 |
| `agent-loop-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充循环轨迹、终止条件与预算证据评测。 |
| `agent-memory-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加记忆轨迹与缺执行证据检查。 |
| `agent-permission-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | 增加权限轨迹 fixture 和缺证据评测。 |
| `agent-tool-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | 增加 MCP/schema 交接和缺工具证据评测。 |
| `ai-agent-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 Agent 轨迹评测与缺执行证据检查。 |
| `ai-assisted-testing` | `1.0.0` → `2.0.0` / `1.0.0` → `2.0.0` | 重写 AI 辅助 QA 协议，补充分派、来源链、人工门禁、假绿和成本评测。 |
| `ai-feature-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 AI 功能轨迹 fixture 和缺运行证据评测。 |
| `ai-generated-test-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 强化生成测试的来源、断言有效性和轨迹证据审查。 |
| `ai-safety-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | 增加安全轨迹校验 fixture 与缺证据用例。 |
| `automation-roi-analysis` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充 AI token、复核、返工与质量成本口径。 |
| `ci-test-optimization` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充模型/数据集身份、分片、缓存、重试和累计成本约束。 |
| `code-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 AI 生成实现的测试影响、CI 完整性和来源证据审查。 |
| `discover-testing` | `1.3.0` → `1.4.0` / `1.3.0` → `1.4.0` | 增加 AI 代码验证、AI 发布、MCP 路由和 176 项能力快照。 |
| `llm-consistency-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加模型迁移轨迹与缺评测证据检查。 |
| `llm-evaluation-design` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充数据集卫生、统计与 judge 校准、CI 门槛及缺证据评测。 |
| `llm-hallucination-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加轨迹和无评测证据边界用例。 |
| `llm-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充采样、成本、领域边界及缺执行证据评测。 |
| `multi-agent-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加协作轨迹、归属证据和缺评测证据检查。 |
| `production-verification` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充模型版本、漂移、拒答、反馈、成本和回滚证据。 |
| `prompt-injection-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | 增加缺证据及 MCP/资源投毒安全评测。 |
| `prompt-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充 Prompt 版本回归和缺评测证据约束。 |
| `quality-gate-design` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加结构化轨迹和 `NOT_RUN`/`UNKNOWN` 评测门禁。 |
| `quality-productivity-metrics` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充 AI 调用、token、复核、返工和质量指标分母。 |
| `rag-quality-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 grounding、引用和检索轨迹证据评测。 |
| `rag-retrieval-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充索引迁移、混合检索、reranker、新鲜度与重建评测。 |
| `requirement-quality-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 AI 生成规格的证据边界和评审用例。 |
| `test-data-generation` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 补充 AI 评测集来源、许可、泄漏和污染检查。 |
| `test-report-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 AI 模型、Prompt、数据集、judge 版本与 run ID 一致性核对。 |
| `test-reporting` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 增加 AI 评测版本、运行、采样、成本和执行状态字段。 |
| `pr-quality-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | 加强 AI Agent PR 的测试影响、效果和证据边界审查。 |
| `release-testing-workflow` | `1.1.0` → `1.2.0` / `1.1.0` → `1.2.0` | 增加 AI 评测门禁向发布阶段交接的契约。 |
