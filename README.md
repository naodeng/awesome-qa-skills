<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# Awesome QA Skills

按语言分区的 **AI 测试辅助技能库**（Agent Skills）。面向 Codex、Cursor、Claude Code、Kiro、OpenCode、Trae 等工具，提供可独立安装、可组合调用的测试工作流与测试类型技能。

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](./LICENSE)
[![Skills](https://img.shields.io/badge/skills-76%20(zh%2Ben)-0A7EA4)](./skills-index.md)
[![Workflows](https://img.shields.io/badge/workflows-4-informational)](./skills/zh/testing-workflows/)
[![Testing types](https://img.shields.io/badge/testing%20types-34-informational)](./skills/zh/testing-types/)

**在线站点：** [https://inaodeng.com/qaskills/](https://inaodeng.com/qaskills/)

---

## 为什么用这个仓库

| 能力 | 说明 |
| --- | --- |
| 双语对齐 | `skills/zh` 与 `skills/en` 同名目录、同结构，团队可按语言选用 |
| 覆盖完整测试链 | 从需求分析、策略、用例、执行到缺陷与报告 |
| 工作流 + 类型技能 | 日常 / 迭代 / 发布工作流，配合 34 类专项技能按需组合 |
| 开箱即装 | 支持一键安装与单 skill 安装脚本 |
| 可评测可演进 | 全量 skill 附带 `evals/`，可用 [skill-up](https://github.com/alibaba/skill-up) 校验与实跑 |

每个 skill 目录复制出去后应自洽：含 `SKILL.md`、主提示词、工具元数据，以及可选的示例、模板、脚本与评测用例。

## 支持的 AI 工具

| 工具 | 典型安装目标 |
| --- | --- |
| Codex | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Claude Code | Claude skills 目录（见安装文档） |
| Kiro / OpenCode / Trae | 见 [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) |

也可手动 `cp -r` 单个 skill 目录到对应工具的 skills 路径。

## 5 分钟上手

### 1. 克隆仓库

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. 安装技能（任选其一）

```bash
# 一键：全部工具 × 中英文
bash ./install-skills-mac.sh --tool all --lang all

# 仅 Codex + 中文
bash ./install-skills-mac.sh --tool codex --lang zh

# 单个 skill（示例：功能测试 → Codex）
bash installers/zh/functional-testing/mac/codex.sh
```

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

手动复制：

```bash
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
```

完整参数与工具路径说明：[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

### 3. 在工具中调用

```text
@skill functional-testing
帮我为用户登录功能生成测试用例
```

不确定用哪个 skill 时，先用路由技能：

```text
@skill discover-testing
我要做一次发布前回归，该选哪些技能？
```

---

## 技能目录

单语合计 **38** 个技能（4 工作流 + 34 测试类型）；中英双语共 **76** 个目录。完整索引见 [skills-index.md](skills-index.md)。

### 工作流技能

| 名称 | 目录 | 适用场景 |
| --- | --- | --- |
| 日常测试工作流程 | [`daily-testing-workflow`](skills/zh/testing-workflows/daily-testing-workflow/) | 日常冒烟、缺陷跟进、当日计划 |
| 迭代测试工作流程 | [`sprint-testing-workflow`](skills/zh/testing-workflows/sprint-testing-workflow/) | Sprint 规划、增量验收、迭代风险 |
| 发布测试工作流程 | [`release-testing-workflow`](skills/zh/testing-workflows/release-testing-workflow/) | 发布门禁、回归范围、上线检查 |
| 测试技能路由 | [`discover-testing`](skills/zh/testing-workflows/discover-testing/) | 根据目标推荐应调用的 skill |

### 测试类型技能

#### 核心执行

| 名称 | 目录 |
| --- | --- |
| 功能测试 | [`functional-testing`](skills/zh/testing-types/functional-testing/) |
| API 测试 | [`api-testing`](skills/zh/testing-types/api-testing/) |
| 自动化测试 | [`automation-testing`](skills/zh/testing-types/automation-testing/) |
| 手动 / 探索性测试 | [`manual-testing`](skills/zh/testing-types/manual-testing/) |
| 性能测试 | [`performance-testing`](skills/zh/testing-types/performance-testing/) |
| 安全测试 | [`security-testing`](skills/zh/testing-types/security-testing/) |
| 移动端测试 | [`mobile-testing`](skills/zh/testing-types/mobile-testing/) |
| 可访问性测试 | [`accessibility-testing`](skills/zh/testing-types/accessibility-testing/) |

#### 过程与产出物

| 名称 | 目录 |
| --- | --- |
| 需求分析 | [`requirements-analysis`](skills/zh/testing-types/requirements-analysis/) |
| 测试策略 | [`test-strategy`](skills/zh/testing-types/test-strategy/) |
| 测试用例编写 | [`test-case-writing`](skills/zh/testing-types/test-case-writing/) |
| 测试用例评审 | [`test-case-reviewer`](skills/zh/testing-types/test-case-reviewer/) |
| 代码审查 | [`code-review`](skills/zh/testing-types/code-review/) |
| 缺陷上报 | [`bug-reporting`](skills/zh/testing-types/bug-reporting/) |
| 测试报告 | [`test-reporting`](skills/zh/testing-types/test-reporting/) |
| AI 辅助测试 | [`ai-assisted-testing`](skills/zh/testing-types/ai-assisted-testing/) |

#### 工具专项

| 名称 | 目录 |
| --- | --- |
| API 测试（Bruno） | [`api-test-bruno`](skills/zh/testing-types/api-test-bruno/) |
| API 测试（Postman） | [`api-test-postman`](skills/zh/testing-types/api-test-postman/) |
| API 测试（Pytest） | [`api-test-pytest`](skills/zh/testing-types/api-test-pytest/) |
| API 测试（Rest Assured） | [`api-test-restassure`](skills/zh/testing-types/api-test-restassure/) |
| API 测试（Supertest） | [`api-test-supertest`](skills/zh/testing-types/api-test-supertest/) |
| UI 自动化测试（Selenium） | [`ui-test-selenium`](skills/zh/testing-types/ui-test-selenium/) |
| UI 自动化测试（Playwright） | [`ui-test-playwright`](skills/zh/testing-types/ui-test-playwright/) |
| UI 自动化测试（TestCafe） | [`ui-test-testcafe`](skills/zh/testing-types/ui-test-testcafe/) |
| UI 自动化测试（Cypress） | [`ui-test-cypress`](skills/zh/testing-types/ui-test-cypress/) |
| UI 自动化测试（Puppeteer） | [`ui-test-puppeteer`](skills/zh/testing-types/ui-test-puppeteer/) |
| UI 自动化测试（WebdriverIO） | [`ui-test-webdriverio`](skills/zh/testing-types/ui-test-webdriverio/) |
| 性能测试（k6） | [`performance-test-k6`](skills/zh/testing-types/performance-test-k6/) |
| 性能测试（Gatling） | [`performance-test-gatling`](skills/zh/testing-types/performance-test-gatling/) |
| 性能测试（JMeter） | [`performance-test-jmeter`](skills/zh/testing-types/performance-test-jmeter/) |

#### 增强版（Plus）

| 名称 | 目录 |
| --- | --- |
| 需求分析增强版 | [`requirements-analysis-plus`](skills/zh/testing-types/requirements-analysis-plus/) |
| 测试策略增强版 | [`test-strategy-plus`](skills/zh/testing-types/test-strategy-plus/) |
| 测试用例编写增强版 | [`testcase-writer-plus`](skills/zh/testing-types/testcase-writer-plus/) |
| 测试用例评审增强版 | [`test-case-reviewer-plus`](skills/zh/testing-types/test-case-reviewer-plus/) |

> 英文版本路径将 `skills/zh` 替换为 `skills/en`，目录名与技能名保持一致。语言分区索引：[skills/zh/README.md](skills/zh/README.md) · [skills/en/README.md](skills/en/README.md)

---

## 仓库结构

```text
awesome-qa-skills/
├── skills/
│   ├── zh/                      # 中文技能
│   │   ├── testing-workflows/   # 工作流
│   │   └── testing-types/       # 测试类型
│   └── en/                      # 英文技能（结构同上）
├── scripts/                     # 安装、校验、评测辅助脚本
├── installers/                  # 按 skill / 工具生成的安装快捷脚本
├── AGENTS.md                    # Coding Agent 操作约定
├── skills-index.md              # 全量技能索引
├── README.md / README_EN.md
└── LICENSE                      # GPL-3.0
```

### 单个 Skill 约定结构

```text
skills/{zh|en}/{testing-types|testing-workflows}/<skill-name>/
├── SKILL.md                 # 入口 + YAML frontmatter（必需）
├── prompts/                 # 主提示词（必需）
├── agents/openai.yaml       # OpenAI / Codex 元数据（必需）
├── evals/                   # skill-up 评测用例（本仓库全量具备）
├── output-formats.md        # 可选：多格式输出说明
├── quick-start.md           # 可选：最短上手路径
├── references/ · examples/ · scripts/
└── ...
```

详细规范：[skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) · [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)

## 设计原则

- **语言分区，名称对齐**：中英文 skill 目录名一致，不再使用 `-en` 后缀；英文 prompt 文件名不带 `_EN`。
- **独立可安装**：禁止 skill A 硬链 skill B 内部文件；跨 skill 只做文案推荐。
- **渐进披露**：`SKILL.md` 保持精简；细节放在 `prompts/`、`references/`、`examples/`。
- **可执行产出**：默认 Markdown；需要 Excel/CSV/JSON/Word 时按 `output-formats.md` 切换。
- **安全默认**：示例与文档不硬编码真实 token、密码、私钥；使用环境变量或占位符。

## 质量与评测

提交前建议在仓库根目录运行：

```bash
bash scripts/check_skills_quality.sh
```

该门禁覆盖目录整理、agents 元数据、独立安装约束、完整性校验，以及 skill-up evals YAML 校验。

用 [skill-up](https://github.com/alibaba/skill-up) 校验 / 实跑（可选）：

```bash
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
bash scripts/validate_skill_evals.sh
bash scripts/run_skill_eval.sh skills/zh/testing-types/functional-testing/evals/eval.yaml
```

推荐试点：`functional-testing`、`api-testing`、`api-test-bruno`、`bug-reporting`、`performance-test-k6`。说明见 [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)。

## 文档导航

| 文档 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Coding Agent 约定与质量检查 |
| [skills-index.md](skills-index.md) | 全量技能索引 |
| [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) | 目录与命名规范 |
| [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md) | 编写与 skill-up 评测约定 |
| [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) | 安装参数与工具路径 |
| [FAQ.md](FAQ.md) | 常见问题 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献流程 |
| [skills-graph.md](skills-graph.md) | 技能关系图（参考） |

## 贡献

欢迎提交 Issue / PR：新增 skill、补齐双语、改进 prompt 与 evals、完善安装与文档。

1. 阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)
2. 中英文通常需同步更新（除非明确只要单语）
3. 本地跑通 `bash scripts/check_skills_quality.sh` 后再提 PR

## 许可证

本仓库采用 [GNU GPL v3](./LICENSE)。可自由使用、修改与分发；衍生作品需遵循相同许可证条款。
