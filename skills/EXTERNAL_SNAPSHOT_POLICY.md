<div align="right"><strong>🇨🇳 中文</strong> | <a href="./EXTERNAL_SNAPSHOT_POLICY_EN.md">🇬🇧 English</a></div>

# 外部资料快照策略

本仓库通过严格规则保证每个 Skill 可独立安装并可持续维护：优先使用直接来源链接或 Skill 内正式文件；默认不建议 `_external`；临时快照必须使用可读文件名、标注来源、每个 Skill 不超过 5 个，并在完成本地化后删除。

提交前必须运行 `bash scripts/check_skills_quality.sh`。完整英文技术规则如下。

## English Technical Reference

# External Reference Policy

This repository uses a strict policy to keep each skill self-contained and maintainable.

## Rule

1. Prefer direct source links (for approved cross-language prompt links) or in-skill formal files.
2. `_external` snapshots are discouraged by default.
3. If `_external` must be used temporarily:
   - readable file name (no hash-only naming),
   - source annotation in file header,
   - max 5 files per skill,
   - remove after source is localized.

## Required checks

Run before commit:

```bash
bash scripts/check_skills_quality.sh
```

This check includes:
- metadata validation
- skills independence validation
- external snapshot hygiene validation
- non-symlink release build generation
