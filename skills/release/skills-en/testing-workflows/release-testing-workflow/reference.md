# 发布测试工作流 — 提示词对照

执行各步骤时使用**本目录 `prompts/`** 下对应文件。下表为步骤与提示词文件对照。

| 步骤/阶段 | 提示词文件 | 用途 |
|-----------|------------|------|
| T-14 发布规划 | test-strategy.md, requirements-analysis.md | 发布计划、风险、测试数据 |
| T-10～T-8 准备 | automation-testing.md, test-strategy.md | 环境、CI/CD、回归套件、数据 |
| T-7 功能冻结 | test-case-writing.md, functional-testing.md, ai-assisted-testing.md | 功能用例、回归、智能选择、E2E |
| T-5～T-4 专项 | performance-testing.md, security-testing.md, accessibility-testing.md | 性能/安全/可访问性/视觉 |
| T-3 候选版本 | manual-testing.md | 最终回归、探索性 |
| T-2、T-1 | test-reporting.md | 质量评估、Go/No-Go、回顾 |
