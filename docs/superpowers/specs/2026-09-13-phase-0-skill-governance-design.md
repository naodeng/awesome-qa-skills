<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-13-phase-0-skill-governance-design_EN.md">🇬🇧 English</a></div>

# Phase 0 Skill 治理数据化设计

## 目标

将现有 79 个双语 Skill 对从“物理目录盘点 + 治理规则文本”升级为可复现、可校验的逐项治理数据：完整 Matrix、可追溯的候选能力匹配结论，以及严格标注证据范围的 Quality Score / Eval 状态。

## 范围与非目标

本期覆盖 `skills/{zh,en}/` 的 79 个逻辑 Skill 对，以及 `SKILL_MATCHING_REGISTER.md` 中已登记的候选能力。每条记录必须提供虚拟 Domain、SDLC 阶段、角色、治理状态、关联关系、证据定位和下一步动作；候选项完成六步 Capability Match 后只可得到 `EXISTING`、`MATCH`、`ENHANCE`、`MERGE` 或 `NEW`。

本期不新增或删除 Skill 目录，不执行 Prompt、模型或外部测试目标，不以目录结构推断语义等价或运行效果，也不把未运行的 Eval 写成通过。Phase 1 的 Shift-Left 功能增强在本期匹配结论之后另行排期。

## 设计

### 单一事实源与生成物

新增 `docs/governance/skill-governance-registry.yaml` 作为逐项治理事实源。每个 logical Skill 使用目录名作为唯一键，并声明：Domain、SDLC 阶段、角色、状态、优先级、输入/输出摘要、关联 Skill、Workflow、Match / Merge / Enhance / Deprecation 字段、Quality Score 状态，以及对应中英文目录。候选能力另以清晰的 `candidates` 记录六步匹配证据、结论、目标和下一步。

新增确定性生成器 `scripts/generate_skill_governance_matrix.py`，将 registry 与物理 `skills/` 清单交叉校验，再生成中英文 `docs/SKILL_MATRIX*.md` 和 `docs/SKILL_MATCHING_REGISTER*.md`。它必须拒绝：缺失或多余的 Skill、未成对语言目录、未知状态/结论、`NEW` 缺少 Scope / Non-goals、以及声称评分已完成却没有可复核证据的记录。

生成的 Matrix 与 Register 是展示层，不能手改；registry 才是治理决定的可审计来源。现有 `generate_skill_inventory.py` 仍只负责物理目录快照，不承担语义或质量断言。

### 证据边界

每个 Skill 的 `quality_score` 固定使用 `NOT_SCORED`、`PARTIALLY_SCORED` 或 `SCORED`。`SCORED` 必须逐维附上 9 个评分维度的数值、评审证据路径与总分；其他状态必须说明缺失证据，且不得产生 Stable / Beta 等质量结论。Eval 同时分离“文件结构”与“执行结果”：当前可从仓库收集的仅是结构证据；执行状态默认 `NOT_RUN`，除非本期实际运行并记录命令和结果。

Capability Match 必须按名称、目的、输入、输出、决策逻辑和 Workflow 角色六项记录证据。匹配结论不等于效果证明，`EXISTING` / `MATCH` 也不自动表示内容无需后续评审。

### 质量门禁与兼容性

`check_skills_quality.sh` 增加 registry-to-generated-output 的新鲜度检查，但保留现有物理目录盘点和 v1.0 治理库存检查。所有现有目录、安装脚本和跨文档入口保持兼容；README、Catalog/Graph 只在导航或生成命令变化时同步。

生成器需要单元测试覆盖：79 对完整输入、缺失/额外目录、无效枚举、`NEW` 的必填边界、未评分状态、评分证据完整性、候选六步证据，以及 `--check` 发现生成物漂移。完整仓库门禁与 `git diff --check` 是本期最终验证；它们不替代模型 Eval 或运行质量结论。

## 数据流

```text
skills/{zh,en}/ + registry.yaml
        │ 交叉校验
        ▼
generate_skill_governance_matrix.py
        ├── docs/SKILL_MATRIX.md / _EN.md
        ├── docs/SKILL_MATCHING_REGISTER.md / _EN.md
        └── --check（质量门禁）
```

## 验收标准

1. registry 对 79 个逻辑双语 Skill 对一一覆盖，且与物理目录无漂移。
2. Matrix 与 Matching Register 均由生成器生成，中文与英文信息结构一致并有互链。
3. 已登记候选项全部拥有六步匹配证据和一个合法结论；只有 `NEW` 才进入后续新增排期。
4. Quality Score 与 Eval 执行状态不夸大证据；未评分/未执行项保持明确状态。
5. 新生成器的针对性测试、完整 `check_skills_quality.sh` 与 `git diff --check` 全部通过。

## 风险与取舍

79 条逐项治理判断需要人工可复核的证据，不能用名称或目录相似度批量猜测。为此，本期宁可将语义/评分保持 `NOT_SCORED` 或 `UNASSESSED`，也不制作虚假的覆盖率或成熟度结论。候选匹配的结论会影响后续是否创建目录，因此任何 `NEW` 都要求比其它结论更完整的边界说明。
