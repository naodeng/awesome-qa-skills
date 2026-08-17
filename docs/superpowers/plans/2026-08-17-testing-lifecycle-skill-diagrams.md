# 测试生命周期 Skill 图集实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 基于仓库现有 Skill 与工作流证据，交付三张经过 Archify showcase 校验和桌面视觉检查的中文交互图。

**Architecture:** 每张图使用独立 Archify JSON 规格与同名自包含 HTML，集中存放在 `docs/diagrams/testing-lifecycle-skills/`。图 1、图 3 使用 `workflow` 表达阶段与节奏，图 2 使用 `dataflow` 表达请求、路由、产物和门禁流转；三张图共享内容口径，但不共享运行时代码或私有依赖。

**Tech Stack:** Archify CLI、JSON、独立 HTML、Chromium 桌面视觉检查、Git。

## Global Constraints

- 只表达仓库已经存在的能力与约束，不虚构运行时编排、自动调用或测试执行结果。
- 读者文案使用中文；Skill 名、命令和代码标识保留英文。
- `meta.quality_profile` 必须为 `showcase`；不设置动画或额外 Viewer Runtime 功能。
- 每张图最多 12 个主节点，保持一条明显主路径与短侧分支。
- 首次候选只使用自动路由；仅在诊断明确要求时增加一个几何控制。
- 每张最终规格必须通过 9 项 artifact checks，且 composition errors 与 warnings 均为 0。
- 每张 HTML 必须通过 1440×900、1600×1000、1920×1080、2048×1320 的 containment 检查，并人工检查最小与最大尺寸明暗主题截图。
- Archify 最终 `validate` 通过后冻结 JSON；不得在交付前后继续修改已冻结规格。

---

### Task 1: 完整测试生命周期全景图

**Files:**
- Create: `docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.json`
- Create: `docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.html`
- Generated evidence: `docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.visual-check.*`

**Interfaces:**
- Consumes: `skills/zh/README.md` 中测试类型清单，以及已确认设计中的生命周期与 Skill 映射。
- Produces: `workflow` 规格和自包含 HTML；供读者按阶段定位主 Skill 与专项执行分支。

- [ ] **Step 1: 读取 Archify workflow 契约**

在 `/Users/nao.deng/.agents/skills/archify/` 中只读取 `schemas/workflow.schema.json`、`schemas/common.schema.json` 和一个 workflow JSON 示例；读取后的下一个工具动作必须创建候选 JSON。

- [ ] **Step 2: 创建首次候选规格**

建立左到右主线：需求分析、策略设计与评审、实现与用例、执行、缺陷闭环、报告与评审、Human 发布决定。将接口/UI、移动/可访问性、性能/安全、自动化压缩为测试执行附近的短分支；使用设计文档列出的真实 Skill 名。

- [ ] **Step 3: 运行 showcase 校验并定向修复**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs validate workflow docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.json --quality showcase --json
```

Expected: 9 项 artifact checks，`compositionErrors: 0`，`warnings: 0`。每轮只修改诊断指出的 subject；若连续两轮没有降低最佳错误数，则停止并如实记录。

- [ ] **Step 4: 交付 HTML**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs deliver workflow docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.json docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.html --quality showcase --json
```

Expected: exit 0，并记录 specification/artifact SHA-256 与字节数。

- [ ] **Step 5: 收集并人工检查视觉证据**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs visual-check docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview.html --json
```

Expected: 四个桌面尺寸均无溢出；打开 contact sheet 检查主路径、中文可读性、明暗主题、空白平衡、遮挡和歧义连线。

- [ ] **Step 6: 提交图 1**

```bash
git add docs/diagrams/testing-lifecycle-skills/testing-lifecycle-overview*
git commit -m "docs(diagrams): add testing lifecycle overview"
```

### Task 2: 阶段与 Skill 路由图

**Files:**
- Create: `docs/diagrams/testing-lifecycle-skills/stage-skill-routing.json`
- Create: `docs/diagrams/testing-lifecycle-skills/stage-skill-routing.html`
- Generated evidence: `docs/diagrams/testing-lifecycle-skills/stage-skill-routing.visual-check.*`

**Interfaces:**
- Consumes: `discover-testing`、三类工作流、类型 Skill、`multi-role-quality-synthesis` 和评审 Skill 的现有职责约束。
- Produces: `dataflow` 规格和自包含 HTML；供读者理解请求、路由、执行产物、角色汇总与 Human 门禁之间的数据流。

- [ ] **Step 1: 读取 Archify dataflow 契约**

在 `/Users/nao.deng/.agents/skills/archify/` 中只读取 `schemas/dataflow.schema.json`、`schemas/common.schema.json` 和一个 dataflow JSON 示例；读取后的下一个工具动作必须创建候选 JSON。

- [ ] **Step 2: 创建首次候选规格**

建立“用户请求 → `discover-testing` → 工作流/类型 Skill → 阶段产物 → 多角色汇总/评审 → Human 决定”的主数据流。用分组说明工作流负责节奏与门禁、类型 Skill 负责具体产物；明确“1 个主 Skill，必要时 1 个辅助 Skill”和“不新增事实”。

- [ ] **Step 3: 运行 showcase 校验并定向修复**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs validate dataflow docs/diagrams/testing-lifecycle-skills/stage-skill-routing.json --quality showcase --json
```

Expected: 9 项 artifact checks，`compositionErrors: 0`，`warnings: 0`；遵循同一轮次停止规则。

- [ ] **Step 4: 交付 HTML**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs deliver dataflow docs/diagrams/testing-lifecycle-skills/stage-skill-routing.json docs/diagrams/testing-lifecycle-skills/stage-skill-routing.html --quality showcase --json
```

Expected: exit 0，并记录 specification/artifact SHA-256 与字节数。

- [ ] **Step 5: 收集并人工检查视觉证据**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs visual-check docs/diagrams/testing-lifecycle-skills/stage-skill-routing.html --json
```

Expected: 四个桌面尺寸均无溢出；contact sheet 中分层、标签、箭头方向和职责边界清晰。

- [ ] **Step 6: 提交图 2**

```bash
git add docs/diagrams/testing-lifecycle-skills/stage-skill-routing*
git commit -m "docs(diagrams): add stage skill routing map"
```

### Task 3: 日常—迭代—发布三级协作图

**Files:**
- Create: `docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.json`
- Create: `docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.html`
- Generated evidence: `docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.visual-check.*`

**Interfaces:**
- Consumes: `daily-testing-workflow`、`sprint-testing-workflow`、`release-testing-workflow` 的阶段、门禁与交接边界。
- Produces: `workflow` 规格和自包含 HTML；供读者比较三种节奏及其共享类型 Skill 能力带。

- [ ] **Step 1: 复用已读取的 workflow 契约并创建首次候选规格**

建立日常、迭代、发布三条泳道，并设置共享能力带：需求与策略、用例设计、专项执行、缺陷报告、测试报告。日常证据进入迭代门禁，迭代证据进入发布门禁；不把时间推进画成测试通过。

- [ ] **Step 2: 运行 showcase 校验并定向修复**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs validate workflow docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.json --quality showcase --json
```

Expected: 9 项 artifact checks，`compositionErrors: 0`，`warnings: 0`；遵循同一轮次停止规则。

- [ ] **Step 3: 交付 HTML**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs deliver workflow docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.json docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.html --quality showcase --json
```

Expected: exit 0，并记录 specification/artifact SHA-256 与字节数。

- [ ] **Step 4: 收集并人工检查视觉证据**

Run:

```bash
node /Users/nao.deng/.agents/skills/archify/bin/archify.mjs visual-check docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration.html --json
```

Expected: 四个桌面尺寸均无溢出；contact sheet 中三条节奏、共享能力和证据升级关系清晰。

- [ ] **Step 5: 运行仓库级收尾检查**

Run:

```bash
git diff --check
rg -n 'TBD|TODO|<[A-Za-z][^>]*>' docs/diagrams/testing-lifecycle-skills docs/superpowers/plans/2026-08-17-testing-lifecycle-skill-diagrams.md
bash scripts/check_skills_quality.sh
```

Expected: `git diff --check` 无输出；占位符扫描仅允许说明性文字中的显式关键词；Skill 质量门禁通过。

- [ ] **Step 6: 提交图 3 与最终证据**

```bash
git add docs/diagrams/testing-lifecycle-skills/workflow-levels-collaboration* docs/superpowers/plans/2026-08-17-testing-lifecycle-skill-diagrams.md
git commit -m "docs(diagrams): add workflow levels collaboration map"
```
