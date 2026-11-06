# Project #4 Skill Cards Batch Closeout Implementation Plan

> **For agentic workers:** 用户审阅后使用 superpowers:executing-plans 按任务顺序实施。步骤用复选框跟踪。

**目标：** 在一个统一执行批次中，完成 GitHub Project #4 当前 23 张 Skill 相关 Todo 卡片的能力匹配、必要的双语 Skill / Workflow 更新、治理同步、验证和卡片收口。

**方案：** 先建立 23 张卡与现有能力之间的映射，再分为 AI / LLM Skill 复核、跨领域增强复核、Workflow 复核三个工作流。所有工作共用一份匹配与验收记录，只有证据证明能力确实缺失时才新建目录；最后统一生成治理视图、运行质量门禁并收口 Project 卡。

**技术栈：** Markdown、JSON-compatible YAML、Python 3、现有治理生成器、skill-up、GitHub Projects CLI。

**依据：** GitHub Project #4；docs/governance/SKILL_GOVERNANCE_ROADMAP.md；docs/SKILL_MATCHING_GUIDE.md；docs/governance/skill-governance-registry.yaml；docs/governance/skill-composition.yaml；仓库 AGENTS.md。

## 当前范围

截至 2026-11-06，Project #4 有 171 张卡，其中 36 张为 Todo。本计划覆盖其中 23 张 Skill 相关卡，当前均为 Todo。Status 仅有 Todo、In Progress、Done 三种值；本批完成必须以 Done 为准：

- 9 张 v4.1 Existing Enhance Review：ai-agent-testing、agent-tool-testing、ai-assisted-testing、ai-feature-testing、ai-generated-test-review、llm-testing、llm-evaluation-design、prompt-testing、prompt-injection-testing（P1 / v1.6）。
- 6 张 Enhance Review：Requirement Strategy Impact（P1 / v1.6）；Test Case 能力边界、API 方法论与 Tool Adapter、UI E2E 方法论与 Tool Adapter、Performance 能力分层（P2 / v1.7）；AI LLM Agent 能力边界（P1 / v1.6）。
- 8 张 Workflow 卡：requirement-quality-workflow（P1 / v1.6）；test-analysis-workflow、automation-quality-workflow、release-quality-workflow、continuous-quality-workflow 两张、ai-native-quality-workflow 两张（P2 / v1.7）。

仓库当前有 169 组双语 Skill 包，结构门禁已覆盖这些包。上述卡片代表待复核或增强的工作，不表示都缺少 Skill 目录。当前 testing-workflows 下每种语言有 14 个 Skill；6 个 Workflow 卡名都不是现存目录的精确 slug，因此必须先匹配现有 Workflow 能力，再决定复用、增强、合并或新增。

## 全局约束

- 先匹配，后增强；先合并，后新增。匹配结论必须记录 EXISTING、ENHANCE、MERGE、MATCH 或 NEW 及其证据。
- 只在结论为 NEW 时新增 Skill 目录。维持目录名、SKILL.md name 和 agents/openai.yaml metadata.key 一致。
- 对需要修改的 Skill 同步中文和英文版本；各包保持独立可安装，不增加跨 Skill 文件依赖。
- 保留卡片现有 Priority 和 Target Version；“一个批次”表示统一实施与验收，不自动改写 v1.6 / v1.7 排期字段。
- 静态审查、YAML 校验、skill-up 行为评测、运行时验证和人工验收分开记录。未执行的证据保持 NOT_RUN / NOT_SCORED / UNASSESSED。
- 每个行为契约发生变化的 Skill 都必须运行对应的 skill-up Eval。若引擎、凭据或环境阻塞，记录 BLOCKED / NOT_RUN，并保留卡片为 Todo 或 In Progress；未获明确接受延期前不得标记 Done。
- 不更新 Project 状态，直到对应交付和证据通过复核。重复卡不删除；确认为重复后，共用一份实施证据并在收口记录中相互注明。

## 评审重点

- ai-native-quality-workflow 存在两张同名 Todo 卡：先核实正文和卡片 ID；若范围相同，复用一份交付证据。
- continuous-quality-workflow 分别出现在 v3.4 与 v4.0 卡片中：核实两张卡的阶段目标是否不同；同一 canonical Skill 的内容只维护一份，阶段性治理交付分别记录。
- 6 个 Workflow 卡名不是现存目录名：检查 14 个双语 Workflow 包及 composition 路由，不从名称推导需要新增目录。
- 9 个 AI / LLM 复核对象彼此相邻：明确 ai-assisted-testing（AI for QA）、ai-feature-testing（AI 产品功能）、ai-agent-testing（Agent 系统）、agent-tool-testing（工具边界）、ai-generated-test-review（AI 生成测试资产审查）、llm-testing / llm-evaluation-design、prompt-testing / prompt-injection-testing 的责任边界；并将“AI LLM Agent 能力边界”卡与这 9 项交叉复核，避免重复分析和重复覆盖。
- 如真实模型或受控执行环境不可用，完成结构和静态验证后仍将行为评测标为 NOT_RUN，不将其描述为通过。

---

### Task 1：建立卡片—能力映射和单一验收记录

**文件：**
- 创建：docs/governance/PROJECT_4_SKILL_CARDS_CLOSEOUT.md
- 创建：docs/governance/PROJECT_4_SKILL_CARDS_CLOSEOUT_EN.md
- 只读来源：GitHub Project #4、docs/governance/skill-governance-registry.yaml、docs/governance/skill-composition.yaml、docs/SKILL_MATRIX.md、docs/SKILL_MATCHING_REGISTER.md

- [x] 读取 23 张目标卡的当前 item ID、标题、正文、Status、Priority 和 Target Version；把其他 13 张 Todo 卡排除在本批范围外。
- [x] 为每张卡记录意图、现有目标 Skill、匹配决策、证据路径、需修改文件、Eval 需求和最终验收状态。
- [x] 对两张 ai-native-quality-workflow 卡及两张 continuous-quality-workflow 卡分别写明重复关系或阶段差异，不预先合并其 Project 状态。
- [x] 让中英文 closeout 文档保持同一张卡清单、同一决策和同一证据边界。

**验收：** 23 张卡都在映射表中各有一行；没有仅凭卡片标题判定 NEW；重复卡处理方式有证据和明确责任范围。

### Task 2：完成 15 张 Enhancement Review 的能力判断

**范围：** 9 张 v4.1 Existing Enhance Review 卡，以及 6 张 Requirement Strategy / Test Case / API / UI E2E / Performance / AI LLM Agent 能力复核卡。

**文件：**
- 复核现有目录：skills/zh/、skills/en/ 下与每项匹配结论对应的 Skill 包。
- 更新来源：docs/governance/skill-governance-registry.yaml。
- 生成视图：docs/SKILL_MATRIX.md、docs/SKILL_MATRIX_EN.md、docs/SKILL_MATCHING_REGISTER.md、docs/SKILL_MATCHING_REGISTER_EN.md。

- [x] 对 9 个 AI / LLM 对象逐对阅读中英文 SKILL.md、Prompt、Eval 和相关 Matrix / Registry 记录，记录现状与责任边界。
- [x] 将“AI LLM Agent 能力边界”与上述 9 个对象合并做一次边界分析；对其余 5 个增强主题定位实际目标 Skill。若主题横跨多个包，记录各包的分工与共同边界，不强行选单一 slug。
- [x] 将每项结论归入 EXISTING、ENHANCE、MERGE、MATCH 或 NEW，并列出具体差异和最小修改范围。
- [x] 对已有能力足够的卡，提供可追溯的匹配证据，不为了把卡做成代码变更而改写 Skill。

**验收：** 15 张卡都有证据支持的决策；需要修改的内容明确落到中英文目标包；不存在因相近名称产生的重复 Skill。

### Task 3：完成 8 张 Workflow 卡的合并复核

**目标卡：** requirement-quality-workflow、test-analysis-workflow、automation-quality-workflow、release-quality-workflow、continuous-quality-workflow（v3.4 与 v4.0）、ai-native-quality-workflow（两张同名卡）。

**文件：**
- 复核现有双语目录：skills/{zh,en}/testing-workflows/
- 来源：docs/governance/skill-composition.yaml
- 生成视图：docs/catalog/skills-composition.md、docs/catalog/skills-composition_EN.md、skills/{zh,en}/testing-workflows/discover-testing/reference.md

- [x] 将 6 个名称映射到现有 Workflow 包、组合路由或现有 testing-types Skill 的工作流角色。
- [x] 区分可由现有包和组合路由承担的内容，以及确实需要独立 Workflow Skill 的剩余能力。
- [x] 对 continuous-quality-workflow 的 v3.4 / v4.0 卡明确是一个内容包加两个治理范围，还是两个有证据的独立范围。
- [x] 对两张同名 ai-native-quality-workflow 卡确认正文范围；相同范围共用一份能力和 Eval 交付，不同范围分别记账。
- [x] 仅当匹配结果为 NEW 时创建目录；否则增强现有包或更新 composition manifest。

**验收：** 每张 Workflow 卡都有目标路径或路由映射；同一 canonical Skill 只维护一份双语内容；新增项有差异证据。

### Task 4：实施获批的双语 Skill 变更

**文件：**
- 修改：Task 1–3 决策确定的 skills/zh/ 与 skills/en/ leaf Skill 包。
- 仅在匹配结论为 NEW 时创建新目录。

- [x] 按目标包更新 SKILL.md、主 Prompt、agents/openai.yaml、evals/eval.yaml 和 evals/cases/*.yaml 中受影响的内容。
- [x] 每个变更后的 Skill 至少保留成功路径、信息不完整、范围或风险边界三类 Eval 用例。
- [x] 对只需要 Match / Existing 结论的卡不改动 Skill 文件；在 closeout 记录中注明 N/A 及来源证据。
- [x] 对行为契约改变的包补充回归用例；不以放宽有效断言来获得通过。

**验收：** 每个变更包中英文结构和能力边界对应；新建包可独立复制；新增或修改的 Eval 通过静态验证。

### Task 5：同步治理来源与生成视图

**文件：**
- 权威来源：docs/governance/skill-governance-registry.yaml、docs/governance/skill-composition.yaml。
- 生成视图：SKILL_MATRIX、SKILL_MATCHING_REGISTER、Skills Composition Catalog、Router reference，以及受实际影响的中英文 README / Catalog。

- [x] 只编辑 Registry 和 Composition manifest 等权威来源，不手改生成视图。
- [x] 运行 python3 scripts/generate_skill_governance_matrix.py 和 python3 scripts/generate_skill_composition_views.py。
- [x] 按新增、改名或边界变化同步 docs/catalog/skills-index.md、skills/zh/README.md、skills/en/README.md 和根 README；未受影响的入口保持不变。
- [x] 运行对应生成器的 --check 模式，确认生成视图与来源一致。

**验收：** 治理文档只声明已审阅内容；未运行的评测、运行时效果、发布批准和业务验收继续保留未验证状态。

### Task 6：运行完整质量与行为验证

- [x] 对所有受影响文件运行 git diff --check。
- [x] 运行 bash scripts/check_skills_quality.sh。
- [x] 运行 bash scripts/check_skills_cli_compatibility.sh。
- [x] 运行 bash scripts/validate_skill_evals.sh，并确认所有新增或修改的 Eval YAML 均通过。
- [x] 对每个行为契约改变的 Skill，按 Task 1 确定的 category 和 canonical slug 分别运行中英文 Eval：bash scripts/run_skill_eval.sh skills/zh/<category>/<canonical-skill>/evals/eval.yaml，以及 bash scripts/run_skill_eval.sh skills/en/<category>/<canonical-skill>/evals/eval.yaml。使用仓库 runner 的隔离输出目录，记录命令、Skill/Eval 版本、engine、case 结果和限制；若引擎、凭据或环境阻塞，记录 BLOCKED / NOT_RUN，该卡不得标记 Done。
- [x] 运行 python3 scripts/check_docs_bilingual.py --repo-root . 和 python3 -m unittest discover -s scripts/tests -v；逐项检查 EN/ZH 路径、元数据、Eval 输入语言和生成目录状态。

**验收：** 静态门禁全部通过；真实模型或目标运行若未执行，显式记录 NOT_RUN，不把静态门禁当作行为验收。

### Task 7：统一收口 Project #4 的 23 张目标卡

- [x] 复读 Project #4 的 23 张目标卡及本次生成的 closeout 记录。
- [x] 只有当卡片要求的交付完成、适用验证有证据、N/A 项已解释后，才更新该卡 Status。
- [x] 对复核后确认已有能力足够的卡，关联匹配记录和证据后再收口。
- [x] 对重复卡保持项目历史可追溯：不删除卡；相同范围复用交付物并在两张卡的收口说明中相互引用。
- [x] 保留每张卡原有 Priority 和 Target Version，不将单批实施误记为版本发布或业务验收。
- [x] 更新后重新查询 Project #4，确认 23 张目标卡全部为 Done，且本批范围外的 13 张 Todo 卡状态未变。若任一必需验证仍为 BLOCKED / NOT_RUN，保持该卡 Todo 或 In Progress，并将批次结论标记为未完成。

**验收：** 只有 23 张目标卡全部为 Done、Project 状态与仓库证据一致、所有变更都可追溯到双语包/治理记录/验证结果时，本批才算完成；Done 不表示未执行的模型、运行时或业务验收已经通过。


## 执行结果（2026-11-06）

- 21 个不同能力候选项：EXISTING 9、MATCH 2、MERGE 10、ENHANCE 0、NEW 0；没有 Skill 行为包需要修改。
- 本批行为 Eval 为 N/A；真实模型/宿主运行仍为 NOT_RUN，语义等价与业务验收仍为 UNASSESSED。
- 仓库质量门禁、Skill CLI 1.7.0 兼容性、组合视图和双语文档检查通过；完整单元测试 412 项通过，Eval YAML 348/348 通过。
- Project #4 的 23 张目标卡均已 Done；批次外 13 张 Todo 的 item ID 保持不变。只更新了 Status，Priority 和 Target Version 未触碰。
