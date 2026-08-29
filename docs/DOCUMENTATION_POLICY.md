<div align="right"><strong>🇨🇳 中文</strong> | <a href="./DOCUMENTATION_POLICY_EN.md">🇬🇧 English</a></div>

# 双语文档维护策略

## 默认语言

中文是项目默认语言。GitHub 默认入口为根目录 `README.md`；英文用户通过页面顶部链接切换到 `README_EN.md`。

## 必须双语镜像的文档

- 根 README、贡献指南、FAQ 和全量 Skill 索引
- 当前能力演进路线图
- 当前有效的设计文档、实施计划和审计报告
- `skills/` 下的目录、编写、风格和外部快照治理规范
- `skills/zh` 与 `skills/en` 的语言入口 README
- Skill 内的 `SKILL.md`、主 Prompt、README、quick-start、tutorial、输出格式和工作流 reference

项目级文档使用 `NAME.md`（中文）和 `NAME_EN.md`（英文），并在顶部提供双向切换。

Skill 内部文档不使用 `_EN` 文件，也不增加逐文件语言切换；它们通过 `skills/zh` 和 `skills/en` 相同相对路径形成语言镜像。

## 不要求逐文件翻译的内容

- `docs/archive/` 中的归档记录
- 2026-08-29 之前已经完成的 `docs/superpowers/plans/` 与 `specs/` 历史执行记录
- `legacy-prompts/` 兼容内容
- examples、references、output templates、评测 fixtures 等语言专属辅助材料
- 自动生成的 `skills-graph.md`、`skills-metadata-report.md` 和评测运行产物
- 内部草稿、Agent 交接上下文和第三方许可文本

这些文件可以保留单语或自身已包含的双语内容，但不得成为当前用户文档的唯一正式入口。

## 自动校验

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
bash scripts/check_skills_quality.sh
```

校验覆盖项目级文档镜像、双向切换、Skill 维护文档路径对齐、README 分类完整性，以及中英文 testing-type 目录一致性。
