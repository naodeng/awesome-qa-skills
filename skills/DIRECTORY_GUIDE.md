<div align="right"><strong>🇨🇳 中文</strong> | <a href="./DIRECTORY_GUIDE_EN.md">🇬🇧 English</a></div>

# Skills 目录指南

本仓库使用一个 `skills` 根目录，并按语言、测试类型、测试工作流和 Skill Engineering 分区：

- `skills/zh/testing-types`
- `skills/zh/testing-workflows`
- `skills/zh/skill-engineering`
- `skills/en/testing-types`
- `skills/en/testing-workflows`
- `skills/en/skill-engineering`

## 物理目录与逻辑能力阶段

上述物理包族是稳定的安装契约。不得为了反映产品定位新建能力阶段顶层目录，也不得仅因能力阶段变化而移动已有 Skill。

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

- `testing-types` 承载具体质量能力。
- `testing-workflows` 负责跨阶段编排、节奏、门禁和交接。
- `skill-engineering` 负责 Skill 编写与仓库治理。
- 新增 Skill 前，先查看[演进路线图](../docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md)和已有 Skill。只有输入、主要产物和路由触发条件具有独立边界时才新增；否则作为已有 Skill 的模式补充。

## 单个 Skill 的目录结构

- `SKILL.md`：轻量激活入口，说明流程、约束、按需加载和交付前自检。
- `prompts/`：完整执行规范，必需。
- `agents/openai.yaml`：OpenAI / Codex 元数据，必需。
- `evals/`：skill-up 评测套件，包含 `eval.yaml` 和 `cases/`。
- `reference.md`、`output-formats.md`、`references/`、`examples/` 与 `scripts/`：按需提供的支持材料。

编写和评测约定见 [SKILL_AUTHORING.md](SKILL_AUTHORING.md)。

```bash
python3 scripts/organize_project_dirs.py
bash scripts/check_skills_quality.sh
```
