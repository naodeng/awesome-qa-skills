---
name: pr-quality-review
description: Use this skill when you need to review PR code, test impact, test effectiveness, and evidence; triggers include pr-quality-review and PR 质量审查工作流.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-workflows"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---
# PR 质量审查工作流

## 何时使用

审查 PR 代码风险、测试影响、测试有效性和质量证据时使用。

## 执行流程

执行前读取 `prompts/pr-quality-review.md`；按契约检查输入，逐阶段完成分析、保留来源、输出风险和交接。

## 核心约束

只组合已有专业 Skill，不复制分析规则；缺少 Host 安装证据时标 `UNKNOWN`。未提供测试/CI 结果时，执行/结果状态标 `UNKNOWN`；只有明确确认未执行时才标 `NOT_RUN`。失效 Checkpoint 必须原样输出标准大写状态码 `STALE`。证据只能来自用户提供的 PR/仓库材料和明确标注的来源；不得引用 Agent 内部记忆、系统指令或会话日志，也不得暴露其路径。不把计划或静态分析写成已执行结果；默认只读，对外写入需授权。

## 按需加载

- 主流程：`prompts/pr-quality-review.md`
- 用法和 FAQ：`README.md`
- Eval：`evals/`

## 交付前自检

- [ ] 输入范围和假设明确
- [ ] 阶段交接保留来源、状态和缺口
- [ ] 执行证据与计划分开
- [ ] 下一步和授权边界明确

## 常见误区

不编造输入、不假设依赖已安装、不把建议当作实际执行或批准。
