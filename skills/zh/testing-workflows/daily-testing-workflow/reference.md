# 日常测试工作流 — 阶段交接对照

编排主提示词：`prompts/daily-testing-workflow.md`（阶段目标、门禁、交接）。  
各步骤深做时交接给对应**类型 skill**（只点名 skill 名，禁止相对路径链到其他 skill 内部文件）。

| 步骤 | 交接 skill | 用途 |
|------|------------|------|
| 早晨审查测试计划 | `requirements-analysis`, `test-strategy` | 审查当日故事与高风险区域 |
| 设置测试环境 | `automation-testing`, `test-strategy` | 流水线与测试数据 |
| 测试用例创建 | `test-case-writing`, `requirements-analysis`, `functional-testing` | 新功能/缺陷修复用例 |
| 测试自动化 | `automation-testing`, `api-testing`, `ai-assisted-testing` | 编写与维护自动化 |
| 探索性测试 | `manual-testing` | 章程与探索会话 |
| 缺陷上报 | `bug-reporting` | 缺陷报告 |
| 可视化 / E2E | `accessibility-testing`, `functional-testing` | 视觉与端到端 |
| 下午审查 | `test-reporting`, `test-strategy` | 覆盖率与质量指标 |
