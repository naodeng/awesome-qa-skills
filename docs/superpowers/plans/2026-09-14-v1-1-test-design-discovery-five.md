<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-test-design-discovery-five_EN.md">🇬🇧 English</a></div>

# v1.1 测试设计发现五个 Skill 实施计划

> **For agentic workers:** 必须按 task 顺序执行；每个 task 使用 checkbox 记录，且每个 Skill 独立完成 RED → GREEN → REFACTOR。当前计划只在 `develop` 工作区执行，不提交、不 push。

**目标：** 在当前工作区完成 `test-gap-analysis`、`risk-based-testing`、`edge-case-discovery`、`negative-scenario-discovery` 和 `test-data-requirement-analysis` 五个 v1.1 P0 候选的双语独立 Skill 包、Eval、本地触发规则、治理登记、生成视图和验证。

**架构：** 五项均按设计文档判定为 `NEW`，每项有独立双语目录和稳定发现 ID。它们共享证据边界和本地验证合同，但不互相链接内部文件；相邻 Skill 只在入口文案中说明边界。

**技术栈：** Markdown、YAML、CSV、JSON、Python 3 标准库、`skill-up validate/run`、仓库本地 trace runner、GitHub Project CLI 和既有质量门禁。

**设计依据：** `docs/superpowers/specs/2026-09-14-v1-1-test-design-discovery-five-design.md` 及其英文镜像。

## Review 后的全局约束

- 只有五个候选各自的双语物理目录允许新增；不创建增强别名或重复目标目录。
- 每个新包必须包含 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml`、`basic-success.yaml`、`edge-incomplete-input.yaml`、`edge-scope-boundary.yaml`、`trigger-prompts.csv` 和 `local-rules.json`。
- `SKILL.md` 的 frontmatter `description` 使用项目现行 `Use this skill when ...; triggers include ...` 约定；中英文目录名、`name`、metadata key 和 Prompt 结构对等。
- Prompt 必须先做 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions` 输入审计，分开事实、证据推断、建议和 Human 决策。
- 五项稳定产物分别为 `TG-##`、`RBT-##`、`EC-##`、`NS-##`、`TDR-##`；没有执行证据时不得写 `passed`、`complete coverage`、已验证或已批准。
- 触发 CSV 覆盖 `explicit`、`implicit`、`contextual`、`negative`，正反样本都存在；`local-rules.json` 的 `skill` 等于物理 slug。
- Project #4 只移动五个精确 item ID 到 `In Progress`，不改变其他卡片；不创建 Issue，不 push，不发布版本，保留已有未提交修改。
- 真实模型 Eval 保持 `NOT_RUN`，治理质量分保持 `NOT_SCORED`；本地 runner 缺少 `skill.selection` 时必须报告 `BLOCKED`。

---

### Task 1：写本批合同测试并观察 RED

**Files**

- Create: `scripts/tests/test_v11_test_design_discovery_contracts.py`
- Read-only: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Read-only: `scripts/run_skill_trace_eval.py`、`scripts/skill_eval_rules.py`

**合同：** `NEW_SLUGS = ("test-gap-analysis", "risk-based-testing", "edge-case-discovery", "negative-scenario-discovery", "test-data-requirement-analysis")`。每种语言检查入口、Prompt、metadata、eval、三类 case、四种 trigger mode、正反触发、物理 slug rule，并按 Skill 检查唯一产物标记和边界标记：`TG-` + “not a coverage claim”；`RBT-` + “not a full test strategy”；`EC-` + “do not invent thresholds”；`NS-` + “do not run fault injection”；`TDR-` + “do not generate data”。泛化的 `risk`、`test` 或 `coverage` 单词不能满足该合同。

- [x] 先写合同测试，不创建任何本批 Skill 内容。
- [x] 运行 `python3 -m unittest scripts.tests.test_v11_test_design_discovery_contracts -v`，预期因为五个双语目录缺失而失败。
- [x] 运行 `git diff --check` 和 `git status --short`，确认 RED 没有覆盖或回退现有修改。
- [x] RED 确认后，移动五个精确 Project #4 item 到 `In Progress`，并立即复核状态：

  ```bash
  project_id=PVT_kwHOAHP1as4BjBhV
  status_field_id=PVTSSF_lAHOAHP1as4BjBhVzhh3bSA
  in_progress_option_id=47fc9ee4
  for item_id in \
    PVTI_lAHOAHP1as4BjBhVzg6ScBw \
    PVTI_lAHOAHP1as4BjBhVzg6ScEE \
    PVTI_lAHOAHP1as4BjBhVzg6ScGA \
    PVTI_lAHOAHP1as4BjBhVzg6ScIs \
    PVTI_lAHOAHP1as4BjBhVzg6ScKk; do
    gh project item-edit --id "$item_id" --project-id "$project_id" \
      --field-id "$status_field_id" --single-select-option-id "$in_progress_option_id"
  done
  gh project item-list 4 --owner @me --format json --limit 200
  ```

  只允许这五张卡片从 `Todo` 变为 `In Progress`；如果任意 ID、项目或字段不匹配，停止实现并先修正状态操作。

### Task 2：新增 `test-gap-analysis`

**Files**：创建 `skills/zh/testing-types/test-gap-analysis/` 与对应 English 目录中的 `SKILL.md`、主 Prompt、metadata、`evals/eval.yaml`、三类 case、`trigger-prompts.csv`、`local-rules.json`。

**合同：** 以需求/风险/变更/缺陷/测试资产为输入，输出 `TG-##` 缺口；区分 missing mapping、orphan、unverified、stale、uncovered risk 和 low-value duplicate；不替代 RT/TC 矩阵或执行证明。

- [x] 先写三类 Eval 和本地触发数据，成功/信息不足/范围边界分别覆盖证据、受限结果和“不能把静态存在写成覆盖”。
- [x] 逐语言运行 `skill-up validate skills/<lang>/testing-types/test-gap-analysis/evals/eval.yaml`，再运行对应 `--dry-run`。
- [x] 写最小双语入口、Prompt、metadata，检查中英文输出合同对等。
- [x] 运行本批合同测试和 `git diff --check`，再进入下一个 Skill。

### Task 3：新增 `risk-based-testing`

**Files**：创建 `skills/zh/testing-types/risk-based-testing/` 与对应 English 目录中的同一组文件。

**合同：** 把风险证据转成 `RBT-##` 测试优先级、级别/方法、深度和范围取舍；不替代风险识别、完整策略、回归选择或执行。

- [x] 写三类 Eval：可解释的风险到测试映射、缺失关键风险材料时的受限初版、资源/时间边界下的取舍和扩大范围触发器。
- [x] 逐语言 validate/dry-run、合同测试、diff check。
- [x] 检查风险数字有证据或标为假设，不输出伪精确分数或 Human 放行结论。

### Task 4：新增 `edge-case-discovery`

**Files**：创建 `skills/zh/testing-types/edge-case-discovery/` 与对应 English 目录中的同一组文件。

**合同：** 输出 `EC-##` 边界候选，至少覆盖值/长度、空值/类型、时间/时区、状态、容量/资源、并发/顺序、平台/本地化和组合维度；不生成完整用例、不发明阈值。

- [x] 写三类 Eval：多维边界发现、输入不足时标记假设和缺口、范围/未知阈值边界。
- [x] 逐语言 validate/dry-run、合同测试、diff check。
- [x] 对每条候选保留来源、触发条件、关注点、优先级、验证建议和未决问题。

### Task 5：新增 `negative-scenario-discovery`

**Files**：创建 `skills/zh/testing-types/negative-scenario-discovery/` 与对应 English 目录中的同一组文件。

**合同：** 输出 `NS-##` 失败/拒绝/降级/恢复候选，区分非法输入、未授权、依赖失败、超时、重试耗尽、重复请求、部分失败和不安全恢复；不执行故障注入、不发明错误码。

- [x] 写三类 Eval：失败路径成功发现、关键失败契约缺失、范围边界拒绝执行或发布结论。
- [x] 逐语言 validate/dry-run、合同测试、diff check。
- [x] 验证预期行为至少包含触发条件、前置条件、可见结果、数据一致性影响和证据需求。

### Task 6：新增 `test-data-requirement-analysis`

**Files**：创建 `skills/zh/testing-types/test-data-requirement-analysis/` 与对应 English 目录中的同一组文件。

**合同：** 输出 `TDR-##` 数据准备需求，覆盖实体/字段、关系、状态、角色、有效/无效/边界/组合、来源、脱敏、初始化、清理和阻塞；不生成记录、不读取生产数据。

- [x] 写三类 Eval：完整数据前置条件、schema/隐私/清理信息不足、真实数据源或生产镜像边界。
- [x] 逐语言 validate/dry-run、合同测试、diff check。
- [x] 检查数据需求分析可以被 `test-data-generation` 消费，但不复制其生成规则/数据集输出。

### Task 7：同步治理、索引和生成视图

**Files**：按本仓库既有生成器更新 `docs/governance/skill-governance-registry.yaml`、双语 `docs/SKILL_MATCHING_REGISTER*`、`docs/SKILL_MATRIX*`、`docs/catalog/*`、`docs/generated/*`、双语 README 和必要的 Phase 1 文档。

- [x] 五条 Skill registry 记录均有双语路径、`Planned-P0` 状态、Engineering QA / Test Design and Preparation 阶段、角色、输入、输出、工作流和证据路径；质量分为 `NOT_SCORED`、执行为 `NOT_RUN`。对应五条 candidate 记录为 `NEW`，并分别登记 scope/non-goals。
- [x] 五条 candidate 记录的六字段 match evidence 与本设计一致，不能把相邻 Skill 名称当作重复或覆盖证明。
- [x] 运行 `python3 scripts/generate_skill_inventory.py`、`python3 scripts/generate_skill_governance_inventory.py`、`python3 scripts/generate_skill_governance_matrix.py`，再运行对应 `--check`；保留既有未提交差异。
- [x] `python3 scripts/check_docs_bilingual.py --repo-root .` 和独立性检查必须通过。

### Task 8：统一验证并核验 Project 卡片

- [x] 对五个 slug 的 zh/en eval 运行 `skill-up validate` 和 `skill-up run ... --dry-run`。
- [x] 运行本批合同测试、上一批两个合同测试和 `python3 -m unittest discover -s scripts/tests -v`。
- [x] 运行 `bash scripts/check_skills_quality.sh`、`bash scripts/validate_skill_evals.sh`、metadata/independence/integrity/external snapshot 检查和 `git diff --check`。
- [x] 对十五个物理目标（上一批十个目标 + 本批五个）运行 `scripts/run_skill_trace_eval.py` 默认 dry-run；无 `skill.selection` 时记录 `BLOCKED`，不伪造触发通过。
- [x] 用 `gh project item-list 4 --owner @me --format json --limit 200` 核验五张精确卡片为 `In Progress`，并确认紧接的 `decision-table-testing`、`state-transition-testing`、`boundary-value-testing` 仍为 `Todo`。
- [x] 对本批新增和治理文档做作用域尾随空白检查，输出最终文件清单、验证命令和未执行边界；不 commit、不 push。

## 计划自检

- [x] 每个候选都有 capability match、六字段证据、明确输入/输出/决策逻辑和相邻 Skill 边界。
- [x] 每个候选都有独立 Task、双语文件清单、三类 Eval、四种 trigger mode 和逐包验证。
- [x] RED 在包内容之前；Project 卡片只在 RED 确认后、实现开始前移动；治理生成在包验证之后执行。
- [x] 不把静态结构、本地 dry-run 或 Project 状态写成真实模型效果、运行结果、Human 决策或 Release 完成。
