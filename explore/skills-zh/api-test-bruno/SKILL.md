---
name: api-test-bruno
description: 解析多格式接口定义，生成 Bruno 请求集合并可执行回归。
---

# api-test-bruno（中文）

## 适用场景

适合把分散接口资料快速统一成 Bruno 集合进行回归验证。

## 技能目标

解析多格式接口定义，生成 Bruno 请求集合并可执行回归。

## 输入

- 支持：curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## 输出

- 输出：规范化接口数据 + Bruno 集合目录

## 前置准备

- 安装 Python 3
- 如需直接执行回归，安装 Bruno CLI
- 输入可用 examples 或真实接口资料

## 快速开始

```bash
bash scripts/run.sh examples
```

## 结果判断

- 能生成 Bruno 集合目录
- 如本机有 Bruno CLI，可继续执行回归

## 常见问题

- 若未安装 Bruno CLI，仍可完成集合生成
- 若解析结果为空，先检查输入文件是否含有效接口定义

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
