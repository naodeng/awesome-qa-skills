---
name: mobile-testing
description: Use this skill when you need to design mobile test plans for iOS or Android covering functionality, compatibility, performance, network, and security; triggers include 移动端测试 and mobile testing.
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

# 移动端测试（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要在真实项目里处理 mobile testing 相关任务。
- 需要一份可以直接用于执行、评审或跟进的结果。

## 执行流程

1. 阅读并遵循「按需加载」中的主提示词（覆盖清单、输出结构、质量要求）。
2. 只补充真正影响结果的项目上下文：范围、环境、限制、风险、依赖、期望产出。
3. 信息不全时先给可用初版，并显式标出假设与信息缺口。
4. 默认 Markdown；用户指定其他格式时再切换。

## 领域执行要点

1. 用生产分布、变化和事故证据选 OS×设备×安装/升级路径×网络×前后台 的风险矩阵，注明样本与未覆盖组合，不能臆造支持列表。
2. deeplink 保留原始 URI、解码规则、路由/参数与授权状态；比较冷启动、热启动和恢复，参数不能在恢复后丢失或二次解码。
3. 中断支付记录订单/operation_id 与提交点，恢复后服务端读回账务与 UI 状态一致；响应丢失先查状态，不能重复付款。
4. 验证升级的数据兼容、权限变化、进程终止后状态和资源；未执行设备只能作为候选，支持范围结论与真实设备证据分开。

## 核心约束

- 按风险/业务影响排优先级，不要平均摊铺。
- 把「已确认事实」和「当前假设」分开写。
- 不要编造用户未提供的接口、字段、环境或根因细节。
- 结果必须可执行：场景具体、有优先级、能指导下一步。

## 按需加载

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 产出前必须阅读并遵循 `prompts/mobile-testing.md`（最低覆盖清单、输出结构、质量要求）。
- 需要 Excel/CSV/JSON/Word 等格式时：读 `output-formats.md`，并按用户格式要求输出。
- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。
- 用户要示例或对标现有资产时：读 `examples/` 中相关样例。
- 需要框架规范、排障、报告 schema 等深资料时：只读 `references/` 里与当前问题相关的文件，不要整目录通读。
- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。
- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。
- 用户只要最短上手路径时：读 `quick-start.md`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 最低覆盖关注：范围、设备和系统覆盖、安装升级检查、核心流程、权限处理、网络和中断行为、推送或 deeplink（如相关）、性能或耗电风险…（细节以主提示词为准）
- [ ] 已覆盖最低清单，或标明为何省略
- [ ] 高风险项有明确优先级
- [ ] 未编造用户未提供的细节
- [ ] 假设与信息缺口已标明

## 常见误区

- 范围和上下文都不清楚时，不要假装已经完整可用。
- 不要把所有项写成同等重要。
- 不要跳过假设与信息缺口。
- 不要输出大段与当前工具链无关的空泛理论。
