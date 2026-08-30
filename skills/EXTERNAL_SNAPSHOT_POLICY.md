<div align="right"><strong>🇨🇳 中文</strong> | <a href="./EXTERNAL_SNAPSHOT_POLICY_EN.md">🇬🇧 English</a></div>

# 外部资料快照策略

本仓库要求每个 Skill 可独立安装、可持续维护。

## 规则

1. 优先使用获准的直接来源链接，或 Skill 内的正式文件。
2. 默认不建议使用 `_external` 快照目录。
3. 若确实需要临时快照：
   - 使用可读文件名，不使用纯哈希名；
   - 在文件头标注来源；
   - 每个 Skill 最多保留 5 个；
   - 来源已本地化后立即删除快照。

## 必做检查

提交前运行：

```bash
bash scripts/check_skills_quality.sh
```

该门禁覆盖元数据、Skill 独立性、快照卫生、双语文档、评测 YAML 和发布目录结构。
