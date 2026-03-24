---
name: api-test-pytest
description: 解析多格式接口定义，生成 Pytest 接口自动化脚本。
---

# api-test-pytest（中文）

## 适用场景

适合 Python 团队快速建立接口自动化基础回归。

## 技能目标

解析多格式接口定义，生成 Pytest 接口自动化脚本。

## 输入

- 支持：curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## 输出

- 输出：规范化接口数据 + Pytest 测试文件

## 前置准备

- 安装 Python 3
- 安装 pytest 与 requests 依赖
- 先跑 examples 验证生成链路

## 快速开始

```bash
bash scripts/run.sh examples
```

## 结果判断

- 能生成 Pytest 测试文件
- 依赖齐全时可直接执行测试

## 常见问题

- 若提示缺依赖，先安装 requirements.txt
- 若生成内容过少，补充更完整的接口输入

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

- 最近验证时间：2026-03-24
- 技能文档版本：1.1.0
