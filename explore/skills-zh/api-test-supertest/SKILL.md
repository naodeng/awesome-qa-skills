---
name: api-test-supertest
description: 解析多格式接口定义，生成并执行 Supertest 自动化脚本。
---

# api-test-supertest（中文）

## 适用场景

适合 Node 服务的接口回归，快速从接口定义生成可执行测试。

## 技能目标

解析多格式接口定义，生成并执行 Supertest 自动化脚本。

## 输入

- 支持：curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## 输出

- 输出：规范化接口数据 + Supertest 测试文件

## 前置准备

- 安装 Python 3
- 如需执行测试，安装 Node 与 npm
- 先用 examples 目录验证生成流程

## 快速开始

```bash
bash scripts/run.sh examples
```

## 结果判断

- 能成功生成测试文件
- 如本机已安装 npm，可继续执行自动化测试

## 常见问题

- 若只想生成不执行，可先单独跑 parse 和 generate 脚本
- 若 npm 依赖缺失，先完成依赖安装

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
