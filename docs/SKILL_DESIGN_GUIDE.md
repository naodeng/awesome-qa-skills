<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_DESIGN_GUIDE_EN.md">🇬🇧 English</a></div>

# Skill 设计指南

每个 New 或 Enhance 交付先声明质量问题、Scope、Non-goals、输入、输出、决策逻辑、证据边界与 Human Decision 边界。Skill 必须可独立复制安装；中英文目录同名，包含 `SKILL.md`、主 Prompt、`agents/openai.yaml` 和成功/信息不足/风险边界 Eval。

不要因工具不同复制方法论：方法论、分析和 Tool Adapter 分层；跨能力编排优先使用 Workflow。信息不足时输出最小可执行方案与待确认项，不得补造需求、执行事实、阈值或根因。
