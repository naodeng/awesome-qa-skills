# v3-v4 两批 Skill 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox ([ ]) syntax for tracking.

**Goal:** 在已合入最新 main 的 develop 上，将 Project #4 的 42 张 v3-v4 P2 Skill 卡片按 Reliability + Security、Quality Engineering + AI Native 两批完成 Capability Match、双语 Skill 交付、治理同步和证据有界的卡片验收。

**Architecture:** 先建立 42 张卡片的 Capability Match ledger 和领域前缀映射。当前审查结论预计为 41 个 NEW 物理 Skill 包（中英文各一份）和 1 个对 prompt-testing 的 prompt-regression 模式增强；若实施中的新证据改变结论，必须先修正 ledger，再决定是否建目录。每批先对实际交付目标做合同测试并确认 RED，再移动精确 Project 卡片，最后同步 registry、Matrix、Register、Catalog、Graph 和双语入口文档。

**Tech Stack:** Markdown、YAML、CSV、JSON、Python 3 标准库、unittest、skill-up validate/run、现有治理生成器、GitHub Project CLI 和 bash scripts/check_skills_quality.sh。

**Spec:** docs/superpowers/specs/2026-09-15-v3-v4-two-batch-design.md

## Global Constraints

- 当前 develop 已在 15c3804 之后包含本任务的双语规格提交；origin/main 为 15c3804，当前工作区既有 v2 交付不回退、不覆盖。
- Batch 1 固定为 17 个：reliability-testing、resilience-testing、chaos-testing、failover-testing、recovery-testing、retry-testing、timeout-testing、circuit-breaker-testing、dependency-failure-testing、disaster-recovery-testing、authentication-testing、authorization-testing、session-security-testing、api-security-testing、security-requirement-review、threat-modeling、secrets-exposure-review。
- Batch 2 固定为 25 个：quality-gate-design、quality-metrics-design、quality-dashboard-design、quality-debt-analysis、quality-maturity-assessment、test-effectiveness-analysis、automation-roi-analysis、testing-bottleneck-analysis、regression-optimization、ci-test-optimization、test-runtime-optimization、test-maintenance-cost-analysis、quality-productivity-metrics、prompt-regression-testing、rag-quality-testing、rag-retrieval-testing、agent-loop-testing、agent-memory-testing、agent-permission-testing、agent-failure-recovery-testing、agent-long-running-testing、multi-agent-testing、llm-hallucination-testing、llm-consistency-testing、ai-safety-testing。
- 预期 Match 结果为 41 个 NEW、1 个 ENHANCE；实际结果以初始 Match 证据为准。只有 NEW 才创建物理目录；prompt-regression-testing 默认增强 prompt-testing，不创建别名目录。
- 每个 NEW 语言包必须有 SKILL.md、prompts/<slug>.md、agents/openai.yaml、evals/eval.yaml、basic-success.yaml、edge-incomplete-input.yaml、edge-scope-boundary.yaml、trigger-prompts.csv 和 local-rules.json。增强目标沿用物理目录，并补充模式合同与三类模式用例。
- 每个 Prompt 先做 known、missing、conflicting、stale、out_of_scope、assumptions 输入审计，再分离 facts、evidence-backed inferences、candidate recommendations 和 Human decisions；发现使用规格中定义的稳定前缀。
- 静态文件、名称、触发 dry-run、skill-up validate、单元测试和质量门禁不证明真实模型效果、外部目标执行、漏洞不存在、覆盖率、质量分、风险接受、业务批准或 Release 完成。
- 只移动本计划列出的精确 Project item；不移动 v4.1 Enhance Review、v4.0 Workflow、v3.4 Performance Review、Release DoD 或其他未纳入卡片，不创建仓库 Issue，不 push，不创建 Release。
- Project #4 的当前状态必须在每次外部状态修改前后用 gh project item-list 实时读取；字段 ID 和状态 option ID 从 gh project field-list 解析，不凭历史值猜测。
- 每个可交付任务结束执行对应验证并提交局部 commit；提交前只暂存本任务路径，保留用户或其他任务已有的无关改动。

## File Map

- Match source and acceptance record: docs/governance/PHASE_3_V3_V4.md、docs/governance/PHASE_3_V3_V4_EN.md。
- Shared batch contract definitions: scripts/tests/v3_v4_skill_contracts.py。
- Match contract: scripts/tests/test_v3_v4_match_contracts.py。
- Batch contracts: scripts/tests/test_v3_v4_batch1_skill_contracts.py、scripts/tests/test_v3_v4_batch2_skill_contracts.py、scripts/tests/test_v3_v4_prompt_regression_contract.py。
- NEW packages: skills/zh/testing-types/<slug>/ and skills/en/testing-types/<slug>/ for the 41 NEW slugs.
- Enhancement target: skills/zh/testing-types/prompt-testing/ and skills/en/testing-types/prompt-testing/。
- Governance source and generated views: docs/governance/skill-governance-registry.yaml、docs/SKILL_MATRIX.md、docs/SKILL_MATRIX_EN.md、docs/SKILL_MATCHING_REGISTER.md、docs/SKILL_MATCHING_REGISTER_EN.md、docs/generated/。
- Navigation and lifecycle documents: README.md、README_EN.md、skills/zh/README.md、skills/en/README.md、docs/catalog/skills-index.md、docs/catalog/skills-index_EN.md、docs/catalog/skills-graph.md、docs/catalog/skills-graph_EN.md、docs/governance/SKILL_GOVERNANCE_ROADMAP.md、docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md。
- External execution record: GitHub Project #4 item status only; transition history remains UNASSESSED if the API exposes only current status.

---

### Task 1: 建立 v3-v4 Capability Match ledger 和共享合同定义

**Files:**

- Create: scripts/tests/v3_v4_skill_contracts.py
- Create: scripts/tests/test_v3_v4_match_contracts.py
- Create: docs/governance/PHASE_3_V3_V4.md
- Create: docs/governance/PHASE_3_V3_V4_EN.md
- Read-only reference: docs/superpowers/specs/2026-09-15-v3-v4-two-batch-design.md
- Read-only reference: docs/governance/skill-governance-registry.yaml
- Read-only reference: skills/zh/testing-types/security-testing/SKILL.md、skills/zh/testing-types/ai-agent-testing/SKILL.md、skills/zh/testing-types/agent-tool-testing/SKILL.md、skills/zh/testing-types/prompt-testing/SKILL.md、skills/zh/testing-types/regression-scope-analysis/SKILL.md、skills/zh/testing-types/regression-test-selection/SKILL.md、skills/zh/testing-types/test-reporting/SKILL.md

**Interfaces:**

- Produces: BATCH_1、BATCH_2、NEW_SKILLS、ENHANCEMENTS、CARD_IDS、PREFIXES、DOMAIN_MARKERS 和每项的 target、conclusion、existing_targets、difference。
- Consumes: Project #4 的 42 个精确 item ID、当前物理 Skill 树、已有治理记录和 v3-v4 书面规格。
- Boundary: 本任务只登记 Match 和静态交付目标，不创建任何 v3-v4 Skill 包，不改变 Project 卡片状态。

- [ ] **Step 1: 读取实时候选卡片和当前 Skill 树。**

  Run:

      gh project item-list 4 --owner naodeng --format json --limit 200 | jq '[.items[] | select((.content.title // "") | startswith("v3-v4 P2｜候选 Skill｜"))] | {count: length, statuses: (group_by(.status) | map({status: .[0].status, count: length}))}'
      rg --files skills/zh skills/en | rg '/SKILL.md$' | sort
      git status --short --branch

  Expected: 42 candidates, all Todo, and the current v2 tree remains unchanged. Record the command date as 2026-09-15 in the phase document.

- [ ] **Step 2: Write exact shared maps and Match evidence.**

  In scripts/tests/v3_v4_skill_contracts.py define the exact 17-card BATCH_1 and 25-card BATCH_2 maps from the spec. Put the 41 non-prompt-regression slugs in NEW_SKILLS with target_section testing-types, and define:

      ENHANCEMENTS = {
          "prompt-regression-testing": {
              "target": "prompt-testing",
              "target_section": "testing-types",
              "mode": "prompt-regression",
              "prefix": "PRT-",
          }
      }

  Keep every prefix unique within the v3-v4 map. Add bilingual domain markers and the minimum input/output focus for every slug. The Match ledger must use existing targets as comparison evidence, including security-testing for security specialists, regression-scope-analysis and regression-test-selection for regression-optimization, test-reporting and quality-risk-analysis for QE candidates, and ai-agent-testing, agent-tool-testing, llm-testing, prompt-testing, and prompt-injection-testing for AI Native candidates. The difference field must explain why the candidate is narrower or structurally different; it must not claim runtime effectiveness.

- [ ] **Step 3: Write the bilingual Phase 3 governance record.**

  Add all 42 rows with the exact item ID, batch, domain, proposed conclusion, target path, six Match fields, difference, non-goals, and planned evidence. Record 41 NEW and prompt-regression-testing ENHANCE as the reviewed working conclusion, while stating that a fresh source review can revise a row before package creation. Include the complete Batch 1 and Batch 2 lists and the card-state protocol.

- [ ] **Step 4: Write a deterministic Match contract test and run it.**

  The test must assert: exact candidate set size 42; exact Batch 1 size 17; exact Batch 2 size 25; no overlap; exact Project item IDs; unique prefixes; 41 NEW plus one ENHANCE; prompt-regression-testing targets prompt-testing; no v4.1/v4.0/v3.4/Release DoD card is selected; both phase documents contain the same slug and item-ID rows; and all six evidence fields are nonempty.

  Run:

      python3 -m unittest scripts.tests.test_v3_v4_match_contracts -v
      git diff --check

  Expected: PASS for the ledger and no new Skill directory. If the live Project result differs, update the ledger and shared map before proceeding.

- [ ] **Step 5: Review and commit the Match ledger.**

  Run:

      git diff --check
      git diff --name-only
      git status --short

  Stage only the four files created in this task and commit:

      git add scripts/tests/v3_v4_skill_contracts.py scripts/tests/test_v3_v4_match_contracts.py docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md
      git commit -m "docs(v3-v4): record capability match ledger"

  Expected: one scoped commit; no Project status changes.

---

### Task 2: 建立 Batch 1 合同测试并确认实际 NEW 目标 RED

**Files:**

- Create: scripts/tests/test_v3_v4_batch1_skill_contracts.py
- Modify: scripts/tests/v3_v4_skill_contracts.py only if the exact Match result changed
- Read-only reference: scripts/tests/v20_skill_contracts.py
- Read-only reference: scripts/tests/test_v20_batch1_skill_contracts.py

**Interfaces:**

- Consumes: Task 1 BATCH_1, NEW_SKILLS, PREFIXES and DOMAIN_MARKERS.
- Produces: a reusable static contract for the 17 Batch 1 NEW package targets.
- Boundary: the test checks package structure and declared text only; it does not run Chaos, security tools, failover, recovery, or production systems.

- [ ] **Step 1: Write the failing contract test before creating package files.**

  Assert for both languages and each actual NEW slug: SKILL.md, prompts/<slug>.md, agents/openai.yaml, evals/eval.yaml, the three exact case files, trigger-prompts.csv, and local-rules.json exist; frontmatter name and metadata key equal the physical slug; the Prompt has the shared audit fields, language separation, domain finding prefix, and all required output fields; eval.yaml names all three cases; CSV has the four modes plus true and false values; and local-rules.json.skill equals the physical slug.

  Add domain assertions for the ten Reliability prompts and seven Security prompts. Edge scope cases must contain the refusal terms for tests executed, all tests passed, and release approved in the corresponding language.

- [ ] **Step 2: Run only the Batch 1 contract test and record RED.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v

  Expected: FAIL because the 17 NEW bilingual package directories and required files are absent. A failure caused by a typo in the test is not an acceptable RED; fix the test until the failure identifies missing target behavior.

- [ ] **Step 3: Verify the RED boundary and commit the contract.**

      git diff --check
      git status --short
      git add scripts/tests/test_v3_v4_batch1_skill_contracts.py
      git commit -m "test(v3-v4): add batch1 skill contracts"

  Do not move cards or create package files before this RED evidence exists.

---

### Task 3: 将 Batch 1 的 17 张卡片移动到 In Progress

**External state:**

- Project #4 exact items: PVTI_lAHOAHP1as4BjBhVzg6Sc5w、PVTI_lAHOAHP1as4BjBhVzg6Sc68、PVTI_lAHOAHP1as4BjBhVzg6Sc8M、PVTI_lAHOAHP1as4BjBhVzg6Sc90、PVTI_lAHOAHP1as4BjBhVzg6Sc_w、PVTI_lAHOAHP1as4BjBhVzg6SdAw、PVTI_lAHOAHP1as4BjBhVzg6SdCU、PVTI_lAHOAHP1as4BjBhVzg6SdEM、PVTI_lAHOAHP1as4BjBhVzg6SdFo、PVTI_lAHOAHP1as4BjBhVzg6SdHI、PVTI_lAHOAHP1as4BjBhVzg6SdJA、PVTI_lAHOAHP1as4BjBhVzg6SdLg、PVTI_lAHOAHP1as4BjBhVzg6SdNI、PVTI_lAHOAHP1as4BjBhVzg6SdPY、PVTI_lAHOAHP1as4BjBhVzg6SdQ0、PVTI_lAHOAHP1as4BjBhVzg6SdSk、PVTI_lAHOAHP1as4BjBhVzg6SdUg
- Project ID: PVT_kwHOAHP1as4BjBhVzg6

- [ ] **Step 1: Resolve the live Status field and options.**

      gh project field-list 4 --owner naodeng --format json | jq '.fields[] | select(.name == "Status")'

  Capture the Status field ID and the live option IDs for Todo, In Progress, and Done. Do not use a hard-coded option if the live output differs.

- [ ] **Step 2: Verify the exact precondition.**

  Read Project #4 and assert the 17 exact titles are Todo, the nine v2 cards remain Done, and all other v3-v4 P2 candidates remain Todo. If any exact item is missing or already changed, stop the mutation and record the actual state.

- [ ] **Step 3: Update only the 17 exact items.**

  For each listed item, run the equivalent of:

      gh project item-edit --project-id PVT_kwHOAHP1as4BjBhVzg6 --id <exact-item-id> --field-id <live-status-field-id> --single-select-option-id <live-in-progress-option-id>

- [ ] **Step 4: Re-read and verify scope.**

      gh project item-list 4 --owner naodeng --format json --limit 200 | jq '[.items[] | select((.content.title // "") | startswith("v3-v4 P2｜候选 Skill｜")) | {title: .content.title, status: .status}]'

  Expected: the Batch 1 exact rows are In Progress; the 25 Batch 2 cards remain Todo; unrelated Project cards have not changed. Record the current snapshot in PHASE_3_V3_V4.md without claiming historical transition evidence.

---

### Task 4: 实现 Batch 1 Reliability 的 10 个双语 NEW Skill 包

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for: reliability-testing, resilience-testing, chaos-testing, failover-testing, recovery-testing, retry-testing, timeout-testing, circuit-breaker-testing, dependency-failure-testing, disaster-recovery-testing.
- Every package creates: SKILL.md, prompts/<slug>.md, agents/openai.yaml, evals/eval.yaml, evals/cases/basic-success.yaml, evals/cases/edge-incomplete-input.yaml, evals/cases/edge-scope-boundary.yaml, evals/trigger-prompts.csv, evals/local-rules.json.
- Modify only the shared contract map if a reviewed Match row changes.

**Interfaces:**

- Inputs and minimum coverage:

  | Skill | Prefix | Minimum focus |
  | --- | --- | --- |
  | reliability-testing | RLT- | reliability objectives, SLI/SLO evidence, failure budget, observable acceptance and residual risk |
  | resilience-testing | RES- | graceful degradation, isolation, bulkheads, dependency loss and service continuity |
  | chaos-testing | CHS- | experiment hypothesis, steady state, blast radius, safety guard, abort and observability |
  | failover-testing | FOV- | failure detection, switchover trigger, fallback target, continuity and split-brain concern |
  | recovery-testing | RCV- | restore sequence, data integrity, recovery point/time objective and verification evidence |
  | retry-testing | RTY- | retryable conditions, backoff/jitter, attempt cap, idempotency and amplification risk |
  | timeout-testing | TMO- | deadline ownership, cancellation, partial result behavior, timeout source and downstream propagation |
  | circuit-breaker-testing | CBR- | closed/open/half-open transitions, thresholds, fallback, probe and recovery evidence |
  | dependency-failure-testing | DPF- | dependency error taxonomy, propagation, fallback, isolation and contract mismatch |
  | disaster-recovery-testing | DRT- | backup/restore, region or site loss, RTO/RPO, communication, ownership and exercise evidence |

- Produces: domain-specific PREFIX-## findings with object/rule, source, trigger/applicability, concern/rationale, evidence state, impact/priority, owner role, close condition, and validation method.
- Boundary: no fault injection, real dependency call, benchmark, failover switch, restore operation, production change, or unverified RTO/RPO value.

- [ ] **Step 1: Write the ten bilingual Eval configurations, case files, trigger CSVs, and local rules.**

  Each basic case must contain a domain-specific input and expected PREFIX-## evidence-bound output. Each incomplete case must name the missing threshold, baseline, dependency, environment, or ownership information. Each boundary case must reject execution/pass/release claims. Trigger rows must include four modes, one positive and one reverse-control row, and language-appropriate wording.

- [ ] **Step 2: Validate all 20 Eval files before writing the long Prompt text.**

      for file in skills/zh/testing-types/{reliability-testing,resilience-testing,chaos-testing,failover-testing,recovery-testing,retry-testing,timeout-testing,circuit-breaker-testing,dependency-failure-testing,disaster-recovery-testing}/evals/eval.yaml skills/en/testing-types/{reliability-testing,resilience-testing,chaos-testing,failover-testing,recovery-testing,retry-testing,timeout-testing,circuit-breaker-testing,dependency-failure-testing,disaster-recovery-testing}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done

- [ ] **Step 3: Write the ten Chinese and English SKILL.md, Prompt, and metadata files.**

  Each SKILL.md must state its real trigger situations, required prompt loading, evidence boundary, on-demand reference rule, self-check, and domain pitfalls. Each Prompt must use the shared audit first, then its minimum coverage table, then the PREFIX-## Finding Contract. The English frontmatter may contain bilingual metadata as required by the repository, but the English body must contain no Chinese.

- [ ] **Step 4: Run the Batch 1 contract, Eval, independence, and diff checks.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

  Expected: the Reliability ten packages pass their domain assertions; the seven Security packages remain the only Batch 1 package targets not yet implemented.

- [ ] **Step 5: Commit only the Reliability package files.**

      git add skills/zh/testing-types/reliability-testing skills/en/testing-types/reliability-testing skills/zh/testing-types/resilience-testing skills/en/testing-types/resilience-testing skills/zh/testing-types/chaos-testing skills/en/testing-types/chaos-testing skills/zh/testing-types/failover-testing skills/en/testing-types/failover-testing skills/zh/testing-types/recovery-testing skills/en/testing-types/recovery-testing skills/zh/testing-types/retry-testing skills/en/testing-types/retry-testing skills/zh/testing-types/timeout-testing skills/en/testing-types/timeout-testing skills/zh/testing-types/circuit-breaker-testing skills/en/testing-types/circuit-breaker-testing skills/zh/testing-types/dependency-failure-testing skills/en/testing-types/dependency-failure-testing skills/zh/testing-types/disaster-recovery-testing skills/en/testing-types/disaster-recovery-testing
      git commit -m "feat(v3-v4): add reliability skill batch"

---

### Task 5: 实现 Batch 1 Security 的 7 个双语 NEW Skill 包

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for: authentication-testing, authorization-testing, session-security-testing, api-security-testing, security-requirement-review, threat-modeling, secrets-exposure-review.
- Every package creates the same nine required files listed in Task 4.

**Interfaces:**

- Inputs and minimum coverage:

  | Skill | Prefix | Minimum focus |
  | --- | --- | --- |
  | authentication-testing | AUT- | identity proof, login/re-authentication, token/session boundary, recovery and abuse evidence |
  | authorization-testing | AZT- | subject-resource-action policy, least privilege, deny-by-default, tenant and role boundary |
  | session-security-testing | SST- | creation, rotation, expiry, revocation, fixation, concurrent use and logout evidence |
  | api-security-testing | AST- | API attack surface, input/output validation, auth, sensitive data, rate limiting and auditability |
  | security-requirement-review | SRR- | security requirement clarity, threat linkage, acceptance criteria, ownership and traceability |
  | threat-modeling | THM- | assets, trust boundaries, data flows, threats, controls, abuse cases and residual uncertainty |
  | secrets-exposure-review | SER- | supplied source/config/log secret patterns, exposure path, severity evidence, remediation and rotation ownership |

- Boundary: do not log in, send credentials, retrieve secrets, run a scanner, attack a target, claim absence of vulnerabilities, or approve a risk exception.

- [ ] **Step 1: Write the seven bilingual Eval sets and trigger controls.**

  Use concrete security-specific inputs and require evidence state plus the Human decision boundary in every expected output. Incomplete cases must preserve missing threat model, scope, identity, policy, secret classification, or rotation evidence.

- [ ] **Step 2: Run 14 skill-up validate commands and confirm the contract stays RED until package content is complete.**

      for file in skills/zh/testing-types/{authentication-testing,authorization-testing,session-security-testing,api-security-testing,security-requirement-review,threat-modeling,secrets-exposure-review}/evals/eval.yaml skills/en/testing-types/{authentication-testing,authorization-testing,session-security-testing,api-security-testing,security-requirement-review,threat-modeling,secrets-exposure-review}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v

- [ ] **Step 3: Write the seven bilingual entrypoints, Prompts, and metadata.**

  Keep the distinction from the generic security-testing package explicit in each Match evidence and Prompt: the new package narrows the input and decision contract; it does not claim stronger runtime security results.

- [ ] **Step 4: Run Batch 1 checks and commit Security files.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

      git add skills/zh/testing-types/authentication-testing skills/en/testing-types/authentication-testing skills/zh/testing-types/authorization-testing skills/en/testing-types/authorization-testing skills/zh/testing-types/session-security-testing skills/en/testing-types/session-security-testing skills/zh/testing-types/api-security-testing skills/en/testing-types/api-security-testing skills/zh/testing-types/security-requirement-review skills/en/testing-types/security-requirement-review skills/zh/testing-types/threat-modeling skills/en/testing-types/threat-modeling skills/zh/testing-types/secrets-exposure-review skills/en/testing-types/secrets-exposure-review
      git commit -m "feat(v3-v4): add security skill batch"

---

### Task 6: 完成 Batch 1 治理同步、质量门禁和 Done 状态

**Files:**

- Modify: docs/governance/PHASE_3_V3_V4.md、docs/governance/PHASE_3_V3_V4_EN.md
- Modify: docs/governance/skill-governance-registry.yaml
- Regenerate: docs/SKILL_MATRIX.md、docs/SKILL_MATRIX_EN.md、docs/SKILL_MATCHING_REGISTER.md、docs/SKILL_MATCHING_REGISTER_EN.md、docs/generated/skill-governance-inventory.md、docs/generated/skill-governance-inventory_EN.md
- Modify: README.md、README_EN.md、skills/zh/README.md、skills/en/README.md、docs/catalog/skills-index.md、docs/catalog/skills-index_EN.md、docs/catalog/skills-graph.md、docs/catalog/skills-graph_EN.md、docs/governance/SKILL_GOVERNANCE_ROADMAP.md、docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
- Read-only reference: scripts/generate_skill_governance_matrix.py、scripts/generate_skill_governance_inventory.py

**Interfaces:**

- Consumes: 17 completed bilingual packages and the Task 1 Match ledger.
- Produces: 17 physical registry records plus 17 reviewed candidate records with Project #4 evidence, bilingual navigation, and generated views.
- Boundary: registry quality_score remains NOT_SCORED; eval_execution remains NOT_RUN; transition history is UNASSESSED when only current status is available.

- [ ] **Step 1: Add Batch 1 physical registry records and candidate evidence without asserting transition completion.**

  For each new package, add section testing-types, status Planned-P2, priority P2, the applicable virtual domain, sdlc_stage, roles, inputs, outputs, related, workflow, governance_evidence, and all bilingual evidence_paths. For each candidate, add decision_state REVIEWED, conclusion NEW, target slug, six Match evidence fields, scope, non_goals, candidate_source, capability_match, and target_evidence_paths. Before Project cards are moved to Done, do not add a project_evidence.current_status other than the value returned by the live Project query; the generator requires Done for a final reviewed Project record, so final project evidence is added after the Done transition.

- [ ] **Step 2: Regenerate and validate the local governance views.**

      python3 scripts/generate_skill_governance_matrix.py
      python3 scripts/generate_skill_governance_inventory.py
      python3 scripts/generate_skill_governance_matrix.py --check
      python3 scripts/generate_skill_governance_inventory.py --check

  Update both language indexes, graph compositions, READMEs, and the governance roadmap with the Reliability + Security Batch 1 route. The graph must state that reliability and security specialists are optional navigation and do not create installation dependencies.

- [ ] **Step 3: Run the full local gates before changing cards to Done.**

      python3 -m unittest scripts.tests.test_v3_v4_match_contracts scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/check_skills_quality.sh
      python3 -m unittest discover -s scripts/tests -v
      git diff --check

- [ ] **Step 4: Move only the exact 17 Batch 1 cards to Done after the gates pass.**

  Resolve the live Status field and Done option again; verify all 17 are In Progress and no Batch 2 card is In Progress. Run the equivalent item-edit command for the same 17 IDs with the live Done option. Re-read Project #4 and record current status, verified_at, verification command, required transition, transition_audit UNASSESSED, and acceptance_state INCOMPLETE for each card.

- [ ] **Step 5: Add final Project evidence and re-run generated checks.**

  Add the current Done evidence to the 17 candidate records, keeping the required transition audit explicitly UNASSESSED. Regenerate Matrix/Register/Inventory and run the full quality gate again. Do not use COMPLETE while transition history is unavailable.

- [ ] **Step 6: Commit Batch 1 governance and acceptance record.**

      git diff --check
      git add docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md docs/governance/skill-governance-registry.yaml docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/generated README.md README_EN.md skills/zh/README.md skills/en/README.md docs/catalog docs/governance/SKILL_GOVERNANCE_ROADMAP.md docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
      git commit -m "feat(v3-v4): close batch1 governance evidence"

  Expected: Batch 1 cards are currently Done; Batch 2 cards and unrelated cards retain their previous statuses.

---

### Task 7: 建立 Batch 2 合同测试、确认 RED 并移动 25 张卡片

**Files:**

- Create: scripts/tests/test_v3_v4_batch2_skill_contracts.py
- Create: scripts/tests/test_v3_v4_prompt_regression_contract.py
- Modify: scripts/tests/v3_v4_skill_contracts.py only for exact Match changes
- Read-only reference: scripts/tests/test_v3_v4_batch1_skill_contracts.py
- External state: the 25 Batch 2 Project item IDs from the spec

**Interfaces:**

- Consumes: BATCH_2, NEW_SKILLS, ENHANCEMENTS, PREFIXES and the completed Batch 1 governance state.
- Produces: a 24-package NEW contract plus an enhancement contract for prompt-testing.
- Boundary: prompt-regression-testing must not create a new physical directory unless fresh Match evidence revises the approved default.

- [ ] **Step 1: Write the Batch 2 NEW contract.**

  Assert the same package structure, bilingual separation, input-audit terms, finding fields, four trigger modes, three case references, and local-rules alignment as Batch 1. Add domain markers for 13 QE packages and 11 AI Native NEW packages; exclude prompt-regression-testing from the NEW package set.

- [ ] **Step 2: Write the prompt-regression enhancement contract.**

  Assert both prompt-testing packages retain their existing physical slug and required files, add a prompt-regression mode marker, add PRT-## regression findings with baseline/version/dataset/observed behavior/evidence state, add three regression-specific cases, include candidate trigger rows, and keep evals/local-rules.json.skill equal to prompt-testing. Assert that no directory named prompt-regression-testing exists.

- [ ] **Step 3: Run both RED tests before Batch 2 package content.**

      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      git diff --check

  Expected: the 24 NEW bilingual package targets and the prompt-regression mode assertions fail for missing target behavior. Fix test defects rather than weakening the boundary.

- [ ] **Step 4: Commit the Batch 2 RED contracts.**

      git add scripts/tests/test_v3_v4_batch2_skill_contracts.py scripts/tests/test_v3_v4_prompt_regression_contract.py scripts/tests/v3_v4_skill_contracts.py
      git commit -m "test(v3-v4): add batch2 skill contracts"

- [ ] **Step 5: Resolve live Project status and move only Batch 2 cards to In Progress.**

  Confirm Batch 1 remains Done, the 25 exact Batch 2 cards are Todo, and unrelated cards are unchanged. Resolve live Status field/option IDs and update only these IDs:

      PVTI_lAHOAHP1as4BjBhVzg6SdWc PVTI_lAHOAHP1as4BjBhVzg6SdY4 PVTI_lAHOAHP1as4BjBhVzg6SdaY PVTI_lAHOAHP1as4BjBhVzg6SdcE PVTI_lAHOAHP1as4BjBhVzg6Sddo PVTI_lAHOAHP1as4BjBhVzg6SdfA PVTI_lAHOAHP1as4BjBhVzg6Sdg8 PVTI_lAHOAHP1as4BjBhVzg6Sdig PVTI_lAHOAHP1as4BjBhVzg6SdkQ PVTI_lAHOAHP1as4BjBhVzg6SdnA PVTI_lAHOAHP1as4BjBhVzg6Sdo4 PVTI_lAHOAHP1as4BjBhVzg6Sdqc PVTI_lAHOAHP1as4BjBhVzg6SdsA PVTI_lAHOAHP1as4BjBhVzg6SdtI PVTI_lAHOAHP1as4BjBhVzg6Sdus PVTI_lAHOAHP1as4BjBhVzg6Sdwg PVTI_lAHOAHP1as4BjBhVzg6SdyQ PVTI_lAHOAHP1as4BjBhVzg6Sdzo PVTI_lAHOAHP1as4BjBhVzg6Sd1E PVTI_lAHOAHP1as4BjBhVzg6Sd2I PVTI_lAHOAHP1as4BjBhVzg6Sd3w PVTI_lAHOAHP1as4BjBhVzg6Sd5g PVTI_lAHOAHP1as4BjBhVzg6Sd7Q PVTI_lAHOAHP1as4BjBhVzg6Sd8Q PVTI_lAHOAHP1as4BjBhVzg6Sd9w

  Re-read Project #4 and record the exact current snapshot.

---

### Task 8: 实现 Batch 2 Quality Engineering 的 13 个双语 NEW Skill 包

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for: quality-gate-design, quality-metrics-design, quality-dashboard-design, quality-debt-analysis, quality-maturity-assessment, test-effectiveness-analysis, automation-roi-analysis, testing-bottleneck-analysis, regression-optimization, ci-test-optimization, test-runtime-optimization, test-maintenance-cost-analysis, quality-productivity-metrics.
- Every package creates the nine required files.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| quality-gate-design | QGD- | gate criteria, evidence prerequisites, owner, override path and Human decision |
| quality-metrics-design | QMD- | metric definition, numerator/denominator, source, freshness, caveat and anti-gaming concern |
| quality-dashboard-design | QDD- | audience, decision questions, panels, drill-down, freshness, access and alert boundary |
| quality-debt-analysis | QDA- | debt item, origin, impact, age, evidence, priority, owner and remediation trade-off |
| quality-maturity-assessment | QMA- | capability dimensions, rubric anchors, evidence sufficiency, gaps and maturity uncertainty |
| test-effectiveness-analysis | TEA- | test signal, defect/risk relation, detection limits, false confidence and validation plan |
| automation-roi-analysis | ARO- | automation candidate, setup/run/maintenance cost, benefit assumption, horizon and sensitivity |
| testing-bottleneck-analysis | TBA- | queue, wait, dependency, capacity, handoff, constraint evidence and improvement experiment |
| regression-optimization | RGO- | selection/order/parallelism/caching trade-off, risk preservation and execution-cost evidence |
| ci-test-optimization | CTO- | pipeline stages, feedback latency, resource use, flakiness, cache/shard constraints and rollback |
| test-runtime-optimization | TRO- | slow tests, profiling evidence, setup/teardown, parallelism, isolation and baseline |
| test-maintenance-cost-analysis | TMC- | change frequency, repair effort, flake cost, ownership, maintainability evidence and confidence |
| quality-productivity-metrics | QPM- | quality and delivery metrics, denominator, attribution limit, gaming risk and Human use boundary |

- Boundary: do not invent metric values, ROI, cost, maturity level, pipeline timing, causal productivity conclusions, release gates, or individual performance rankings.

- [ ] **Step 1: Write the 26 bilingual Eval files and trigger datasets with the table's domain markers.**
- [ ] **Step 2: Run skill-up validate for all 26 files, then implement the SKILL.md, Prompt, and metadata files.**
- [ ] **Step 3: Run Batch 2 contract tests, Eval validation, independence validation, and git diff --check.**

      for file in skills/zh/testing-types/{quality-gate-design,quality-metrics-design,quality-dashboard-design,quality-debt-analysis,quality-maturity-assessment,test-effectiveness-analysis,automation-roi-analysis,testing-bottleneck-analysis,regression-optimization,ci-test-optimization,test-runtime-optimization,test-maintenance-cost-analysis,quality-productivity-metrics}/evals/eval.yaml skills/en/testing-types/{quality-gate-design,quality-metrics-design,quality-dashboard-design,quality-debt-analysis,quality-maturity-assessment,test-effectiveness-analysis,automation-roi-analysis,testing-bottleneck-analysis,regression-optimization,ci-test-optimization,test-runtime-optimization,test-maintenance-cost-analysis,quality-productivity-metrics}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

- [ ] **Step 4: Commit only the QE package files.**

      git add skills/zh/testing-types/quality-gate-design skills/en/testing-types/quality-gate-design skills/zh/testing-types/quality-metrics-design skills/en/testing-types/quality-metrics-design skills/zh/testing-types/quality-dashboard-design skills/en/testing-types/quality-dashboard-design skills/zh/testing-types/quality-debt-analysis skills/en/testing-types/quality-debt-analysis skills/zh/testing-types/quality-maturity-assessment skills/en/testing-types/quality-maturity-assessment skills/zh/testing-types/test-effectiveness-analysis skills/en/testing-types/test-effectiveness-analysis skills/zh/testing-types/automation-roi-analysis skills/en/testing-types/automation-roi-analysis skills/zh/testing-types/testing-bottleneck-analysis skills/en/testing-types/testing-bottleneck-analysis skills/zh/testing-types/regression-optimization skills/en/testing-types/regression-optimization skills/zh/testing-types/ci-test-optimization skills/en/testing-types/ci-test-optimization skills/zh/testing-types/test-runtime-optimization skills/en/testing-types/test-runtime-optimization skills/zh/testing-types/test-maintenance-cost-analysis skills/en/testing-types/test-maintenance-cost-analysis skills/zh/testing-types/quality-productivity-metrics skills/en/testing-types/quality-productivity-metrics
      git commit -m "feat(v3-v4): add quality engineering skill batch"

---

### Task 9: 实现 Batch 2 AI Native 的 11 个 NEW 包并增强 prompt-testing

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for: rag-quality-testing, rag-retrieval-testing, agent-loop-testing, agent-memory-testing, agent-permission-testing, agent-failure-recovery-testing, agent-long-running-testing, multi-agent-testing, llm-hallucination-testing, llm-consistency-testing, ai-safety-testing.
- Modify: skills/zh/testing-types/prompt-testing/SKILL.md、skills/zh/testing-types/prompt-testing/prompts/prompt-testing.md、skills/zh/testing-types/prompt-testing/evals/eval.yaml、skills/zh/testing-types/prompt-testing/evals/trigger-prompts.csv、skills/zh/testing-types/prompt-testing/evals/local-rules.json
- Add: three prompt-regression-specific case files under skills/zh/testing-types/prompt-testing/evals/cases/
- Modify/add matching English prompt-testing files.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| rag-quality-testing | RAGQ- | grounding, relevance, completeness, citation/support, abstention and answer-level evidence |
| rag-retrieval-testing | RAGT- | query variants, chunking, filters, recall/precision proxy, ranking, freshness and retrieval evidence |
| agent-loop-testing | ALT- | loop state, planning/action/observation cycle, stop condition, budget, repetition and trace evidence |
| agent-memory-testing | AMT- | memory write/read/update/delete, retention, contamination, isolation, provenance and forgetting |
| agent-permission-testing | AGP- | Agent identity, tool/resource scope, approval, deny path, escalation and side-effect boundary |
| agent-failure-recovery-testing | AFR- | failure classification, retry/fallback/escalation, state consistency, user notice and recovery evidence |
| agent-long-running-testing | ALR- | checkpoint, heartbeat, resume, cancel, duplicate submission, timeout and resource lifecycle |
| multi-agent-testing | MAT- | delegation, coordination, shared state, conflict, ownership, termination and traceability |
| llm-hallucination-testing | LHT- | claim/source relation, unsupported assertion, abstention, uncertainty and evidence review |
| llm-consistency-testing | LCT- | repeat inputs, version/model/prompt factors, invariant, variance evidence and comparison boundary |
| ai-safety-testing | AIS- | safety policy, abuse category, refusal/redirect, privacy, escalation and Human risk decision |

- prompt-regression enhancement: add mode prompt-regression and PRT-## findings to prompt-testing. Findings must include baseline, candidate version, dataset/test prompt identity, expected behavior, observed behavior, evidence state, difference, validation method, and Human decision. Preserve all existing prompt-testing modes and IDs.
- Boundary: no model call, retrieval call, Agent run, tool call, prompt injection attempt against a live system, safety approval, or semantic quality score.

- [ ] **Step 1: Write 22 NEW package Eval sets and trigger data, plus three prompt-testing regression cases.**

  The prompt-regression cases must be named with a prompt-regression prefix, referenced by the existing eval.yaml, and use the physical local-rules skill value prompt-testing. Do not create a prompt-regression-testing directory.

- [ ] **Step 2: Run skill-up validate and the enhancement RED/green contract checks.**

      for file in skills/zh/testing-types/{rag-quality-testing,rag-retrieval-testing,agent-loop-testing,agent-memory-testing,agent-permission-testing,agent-failure-recovery-testing,agent-long-running-testing,multi-agent-testing,llm-hallucination-testing,llm-consistency-testing,ai-safety-testing}/evals/eval.yaml skills/en/testing-types/{rag-quality-testing,rag-retrieval-testing,agent-loop-testing,agent-memory-testing,agent-permission-testing,agent-failure-recovery-testing,agent-long-running-testing,multi-agent-testing,llm-hallucination-testing,llm-consistency-testing,ai-safety-testing}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      skill-up validate skills/zh/testing-types/prompt-testing/evals/eval.yaml
      skill-up validate skills/en/testing-types/prompt-testing/evals/eval.yaml
      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v

- [ ] **Step 3: Write the 11 bilingual AI Native packages and the prompt-testing enhancement.**

  Keep RAG quality distinct from retrieval mechanics, Agent permission distinct from tool-call mechanics, Agent failure recovery distinct from generic AI Agent testing, and LLM hallucination/consistency distinct from generic LLM testing. The Prompt and SKILL.md must state these boundaries and the lack of runtime evidence.

- [ ] **Step 4: Run all Batch 2 checks and commit the AI changes.**

      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

      git add skills/zh/testing-types/rag-quality-testing skills/en/testing-types/rag-quality-testing skills/zh/testing-types/rag-retrieval-testing skills/en/testing-types/rag-retrieval-testing skills/zh/testing-types/agent-loop-testing skills/en/testing-types/agent-loop-testing skills/zh/testing-types/agent-memory-testing skills/en/testing-types/agent-memory-testing skills/zh/testing-types/agent-permission-testing skills/en/testing-types/agent-permission-testing skills/zh/testing-types/agent-failure-recovery-testing skills/en/testing-types/agent-failure-recovery-testing skills/zh/testing-types/agent-long-running-testing skills/en/testing-types/agent-long-running-testing skills/zh/testing-types/multi-agent-testing skills/en/testing-types/multi-agent-testing skills/zh/testing-types/llm-hallucination-testing skills/en/testing-types/llm-hallucination-testing skills/zh/testing-types/llm-consistency-testing skills/en/testing-types/llm-consistency-testing skills/zh/testing-types/ai-safety-testing skills/en/testing-types/ai-safety-testing skills/zh/testing-types/prompt-testing skills/en/testing-types/prompt-testing
      git commit -m "feat(v3-v4): add ai native skill batch"

---

### Task 10: 完成 Batch 2 治理同步、质量门禁和 Done 状态

**Files:**

- Modify: docs/governance/PHASE_3_V3_V4.md、docs/governance/PHASE_3_V3_V4_EN.md、docs/governance/skill-governance-registry.yaml
- Regenerate: docs/SKILL_MATRIX.md、docs/SKILL_MATRIX_EN.md、docs/SKILL_MATCHING_REGISTER.md、docs/SKILL_MATCHING_REGISTER_EN.md、docs/generated/
- Modify: README.md、README_EN.md、skills/zh/README.md、skills/en/README.md、docs/catalog/skills-index.md、docs/catalog/skills-index_EN.md、docs/catalog/skills-graph.md、docs/catalog/skills-graph_EN.md、docs/governance/SKILL_GOVERNANCE_ROADMAP.md、docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md

**Interfaces:**

- Consumes: 24 Batch 2 NEW packages, prompt-testing enhancement, and Batch 1 accepted current-state evidence.
- Produces: 24 new physical registry records, one ENHANCE candidate record targeting prompt-testing, generated bilingual governance views, and final current Project status evidence for 25 cards.
- Boundary: do not add a prompt-regression-testing physical registry skill record; record it only in candidates with conclusion ENHANCE and target prompt-testing.

- [ ] **Step 1: Add Batch 2 physical and candidate registry records.**

  Add P2 roles, lifecycle stage, input/output evidence, related/workflow boundary, and all physical paths for the 24 NEW packages. Add prompt-regression-testing as decision_state REVIEWED, conclusion ENHANCE, target prompt-testing, existing_targets pointing to both prompt-testing packages and Prompt, difference describing the regression mode, target_evidence_paths for the enhanced files, and no duplicate physical slug. Keep all new quality and Eval states NOT_SCORED and NOT_RUN.

- [ ] **Step 2: Add the v3-v4 navigation compositions.**

  Add Reliability + Security, Quality Engineering, and AI Native rows to both skills indexes and graphs. Add a prompt-testing regression-mode note instead of a new catalog entry. Update root and language READMEs with only the actual physical NEW packages. Update the governance roadmap and Phase 3 record with current batch states and the explicit static-evidence boundary.

- [ ] **Step 3: Generate and run all local gates before Done.**

      python3 scripts/generate_skill_governance_matrix.py
      python3 scripts/generate_skill_governance_inventory.py
      python3 scripts/generate_skill_governance_matrix.py --check
      python3 scripts/generate_skill_governance_inventory.py --check
      python3 -m unittest scripts.tests.test_v3_v4_match_contracts scripts.tests.test_v3_v4_batch1_skill_contracts scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      python3 -m unittest discover -s scripts/tests -v
      bash scripts/check_skills_quality.sh
      git diff --check

- [ ] **Step 4: Move only the 25 exact Batch 2 cards from In Progress to Done.**

  Re-resolve live Status and Done option IDs, assert all 25 are In Progress and all 17 Batch 1 cards remain Done, then edit only the 25 exact IDs. Read the Project again and record current status and the command/date evidence. Keep transition_audit UNASSESSED and acceptance_state INCOMPLETE unless an independent event-history source is available.

- [ ] **Step 5: Regenerate after Project evidence and commit Batch 2 governance.**

  Add final Project evidence to the 25 candidate records, regenerate all views, run the generators with --check and the full quality gate again, then stage only the governance/navigation files and commit:

      git add docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md docs/governance/skill-governance-registry.yaml docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/generated README.md README_EN.md skills/zh/README.md skills/en/README.md docs/catalog docs/governance/SKILL_GOVERNANCE_ROADMAP.md docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
      git commit -m "feat(v3-v4): close batch2 governance evidence"

---

### Task 11: 两批最终验收与交付边界核对

**Files:**

- Read-only: all files changed by Tasks 1–10
- Modify only if a verified generated-file or bilingual parity defect is found; do not widen scope for cosmetic cleanup.

**Interfaces:**

- Consumes: both batch commits, final Project snapshot, registry, generated views, and all contract reports.
- Produces: a reproducible local acceptance record with exact counts and explicit unrun boundaries.
- Boundary: no push, Release, real-model Eval, external target execution, or historical-transition claim.

- [ ] **Step 1: Verify physical and logical counts.**

  With the expected Match result, verify 41 new slugs exist under both languages, prompt-regression-testing has no physical directory, and the current baseline of 121 packages per language has become 162 per language and 324 physical directories total. If Match evidence changed the number, report the actual count and explain the difference in Phase 3.

      rg --files skills/zh | rg '/SKILL.md$' | wc -l
      rg --files skills/en | rg '/SKILL.md$' | wc -l
      test ! -d skills/zh/testing-types/prompt-regression-testing
      test ! -d skills/en/testing-types/prompt-regression-testing

- [ ] **Step 2: Run the complete verification set.**

      python3 -m unittest discover -s scripts/tests -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_agents_metadata.py --report /tmp/v3-v4-metadata.md
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v3-v4-independence.md
      python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/v3-v4-integrity.md
      python3 scripts/generate_skill_governance_matrix.py --check
      python3 scripts/generate_skill_governance_inventory.py --check
      bash scripts/check_skills_quality.sh
      git diff --check

- [ ] **Step 3: Verify Project scope and status.**

  Read Project #4 and assert the 17 Batch 1 and 25 Batch 2 cards are Done, no unrelated card changed during this task, and the final record names the current-status limitation. Current Done does not prove the historical In Progress -> Done sequence.

- [ ] **Step 4: Inspect Git scope and report exact delivery state.**

      git status --short --branch
      git log --oneline --decorate -12
      git diff origin/main...HEAD --stat
      git diff origin/main...HEAD --check

  Report the merge commit 15c3804, the v3-v4 design/plan and implementation commits, exact changed package/registry/doc counts, all passing commands, Project current-status evidence, and remaining NOT_RUN/NOT_SCORED/UNASSESSED boundaries. Do not report the work as a published release or pushed branch.
