<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# Awesome QA Skills

本仓库基于 [awesome-qa-prompt](https://github.com/awesome-qa-prompt) 的提示词与工作流，为 **Cursor**、**Claude Code**、**OpenCode** 三种 AI 编码工具生成可直接使用的 **QA 工作流技能（Skills）**。  
**中英文在目录层面分离**：中文技能目录如 `daily-testing-workflow`，英文技能目录如 `daily-testing-workflow-en`，按使用语言复制对应目录即可，无需依赖仓库根目录。

---

## 三个工作流

| 工作流         | 英文名                  | 简要说明 |
|----------------|-------------------------|----------|
| **日常测试工作流程** | Daily Testing Workflow  | 每日测试：早晨例行、用例编写、自动化、探索性测试、缺陷上报、下午审查、收尾 |
| **迭代测试工作流程** | Sprint Testing Workflow | 2 周迭代：规划、环境与早期测试、积极测试、密集回归、稳定化、评审与演示、回顾与下一迭代准备 |
| **发布测试工作流程** | Release Testing Workflow| 发布前 1–2 周至发布后：T-14 规划、功能冻结、专项测试（性能/安全/可访问性/视觉）、RC、Go/No-Go、部署、发布后监控与回顾 |

每个工作流均提供**何时使用**、**步骤说明**、**如何使用提示词**、**常见误区**、**最佳实践**及**参考文件**，便于 AI 与测试人员按步骤执行。

---

## 目录结构（中/英技能分目录）

每个工作流在 Cursor、Claude、OpenCode 下各有一组**中文目录**和**英文目录**：

- **中文技能**：目录名如 `daily-testing-workflow`，内含中文 `SKILL.md`、中文 `reference.md`、以及仅含中文提示词（`xxx.md`）的 `prompts/`。
- **英文技能**：目录名如 `daily-testing-workflow-en`，内含英文 `SKILL.md`、英文 `reference.md`、以及仅含英文提示词（`xxx_EN.md`）的 `prompts/`。

**按语言复制对应目录即可单独使用**，不依赖仓库根目录的 `prompts/`。

| 语言 | 技能目录名示例 | 说明 |
|------|----------------|------|
| 中文 | daily-testing-workflow、sprint-testing-workflow、release-testing-workflow | 技能名与目录名一致 |
| 英文 | daily-testing-workflow-en、sprint-testing-workflow-en、release-testing-workflow-en | 技能名带 `-en` 后缀 |

```
awesome-qa-skills/
├── cursor/                          # Cursor 用
│   ├── daily-testing-workflow/      # 日常测试（中文）
│   │   ├── SKILL.md
│   │   ├── reference.md
│   │   └── prompts/                 # 仅中文 .md
│   ├── daily-testing-workflow-en/   # 日常测试（英文）
│   │   ├── SKILL.md
│   │   ├── reference.md
│   │   └── prompts/                 # 仅 xxx_EN.md
│   ├── sprint-testing-workflow/
│   ├── sprint-testing-workflow-en/
│   ├── release-testing-workflow/
│   └── release-testing-workflow-en/
├── claude/                          # Claude Code 用（结构同上）
├── opencode/                        # OpenCode 用（结构同上）
├── prompts/                         # 根目录提示词源（中英文均有，供维护与参考）
├── README.md                        # 本文件（中文默认）
└── README_EN.md                     # 英文说明
```

---

## 各平台使用方式

### Cursor

- **项目级**：将对应技能目录复制到项目的 `.cursor/skills/` 下。
  ```bash
  # 中文
  cp -r cursor/daily-testing-workflow /你的项目路径/.cursor/skills/
  # 英文
  cp -r cursor/daily-testing-workflow-en /你的项目路径/.cursor/skills/
  ```
- **用户级**：复制到 `~/.cursor/skills/`，同样按语言选择 `daily-testing-workflow` 或 `daily-testing-workflow-en`。
- 规范：`SKILL.md` 需包含 `name`、`description`（第三人称，含触发场景）；正文建议控制在 500 行以内。

### Claude Code

- 技能目录放在项目的 `.claude/skills/` 下，目录名需与技能 `name` 一致。
  ```bash
  mkdir -p .claude/skills
  cp -r claude/daily-testing-workflow .claude/skills/           # 中文
  cp -r claude/daily-testing-workflow-en .claude/skills/        # 英文
  ```
- 规范：frontmatter 需包含 `name`、`version`（语义化版本）、`description`（建议 ≤ 200 字符）。

### OpenCode

- **项目级**：`.opencode/skills/<技能名>/SKILL.md`
- **全局**：`~/.config/opencode/skills/<技能名>/SKILL.md`
  ```bash
  mkdir -p .opencode/skills
  cp -r opencode/daily-testing-workflow .opencode/skills/        # 中文
  cp -r opencode/daily-testing-workflow-en .opencode/skills/     # 英文
  ```
- 规范：`name` 为小写字母、数字与单连字符（1–64 字符），与目录名一致；`description` 1–1024 字符。

---

## 提示词与 reference（中英文双版本）

- **根目录 `prompts/`**：13 类提示词来源于 awesome-qa-prompt 的 `testing-types/<类型>/`，每类提供**中文 `xxx.md`** 与**英文 `xxx_EN.md`**，用于集中维护与参考。各技能目录下的 `prompts/` 与语言一致：**中文技能**仅包含 `xxx.md`，**英文技能**仅包含 `xxx_EN.md`。执行某一步时，打开当前技能目录下 `prompts/` 中对应文件，与 AI 协同即可。
- **各工作流下的 `reference.md`**：列出该工作流涉及的提示词类型、在本工作流中的用途，以及步骤与提示词文件的对照表，便于在单技能目录内完成「步骤 → 提示词」的查找与执行。
- **SKILL.md 中的「如何使用本技能中的提示词」**：说明「查 reference → 打开本目录 prompts 下对应文件 → 结合上下文与 AI 执行」的三步用法。

---

## 内容来源与约定

- 工作流的阶段、步骤、检查清单与推荐提示词均来自 **awesome-qa-prompt** 的 `workflows/`（中英文版本）。
- 具体执行用的提示词（Role、Task、执行指令等）来自 awesome-qa-prompt 的 `testing-types/<类型>/`，在本仓库的根目录 `prompts/` 以及各工作流目录的 `prompts/` 中以中英文双版本提供，并在各技能的 `reference.md` 中可速查，便于按步骤执行。
- 各平台均按语言拆分为**中文技能目录**（如 `daily-testing-workflow`）与**英文技能目录**（如 `daily-testing-workflow-en`），技能的 `name` 与目录名一致，并按各平台规范调整 frontmatter 与篇幅。

---

## 许可证

与 awesome-qa-prompt 项目保持一致；本仓库仅提供供 AI 工具使用的 Skill 封装，不单独声明新版权。
