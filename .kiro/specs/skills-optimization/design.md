# Skills 优化项目设计文档

## 架构设计

### 整体架构

```
awesome-qa-skills/
├── skills/                          # Skills 主目录
│   ├── testing-workflows/           # 工作流 skills
│   ├── testing-types/               # 测试类型 skills
│   └── advanced/                    # 新增：高级 skills
│       ├── test-strategy-generator/
│       ├── test-metrics-analysis/
│       └── skill-orchestrator/
├── templates/                       # 新增：模板目录
│   ├── output-templates/            # 输出格式模板
│   ├── workflow-templates/          # 工作流组合模板
│   └── skill-templates/             # Skill 创建模板
├── examples/                        # 新增：代码示例库
│   ├── functional-testing/
│   ├── api-testing/
│   ├── automation-testing/
│   └── ...
├── docs/                            # 新增：文档目录
│   ├── tutorials/                   # 交互式教程
│   ├── guides/                      # 使用指南
│   ├── api/                         # API 文档
│   └── faq/                         # FAQ
├── tools/                           # 新增：工具脚本
│   ├── skill-generator.sh           # Skill 生成器
│   ├── sync-check.sh                # 中英文同步检查
│   ├── quality-check.sh             # 质量检查
│   └── context-detector.sh          # 上下文检测
├── ci-cd/                           # 新增：CI/CD 集成
│   ├── github-actions/
│   ├── gitlab-ci/
│   └── jenkins/
├── tests/                           # 新增：测试目录
│   ├── skill-tests/                 # Skill 测试用例
│   └── integration-tests/           # 集成测试
├── CHANGELOG.md                     # 新增：更新日志
├── CONTRIBUTING.md                  # 新增：贡献指南
├── skills-index.md                  # 新增：Skills 索引
├── skills-graph.md                  # 新增：Skills 关系图
└── FAQ.md                           # 新增：常见问题
```

### 核心组件设计

#### 1. 上下文感知系统

**组件**: Context Detector
**功能**: 自动检测项目上下文并调整 skill 行为

```yaml
# context-config.yaml
detection-rules:
  project-type:
    web:
      patterns: ["package.json", "index.html", "webpack.config.js"]
      frameworks:
        react: ["react", "react-dom"]
        vue: ["vue"]
        angular: ["@angular/core"]
    mobile:
      patterns: ["android/", "ios/", "pubspec.yaml"]
      frameworks:
        flutter: ["flutter"]
        react-native: ["react-native"]
    api:
      patterns: ["openapi.yaml", "swagger.json", "api/"]
  
  test-framework:
    jest: ["jest.config.js", "jest"]
    vitest: ["vitest.config.ts", "vitest"]
    pytest: ["pytest.ini", "pytest"]
    junit: ["pom.xml", "junit"]
```

**实现方式**:
```bash
# tools/context-detector.sh
#!/bin/bash
# 检测项目类型、技术栈、测试框架
# 输出 JSON 格式的上下文信息
```

#### 2. Skills 依赖管理系统

**组件**: Skills Graph Manager
**功能**: 管理 skills 之间的依赖关系和推荐组合

```yaml
# skills-graph.yaml
skills:
  functional-testing:
    depends-on: []
    recommended-with:
      - test-case-writing
      - requirements-analysis
    use-cases:
      - "新功能测试"
      - "回归测试"
    tags: [core, functional, manual]
  
  automation-testing:
    depends-on: [functional-testing]
    recommended-with:
      - api-testing
      - ai-assisted-testing
    use-cases:
      - "自动化脚本开发"
      - "CI/CD 集成"
    tags: [automation, ci-cd]
```

#### 3. 分层提示词系统

**结构**:
```
skill/prompts/
├── quick-start.md           # 快速开始（5分钟）
├── basic.md                 # 基础层（初学者）
├── intermediate.md          # 中级层（有经验）
├── advanced.md              # 高级层（专家）
└── patterns/                # 设计模式和最佳实践
    ├── page-object-model.md
    ├── data-driven-testing.md
    └── behavior-driven-testing.md
```

#### 4. 智能输出系统

**组件**: Output Formatter
**功能**: 根据上下文和用户偏好智能选择输出格式

```yaml
# output-config.yaml
format-detection:
  jira:
    indicators: [".jira", "jira-config.json"]
    template: "templates/output-templates/jira-format.md"
  
  testrail:
    indicators: [".testrail", "testrail.config"]
    template: "templates/output-templates/testrail-format.md"
  
  custom:
    location: ".kiro/custom-templates/"
    priority: highest
```

#### 5. 工作流编排系统

**组件**: Workflow Orchestrator
**功能**: 管理复杂工作流的执行和状态追踪

```yaml
# workflow-config.yaml
daily-testing-workflow:
  steps:
    - id: morning-review
      name: "早晨审查"
      duration: "5-10min"
      skills: [requirements-analysis, test-strategy]
      required: true
      checkpoint: true
    
    - id: test-case-creation
      name: "测试用例创建"
      duration: "30-60min"
      skills: [test-case-writing, functional-testing]
      required: true
      checkpoint: true
  
  adaptations:
    team-size:
      solo: [skip: [team-sync]]
      small: [duration-multiplier: 0.8]
      large: [add: [cross-team-coordination]]
    
    project-phase:
      mvp: [focus: [smoke-testing, critical-path]]
      growth: [focus: [regression, integration]]
      mature: [focus: [performance, security]]
```

## 数据模型

### Skill 元数据模型

```yaml
# SKILL.md frontmatter
---
name: functional-testing
version: 2.0.0
last-updated: 2024-02-06
description: 设计功能测试方案与用例
category: testing-types
level: intermediate
tags: [functional, manual, core]
dependencies: []
recommended-with: [test-case-writing, requirements-analysis]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop]
  frameworks: [react, vue, angular, flutter]
  test-frameworks: [jest, vitest, playwright, cypress]
output-formats: [markdown, excel, csv, json, jira, testrail]
examples-count: 5
has-tutorial: true
has-troubleshooting: true
---
```

### 工作流状态模型

```json
{
  "workflow": "daily-testing-workflow",
  "date": "2024-02-06",
  "status": "in-progress",
  "steps": [
    {
      "id": "morning-review",
      "status": "completed",
      "duration": "8min",
      "notes": "审查了3个用户故事"
    },
    {
      "id": "test-case-creation",
      "status": "in-progress",
      "duration": "25min",
      "notes": "已完成登录功能测试用例"
    }
  ],
  "health-score": 85,
  "blockers": []
}
```

## 接口设计

### Skill 调用接口

```markdown
# 基础调用
@skill functional-testing
需求：用户登录功能

# 带参数调用
@skill functional-testing --level=advanced --format=jira --context=react

# 组合调用
@skills [requirements-analysis, functional-testing, test-case-writing]
需求：用户登录功能
```

### 工作流调用接口

```markdown
# 启动工作流
@workflow daily-testing --team-size=small --project-phase=growth

# 检查工作流状态
@workflow-status daily-testing

# 继续工作流
@workflow-continue daily-testing --from=test-case-creation
```

## 技术选型

### 脚本语言
- **Bash**: 用于简单的文件操作和检测
- **Python**: 用于复杂的数据处理和分析

### 配置格式
- **YAML**: 用于配置文件（易读易写）
- **JSON**: 用于数据交换（标准化）

### 文档格式
- **Markdown**: 主要文档格式
- **Mermaid**: 图表和流程图

### 测试框架
- **Bats**: Bash 脚本测试
- **Pytest**: Python 脚本测试

## 实现策略

### 阶段1: 基础设施（P0）
1. 创建新的目录结构
2. 建立模板系统
3. 添加代码示例库
4. 创建快速开始文档

### 阶段2: 核心功能（P0-P1）
1. 实现上下文检测
2. 增强提示词（添加代码示例）
3. 实现分层提示词
4. 添加工作流追踪

### 阶段3: 智能化（P1-P2）
1. 实现智能测试用例生成
2. 添加 AI 辅助能力
3. 实现智能输出格式
4. 建立 skills 依赖图

### 阶段4: 集成与扩展（P2-P3）
1. CI/CD 集成
2. 自适应工作流
3. 测试度量分析
4. 高级特性

## 质量保证

### 代码质量
- 所有脚本通过 shellcheck/pylint
- 所有代码示例可运行
- 单元测试覆盖率 > 80%

### 文档质量
- 所有 skills 有完整文档
- 所有示例有说明
- 中英文版本同步

### 用户体验
- 快速开始 < 5 分钟
- 错误信息清晰
- Troubleshooting 完善

## 性能优化

### 加载优化
- 延迟加载非核心 skills
- 缓存上下文检测结果
- 压缩大型文档

### 搜索优化
- 建立全文索引
- 使用标签快速过滤
- 缓存搜索结果

## 安全考虑

### 脚本安全
- 所有用户输入验证
- 避免命令注入
- 最小权限原则

### 数据安全
- 不存储敏感信息
- 配置文件权限控制
- 日志脱敏

## 兼容性

### 工具兼容
- Cursor (v0.40+)
- Claude Code (v1.0+)
- OpenCode (v0.5+)

### 平台兼容
- macOS (10.15+)
- Linux (Ubuntu 20.04+)
- Windows (WSL2)

## 监控与反馈

### 使用统计
- Skills 使用频率
- 工作流完成率
- 错误发生率

### 用户反馈
- 满意度调查
- 功能请求
- Bug 报告

## 迁移策略

### 向后兼容
- 保留旧版 skills 结构
- 提供迁移脚本
- 文档说明变更

### 迁移步骤
1. 备份现有配置
2. 运行迁移脚本
3. 验证功能
4. 更新文档引用

## 文档计划

### 用户文档
- README.md (更新)
- Quick Start Guide
- User Guide
- FAQ
- Troubleshooting

### 开发者文档
- CONTRIBUTING.md
- Architecture Guide
- API Reference
- Testing Guide

### 示例文档
- Code Examples
- Workflow Examples
- Integration Examples
