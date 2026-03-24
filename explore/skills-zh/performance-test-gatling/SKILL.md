---
name: performance-test-gatling
description: 提供 Gatling 性能测试范围、仿真脚本样例和执行入口。
---

# performance-test-gatling（中文）

## 适用场景

适合需要更长时间或更复杂并发模型的性能验证场景。

## 技能目标

提供 Gatling 性能测试范围、仿真脚本样例和执行入口。

## 输入

- 可选：仿真类型（load/stress/spike/soak）与目标环境参数

## 输出

- 输出：执行结果与报告目录

## 前置准备

- 安装 Gatling 命令行工具
- 配置可访问的目标环境
- 按测试目标选择仿真类型

## 快速开始

```bash
bash scripts/run-tests.sh load
```

## 离线演示（本地可跑）

```bash
bash scripts/run-local-smoke.sh
```

## 结果判断

- 能正常识别并启动所选仿真类型
- 执行后可查看报告结果

## 常见问题

- 若提示找不到 gatling，先安装或设置 GATLING_BIN
- 若结果异常，先缩小并发规模做基线验证

## 目录说明

- `prompts/`：中文提示词
- `scripts/`：执行脚本
- `examples/`：示例输入输出
- `output-templates/`：输出模板（如目录存在）
- `references/`：规范说明（如目录存在）

## 独立使用声明

- 本技能可脱离英文目录单独使用。
- 运行所需文件全部位于当前技能目录内。
- 文档、提示词、示例均为中文可读版本。

## 审计信息

- 最近验证时间：2026-03-23
- 技能文档版本：1.1.0
