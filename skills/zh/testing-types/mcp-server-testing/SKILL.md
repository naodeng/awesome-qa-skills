---
name: mcp-server-testing
description: Use this skill when planning or reviewing versioned tests for Model Context Protocol servers, including discovery, tools, transports, authorization, and safe side-effect boundaries; triggers include MCP server testing and MCP 服务端测试.
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

# MCP 服务端测试

## 何时使用

- 规划或审查 MCP 服务端的协议行为、工具契约、传输、授权或错误处理测试。
- 核对明确声明的 MCP 修订版和兼容范围，不假设浮动的最新版本。
- 为工具副作用、schema 和服务端安全属性准备隔离验证。

## 使用方法

1. 阅读 [prompts/mcp-server-testing.md](prompts/mcp-server-testing.md)，其中是完整执行约定。
2. 提取目标协议修订版、SDK/服务端版本、传输、能力、工具契约、授权模型、环境和证据；将缺失输入标为假设或待确认问题。
3. 目标为 2026-07-28 时，阅读 [references/mcp-spec-2026-07-28.md](references/mcp-spec-2026-07-28.md)；目标为其他修订版时，先查对应官方规范再判断协议要求。
4. 设计带可观察判定依据、安全准备条件、证据和停止条件的正向、负向、边界与兼容用例，并按风险排序。
5. 将计划和 fixture 判定与实际执行结果分开报告。

## 范围与约束

- 把 MCP 资源与工具描述当作不可信数据测试；双代兼容只覆盖产品明确声明的修订版，并逐版核对官方规范。

- 关注 MCP 服务端协议与服务端行为。除非用户明确要求，不将 host/client 体验、模型质量和一般应用安全混作本 Skill 的范围。
- MCP 协议符合性不定义所有业务工具副作用；根据目标工具契约确定副作用，并使用隔离数据。
- 用户要求测试并不自动授权使用真实凭据、调用生产工具或执行破坏性动作；必须有明确授权和隔离安全环境。
- 服务端自报身份、旧协议上的成功交互或单独的 SDK 版本均不能证明实际覆盖了哪种行为。

## 按需加载参考资料

- 阅读 `references/mcp-spec-2026-07-28.md` 获取固定修订版要求及官方来源链接。
- 复核本包预期覆盖范围时阅读对应 eval case；其中的合成数据不能证明运行时行为。

## 交付前检查

- [ ] 协议修订版、传输、能力与兼容目标明确。
- [ ] 拒绝、错误和畸形输入用例旁边保留合法正向对照。
- [ ] 工具副作用、身份、授权和重试有可观察判定依据。
- [ ] 缺失运行证据保持 NOT_RUN 或 UNKNOWN；不编造生产结果。
