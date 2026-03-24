---
name: api-test-restassure
description: 解析多格式接口定义，生成 Rest Assured 接口自动化测试类。
---

# api-test-restassure（中文）

## 适用场景

适合 Java 项目在接口层做持续回归和发布前验证。

## 技能目标

解析多格式接口定义，生成 Rest Assured 接口自动化测试类。

## 输入

- 支持：curl/Postman/Swagger/Bruno/OpenCollection/Insomnia/OpenAPI v3/WSDL/ZIP

## 输出

- 输出：规范化接口数据 + Java 测试类

## 前置准备

- 安装 Python 3
- 如需执行测试，安装 Maven
- 使用 examples 先验证生成结果

## 快速开始

```bash
bash scripts/run.sh examples
```

## 结果判断

- 能生成 Java 测试类
- Maven 可用时可直接执行测试

## 常见问题

- 若本机没有 Maven，也可先完成测试类生成
- 若路径不一致，按项目结构调整输出位置

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
