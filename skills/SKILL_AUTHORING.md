# Skill Authoring Guide（对齐 skill-up / Agent Skills）

本指南把 [alibaba/skill-up](https://github.com/alibaba/skill-up) 与 [Agent Skills 最佳实践](https://agentskills.io/skill-creation/best-practices) 落到本仓库的 QA skill 上。人类贡献者与 coding agent 改 skill 时都应遵守。

## 目标

Skill 质量应**可度量、可复现、可演进**：

1. **触发准**：`description` 能让 Agent 在正确时机加载本 skill。
2. **上下文省**：`SKILL.md` 只放每次都会用到的核心约束；细节按需加载。
3. **产出稳**：主 prompt 给出最低覆盖清单、输出结构、质量门槛。
4. **可评测**：关键 skill 提供 `evals/`，可用 `skill-up` 跑回归。

## SKILL.md 约定

### Frontmatter

```yaml
---
name: skill-name
description: Use this skill when ...; triggers include 中文触发词 and English triggers.
---
```

- `name`：小写、数字、连字符；与目录名、`agents/openai.yaml` 的 `metadata.key` 一致。
- `description`：第三人称祈使（`Use this skill when...`）；同时写清 **做什么** 与 **何时用**；含中英触发词；≤1024 字符。
- 不要只写「功能介绍」而缺少 `when` / triggers（触发会偏弱）。

### 正文结构（推荐）

1. **何时使用**：2–4 条真实触发场景。
2. **执行流程**：先读 `prompts/<name>.md`，再补项目上下文；信息不全时给初版并标缺口。
3. **核心约束**：Agent 不知道就会做错的规则（优先级、事实/假设分离、工具默认值等）。
4. **按需加载**：明确 *何时* 读 `references/`、`examples/`、`scripts/`、`output-formats.md`，禁止「见 references/」这种空指针。
5. **交付前自检**：清单式自检，对应 skill-up / agentskills 的 validation loop。
6. **常见误区**：针对本 skill 的 gotchas，而不是万能空话。

`SKILL.md` 宜短于 ~500 行；本仓库多数 skill 应远短于此。

### 与 prompts/ 的关系

- `prompts/` **仍是完整执行规范**（校验脚本要求存在）。
- `SKILL.md` 在激活时加载：写清「必须遵循 prompt 中的覆盖清单/输出结构/质量要求」，避免只有「打开 prompts」而无约束摘要。
- 细节、长模板、框架规范放 `references/` 或 `prompts/`，由 SKILL 按条件引用。

## evals/（skill-up）

与 [skill-up 编写评测](https://alibaba.github.io/skill-up/zh/guide/writing-evals) 对齐：

```text
<skill>/
  SKILL.md
  prompts/
  evals/
    eval.yaml
    cases/
      basic-success.yaml
      edge-incomplete-input.yaml
    fixtures/          # 可选
```

建议：

- 每个 skill 先从 **2–3** 个真实用例起步（成功路径 + 信息不全 + 边界/近邻误用）。
- 优先 `judge.type: rule_based`；语义强、难写关键字时再用 `agent_judge`。
- `environment.type: none` 适合纯文本 QA skill；需要跑脚本/沙箱再换 `opensandbox` / `docker`。
- 用例语言与 skill 语言一致（中文 skill → 中文 prompt/断言；英文 skill → 英文）。
- 不要为了让用例通过而削弱合理断言。

生成脚手架：

```bash
python3 scripts/scaffold_skill_evals.py --skill skills/zh/testing-types/functional-testing
python3 scripts/scaffold_skill_evals.py --all-missing --lang zh
```

本地运行（需已安装 skill-up 与对应 Agent Engine；本机可用已登录的 Codex / Claude）：

```bash
# 安装 CLI
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash

# 仅校验 YAML（不消耗模型，已接入 check_skills_quality.sh）
bash scripts/validate_skill_evals.sh

# 实跑（示例：用 Codex 引擎跑单个 case；产物放到仓库外的工作区，避免污染 skills/）
mkdir -p .skill-up-workspaces
skill-up run skills/zh/testing-types/functional-testing/evals/eval.yaml \
  --engine codex \
  --include-case-name "basic-success" \
  --output-dir .skill-up-workspaces/functional-testing

# Claude Code 需先完成非交互登录 / 配置 ANTHROPIC_API_KEY
skill-up run skills/zh/testing-types/functional-testing/evals/eval.yaml --engine claude_code
```

注意：

- `title` 等含英文冒号 `:` 的字段必须加引号，否则 `skill-up validate` 会失败。
- 信息不完整类用例优先断言 prompt 输出结构词（如中文「待确认」、英文 `Open Questions`），避免过脆的同义词。
- 运行产物在 `<skill>-workspace/`（已 gitignore），不要提交。

演进闭环（推荐配合上游 [skill-upper](https://github.com/alibaba/skill-up/tree/main/skills/skill-upper)）：评测 → 诊断失败 → 修 SKILL/prompt 或修 eval → 补回归用例 → 再跑。

安装 skill-upper（可选）：

```bash
npx skills add https://github.com/alibaba/skill-up/tree/main/skills/skill-upper -g -a codex -y
```

## description 优化提示

- 写用户意图，不写内部实现细节。
- 覆盖「用户没点名 skill 但语义匹配」的场景。
- 用近邻负例自检（例如 CSV 分析 vs Excel 改公式），避免 description 过宽误触发。
- 改完后可用 skill-up / 手工抽样验证触发是否合理。

## 禁止事项

- 示例与 prompt 中硬编码真实 token、密码、cookie、私钥。
- skill A 的 markdown 链接指向 skill B 内部文件（破坏独立安装）。
- 把 `Reference/` 大段无差别复制进多个 skill。
- 为通过评测而删除有效断言。

## 改完后

```bash
bash scripts/check_skills_quality.sh
```
