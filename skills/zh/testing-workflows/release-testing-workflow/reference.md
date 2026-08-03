# 发布测试工作流 — 阶段交接对照

编排主提示词：`prompts/release-testing-workflow.md`（T 窗口、发布门禁、Go/No-Go、交接）。  
各步骤深做时交接给对应**类型 skill**（只点名 skill 名，禁止相对路径链到其他 skill 内部文件）。

| 步骤/阶段 | 交接 skill | 用途 |
|-----------|------------|------|
| T-14 发布规划 | `test-strategy`, `requirements-analysis` | 发布计划、风险、测试数据 |
| T-10～T-8 准备 | `automation-testing`, `test-strategy` | 环境、CI/CD、回归套件、数据 |
| T-7 功能冻结 | `test-case-writing`, `functional-testing`, `ai-assisted-testing` | 功能用例、回归、智能选择、E2E |
| T-5～T-4 专项 | `performance-testing`, `security-testing`, `accessibility-testing` | 性能/安全/可访问性/视觉 |
| T-3 候选版本 | `manual-testing` | 最终回归、探索性 |
| T-2、T-1 | `test-reporting` | 质量评估、Go/No-Go、回顾 |
