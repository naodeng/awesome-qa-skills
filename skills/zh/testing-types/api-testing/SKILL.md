---
name: api-testing
description: Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API 测试 and api testing.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# API 测试（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要 API 测试方案、API 用例或 API 风险分析。
- 请求涉及 REST、GraphQL、SOAP、gRPC、WebSocket 或混合接口场景。

## 执行流程

1. 阅读并遵循「按需加载」中的主提示词（覆盖清单、输出结构、质量要求）。
2. 只补充真正影响结果的项目上下文：范围、环境、限制、风险、依赖、期望产出。
3. 信息不全时先给可用初版，并显式标出假设与信息缺口。
4. 默认 Markdown；用户指定其他格式时再切换。

## 领域执行要点

1. 按已确认协议选择分支：REST 校验 method/status/schema/幂等；GraphQL 校验 data 与 errors、null 和字段权限；gRPC 校验 status/metadata/deadline/流终止；WebSocket 校验握手、消息 ID/顺序/重连；SOAP 校验 WSDL、namespace 与 Fault。未使用协议不强行覆盖。
2. 将契约检查与跨请求业务后置条件分开：创建/更新→读回→权限视图→重复请求/下游效果；每步保留请求 ID、业务键、版本与证据。
3. 状态码正确但读回余额、状态或关联错误仍为业务失败；响应可能异步时按项目一致性窗口等待，不自定窗口。
4. 数据由隔离命名空间和唯一业务键准备，清理按依赖逆序执行并记录残留；未知授权或真实副作用限制保持 blocked。

## 核心约束

- 按风险/业务影响排优先级，不要平均摊铺。
- 把「已确认事实」和「当前假设」分开写。
- 不要编造用户未提供的接口、字段、环境或根因细节。
- 结果必须可执行：场景具体、有优先级、能指导下一步。

## 按需加载

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 产出前必须阅读并遵循 `prompts/api-testing.md`（最低覆盖清单、输出结构、质量要求）。
- 需要 Excel/CSV/JSON/Word 等格式时：读 `output-formats.md`，并按用户格式要求输出。
- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。
- 用户要示例或对标现有资产时：读 `examples/` 中相关样例。
- 需要框架规范、排障、报告 schema 等深资料时：只读 `references/` 里与当前问题相关的文件，不要整目录通读。
- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。
- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。
- 用户只要最短上手路径时：读 `quick-start.md`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 最低覆盖关注：本次纳入的接口或业务流程、优先级和风险等级、正向场景、异常场景、边界场景、鉴权和权限检查、请求与响应校验、错误处理…（细节以主提示词为准）
- [ ] 已覆盖最低清单，或标明为何省略
- [ ] 高风险项有明确优先级
- [ ] 未编造用户未提供的细节
- [ ] 假设与信息缺口已标明

## 常见误区

- 范围和上下文都不清楚时，不要假装已经完整可用。
- 不要把所有项写成同等重要。
- 不要跳过假设与信息缺口。
- 不要输出大段与当前工具链无关的空泛理论。
