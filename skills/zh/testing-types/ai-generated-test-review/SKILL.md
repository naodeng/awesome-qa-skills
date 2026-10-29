---
name: ai-generated-test-review
description: Use this skill when reviewing AI-generated unit, functional, API, or end-to-end tests for false confidence, weak assertions, missing risks, or unsafe test behavior; triggers include AI 生成测试评审, AI-generated test review, and functional test review.
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

# AI 生成测试评审（中文版）

审查 AI 生成的测试是否能证明真实行为，而不是只增加覆盖率或制造“全绿”的假象。

## 何时使用

- 需要合入、修改或评估 AI 生成的单元、功能、API 或 E2E 测试。
- 测试看似通过，但断言、隔离、数据或覆盖价值值得怀疑。

## 工作方式

1. 先盘点当前范围内实际存在的测试类型与文件：单元、功能（functional testing）、API、E2E 或其组合；只审查已发现或用户明确指定的类型。
2. 再明确被测行为、风险和可用的需求或实现证据；缺失时列为待确认，不虚构结论。
3. 阅读 `prompts/review-test.md`，按严重度输出可行动的发现；每项关联具体测试、风险和修正方向。
4. 仅加载已发现层级的规则：单元测试、功能测试（functional testing）、API 或 E2E；跨层问题可加载多份。不要因存在多个规则文件而直接全局审查。
5. 将“阻断合入”的错误与可接受的改进分开；不要因风格偏好把有效测试判为问题。

## 领域执行要点

1. 按所验证的契约判断断言，不能仅因出现 mock、snapshot 或状态码就标为 WEAK/FAKE。
2. 边界 mock 可替代已确认的外部依赖，但被测生产逻辑必须真实执行；mock 被测对象并断言它返回的预设值才缺乏保护。
3. 快照需基于独立审核的业务结构、稳定字段且错误结果会产生差异；忽略所有业务字段的快照无保护。状态码足以完整表达所给契约时可为 STRONG；持久化义务存在则需追加业务后置条件。
4. 每个分类给具体可逃逸缺陷或会被检出的变异，以及契约来源；证据不足保留置信度和缺口，中英文采用同一分类理由。
## 核心约束

- 以可观察行为、失败信号和风险覆盖为准，不能只评价行覆盖率、测试名称或 mock 调用次数。
- 发现测试会在实现被破坏后仍通过时，明确说明最小破坏方式和需要加强的断言。
- 不建议为了绿灯删除断言、吞掉异常、放宽时间阈值或改生产逻辑以适应测试。
- 测试代码、日志和示例中不得泄露真实凭据、个人数据或生产写操作。

## 按需加载

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次评审必须读 `prompts/review-test.md`；其中的“测试类型路由”先于逐条评审。
- 识别伪测试、过度 mock 或无效断言时读 `references/fake-test-patterns.md`。
- 单元测试读 `references/unit-test-rules.md`；功能测试 / functional testing 读 `references/functional-test-rules.md`；API 测试读 `references/api-test-rules.md`；E2E 测试读 `references/e2e-test-rules.md`。
- 需要展示期望水准或反例时，读取 `examples/good/` 或 `examples/bad/` 的相关样例。

## 交付前自检

- [ ] 已说明审查范围、证据和待确认信息
- [ ] 发现按严重度排序，且每项有位置、影响和建议
- [ ] 已审查真实断言、负向路径、边界、隔离和可重复性
- [ ] 未把无证据的推测写成事实
