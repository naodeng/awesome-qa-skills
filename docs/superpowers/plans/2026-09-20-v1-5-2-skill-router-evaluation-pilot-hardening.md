# v1.5.2 Skill Router 与 Evaluation Pilot Hardening 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在不增加 Skill 数量和不引入第二套评测引擎的前提下，把现有 `discover-testing`、Skill Composition 图和 v1.5.1 评测基础连接成一个可发现、可验证、可回归的最小闭环。

**Architecture:** 新增一个受验证的 `skill-composition.yaml` 作为路由、组合关系和 Recipe 的唯一输入；生成双语 Catalog 视图和可随 `discover-testing` 独立复制的本地 `reference.md`。Router Pilot 复用现有 `skill-up`、trace runner、`skill.selection` 证据、run metadata 和 regression comparator，不新增通用 Eval Engine、Judge 或 Quality Score。

**Tech Stack:** Markdown, JSON-compatible YAML, Python 3 standard library, existing `skill-up` 0.12.0, existing shell quality gates, GitHub Project #4.

---

## 版本边界

### 纳入范围

- `discover-testing` 的结构化路由来源和独立安装参考文档。
- 五条高频组合路线：新功能质量准备、API 交付、变更与回归、性能决策、AI 功能验证。
- 关系类型的最小集合：`precedes`、`recommended_with`、`alternative_to`、`conflicts_with`。
- `discover-testing` Router Pilot、双语 Eval cases、选择事件证据和版本回归比较。
- Composition Manifest 的双语 Catalog 视图、Graph/Recipe 导航和质量门禁。

### 不纳入范围

- 不新增新的物理 Skill 目录。
- 不把 `skill-composition.yaml` 变成安装依赖；复制单个 `discover-testing` 目录后仍必须能读取其本地路由参考。
- 不实现服务端语义路由器、自动执行目标 Skill 或多 Agent 编排器。
- 不引入第二套通用 Eval Engine、Judge、Benchmark runner 或 Quality Score。
- 没有授权模型 endpoint、真实目标或 `skill.selection` trace 时，不把静态验证写成模型、运行时或业务效果证据。
- Cross-model Matrix、真实项目 Benchmark、Usage Analytics 和 `xxx-plus` 到 mode 的迁移留给后续版本。

## 设计单位与文件职责

| 文件 | 职责 |
| --- | --- |
| `docs/governance/skill-composition.yaml` | 路由场景、关系边界、目标 Skill 名称和双语展示信息的唯一结构化输入 |
| `scripts/validate_skill_composition.py` | 校验 schema、目标 Skill 存在性、语言路径、重复关系、主/辅路由约束和独立安装边界 |
| `scripts/generate_skill_composition_views.py` | 从 Manifest 生成 Catalog 视图与 `discover-testing` 本地参考，不手工维护重复表格 |
| `skills/{zh,en}/testing-workflows/discover-testing/reference.md` | 可随单个 Router Skill 复制的本地路由表、组合建议和排除条件 |
| `docs/catalog/skills-composition.md` / `_EN.md` | 面向仓库读者的完整关系与 Recipe 视图 |
| `skills/{zh,en}/testing-workflows/discover-testing/evals/` | Router Pilot 的成功、信息不足、反向控制和代表性路线用例 |
| `docs/governance/SKILL_EVALUATION_PILOTS.md` / `_EN.md` | 登记 Router Pilot 的证据范围、执行命令和 `NOT_RUN` 边界 |
| `scripts/check_skills_quality.sh` | 将 Composition validator、生成视图 freshness 和现有质量门禁串联起来 |

## Task 1: 定义 Composition Contract 并建立 RED 测试

**Files:**
- Create: `docs/governance/skill-composition.yaml`
- Create: `scripts/validate_skill_composition.py`
- Test: `scripts/tests/test_skill_composition.py`

- [x] **Step 1: 写失败测试，锁定 Manifest 合同。**

  测试必须覆盖：五个唯一 route ID；每条路线恰好一个 `primary`；`optional` 最多一个；所有目标 slug 在 `skills/zh` 和 `skills/en` 成对存在；关系类型只能来自四个允许值；关系两端不能相同；同一方向关系不能重复；未知语言文案、未知目标和跨 Skill 内部文件路径必须失败。

- [x] **Step 2: 运行测试并确认 RED。**

  Run:

  ```bash
  python3 -m unittest scripts.tests.test_skill_composition -v
  ```

  Expected: FAIL，因为 Manifest、validator 和测试 API 尚未存在。

- [x] **Step 3: 写入最小 `skill-composition.yaml`。**

  Manifest 至少包含以下五条路线：

  ```yaml
  routes:
    - id: new-feature-quality
      primary: requirements-analysis
      optional: test-strategy
    - id: api-delivery
      primary: api-testing
      optional: api-contract-testing
    - id: change-regression
      primary: change-impact-analysis
      optional: regression-test-selection
    - id: performance-decision
      primary: performance-workload-modeling
      optional: performance-result-analysis
    - id: ai-feature-validation
      primary: ai-feature-testing
      optional: llm-testing
  ```

  每条路线同时记录中文/英文触发意图、适用阶段、`not_for` 边界和交接目标；关系只记录导航语义，不表达安装依赖。

- [x] **Step 4: 实现标准库 validator。**

  `scripts/validate_skill_composition.py --repo-root .` 必须读取 JSON-compatible YAML，复用仓库已有的轻量解析约定；校验失败时输出 route ID、字段名和可修复原因，退出码为 `1`。校验通过时输出路线数、关系数和目标 Skill 数，退出码为 `0`。

- [x] **Step 5: 运行 RED/Green 测试。**

  ```bash
  python3 -m unittest scripts.tests.test_skill_composition -v
  python3 scripts/validate_skill_composition.py --repo-root .
  ```

  Expected: 测试全部通过，Manifest 只引用已有双语 Skill，且没有安装依赖声明。

## Task 2: 生成独立安装 Router Reference 和双语 Composition 视图

**Files:**
- Create: `scripts/generate_skill_composition_views.py`
- Test: `scripts/tests/test_generate_skill_composition_views.py`
- Create: `skills/zh/testing-workflows/discover-testing/reference.md`
- Create: `skills/en/testing-workflows/discover-testing/reference.md`
- Create: `docs/catalog/skills-composition.md`
- Create: `docs/catalog/skills-composition_EN.md`
- Modify: `skills/zh/testing-workflows/discover-testing/SKILL.md`
- Modify: `skills/en/testing-workflows/discover-testing/SKILL.md`
- Modify: `docs/catalog/skills-graph.md`
- Modify: `docs/catalog/skills-graph_EN.md`

- [x] **Step 1: 写生成器测试。**

  测试临时构造一个最小 Manifest，验证生成器能分别生成中文和英文文本；生成结果包含主 Skill、可选 Skill、适用条件和排除条件；生成结果不包含跨 Skill 内部 Markdown 链接；`--check` 能发现被手工改动的输出。

- [x] **Step 2: 运行测试并确认 RED。**

  ```bash
  python3 -m unittest scripts.tests.test_generate_skill_composition_views -v
  ```

  Expected: FAIL，因为生成器和目标视图尚未存在。

- [x] **Step 3: 实现生成器和两个语言版本。**

  生成器必须：

  - 先调用同一套 Manifest 解析/校验逻辑；
  - 输出仓库 Catalog 的完整表格和 Router Skill 的本地参考；
  - 使用 `skills/zh` 与 `skills/en` 的相对目录文字，不写入绝对路径；
  - 保证单独复制 `discover-testing` 后，`reference.md` 不依赖仓库外部文件；
  - 支持 `--check`，输出与现有质量门禁一致的 freshness 结果。

- [x] **Step 4: 将 Router 与 Graph 导航接入生成结果。**

  在两个 `discover-testing/SKILL.md` 中明确先读取同目录 `reference.md`；在现有 `skills-graph` 中增加 Composition Catalog 入口，并保留原有静态生命周期图和“导航不等于安装依赖”的边界说明。

- [x] **Step 5: 运行生成器并验证输出。**

  ```bash
  python3 scripts/generate_skill_composition_views.py --repo-root .
  python3 scripts/generate_skill_composition_views.py --repo-root . --check
  python3 -m unittest scripts.tests.test_generate_skill_composition_views -v
  ```

  Expected: 两种语言的四个输出文件一致更新，第二次 `--check` 通过。

## Task 3: 扩展 `discover-testing` Router Pilot

**Files:**
- Modify: `skills/zh/testing-workflows/discover-testing/prompts/discover-testing.md`
- Modify: `skills/en/testing-workflows/discover-testing/prompts/discover-testing.md`
- Modify: `skills/zh/testing-workflows/discover-testing/evals/eval.yaml`
- Modify: `skills/en/testing-workflows/discover-testing/evals/eval.yaml`
- Create: `skills/zh/testing-workflows/discover-testing/evals/cases/route-new-feature-quality.yaml`
- Create: `skills/zh/testing-workflows/discover-testing/evals/cases/route-api-delivery.yaml`
- Create: `skills/zh/testing-workflows/discover-testing/evals/cases/route-change-regression.yaml`
- Create: `skills/zh/testing-workflows/discover-testing/evals/cases/route-performance-decision.yaml`
- Create: `skills/zh/testing-workflows/discover-testing/evals/cases/route-ai-feature.yaml`
- Create: `skills/en/testing-workflows/discover-testing/evals/cases/route-new-feature-quality.yaml`
- Create: `skills/en/testing-workflows/discover-testing/evals/cases/route-api-delivery.yaml`
- Create: `skills/en/testing-workflows/discover-testing/evals/cases/route-change-regression.yaml`
- Create: `skills/en/testing-workflows/discover-testing/evals/cases/route-performance-decision.yaml`
- Create: `skills/en/testing-workflows/discover-testing/evals/cases/route-ai-feature.yaml`
- Modify: `scripts/tests/test_run_skill_trace_eval.py`

- [x] **Step 1: 为五条路线写失败的 Eval 合同。**

  每个 case 必须要求：一句目标总结、唯一主 Skill、最多一个辅助 Skill、选择理由、下一步交接输入；不得输出完整测试方案；不得把未来未安装能力当作可调用 Skill。中文 case 使用中文自然语言，英文 case 不混入中文描述。

- [x] **Step 2: 运行 `skill-up validate` 并确认新增 case 失败。**

  ```bash
  skill-up validate skills/zh/testing-workflows/discover-testing/evals/eval.yaml
  skill-up validate skills/en/testing-workflows/discover-testing/evals/eval.yaml
  ```

  Expected: 新增 case 尚未满足完整断言时失败；修正断言和 case 引用后再进入 Green。

- [x] **Step 3: 更新 Router Prompt 的来源和交接规则。**

  Prompt 保留现有“唯一主 Skill、辅助最多一个、信息不足仍给当前最佳路由”的原则；新增规则：先读取同目录 `reference.md`，按 Composition route 选择，再回到现有阶段/类型/工具链规则；输出必须说明假设和证据缺口。

- [x] **Step 4: 补充 trace selection 的离线合同测试。**

  在现有 trace runner 测试中加入一个带合法 `skill.selection` 的 Router case 和一个缺少 selection event 的 case；前者验证可观察选择，后者必须保持 `BLOCKED`，不能被解释成 negative trigger 或 PASS。

- [x] **Step 5: 运行 Router Pilot 的结构校验。**

  ```bash
  skill-up validate skills/zh/testing-workflows/discover-testing/evals/eval.yaml
  skill-up validate skills/en/testing-workflows/discover-testing/evals/eval.yaml
  python3 -m unittest scripts.tests.test_run_skill_trace_eval -v
  bash scripts/validate_skill_evals.sh
  ```

  Expected: 双语 Eval 配置通过；离线 trace 合同通过；没有真实模型 replay 时报告状态仍为 `NOT_RUN` 或 `BLOCKED`。

## Task 4: 登记 Router Pilot 并复用现有回归证据链

**Files:**
- Modify: `docs/governance/SKILL_EVALUATION_PILOTS.md`
- Modify: `docs/governance/SKILL_EVALUATION_PILOTS_EN.md`
- Modify: `docs/governance/SKILL_EVALUATION_CONTRACT.md`
- Modify: `docs/governance/SKILL_EVALUATION_CONTRACT_EN.md`
- Test: `scripts/tests/test_skill_evaluation_contract.py`

- [x] **Step 1: 增加 Router Pilot 记录。**

  记录 Skill 为 `discover-testing`，关注 route intent、主/辅唯一性、`skill.selection` 观察、信息不足、负向控制和交接可执行性；明确结构与 `skill-up validate` 可验证，真实模型选择、跨模型一致性和业务路由效果仍为 `NOT_RUN`。

- [x] **Step 2: 扩展 Evaluation Contract 的路由边界。**

  明确 expected route/primary/optional 来自 case，observed route/selection 必须来自包含 `route`、`primary`、`optional`、`selected_skills` 的可观察选择事件或明确的适配器输出；缺少或非法结构化证据为 `BLOCKED`，值不匹配或多选为 `FAIL`。Router Pilot 不产生新的 Quality Score 维度，不把推荐 Recipe 当作强制执行链。

- [x] **Step 3: 写契约测试并先运行失败路径。**

  测试必须检查双语 Pilot 都包含 `discover-testing`、五类 route case、结构化 `skill.selection`、`selected_skills`、`NOT_RUN` 边界和“不新增 Engine/Score”约束。

  ```bash
  python3 -m unittest scripts.tests.test_skill_evaluation_contract -v
  ```

- [x] **Step 4: 更新双语记录并通过测试。**

  ```bash
  python3 -m unittest scripts.tests.test_skill_evaluation_contract -v
  python3 scripts/validate_skill_evaluation_contract.py --repo-root .
  ```

## Task 5: 同步 Catalog、质量门禁和双语文档

**Files:**
- Modify: `scripts/check_skills_quality.sh`
- Modify: `scripts/check_docs_bilingual.py`
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`
- Modify: `docs/catalog/skills-index.md`
- Modify: `docs/catalog/skills-index_EN.md`
- Generated: `docs/catalog/skills-composition.md`
- Generated: `docs/catalog/skills-composition_EN.md`
- Generated: `skills/zh/testing-workflows/discover-testing/reference.md`
- Generated: `skills/en/testing-workflows/discover-testing/reference.md`

- [x] **Step 1: 把 Composition validator 和 freshness check 接入质量门禁。**

  在 `check_skills_quality.sh` 中增加明确的 Composition 检查步骤；失败必须阻断，不允许只打印警告。现有 328 Skill、CLI compatibility、Eval validation、治理 Matrix/Register 和 155+ 仓库测试保持原有语义。

- [x] **Step 2: 更新双语入口和路线图。**

  README 只新增 Router/Composition 入口和简短 Quick Start，不复制完整关系表；两份治理路线图记录 v1.5.2 的目标、非目标、证据边界和当前状态，不能把 Project 卡状态写成发布批准。

- [x] **Step 3: 注册双语文档镜像。**

  将 `docs/catalog/skills-composition.md` 与 `_EN.md` 加入 `check_docs_bilingual.py` 的维护列表；确认 `discover-testing/reference.md` 通过内部 Skill 的 zh/en 路径对等检查。

- [x] **Step 4: 运行所有生成器并检查无无关变更。**

  ```bash
  python3 scripts/generate_skill_inventory.py
  python3 scripts/generate_skill_composition_views.py --repo-root .
  python3 scripts/generate_skill_composition_views.py --repo-root . --check
  python3 scripts/check_docs_bilingual.py --repo-root .
  git diff --check
  git status --short
  ```

  Expected: 只出现 v1.5.2 计划范围内的文件；不修改无关 Skill 内容，不创建新的物理 Skill 目录。

## Task 6: 最终验证和交付判断

**Files:**
- Verify: `scripts/check_skills_quality.sh`
- Verify: `scripts/check_skills_cli_compatibility.sh`
- Verify: `docs/governance/skill-composition.yaml`
- Verify: `docs/governance/SKILL_EVALUATION_PILOTS.md`

- [x] **Step 1: 运行聚焦测试。**

  ```bash
  python3 -m unittest scripts.tests.test_skill_composition -v
  python3 -m unittest scripts.tests.test_generate_skill_composition_views -v
  python3 -m unittest scripts.tests.test_skill_evaluation_contract -v
  python3 -m unittest scripts.tests.test_run_skill_trace_eval -v
  ```

- [x] **Step 2: 运行完整仓库质量门禁。**

  ```bash
  bash scripts/check_skills_quality.sh
  SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh
  git diff --check
  ```

  Expected: 328 Skill compatibility scan 通过，生成视图 freshness 通过，仓库测试通过；若网络、CLI 或真实模型环境不可用，分别记录 `BLOCKED` / `NOT_RUN`，不改写结果。

- [x] **Step 3: 形成证据摘要。**

  摘要必须分别列出：静态 Contract、Skill-up schema、离线 trace selection、真实模型 replay、目标执行、跨模型一致性、Benchmark、Quality Score 和 Project 状态。只有前四项中实际有证据的部分才能写 `PASS`；未执行层保持 `NOT_RUN`、`BLOCKED` 或 `INSUFFICIENT_EVIDENCE`。

- [x] **Step 4: 更新 Project #4 卡片状态。**

  实施开始时为 `In Progress`；只有双语 Composition、Router Pilot、质量门禁和证据摘要全部完成后才转 `Done`。Project 状态不等同 GitHub Release、模型效果或业务验收。

## Definition of Done

- Manifest 合同、validator、生成器和双语视图均有测试。
- `discover-testing` 可在只复制自身目录时读取本地 Router Reference。
- 五条路线能生成稳定的主/辅路由建议，且不输出三项以上候选菜单。
- Router Pilot 有成功、信息不足、负向控制和五条路线用例；结构化选择证据能校验唯一主 Skill 和至多一个辅助 Skill。
- `skill.selection` 缺失时为 `BLOCKED`，不会被推断为未触发或通过。
- 现有 `skill-up`、trace runner、regression comparator 和 Quality Score 合同保持不变。
- 328 个物理 Skill 的既有 CLI/质量门禁通过；无无关目录、路径、canonical name 或安装行为变化。
- 中文和英文文档、Catalog、路线图、Eval、生成视图同步。
- 真实模型、跨模型、目标运行和业务验收证据明确标注，未运行内容不被版本完成状态覆盖。

## Implementation checkpoints

实施时按以下顺序形成可审查的小提交：

1. Composition Contract、validator 和测试。
2. 生成器、本地 Router Reference 和 Catalog 视图。
3. Router Prompt/Eval cases 与 trace contract。
4. Router Pilot、Evaluation Contract 和双语治理记录。
5. CI/README/路线图同步与完整门禁。

本计划本身不执行上述实现、不创建新的 Skill 目录、不提交 Git commit，也不发布版本。
