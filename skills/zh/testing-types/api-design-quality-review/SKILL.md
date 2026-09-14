---
name: api-design-quality-review
description: Use this skill when an API, OpenAPI, or consumer contract needs a quality review before implementation or versioning; triggers include API 设计质量评审, API design review, and contract readiness review.
---

# API 设计质量评审

在实现前评审 API 设计、OpenAPI/契约、请求响应样例、错误模型、鉴权授权、幂等、分页、状态码、版本演进和消费者影响。输出 `API-##` 发现与验证准备，不执行 API，也不批准最终版本策略。

## 何时使用

- 需要检查 operation、输入输出、错误、权限和兼容演进是否可验证。
- 需要在多个消费者、版本或迁移方案之间发现契约缺口。
- 需要识别样例不完整、未定义边界和缺少运行证据的 API 风险。

不适用于直接发请求、压测、执行安全测试或替团队决定最终 API 版本策略。

## 工作方式

1. 阅读 `prompts/api-design-quality-review.md`，审计 API 目标、版本、消费者、范围和证据。
2. 将材料归入 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
3. 按 operation 和稳定字段建立设计覆盖矩阵，使用 `API-##` 绑定来源、证据、影响和验证方法。
4. 分离契约事实、证据推断、建议和 Human 决策；明确兼容性、鉴权和错误处理仍需什么证据。
5. 信息不完整时给出受限初版，不能把请求响应样例当成完整契约。

## 核心约束

- 不执行 API、调用外部服务或声称安全、兼容、性能测试已通过。
- 不从一个样例补造所有字段、错误、权限、限流、幂等或版本规则。
- 每条 `API-##` 至少包含 operation、来源/证据、影响、兼容风险、责任角色、待决策问题和验证方式。
- 未提供执行身份、时间、环境、输入和原始结果时，运行状态只能是 `unverified`、`unexecuted` 或 `unassessed`。

## 按需加载

- 每次产出前必须阅读 `prompts/api-design-quality-review.md`。
- 回归时读取 `evals/eval.yaml` 与用例；结构通过不等于 API 行为通过。
- 触发检查使用 `evals/trigger-prompts.csv` 和 `evals/local-rules.json`；selection trace 缺失时报告 `BLOCKED`。

## 交付前自检

- [ ] 已审计 operation、版本、消费者、范围和证据
- [ ] 已检查输入输出、错误、鉴权、幂等、分页、状态码、演进和迁移影响
- [ ] 每个 `API-##` 有最小证据、影响、责任角色和验证方式
- [ ] 已区分样例、设计声明与真实执行证据
- [ ] 没有替团队作兼容策略、风险接受或发布批准

## 常见误区

- 把一个成功响应样例当成完整 OpenAPI 契约。
- 只看状态码，不看错误体、权限、重试、幂等和消费者行为。
- 把文档版本号或工具 lint 通过当成兼容性测试通过。
