---
name: api-testing
description: Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API 测试 and api testing.
---

# API 测试（中文版）

**英文版：** 见技能 `api-testing-en`。

提示词见本目录 `prompts/api-testing.md`。

## 何时使用

- 用户提到「API 测试」「api-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 代码示例

### 1. Postman + Newman REST API 测试

完整的用户管理 API 测试示例，包含 10 个测试用例。

**位置：** `examples/postman-rest-api/`

**包含内容：**
- Postman 集合文件（10 个测试用例）
- 环境变量配置
- Newman 自动化运行脚本
- 详细的 README 文档

**快速开始：**
```bash
cd examples/postman-rest-api
npm install -g newman
./newman-run.sh
```

**测试覆盖：**
- 用户 CRUD 操作（创建、读取、更新、删除）
- 认证和授权测试
- 错误处理和边界条件
- 响应时间验证
- 数据格式验证

详见：[examples/postman-rest-api/README.md](examples/postman-rest-api/README.md)

## 最佳实践

### API 测试设计原则

1. **测试金字塔**
   - 单元测试：测试单个 API 端点
   - 集成测试：测试多个端点的交互
   - 端到端测试：测试完整的业务流程

2. **测试数据管理**
   - 使用环境变量管理不同环境配置
   - 使用动态变量避免硬编码
   - 测试后清理数据

3. **断言策略**
   - 验证状态码
   - 验证响应结构（Schema Validation）
   - 验证响应数据
   - 验证响应时间

4. **错误处理**
   - 测试各种错误场景（4xx, 5xx）
   - 验证错误消息格式
   - 测试边界条件

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| Postman/Newman | REST API 测试 | 易用、可视化、CI/CD 集成 |
| REST Assured | Java 项目 | 强类型、BDD 风格 |
| Pytest + Requests | Python 项目 | 灵活、生态丰富 |
| SuperTest | Node.js 项目 | 与 Express 集成好 |
| GraphQL Playground | GraphQL API | 专为 GraphQL 设计 |

## 常见误区 | Common Pitfalls

- ❌ 只测成功路径 → ✅ 覆盖参数校验、异常处理、鉴权失败与边界场景
- ❌ 契约校验不完整 → ✅ 同时校验状态码、Schema、业务字段与兼容性
- ❌ 测试数据相互污染 → ✅ 使用可重复的种子数据并明确清理策略
- ❌ 忽略环境差异 → ✅ 校验不同环境的地址、鉴权配置与依赖版本

## 故障排除

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。
## 参考文件

- **prompts/api-testing.md** — API 测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/postman-rest-api/** — Postman + Newman 完整示例
- **quick-start.md** — 5 分钟快速上手指南

## 目标受众

- 在真实项目中执行该测试域工作的 QA 与开发人员
- 需要结构化、可复用测试交付物的测试负责人
- 需要快速生成可落地测试产出的 AI 使用者

## 不适用场景

- 无测试范围上下文的纯线上应急处置
- 需要法律/合规最终裁定但缺少专家复核的决策
- 缺少最小输入（范围、环境、期望行为）的请求

## 关键成功因素

- 先明确范围、环境与验收标准，再生成测试内容
- 生成结果必须结合真实系统约束做二次校验
- 保持产物可追踪（需求 -> 测试点 -> 缺陷 -> 决策）

## 输出模板与解析脚本

- 模板目录：`output-templates/`
  - `template-word.md`（Word 友好结构）
  - `template-excel.tsv`（Excel 可直接粘贴）
  - `template-xmind.md`（XMind 结构化大纲）
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- 解析脚本目录：`scripts/`
  - 解析通用：`parse_output_formats.py`
  - 解析按格式：`parse_word.py`、`parse_excel.py`、`parse_xmind.py`、`parse_json.py`、`parse_csv.py`、`parse_markdown.py`
  - 转换通用：`convert_output_formats.py`
  - 转换按格式：`convert_to_word.py`、`convert_to_excel.py`、`convert_to_xmind.py`、`convert_to_json.py`、`convert_to_csv.py`、`convert_to_markdown.py`
  - 批量转换：`batch_convert_templates.py`（批量输出到 `artifacts/`）

示例：
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
