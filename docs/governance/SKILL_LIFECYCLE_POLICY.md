<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_LIFECYCLE_POLICY_EN.md">🇬🇧 English</a></div>

# Skill 生命周期治理

## 状态

生命周期状态独立于能力治理中的 `Existing`、`Planned-P0`、`Enhance` 等分类。没有实际效果和采用证据时，生命周期保持 `UNASSESSED`；目录存在、Eval 配置有效或静态门禁通过，都不能单独证明 Skill 已稳定或有使用价值。

| 状态 | 含义 | 进入/退出依据 |
| --- | --- | --- |
| `UNASSESSED` | 缺少足够证据作生命周期判断 | 默认状态；补齐使用、行为和维护证据后再评审 |
| `EXPERIMENTAL` | 新能力或重要变更的试点 | 需要明确范围、维护人和 Eval；达到稳定性及采用要求后申请 `STABLE`，无价值则退役 |
| `STABLE` | 行为、兼容和维护预期经过重复验证 | 需要多次版本化行为 Eval、兼容性证据、使用场景记录和维护承诺 |
| `MAINTENANCE` | 保留使用但不继续扩展 | 记录支持边界、已知限制、必要安全修复和迁移目标；需求消失后进入弃用评审 |
| `DEPRECATED` | 不建议新采用，现有用户有迁移窗口 | 必须说明替代方案、兼容窗口、迁移步骤和停止维护日期；不得静默删除 |
| `ARCHIVED` | 停止维护并从常规分发移除 | 迁移与保留期限结束后归档；历史来源和兼容信息仍可查 |

当前治理 Registry 的 `status` 表达能力匹配或路线图分类；新增 `lifecycle` 字段单独记录生命周期。旧条目缺少真实调用/效果数据时标为 `UNASSESSED`。本次三个编排试点保持 `EXPERIMENTAL`，即使结构门禁或个别 Eval 通过也不自动升级。

## 评审证据

生命周期复核至少检查：

- **使用价值：** 来自可核验的实际使用记录；没有采用数据时明确记 `UNASSESSED`。
- **效果与可靠性：** 版本化 Eval 与回归记录；区分配置校验、规则断言、模型行为和宿主运行。
- **独特性与重叠：** 能力范围、输入/输出和触发语义；重叠必须由人工审查后决定增强、合并或退役。
- **兼容与维护：** 独立安装、资源完整性、代理兼容边界、维护成本和安全责任。
- **关键性：** 低频、高风险能力（如灾备、安全事件）可因关键性保留，不以调用次数自动淘汰。

Stable、Maintenance、Deprecated、Archived 的状态变更需要写明审核日期、证据路径、决定理由和复核人；模型生成的自评不能代替独立采纳或业务验收证据。

## 退役与残留

弃用前必须先检查引用、索引、安装入口和下游兼容，并发布迁移说明。旧安装残留检查只读扫描用户指定的安装根目录：识别带 `-en` 旧语言后缀、仓库中已不存在的 Skill、目录名与 `SKILL.md` canonical name 不一致的包。脚本不会自动删除。

```bash
python3 scripts/manage_skill_packages.py check-residue \
  --install-root /path/to/agent/skills --repo-root . --json
```

独立 Skill 包可以打 ZIP；卸载默认为预览，只有显式 `--apply` 才会移除安装根目录下一个带 `SKILL.md` 的直接子目录。升级通过已有安装器覆盖同一 canonical 目录；禁止为升级或清理扫描执行宽泛删除。

```bash
python3 scripts/manage_skill_packages.py pack \
  --skill-dir skills/en/testing-workflows/pr-quality-review \
  --output /tmp/pr-quality-review-en.zip
python3 scripts/manage_skill_packages.py uninstall \
  --install-root /path/to/agent/skills --skill pr-quality-review  # preview
```

## 验证

治理视图使用现有 Registry 和矩阵生成器；证据、状态与安装兼容门禁按其自身范围记录。完成该 Skill 的索引、分类或生命周期更新后，运行 `bash scripts/check_skills_quality.sh` 和 `bash scripts/check_skills_cli_compatibility.sh`。
