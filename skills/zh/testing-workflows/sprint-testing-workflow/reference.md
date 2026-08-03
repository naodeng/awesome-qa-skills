# 迭代测试工作流 — 阶段交接对照

编排主提示词：`prompts/sprint-testing-workflow.md`（阶段目标、门禁、DoD、交接）。  
各步骤深做时交接给对应**类型 skill**（只点名 skill 名，禁止相对路径链到其他 skill 内部文件）。

| 步骤/阶段 | 交接 skill | 用途 |
|-----------|------------|------|
| 第 1 天·规划 | `test-strategy`, `requirements-analysis` | 策略、范围、风险、测试数据 |
| 第 2–3 天·设置 | `automation-testing`, `test-strategy`, `test-case-writing` | 环境、CI/CD、早期用例 |
| 第 4–8 天·执行 | `manual-testing`, `bug-reporting`, `automation-testing`, `api-testing` | 探索、缺陷、自动化、API |
| 第 9–10 天·密集测试 | `functional-testing`, `ai-assisted-testing`, `api-testing`, `accessibility-testing` | 回归、E2E、智能选择、视觉 |
| 第 11 天·稳定化 | `manual-testing` | 探索性缺陷突击 |
| 第 12 天·评审 | `test-reporting`, `test-strategy` | 摘要、指标、仪表板 |
