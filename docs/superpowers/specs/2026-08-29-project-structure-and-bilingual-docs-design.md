<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-08-29-project-structure-and-bilingual-docs-design_EN.md">🇬🇧 English</a></div>

# 项目目录与双语文档治理设计

## 目标

整理项目级目录，让根目录只保留用户入口、贡献入口、许可、Agent 约定和兼容安装入口；同时审查当前有效的项目级文档，确保中文为默认版本、英文镜像完整、内容正确且可双向切换。

`skills/` 是安装与分发契约，本次不移动、不改名、不删除其下任何目录。

## 目录设计

```text
docs/
├── catalog/       # Skill 索引与关系图
├── governance/    # 文档策略与能力演进路线图
├── generated/     # 可重新生成的项目报告
├── reviews/       # 当前有效审查
├── superpowers/   # 设计与实施记录
└── archive/
    ├── reviews/   # 过期审查
    └── internal/  # 内部草稿
```

根目录保留 `README*`、`CONTRIBUTING*`、`FAQ*`、`LICENSE`、`AGENTS.md`、两份安装兼容入口及现有工程目录。

## 文件迁移

- `skills-index.md` / `skills-index_EN.md` → `docs/catalog/`
- `skills-graph.md` → `docs/catalog/skills-graph.md`
- `skills-metadata-report.md` → `docs/generated/skills-metadata-report.md`
- `docs/DOCUMENTATION_POLICY*` → `docs/governance/`
- `docs/QA_SKILLS_EVOLUTION_ROADMAP*` → `docs/governance/`
- `SKILLS_REVIEW_REPORT.md` → `docs/archive/reviews/SKILLS_REVIEW_REPORT-2026-08-07.md`
- `SYSTEM_AGENT_DRAFT.md` → `docs/archive/internal/SYSTEM_AGENT_DRAFT.md`

被迁移文件的站内链接、校验清单和生成脚本输出路径同步更新。根级安装脚本不迁移，以保持 README 和生成安装器的兼容接口。

## 双语文档边界

当前有效的项目级用户与治理文档必须采用中文 `NAME.md`、英文 `NAME_EN.md`，并在顶部提供双向切换。中文是默认入口。

以下内容不强制双语：历史归档、生成报告、内部草稿、第三方许可、评测与本地运行产物。Skill 内部文档继续通过 `skills/zh` 与 `skills/en` 同路径镜像，不增加逐文件切换链接。

## 内容审查

审查不仅确认文件存在，还核对：

- 中英文标题、章节与核心结论一致；
- Skill 数量、分类和演进状态与当前仓库一致；
- 相对链接在迁移后仍能解析；
- 中文文档保持默认入口，英文文档可返回中文；
- 过期报告不得继续被描述为当前结论。

## 自动校验

扩展 `scripts/check_docs_bilingual.py`：

- 使用新的项目文档路径；
- 验证项目级文档对及双向切换；
- 检查维护型项目文档的相对 Markdown 链接；
- 保留 README Skill 分类完整性和中英文 Skill 目录一致性检查。

最终运行单元测试、`bash scripts/check_skills_quality.sh`、`git diff --check`，并比较变更前后 `skills/` 目录树。

## 工作区安全

仓库当前存在用户未提交的脚本修改。实施时保留这些内容；若必须修改同一脚本，只提交本任务新增的相关差异，不回退其他改动。
