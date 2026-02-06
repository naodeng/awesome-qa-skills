<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# Awesome QA Skills

本仓库提供一套**统一的 QA 工作流技能（Skills）**，适用于 **Cursor**、**Claude Code**、**OpenCode** 等 AI 编码工具。  
**中英文在目录层面分离**：中文技能目录如 `daily-testing-workflow`，英文技能目录如 `daily-testing-workflow-en`。  
- **工作流技能**位于 **`skills/testing-workflows/`**（日常 / 迭代 / 发布）。  
- **测试类型技能**位于 **`skills/testing-types/`**（功能测试、API 测试等 15 类 × 中英文）。  
按使用语言将对应目录复制到各工具指定位置即可。

---

## 🚀 5 分钟快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-repo/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. 安装 Skill（以 Cursor 为例）

```bash
# 复制日常测试工作流（中文）
cp -r skills/testing-workflows/daily-testing-workflow ~/.cursor/skills/

# 或复制功能测试 skill（中文）
cp -r skills/testing-types/functional-testing ~/.cursor/skills/
```

### 3. 在 AI 工具中使用

```
@skill daily-testing-workflow
今天需要测试用户登录功能
```

### 4. 探索更多

- 📚 查看 [skills-index.md](skills-index.md) 了解所有可用 skills
- 🔗 查看 [skills-graph.md](skills-graph.md) 了解 skills 依赖关系
- ❓ 查看 [FAQ.md](FAQ.md) 获取常见问题解答
- 🛠️ 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献

---

## 三个工作流（skills/testing-workflows/）

| 工作流         | 英文名                  | 简要说明 |
|----------------|-------------------------|----------|
| **日常测试工作流程** | Daily Testing Workflow  | 每日测试：早晨例行、用例编写、自动化、探索性测试、缺陷上报、下午审查、收尾 |
| **迭代测试工作流程** | Sprint Testing Workflow | 2 周迭代：规划、环境与早期测试、积极测试、密集回归、稳定化、评审与演示、回顾与下一迭代准备 |
| **发布测试工作流程** | Release Testing Workflow| 发布前 1–2 周至发布后：T-14 规划、功能冻结、专项测试（性能/安全/可访问性/视觉）、RC、Go/No-Go、部署、发布后监控与回顾 |

每个工作流均提供**何时使用**、**步骤说明**、**如何使用提示词**、**常见误区**、**最佳实践**及**参考文件**，便于 AI 与测试人员按步骤执行。

---

## 测试类型技能（skills/testing-types/）

按**测试类型**单独封装的技能，**中英文分目录**（如 `functional-testing` / `functional-testing-en`）。  

**输出格式**：默认输出为 **Markdown**；可在对话末尾说明以获取 **Excel**（制表符分隔表）、**CSV** 或 **JSON** 格式结果。各技能目录下 **output-formats.md** 有详细请求说明与示例。

| 类型 | 中文目录 | 英文目录 |
|------|----------|----------|
| 功能测试、API 测试、自动化测试、缺陷上报、手动测试、测试用例编写、测试报告、测试策略、需求分析、性能测试、安全测试、可访问性测试、AI 辅助测试、测试用例评审、移动端测试 | `skills/testing-types/<类型名>/` | `skills/testing-types/<类型名>-en/` |

详见 **[skills/testing-types/README.md](skills/testing-types/README.md)**。

---

## 目录结构

所有技能在 **`skills/`** 下分为两类：

- **`skills/testing-workflows/`** — 三个工作流（日常 / 迭代 / 发布），中英文各一目录。
- **`skills/testing-types/`** — 按测试类型分的技能（15 类 × 中英文），每类含输出格式选项。

**中文技能**：如 `daily-testing-workflow`，内含中文 `SKILL.md`、`reference.md`、及仅含中文提示词（`xxx.md`）的 `prompts/`。  
**英文技能**：如 `daily-testing-workflow-en`，内含英文 `SKILL.md`、`reference.md`、及仅含英文提示词（`xxx_EN.md`）的 `prompts/`。  
**按语言复制对应目录到目标工具即可**，不依赖仓库根目录的 `prompts/`。

| 类型 | 中文目录示例 | 英文目录示例 |
|------|----------------|----------------|
| 工作流 | testing-workflows/daily-testing-workflow、sprint-testing-workflow、release-testing-workflow | testing-workflows/daily-testing-workflow-en、…-en |
| 测试类型 | testing-types/functional-testing、api-testing、… | testing-types/functional-testing-en、…-en |

```
awesome-qa-skills/
├── skills/
│   ├── testing-workflows/            # 三个工作流（中/英）
│   │   ├── daily-testing-workflow/   # 日常测试（中文）
│   │   │   ├── SKILL.md
│   │   │   ├── reference.md
│   │   │   └── prompts/              # 仅中文 .md
│   │   ├── daily-testing-workflow-en/
│   │   ├── sprint-testing-workflow/
│   │   ├── sprint-testing-workflow-en/
│   │   ├── release-testing-workflow/
│   │   └── release-testing-workflow-en/
│   └── testing-types/                # 按测试类型（中/英 + 输出格式）
│       ├── functional-testing/
│       ├── functional-testing-en/
│       ├── api-testing/  … 共 15 类 × 中英文
│       └── README.md
├── prompts/                          # 根目录提示词源（供维护与参考）
├── README.md
└── README_EN.md
```

---

## 各工具使用方式

将 **`skills/testing-workflows/`** 或 **`skills/testing-types/`** 下对应技能目录复制到各工具指定位置即可，同一套技能适用于以下工具。

### Cursor

- **项目级**：复制到项目的 `.cursor/skills/`。
  ```bash
  # 工作流示例
  cp -r skills/testing-workflows/daily-testing-workflow /你的项目路径/.cursor/skills/        # 中文
  cp -r skills/testing-workflows/daily-testing-workflow-en /你的项目路径/.cursor/skills/    # 英文
  ```
- **用户级**：复制到 `~/.cursor/skills/`，同样按语言选择目录。

### Claude Code

- 复制到项目的 `.claude/skills/`，目录名需与技能 `name` 一致。
  ```bash
  mkdir -p .claude/skills
  cp -r skills/testing-workflows/daily-testing-workflow .claude/skills/           # 中文
  cp -r skills/testing-workflows/daily-testing-workflow-en .claude/skills/        # 英文
  ```

### OpenCode

- **项目级**：`.opencode/skills/<技能名>/`
- **全局**：`~/.config/opencode/skills/<技能名>/`
  ```bash
  mkdir -p .opencode/skills
  cp -r skills/testing-workflows/daily-testing-workflow .opencode/skills/         # 中文
  cp -r skills/testing-workflows/daily-testing-workflow-en .opencode/skills/     # 英文
  ```

---

## 提示词与 reference（中英文双版本）

- **根目录 `prompts/`**：多类提示词，每类提供**中文 `xxx.md`** 与**英文 `xxx_EN.md`**，用于集中维护与参考。各技能目录下的 `prompts/` 与语言一致：**中文技能**仅包含 `xxx.md`，**英文技能**仅包含 `xxx_EN.md`。执行某一步时，打开当前技能目录下 `prompts/` 中对应文件，与 AI 协同即可。
- **各工作流下的 `reference.md`**：列出该工作流涉及的提示词类型、在本工作流中的用途，以及步骤与提示词文件的对照表，便于在单技能目录内完成「步骤 → 提示词」的查找与执行。
- **SKILL.md 中的「如何使用本技能中的提示词」**：说明「查 reference → 打开本目录 prompts 下对应文件 → 结合上下文与 AI 执行」的三步用法。

---

## 约定

- 技能的 `name` 与目录名一致，复制到各工具时保持目录名即可。

---

## 许可证

本仓库仅提供供 AI 工具使用的 Skill 封装。
