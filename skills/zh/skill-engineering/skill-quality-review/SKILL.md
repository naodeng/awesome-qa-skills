---
name: skill-quality-review
description: 在需要审查完整 Skill 包的架构、范围、触发、独立安装、双语一致性、Eval 准备度和证据边界时使用；触发词包括 Skill 质量审查、Skill package review、评测准备度。
---

# Skill 质量审查

## 何时使用

- 需要从 package 级别审查 Skill 的工程完整性，而不只是润色文案。
- 需要检查 `SKILL.md`、Prompt、metadata、示例、references 和 `evals/` 是否形成一致契约。
- 需要判断 Skill 是否可独立复制/安装，以及哪些结论仍缺少 runtime 证据。

## 执行流程

1. 确认 Skill、语言、目录和审查目标；没有文件时先列信息缺口。
2. 检查架构职责、范围/非目标、触发条件、输入审计、输出契约、progressive disclosure 和邻近能力边界。
3. 检查 `SKILL.md`、主 Prompt、`agents/openai.yaml`、示例/引用和 `evals/` 的路径、名称和内容是否一致。
4. 检查独立安装：只复制当前 Skill 目录时，相对资源仍可解析，且不依赖另一个 Skill 的内部文件。
5. 按阻塞问题、重要建议、信息缺口、证据边界输出结果；把静态结论与 runtime/model 结论分开。

## 核心约束

- 这是静态 package review，不执行目标业务，不替用户修改 Skill。
- 不能用目录完整、`skill-up validate`、CLI install smoke 或 Project 状态声称 runtime 行为、模型效果、业务验收、Quality Score 或发布批准。
- 不凭空补充环境、依赖、指标、触发结果或执行事实；缺少证据时使用 `UNASSESSED`、`NOT_RUN`、`BLOCKED` 或 `INSUFFICIENT_EVIDENCE`。
- 不新增第二套 Eval Engine、Judge、Benchmark 或 Quality Score。

## 按需加载

- 产出前阅读 `prompts/skill-quality-review.md`，以它的输出契约为准。
- 需要判断行为时读取当前 Skill 的 `evals/`，但不要把配置验证写成 runtime 通过。
- 需要深层证据时读取仓库提供的 Evaluation Contract 和 local trace rules；若它们不在独立复制的目录中，保留证据限制，不建立硬依赖。

## 交付前自检

- [ ] 范围、文档角色和输入缺口明确
- [ ] 触发、输入、输出、约束、独立安装和 Eval readiness 已检查
- [ ] 阻塞问题、建议、未评估项和证据等级可追溯
- [ ] 没有把静态检查冒充 runtime/model 证据
