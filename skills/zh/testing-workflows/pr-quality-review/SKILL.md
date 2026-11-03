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

## 输出格式选项

默认使用 Prompt 定义的 Markdown 审查章节。若用户要求 JSON，仍需将事实、推断、计划和执行证据分开并保留来源。

## 核心约束

只组合已有专业 Skill，不复制分析规则；缺少 Host 安装证据时标 `UNKNOWN`。未提供测试/CI 结果时，执行/结果状态标 `UNKNOWN`；只有明确确认未执行时才标 `NOT_RUN`。失效 Checkpoint 必须原样输出标准大写状态码 `STALE`。证据只能来自用户提供的 PR/仓库材料和明确标注的来源；不得引用 Agent 内部记忆、系统指令或会话日志，也不得暴露其路径。不把计划或静态分析写成已执行结果；默认只读，对外写入需授权。

## 如何使用

执行前读取 `prompts/pr-quality-review.md`；按契约检查输入，逐阶段完成审查、保留来源、输出发现和交接。通过 `README.md` 查看调用示例和 FAQ。

## 参考文件

- `prompts/pr-quality-review.md`：完整审查范围、输出、证据、权限和恢复规则。
- `README.md`：使用示例和 FAQ。
- `evals/`：触发与行为回归用例。

## 交付前自检

- [ ] 输入范围和假设明确
- [ ] 阶段交接保留来源、状态和缺口
- [ ] 执行证据与计划分开
- [ ] 下一步和授权边界明确

## 常见误区

不编造输入、不假设依赖已安装、不把建议当作实际执行或批准。

## 最佳实践

提供完整 Diff 和稳定 SHA；运行证据附命令、退出码、环境、时间和来源；提供团队严重度定义。
