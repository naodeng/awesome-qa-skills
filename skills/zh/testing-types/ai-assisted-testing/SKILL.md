---
name: ai-assisted-testing
description: Use this skill when you want AI to draft, analyze, review, or prioritize ordinary QA work under human verification; triggers include AI 辅助测试, AI-assisted testing, and AI for QA.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "2.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# AI 辅助测试（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 用 AI 协助需求分析、测试设计、数据准备、脚本草拟、缺陷归纳或测试报告。
- 需要区分 AI 草稿、人工采纳和真实执行证据，并记录投入与质量结果。
- 验证 AI 产品本身时，应改用对应 AI Native QA 技能。

## 执行流程

1. 阅读 `prompts/ai-assisted-testing.md`，识别任务、范围、风险、允许的数据用途和交付物。
2. 按分派矩阵说明 AI 可起草的部分、必须由人判断的部分及所需证据。
3. 为每项 AI 产物记录来源快照、模型与指令版本、草稿、复核、采纳和执行证据；缺失项标记 `UNKNOWN`。
4. 用同范围、复杂度和时间窗比较人工基线与 AI 全流程投入，分开报告缺陷、返工和假绿。
5. 未经人工复核的产物保持 `DRAFT`；未经真实执行的结果保持 `NOT_RUN` 或 `BLOCKED`。

## 核心约束

- 人工必须确认业务 oracle、断言有效性、隐私、高风险取舍和发布接受；AI 不代替这些决定。
- 涉及发布批准时报告 `release_gate_status` 和 `human_release_decision`；人工接受证据前，人工决定保持 `PENDING`，门禁不得为 `PASS`。涉及提效结论时报告 `productivity_claim_status`。
- `review_decision` 仅用 `ACCEPTED`、`DRAFT`、`REJECTED`；执行状态仅用 `PASS`、`FAIL`、`BLOCKED`、`NOT_RUN`、`UNKNOWN`、`STALE`。
- 缺 `model_version` 或 `run_id` 时，AI 效果结论为 `UNKNOWN`；缺执行证据时不得写通过。
- 不得删除或削弱失败检查来制造全绿，不得把覆盖率或生成速度当作缺陷检出或提效证据。
- 不编造接口、字段、测试结果、token 成本或人工基线；有版本冲突时列为缺口。

## 按需加载

- 产出前必须遵循 `prompts/ai-assisted-testing.md` 的分派、来源链、输出合同和人工门禁。
- 需要按产物和阶段分工时，读取 [references/ai-delegation-matrix.md](references/ai-delegation-matrix.md)。
- 评估假绿、虚假提效或未经复核的采纳时，读取 [references/false-confidence-catalog.md](references/false-confidence-catalog.md)。
- 校准逐项判定和成本计算时，读取 [references/domain-decision-example.md](references/domain-decision-example.md)。
- 需要对照已有项目样例时，读取 `examples/` 中相关内容；只读与当前任务匹配的文件。
- 用户要求 Excel、CSV、JSON、Word 等格式时，读取 `output-formats.md`；格式转换脚本和模板仍是可选工具。
- 需要格式转换或辅助检查时，使用 `scripts/` 中现有工具；用户只要最短上手路径时，读取 `quick-start.md`。
- 评测本 Skill 时使用 `evals/`；行为评测需要模型或凭据时，未授权前标记 `NOT_RUN`。

## 交付前自检

- [ ] 已区分事实、假设、缺口与建议
- [ ] AI 草稿有 `AIA-##` 编号、来源链和复核状态
- [ ] 人工门禁与真实执行证据已明确
- [ ] 成本覆盖基线、生成、复核、返工、验收和 token 费用口径
- [ ] 未把草稿、静态分析或覆盖率说成已执行或已验收

## 常见误区

- 只报生成耗时便宣称提效。
- 未审断言就把全绿当成质量证据。
- 未复核的草稿标记为已采纳。
- 用 AI 摘要代替原始执行记录或来源证据。
