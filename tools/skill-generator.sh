#!/bin/bash

# Skill Generator - 快速生成新 skill 的骨架结构
# Usage: ./skill-generator.sh --name <skill-name> --category <category> --level <level> --language <zh|en>

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 默认值
SKILL_NAME=""
CATEGORY="testing-types"
LEVEL="intermediate"
LANGUAGE="zh"
VERSION="1.0.0"
DESCRIPTION=""

# 打印帮助信息
print_help() {
    echo -e "${BLUE}Skill Generator - 快速生成新 skill 的骨架结构${NC}"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --name <name>        Skill 名称（必需，使用 kebab-case）"
    echo "  --category <cat>     Skill 类别（默认: testing-types）"
    echo "                       可选: testing-types, testing-workflows, advanced"
    echo "  --level <level>      难度级别（默认: intermediate）"
    echo "                       可选: beginner, intermediate, advanced, expert"
    echo "  --language <lang>    语言（默认: zh）"
    echo "                       可选: zh, en"
    echo "  --description <desc> 简短描述（一句话）"
    echo "  --version <ver>      版本号（默认: 1.0.0）"
    echo "  --help               显示此帮助信息"
    echo ""
    echo "Examples:"
    echo "  $0 --name integration-testing --category testing-types --level intermediate --language zh"
    echo "  $0 --name contract-testing --category testing-types --level advanced --language en"
    echo ""
}

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --name)
            SKILL_NAME="$2"
            shift 2
            ;;
        --category)
            CATEGORY="$2"
            shift 2
            ;;
        --level)
            LEVEL="$2"
            shift 2
            ;;
        --language)
            LANGUAGE="$2"
            shift 2
            ;;
        --description)
            DESCRIPTION="$2"
            shift 2
            ;;
        --version)
            VERSION="$2"
            shift 2
            ;;
        --help)
            print_help
            exit 0
            ;;
        *)
            echo -e "${RED}错误: 未知参数 $1${NC}"
            print_help
            exit 1
            ;;
    esac
done

# 验证必需参数
if [ -z "$SKILL_NAME" ]; then
    echo -e "${RED}错误: --name 参数是必需的${NC}"
    print_help
    exit 1
fi

# 验证 skill 名称格式（kebab-case）
if ! [[ "$SKILL_NAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo -e "${RED}错误: Skill 名称必须使用 kebab-case 格式（例如: my-skill-name）${NC}"
    exit 1
fi

# 验证类别
if [[ ! "$CATEGORY" =~ ^(testing-types|testing-workflows|advanced)$ ]]; then
    echo -e "${RED}错误: 类别必须是 testing-types, testing-workflows 或 advanced${NC}"
    exit 1
fi

# 验证难度级别
if [[ ! "$LEVEL" =~ ^(beginner|intermediate|advanced|expert)$ ]]; then
    echo -e "${RED}错误: 难度级别必须是 beginner, intermediate, advanced 或 expert${NC}"
    exit 1
fi

# 验证语言
if [[ ! "$LANGUAGE" =~ ^(zh|en)$ ]]; then
    echo -e "${RED}错误: 语言必须是 zh 或 en${NC}"
    exit 1
fi

# 设置目标目录
if [ "$LANGUAGE" = "en" ]; then
    SKILL_DIR="skills/${CATEGORY}/${SKILL_NAME}-en"
else
    SKILL_DIR="skills/${CATEGORY}/${SKILL_NAME}"
fi

# 检查目录是否已存在
if [ -d "$SKILL_DIR" ]; then
    echo -e "${RED}错误: 目录 $SKILL_DIR 已存在${NC}"
    exit 1
fi

# 创建目录结构
echo -e "${BLUE}创建 Skill 目录结构...${NC}"
mkdir -p "$SKILL_DIR/prompts"
mkdir -p "$SKILL_DIR/examples"
mkdir -p "$SKILL_DIR/tests"

# 获取当前日期
CURRENT_DATE=$(date +%Y-%m-%d)

# 生成 SKILL.md
echo -e "${BLUE}生成 SKILL.md...${NC}"
cat > "$SKILL_DIR/SKILL.md" << EOF
---
name: ${SKILL_NAME}$([ "$LANGUAGE" = "en" ] && echo "-en" || echo "")
version: ${VERSION}
last-updated: ${CURRENT_DATE}
description: ${DESCRIPTION:-"TODO: 添加简短描述"}
category: ${CATEGORY}
level: ${LEVEL}
tags: [TODO, add, tags]
dependencies: []
recommended-with: []
context-aware: false
context-patterns:
  project-types: []
  frameworks: []
  test-frameworks: []
output-formats: [markdown, excel, csv, json]
examples-count: 0
has-tutorial: false
has-troubleshooting: false
---

# ${SKILL_NAME}$([ "$LANGUAGE" = "en" ] && echo " (English)" || echo " (中文版)")

$([ "$LANGUAGE" = "en" ] && echo "**Chinese Version:** See skill \`${SKILL_NAME}\`" || echo "**英文版：** 见技能 \`${SKILL_NAME}-en\`")

提示词见本目录 \`prompts/${SKILL_NAME}.md\`。

## 何时使用 | When to Use

- TODO: 添加使用场景
- TODO: 添加触发条件
- **触发示例：** TODO: 添加示例

## 输出格式选项 | Output Format Options

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明：

| 格式 | 说明 | 如何请求（示例） |
|------|------|------------------|
| **Markdown** | 默认，便于阅读与版本管理 | 无需额外说明 |
| **Excel** | 制表符分隔，可粘贴到 Excel | 「请以 Excel 可粘贴的制表符分隔表格输出」 |
| **CSV** | 逗号分隔，首行为表头 | 「请以 CSV 格式输出」 |
| **JSON** | 便于程序解析 | 「请以 JSON 形式输出」 |

详细说明与示例见本目录 **[output-formats.md](output-formats.md)**。

## 如何使用本技能中的提示词 | How to Use Prompts

1. 打开本目录 \`prompts/${SKILL_NAME}.md\`，将虚线以下内容复制到 AI 对话。
2. 附加你的具体需求或上下文。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 参考文件 | Reference Files

- **[prompts/${SKILL_NAME}.md](prompts/${SKILL_NAME}.md)** — 主提示词
- **[prompts/basic.md](prompts/basic.md)** — 基础层提示词
- **[prompts/intermediate.md](prompts/intermediate.md)** — 中级层提示词
- **[prompts/advanced.md](prompts/advanced.md)** — 高级层提示词
- **[quick-start.md](quick-start.md)** — 快速开始指南
- **[output-formats.md](output-formats.md)** — 输出格式说明
- **[examples/](examples/)** — 代码示例

## 常见误区 | Common Pitfalls

- ❌ TODO: 添加常见误区
- ✅ TODO: 添加正确做法

## 最佳实践 | Best Practices

- TODO: 添加最佳实践建议

## 相关技能 | Related Skills

TODO: 添加相关 skills

---

**创建日期 | Created**: ${CURRENT_DATE}
**最后更新 | Last Updated**: ${CURRENT_DATE}
EOF

# 生成 quick-start.md
echo -e "${BLUE}生成 quick-start.md...${NC}"
cat > "$SKILL_DIR/quick-start.md" << EOF
# ${SKILL_NAME} - 快速开始 | Quick Start

$([ "$LANGUAGE" = "en" ] && echo "5-minute guide to get started with ${SKILL_NAME}." || echo "5 分钟快速上手 ${SKILL_NAME}。")

---

## 1. $([ "$LANGUAGE" = "en" ] && echo "What is it?" || echo "这是什么？")

TODO: 一句话说明这个 skill 的用途

## 2. $([ "$LANGUAGE" = "en" ] && echo "When to use?" || echo "何时使用？")

TODO: 列出 2-3 个典型使用场景

## 3. $([ "$LANGUAGE" = "en" ] && echo "Quick Example" || echo "快速示例")

\`\`\`
@skill ${SKILL_NAME}$([ "$LANGUAGE" = "en" ] && echo "-en" || echo "")
TODO: 添加示例输入
\`\`\`

**$([ "$LANGUAGE" = "en" ] && echo "Expected Output" || echo "预期输出"):**

TODO: 添加示例输出

## 4. $([ "$LANGUAGE" = "en" ] && echo "Key Points" || echo "关键要点")

- TODO: 要点 1
- TODO: 要点 2
- TODO: 要点 3

## 5. $([ "$LANGUAGE" = "en" ] && echo "Next Steps" || echo "下一步")

- $([ "$LANGUAGE" = "en" ] && echo "Read full documentation: [SKILL.md](SKILL.md)" || echo "阅读完整文档：[SKILL.md](SKILL.md)")
- $([ "$LANGUAGE" = "en" ] && echo "Try examples: [examples/](examples/)" || echo "尝试示例：[examples/](examples/)")
- $([ "$LANGUAGE" = "en" ] && echo "Learn advanced usage: [prompts/advanced.md](prompts/advanced.md)" || echo "学习高级用法：[prompts/advanced.md](prompts/advanced.md)")

---

**$([ "$LANGUAGE" = "en" ] && echo "Estimated Time" || echo "预计时间")**: 5 $([ "$LANGUAGE" = "en" ] && echo "minutes" || echo "分钟")
EOF

# 生成 output-formats.md
echo -e "${BLUE}生成 output-formats.md...${NC}"
cat > "$SKILL_DIR/output-formats.md" << EOF
# 输出格式说明 | Output Format Documentation

本技能默认输出为 **Markdown**。若需要 **Excel**、**CSV** 或 **JSON** 格式，请在向 AI 提交需求时**在末尾明确说明**。

---

## 1. Markdown（默认）

不特别说明时，AI 按提示词中的 Markdown 模板输出，便于阅读与版本管理。

---

## 2. Excel 格式

**如何请求：** 在需求末尾加上一句，例如：

- 「请将上述内容以 **Excel 可粘贴的制表符分隔表格** 形式再输出一遍。」
- 「请用**制表符分隔的表格**输出，便于我复制到 Excel。」

**输出约定：** 第一行为表头，列之间用 **Tab** 分隔，可直接粘贴到 Excel 分列。

---

## 3. CSV 格式

**如何请求：** 例如「请将结果以 **CSV 格式**（逗号分隔，首行为表头）输出。」

**输出约定：** 首行为列名，列之间用英文逗号 \`,\` 分隔；单元格含逗号或换行时用双引号 \`"\` 包裹。

---

## 4. JSON 格式

**如何请求：** 例如「请将上述内容以 **JSON** 形式输出。」

**输出约定：** 使用标准 JSON；表格类内容为对象数组，字段与 Markdown 中的信息一致。

---

详见仓库 \`skills/testing-types/_output-formats-template-$([ "$LANGUAGE" = "en" ] && echo "en" || echo "zh").md\` 中的通用示例。
EOF

# 生成主提示词文件
echo -e "${BLUE}生成 prompts/${SKILL_NAME}.md...${NC}"
cat > "$SKILL_DIR/prompts/${SKILL_NAME}.md" << EOF
# ${SKILL_NAME} Prompt

> 💡 **使用说明**：请复制下方虚线以下的所有内容到 AI 助手（如 ChatGPT、Claude、Cursor AI 等），然后附加你的具体需求即可开始使用。

---

**Role:** $([ "$LANGUAGE" = "en" ] && echo "Senior QA Expert" || echo "资深测试专家")

**Context:** TODO: 添加角色背景和专业领域描述

**Task:** TODO: 添加任务描述

---

## TODO: 添加方法论章节

### 1. TODO: 方法 1

TODO: 描述

### 2. TODO: 方法 2

TODO: 描述

---

## TODO: 添加分类章节

### 1. TODO: 类别 1

TODO: 描述

### 2. TODO: 类别 2

TODO: 描述

---

## Output Format (输出格式规范)

请按以下 Markdown 格式输出：

\`\`\`markdown
---

## TODO: 添加输出模板

### TODO: 章节 1

TODO: 内容

### TODO: 章节 2

TODO: 内容

---
\`\`\`

---

## Quality Requirements (质量要求)

### 1. TODO: 质量要求 1

TODO: 描述

### 2. TODO: 质量要求 2

TODO: 描述

---

## Special Considerations (特殊注意事项)

### 1. TODO: 注意事项 1

TODO: 描述

### 2. TODO: 注意事项 2

TODO: 描述

---

## Execution Instructions (执行指令)

1. **TODO: 步骤 1**
2. **TODO: 步骤 2**
3. **TODO: 步骤 3**

**请在收到需求后，立即开始执行上述任务。**
EOF

# 生成分层提示词
echo -e "${BLUE}生成分层提示词...${NC}"

# Basic
cat > "$SKILL_DIR/prompts/basic.md" << EOF
# ${SKILL_NAME} - 基础层提示词 | Basic Level Prompt

适合初学者使用的简化版提示词。

---

TODO: 添加基础层提示词内容（简化版，重点在核心概念和基本用法）

---

**难度级别 | Level**: Beginner
**预计时间 | Estimated Time**: 10-15 minutes
EOF

# Intermediate
cat > "$SKILL_DIR/prompts/intermediate.md" << EOF
# ${SKILL_NAME} - 中级层提示词 | Intermediate Level Prompt

适合有一定经验的用户。

---

TODO: 添加中级层提示词内容（标准版，包含常用方法和最佳实践）

---

**难度级别 | Level**: Intermediate
**预计时间 | Estimated Time**: 20-30 minutes
EOF

# Advanced
cat > "$SKILL_DIR/prompts/advanced.md" << EOF
# ${SKILL_NAME} - 高级层提示词 | Advanced Level Prompt

适合专家用户，包含高级技巧和复杂场景。

---

TODO: 添加高级层提示词内容（完整版，包含高级技巧、边界情况和优化策略）

---

**难度级别 | Level**: Advanced/Expert
**预计时间 | Estimated Time**: 30-60 minutes
EOF

# 生成 README.md（examples 目录）
echo -e "${BLUE}生成 examples/README.md...${NC}"
cat > "$SKILL_DIR/examples/README.md" << EOF
# ${SKILL_NAME} - 代码示例 | Code Examples

本目录包含 ${SKILL_NAME} 的真实代码示例。

---

## 示例列表 | Example List

TODO: 添加示例列表

### 示例 1: TODO

**描述**: TODO

**文件**: \`example-1/\`

**运行方式**:
\`\`\`bash
cd example-1
# TODO: 添加运行命令
\`\`\`

---

## 依赖要求 | Dependencies

TODO: 列出所有示例的依赖要求

---

## 故障排除 | Troubleshooting

TODO: 添加常见问题和解决方案
EOF

# 生成 README.md（tests 目录）
echo -e "${BLUE}生成 tests/README.md...${NC}"
cat > "$SKILL_DIR/tests/README.md" << EOF
# ${SKILL_NAME} - 测试用例 | Test Cases

本目录包含 ${SKILL_NAME} 的测试用例，用于验证 skill 的输出质量。

---

## 测试用例列表 | Test Case List

TODO: 添加测试用例列表

### TC-001: TODO

**输入**: TODO

**预期输出**: TODO

**验证标准**: TODO

---

## 运行测试 | Run Tests

\`\`\`bash
# TODO: 添加测试运行命令
\`\`\`

---

## 测试覆盖率 | Test Coverage

TODO: 添加测试覆盖率信息
EOF

# 生成成功消息
echo ""
echo -e "${GREEN}✓ Skill 生成成功！${NC}"
echo ""
echo -e "${BLUE}生成的文件：${NC}"
echo "  $SKILL_DIR/"
echo "  ├── SKILL.md"
echo "  ├── quick-start.md"
echo "  ├── output-formats.md"
echo "  ├── prompts/"
echo "  │   ├── ${SKILL_NAME}.md"
echo "  │   ├── basic.md"
echo "  │   ├── intermediate.md"
echo "  │   └── advanced.md"
echo "  ├── examples/"
echo "  │   └── README.md"
echo "  └── tests/"
echo "      └── README.md"
echo ""
echo -e "${YELLOW}下一步：${NC}"
echo "  1. 编辑 $SKILL_DIR/SKILL.md，完善元数据和描述"
echo "  2. 编辑 $SKILL_DIR/prompts/${SKILL_NAME}.md，添加详细的提示词内容"
echo "  3. 添加代码示例到 $SKILL_DIR/examples/"
echo "  4. 添加测试用例到 $SKILL_DIR/tests/"
echo "  5. 更新 skills-index.md 和 skills-graph.md"
echo "  6. 运行质量检查: ./tools/quality-check.sh $SKILL_DIR"
echo ""
echo -e "${BLUE}参考文档：${NC}"
echo "  - CONTRIBUTING.md - 贡献指南"
echo "  - skills/testing-types/functional-testing/ - 参考示例"
echo ""
