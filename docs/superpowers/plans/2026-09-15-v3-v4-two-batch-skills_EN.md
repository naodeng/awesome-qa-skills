# v3-v4 Two-Batch Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox ([ ]) syntax for tracking.

**Goal:** On develop after the latest main merge, complete Capability Match, bilingual Skill delivery, governance synchronization, and evidence-bounded Project acceptance for the 42 v3-v4 P2 cards in two batches: Reliability + Security, then Quality Engineering + AI Native.

**Architecture:** Establish one Match ledger and domain-prefix map for all 42 cards first. The current working conclusion is 41 NEW physical Skill packages in both languages plus one prompt-regression mode enhancement on prompt-testing; if fresh evidence changes a conclusion, update the ledger before creating a directory. Each batch tests only its actual NEW or ENHANCE/MERGE deliverables to RED, moves only exact Project cards, and then synchronizes the registry, Matrix, Register, Catalog, Graph, and bilingual entry documents.

**Tech Stack:** Markdown, YAML, CSV, JSON, Python 3 standard library, unittest, skill-up validate/run, existing governance generators, GitHub Project CLI, and bash scripts/check_skills_quality.sh.

**Spec:** docs/superpowers/specs/2026-09-15-v3-v4-two-batch-design_EN.md

## Global Constraints

- The phase-start snapshot is `15c3804`; this PR's review base is `origin/main@7f981931`. Preserve all existing v2 work and do not reset or overwrite unrelated changes.
- Batch 1 contains exactly 17 slugs: reliability-testing, resilience-testing, chaos-testing, failover-testing, recovery-testing, retry-testing, timeout-testing, circuit-breaker-testing, dependency-failure-testing, disaster-recovery-testing, authentication-testing, authorization-testing, session-security-testing, api-security-testing, security-requirement-review, threat-modeling, and secrets-exposure-review.
- Batch 2 contains exactly 25 slugs: quality-gate-design, quality-metrics-design, quality-dashboard-design, quality-debt-analysis, quality-maturity-assessment, test-effectiveness-analysis, automation-roi-analysis, testing-bottleneck-analysis, regression-optimization, ci-test-optimization, test-runtime-optimization, test-maintenance-cost-analysis, quality-productivity-metrics, prompt-regression-testing, rag-quality-testing, rag-retrieval-testing, agent-loop-testing, agent-memory-testing, agent-permission-testing, agent-failure-recovery-testing, agent-long-running-testing, multi-agent-testing, llm-hallucination-testing, llm-consistency-testing, and ai-safety-testing.
- The expected Match result is 41 NEW and one ENHANCE; live evidence controls the final result. Create a physical directory only for NEW. By default prompt-regression-testing enhances prompt-testing and does not create an alias directory.
- Every NEW language package contains SKILL.md, prompts/<slug>.md, agents/openai.yaml, evals/eval.yaml, basic-success.yaml, edge-incomplete-input.yaml, edge-scope-boundary.yaml, trigger-prompts.csv, and local-rules.json. Enhancement targets keep their physical directory and gain the mode contract and three mode cases.
- Every Prompt starts with the known, missing, conflicting, stale, out_of_scope, and assumptions audit, then separates facts, evidence-backed inferences, candidate recommendations, and Human decisions. Findings use the stable prefixes in the spec.
- Static files, names, trigger dry-runs, skill-up validate, unit tests, and quality gates do not prove model effectiveness, external execution, absence of vulnerabilities, coverage, quality score, risk acceptance, business approval, or Release completion.
- Move only the exact Project items listed by this plan. Do not move v4.1 Enhance Review, v4.0 Workflow, v3.4 Performance Review, Release DoD, or other cards; do not create repository Issues, push, or create a Release.
- Before and after every external mutation, read Project #4 live with gh project item-list. Resolve the Status field ID and option IDs from gh project field-list rather than assuming historical IDs.
- End each deliverable task with its relevant verification and a scoped commit. Stage only that task's paths and preserve unrelated work.

## File Map

- Match source and acceptance record: docs/governance/PHASE_3_V3_V4.md and docs/governance/PHASE_3_V3_V4_EN.md.
- Shared batch contract definitions: scripts/tests/v3_v4_skill_contracts.py.
- Match contract: scripts/tests/test_v3_v4_match_contracts.py.
- Batch contracts: scripts/tests/test_v3_v4_batch1_skill_contracts.py, scripts/tests/test_v3_v4_batch2_skill_contracts.py, and scripts/tests/test_v3_v4_prompt_regression_contract.py.
- NEW packages: skills/zh/testing-types/<slug>/ and skills/en/testing-types/<slug>/ for the 41 NEW slugs.
- Enhancement target: skills/zh/testing-types/prompt-testing/ and skills/en/testing-types/prompt-testing/.
- Governance source and generated views: docs/governance/skill-governance-registry.yaml, docs/SKILL_MATRIX.md, docs/SKILL_MATRIX_EN.md, docs/SKILL_MATCHING_REGISTER.md, docs/SKILL_MATCHING_REGISTER_EN.md, and docs/generated/.
- Navigation and lifecycle documents: README.md, README_EN.md, skills/zh/README.md, skills/en/README.md, docs/catalog/skills-index.md, docs/catalog/skills-index_EN.md, docs/catalog/skills-graph.md, docs/catalog/skills-graph_EN.md, docs/governance/SKILL_GOVERNANCE_ROADMAP.md, and docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md.
- External execution record: GitHub Project #4 current status only; transition history remains UNASSESSED if the API exposes only current status.

---

### Task 1: Establish the v3-v4 Capability Match ledger and shared contracts

**Files:**

- Create: scripts/tests/v3_v4_skill_contracts.py
- Create: scripts/tests/test_v3_v4_match_contracts.py
- Create: docs/governance/PHASE_3_V3_V4.md
- Create: docs/governance/PHASE_3_V3_V4_EN.md
- Read-only reference: docs/superpowers/specs/2026-09-15-v3-v4-two-batch-design_EN.md
- Read-only reference: docs/governance/skill-governance-registry.yaml
- Read-only reference: current generic security, regression, reporting, Agent, LLM, and Prompt Skill packages

**Interfaces:**

- Produces: BATCH_1, BATCH_2, NEW_SKILLS, ENHANCEMENTS, CARD_IDS, PREFIXES, DOMAIN_MARKERS, and each target, conclusion, existing_targets, and difference.
- Consumes: 42 exact Project item IDs, the current physical Skill tree, governance records, and the written v3-v4 specification.
- Boundary: this task records Match and static targets only; it creates no v3-v4 package and changes no Project status.

- [ ] **Step 1: Read the live candidate cards and current Skill tree.**

      gh project item-list 4 --owner naodeng --format json --limit 200 | jq '[.items[] | select((.content.title // "") | startswith("v3-v4 P2｜候选 Skill｜"))] | {count: length, statuses: (group_by(.status) | map({status: .[0].status, count: length}))}'
      rg --files skills/zh skills/en | rg '/SKILL.md$' | sort
      git status --short --branch

  Expected: 42 candidates, all Todo, with the current v2 tree unchanged. Record the command date as 2026-09-15 in the Phase 3 document.

- [ ] **Step 2: Write the exact shared maps and Match evidence.**

  Define the exact BATCH_1 and BATCH_2 maps from the spec in scripts/tests/v3_v4_skill_contracts.py. Put all 41 non-prompt-regression slugs in NEW_SKILLS with target_section testing-types, and define:

      ENHANCEMENTS = {
          "prompt-regression-testing": {
              "target": "prompt-testing",
              "target_section": "testing-types",
              "mode": "prompt-regression",
              "prefix": "PRT-",
          }
      }

  Keep every v3-v4 prefix unique. Add bilingual domain markers and minimum input/output focus for every slug. Use security-testing as comparison evidence for security specialists, regression-scope-analysis and regression-test-selection for regression-optimization, test-reporting and quality-risk-analysis for QE candidates, and ai-agent-testing, agent-tool-testing, llm-testing, prompt-testing, and prompt-injection-testing for AI Native candidates. Every difference statement must explain the narrower or structurally different contract without claiming runtime effectiveness.

- [ ] **Step 3: Write the bilingual Phase 3 governance record.**

  Add all 42 rows with exact item ID, batch, domain, proposed conclusion, target path, six Match fields, difference, non-goals, and planned evidence. Record 41 NEW and prompt-regression-testing ENHANCE as the reviewed working conclusion, while stating that fresh source evidence may revise a row before package creation. Include complete Batch 1 and Batch 2 lists and the card-state protocol.

- [ ] **Step 4: Write and run a deterministic Match contract test.**

  Assert exact candidate count 42; exact Batch 1 count 17; exact Batch 2 count 25; no overlap; exact Project item IDs; unique prefixes; 41 NEW plus one ENHANCE; prompt-regression-testing targets prompt-testing; no v4.1/v4.0/v3.4/Release DoD card is selected; both Phase documents contain the same slug and item-ID rows; and all six evidence fields are nonempty.

      python3 -m unittest scripts.tests.test_v3_v4_match_contracts -v
      git diff --check

  Expected: the ledger passes and no v3-v4 Skill directory exists. If the live Project result differs, update the ledger and shared map before proceeding.

- [ ] **Step 5: Review and commit the ledger.**

      git diff --check
      git diff --name-only
      git status --short
      git add scripts/tests/v3_v4_skill_contracts.py scripts/tests/test_v3_v4_match_contracts.py docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md
      git commit -m "docs(v3-v4): record capability match ledger"

  Expected: one scoped commit and no Project status changes.

---

### Task 2: Add Batch 1 contracts and confirm RED for actual NEW targets

**Files:**

- Create: scripts/tests/test_v3_v4_batch1_skill_contracts.py
- Modify: scripts/tests/v3_v4_skill_contracts.py only if live Match changes
- Read-only reference: scripts/tests/v20_skill_contracts.py and scripts/tests/test_v20_batch1_skill_contracts.py

**Interfaces:**

- Consumes: Task 1 BATCH_1, NEW_SKILLS, PREFIXES, and DOMAIN_MARKERS.
- Produces: a reusable static contract for the 17 Batch 1 NEW package targets.
- Boundary: the test checks structure and declared text; it does not run Chaos, security tools, failover, recovery, or production systems.

- [ ] **Step 1: Write the failing contract test before package files.**

  For both languages and every actual NEW slug, assert all nine required files, physical frontmatter and metadata identity, shared input-audit terms, language separation, domain finding prefix, required output fields, all three eval references, four trigger modes with true and false values, and local-rules alignment. Add domain markers for all ten Reliability and seven Security prompts. Scope cases must contain the corresponding refusal terms for tests executed, all tests passed, and release approved.

- [ ] **Step 2: Run only the Batch 1 contract and record RED.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v

  Expected: FAIL because the 17 NEW bilingual package directories and required files are absent. A test typo is not acceptable RED; fix the test until the failure identifies missing target behavior.

- [ ] **Step 3: Verify the RED boundary and commit the contract.**

      git diff --check
      git status --short
      git add scripts/tests/test_v3_v4_batch1_skill_contracts.py
      git commit -m "test(v3-v4): add batch1 skill contracts"

  Do not move cards or create package files before this RED evidence exists.

---

### Task 3: Move the 17 Batch 1 cards to In Progress

**External state:**

- Exact Project #4 items: PVTI_lAHOAHP1as4BjBhVzg6Sc5w, PVTI_lAHOAHP1as4BjBhVzg6Sc68, PVTI_lAHOAHP1as4BjBhVzg6Sc8M, PVTI_lAHOAHP1as4BjBhVzg6Sc90, PVTI_lAHOAHP1as4BjBhVzg6Sc_w, PVTI_lAHOAHP1as4BjBhVzg6SdAw, PVTI_lAHOAHP1as4BjBhVzg6SdCU, PVTI_lAHOAHP1as4BjBhVzg6SdEM, PVTI_lAHOAHP1as4BjBhVzg6SdFo, PVTI_lAHOAHP1as4BjBhVzg6SdHI, PVTI_lAHOAHP1as4BjBhVzg6SdJA, PVTI_lAHOAHP1as4BjBhVzg6SdLg, PVTI_lAHOAHP1as4BjBhVzg6SdNI, PVTI_lAHOAHP1as4BjBhVzg6SdPY, PVTI_lAHOAHP1as4BjBhVzg6SdQ0, PVTI_lAHOAHP1as4BjBhVzg6SdSk, PVTI_lAHOAHP1as4BjBhVzg6SdUg
- Project ID: PVT_kwHOAHP1as4BjBhVzg6

- [ ] **Step 1: Resolve live Status field and options.**

      gh project field-list 4 --owner naodeng --format json | jq '.fields[] | select(.name == "Status")'

  Capture the Status field ID and the live option IDs for Todo, In Progress, and Done. Do not use a hard-coded option if live output differs.

- [ ] **Step 2: Verify the exact precondition.**

  Read Project #4 and assert the 17 exact titles are Todo, the nine v2 cards remain Done, and all other v3-v4 P2 candidates remain Todo. Stop mutation if an exact item is missing or already changed.

- [ ] **Step 3: Update only the exact 17 items.**

  For each item, run the equivalent of:

      gh project item-edit --project-id PVT_kwHOAHP1as4BjBhVzg6 --id <exact-item-id> --field-id <live-status-field-id> --single-select-option-id <live-in-progress-option-id>

- [ ] **Step 4: Re-read and verify scope.**

      gh project item-list 4 --owner naodeng --format json --limit 200 | jq '[.items[] | select((.content.title // "") | startswith("v3-v4 P2｜候选 Skill｜")) | {title: .content.title, status: .status}]'

  Expected: the exact Batch 1 rows are In Progress; all 25 Batch 2 cards remain Todo; unrelated Project cards are unchanged. Record the current snapshot in PHASE_3_V3_V4.md without claiming historical transition evidence.

---

### Task 4: Implement the 10 bilingual Reliability NEW packages in Batch 1

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for reliability-testing, resilience-testing, chaos-testing, failover-testing, recovery-testing, retry-testing, timeout-testing, circuit-breaker-testing, dependency-failure-testing, and disaster-recovery-testing.
- Every package creates SKILL.md, prompts/<slug>.md, agents/openai.yaml, evals/eval.yaml, the three required case files, evals/trigger-prompts.csv, and evals/local-rules.json.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| reliability-testing | RLT- | reliability objectives, SLI/SLO evidence, failure budget, observable acceptance, and residual risk |
| resilience-testing | RES- | graceful degradation, isolation, bulkheads, dependency loss, and service continuity |
| chaos-testing | CHS- | experiment hypothesis, steady state, blast radius, safety guard, abort, and observability |
| failover-testing | FOV- | failure detection, switchover trigger, fallback target, continuity, and split-brain concern |
| recovery-testing | RCV- | restore sequence, data integrity, recovery point/time objective, and verification evidence |
| retry-testing | RTY- | retryable conditions, backoff/jitter, attempt cap, idempotency, and amplification risk |
| timeout-testing | TMO- | deadline ownership, cancellation, partial result behavior, timeout source, and downstream propagation |
| circuit-breaker-testing | CBR- | closed/open/half-open transitions, thresholds, fallback, probe, and recovery evidence |
| dependency-failure-testing | DPF- | dependency error taxonomy, propagation, fallback, isolation, and contract mismatch |
| disaster-recovery-testing | DRT- | backup/restore, region/site loss, RTO/RPO, communication, ownership, and exercise evidence |

- Produces: domain-specific PREFIX-## findings with object/rule, source, trigger/applicability, concern/rationale, evidence state, impact/priority, owner role, close condition, and validation method.
- Boundary: no fault injection, real dependency call, benchmark, failover switch, restore operation, production change, or unverified RTO/RPO value.

- [ ] **Step 1: Write all ten bilingual Eval configurations, cases, trigger CSVs, and local rules.**

  Basic cases need domain-specific input and expected evidence-bound PREFIX-## output. Incomplete cases name missing threshold, baseline, dependency, environment, or ownership information. Boundary cases reject execution/pass/release claims. Trigger rows include four modes, a positive row, and a reverse-control row in the correct language.

- [ ] **Step 2: Validate all 20 Eval files before the long Prompt text.**

      for file in skills/zh/testing-types/{reliability-testing,resilience-testing,chaos-testing,failover-testing,recovery-testing,retry-testing,timeout-testing,circuit-breaker-testing,dependency-failure-testing,disaster-recovery-testing}/evals/eval.yaml skills/en/testing-types/{reliability-testing,resilience-testing,chaos-testing,failover-testing,recovery-testing,retry-testing,timeout-testing,circuit-breaker-testing,dependency-failure-testing,disaster-recovery-testing}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done

- [ ] **Step 3: Write the ten Chinese and English entrypoints, Prompts, and metadata.**

  Each entrypoint states real triggers, required Prompt loading, evidence boundary, on-demand reference rule, self-check, and domain pitfalls. Each Prompt uses the shared audit, its minimum coverage, and the PREFIX-## Finding Contract. The English body contains no Chinese.

- [ ] **Step 4: Run Batch 1 contract, Eval, independence, and diff checks.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

  Expected: the Reliability ten packages pass; the seven Security package targets remain the only unfinished Batch 1 NEW packages.

- [ ] **Step 5: Commit only Reliability package files.**

      git add skills/zh/testing-types/reliability-testing skills/en/testing-types/reliability-testing skills/zh/testing-types/resilience-testing skills/en/testing-types/resilience-testing skills/zh/testing-types/chaos-testing skills/en/testing-types/chaos-testing skills/zh/testing-types/failover-testing skills/en/testing-types/failover-testing skills/zh/testing-types/recovery-testing skills/en/testing-types/recovery-testing skills/zh/testing-types/retry-testing skills/en/testing-types/retry-testing skills/zh/testing-types/timeout-testing skills/en/testing-types/timeout-testing skills/zh/testing-types/circuit-breaker-testing skills/en/testing-types/circuit-breaker-testing skills/zh/testing-types/dependency-failure-testing skills/en/testing-types/dependency-failure-testing skills/zh/testing-types/disaster-recovery-testing skills/en/testing-types/disaster-recovery-testing
      git commit -m "feat(v3-v4): add reliability skill batch"

---

### Task 5: Implement the seven bilingual Security NEW packages in Batch 1

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for authentication-testing, authorization-testing, session-security-testing, api-security-testing, security-requirement-review, threat-modeling, and secrets-exposure-review.
- Every package creates the same nine required files as Task 4.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| authentication-testing | AUT- | identity proof, login/re-authentication, token/session boundary, recovery, and abuse evidence |
| authorization-testing | AZT- | subject-resource-action policy, least privilege, deny-by-default, tenant, and role boundary |
| session-security-testing | SST- | creation, rotation, expiry, revocation, fixation, concurrent use, and logout evidence |
| api-security-testing | AST- | API attack surface, input/output validation, auth, sensitive data, rate limiting, and auditability |
| security-requirement-review | SRR- | security requirement clarity, threat linkage, acceptance criteria, ownership, and traceability |
| threat-modeling | THM- | assets, trust boundaries, data flows, threats, controls, abuse cases, and residual uncertainty |
| secrets-exposure-review | SER- | supplied source/config/log secret patterns, exposure path, severity evidence, remediation, and rotation ownership |

- Boundary: do not log in, send credentials, retrieve secrets, run a scanner, attack a target, claim absence of vulnerabilities, or approve a risk exception.

- [ ] **Step 1: Write seven bilingual Eval sets and trigger controls.**

  Use security-specific inputs and require evidence state plus the Human decision boundary in every expected output. Incomplete cases preserve missing threat-model, scope, identity, policy, secret-classification, or rotation evidence.

- [ ] **Step 2: Validate all 14 Eval files and run the Batch 1 contract.**

      for file in skills/zh/testing-types/{authentication-testing,authorization-testing,session-security-testing,api-security-testing,security-requirement-review,threat-modeling,secrets-exposure-review}/evals/eval.yaml skills/en/testing-types/{authentication-testing,authorization-testing,session-security-testing,api-security-testing,security-requirement-review,threat-modeling,secrets-exposure-review}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v

- [ ] **Step 3: Write the seven bilingual entrypoints, Prompts, and metadata.**

  State the distinction from generic security-testing in every Prompt and Match record: each new package narrows the input and decision contract and does not claim stronger runtime security results.

- [ ] **Step 4: Run checks and commit Security files.**

      python3 -m unittest scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check
      git add skills/zh/testing-types/authentication-testing skills/en/testing-types/authentication-testing skills/zh/testing-types/authorization-testing skills/en/testing-types/authorization-testing skills/zh/testing-types/session-security-testing skills/en/testing-types/session-security-testing skills/zh/testing-types/api-security-testing skills/en/testing-types/api-security-testing skills/zh/testing-types/security-requirement-review skills/en/testing-types/security-requirement-review skills/zh/testing-types/threat-modeling skills/en/testing-types/threat-modeling skills/zh/testing-types/secrets-exposure-review skills/en/testing-types/secrets-exposure-review
      git commit -m "feat(v3-v4): add security skill batch"

---

### Task 6: Complete Batch 1 governance, gates, and Done status

**Files:**

- Modify: docs/governance/PHASE_3_V3_V4.md, docs/governance/PHASE_3_V3_V4_EN.md
- Modify: docs/governance/skill-governance-registry.yaml
- Regenerate: docs/SKILL_MATRIX.md, docs/SKILL_MATRIX_EN.md, docs/SKILL_MATCHING_REGISTER.md, docs/SKILL_MATCHING_REGISTER_EN.md, docs/generated/skill-governance-inventory.md, docs/generated/skill-governance-inventory_EN.md
- Modify: README.md, README_EN.md, skills/zh/README.md, skills/en/README.md, docs/catalog/skills-index.md, docs/catalog/skills-index_EN.md, docs/catalog/skills-graph.md, docs/catalog/skills-graph_EN.md, docs/governance/SKILL_GOVERNANCE_ROADMAP.md, docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md

**Interfaces:**

- Consumes: 17 completed bilingual packages and the Task 1 Match ledger.
- Produces: 17 physical registry records, 17 reviewed candidate records with Project evidence, bilingual navigation, and generated views.
- Boundary: quality_score stays NOT_SCORED; eval_execution stays NOT_RUN; transition history is UNASSESSED when only current status is available.

- [ ] **Step 1: Add Batch 1 physical registry records and candidate evidence.**

  Each new package record uses section testing-types, status Planned-P2, priority P2, the applicable virtual domain, sdlc_stage, roles, inputs, outputs, related, workflow, governance_evidence, and all bilingual evidence_paths. Each candidate record uses decision_state REVIEWED, conclusion NEW, target slug, six Match fields, scope, non_goals, candidate_source, capability_match, and target_evidence_paths. Before Done, do not invent a final project_evidence current_status; the generator requires Done for a final reviewed Project record, so add final evidence after the transition.

- [ ] **Step 2: Regenerate and validate local governance views.**

      python3 scripts/generate_skill_governance_matrix.py
      python3 scripts/generate_skill_governance_inventory.py
      python3 scripts/generate_skill_governance_matrix.py --check
      python3 scripts/generate_skill_governance_inventory.py --check

  Update both-language indexes, graph compositions, READMEs, and the governance roadmap with the Reliability + Security Batch 1 route. State that the specialists are optional navigation and do not create installation dependencies.

- [ ] **Step 3: Run full local gates before Done.**

      python3 -m unittest scripts.tests.test_v3_v4_match_contracts scripts.tests.test_v3_v4_batch1_skill_contracts -v
      bash scripts/check_skills_quality.sh
      python3 -m unittest discover -s scripts/tests -v
      git diff --check

- [ ] **Step 4: Move only the exact 17 Batch 1 cards to Done.**

  Resolve live Status and Done option IDs again; verify all 17 are In Progress and no Batch 2 card is In Progress. Edit only the same 17 IDs, re-read Project #4, and record current status, verified_at, verification command, required transition, transition_audit UNASSESSED, and acceptance_state INCOMPLETE.

- [ ] **Step 5: Add final Project evidence and re-run generated checks.**

  Add current Done evidence to the 17 candidate records, keep transition_audit explicitly UNASSESSED, regenerate Matrix/Register/Inventory, and run the full quality gate again. Never use COMPLETE while transition history is unavailable.

- [ ] **Step 6: Commit Batch 1 governance and acceptance.**

      git diff --check
      git add docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md docs/governance/skill-governance-registry.yaml docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/generated README.md README_EN.md skills/zh/README.md skills/en/README.md docs/catalog docs/governance/SKILL_GOVERNANCE_ROADMAP.md docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
      git commit -m "feat(v3-v4): close batch1 governance evidence"

  Expected: Batch 1 is currently Done; Batch 2 and unrelated cards retain their prior status.

---

### Task 7: Add Batch 2 contracts, confirm RED, and move its 25 cards

**Files:**

- Create: scripts/tests/test_v3_v4_batch2_skill_contracts.py
- Create: scripts/tests/test_v3_v4_prompt_regression_contract.py
- Modify: scripts/tests/v3_v4_skill_contracts.py only for an exact Match change
- Read-only reference: scripts/tests/test_v3_v4_batch1_skill_contracts.py
- External state: the exact 25 Batch 2 item IDs in the spec

**Interfaces:**

- Consumes: BATCH_2, NEW_SKILLS, ENHANCEMENTS, PREFIXES, and completed Batch 1 governance state.
- Produces: a 24-package NEW contract plus a prompt-testing enhancement contract.
- Boundary: prompt-regression-testing does not create a physical directory unless fresh Match evidence revises the approved default.

- [ ] **Step 1: Write the Batch 2 NEW contract.**

  Assert the same package structure, language separation, input audit, finding fields, four trigger modes, three case references, and local-rules alignment as Batch 1. Add markers for 13 QE packages and 11 AI Native NEW packages; exclude prompt-regression-testing from NEW.

- [ ] **Step 2: Write the prompt-regression enhancement contract.**

  Assert both prompt-testing packages retain their physical slug and required files, add a prompt-regression mode marker, add PRT-## regression findings with baseline/version/dataset/observed behavior/evidence state, add three regression cases, include candidate trigger rows, keep local-rules.json.skill equal to prompt-testing, and prove no prompt-regression-testing directory exists.

- [ ] **Step 3: Run both RED tests before Batch 2 content.**

      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      git diff --check

  Expected: the 24 NEW bilingual package targets and prompt-regression mode assertions fail for missing target behavior. Fix test defects instead of weakening the boundary.

- [ ] **Step 4: Commit the Batch 2 RED contracts.**

      git add scripts/tests/test_v3_v4_batch2_skill_contracts.py scripts/tests/test_v3_v4_prompt_regression_contract.py scripts/tests/v3_v4_skill_contracts.py
      git commit -m "test(v3-v4): add batch2 skill contracts"

- [ ] **Step 5: Resolve live Project state and move only Batch 2 to In Progress.**

  Confirm Batch 1 remains Done, the exact 25 Batch 2 cards are Todo, and unrelated cards are unchanged. Resolve live Status and option IDs, then update only:

      PVTI_lAHOAHP1as4BjBhVzg6SdWc PVTI_lAHOAHP1as4BjBhVzg6SdY4 PVTI_lAHOAHP1as4BjBhVzg6SdaY PVTI_lAHOAHP1as4BjBhVzg6SdcE PVTI_lAHOAHP1as4BjBhVzg6Sddo PVTI_lAHOAHP1as4BjBhVzg6SdfA PVTI_lAHOAHP1as4BjBhVzg6Sdg8 PVTI_lAHOAHP1as4BjBhVzg6Sdig PVTI_lAHOAHP1as4BjBhVzg6SdkQ PVTI_lAHOAHP1as4BjBhVzg6SdnA PVTI_lAHOAHP1as4BjBhVzg6Sdo4 PVTI_lAHOAHP1as4BjBhVzg6Sdqc PVTI_lAHOAHP1as4BjBhVzg6SdsA PVTI_lAHOAHP1as4BjBhVzg6SdtI PVTI_lAHOAHP1as4BjBhVzg6Sdus PVTI_lAHOAHP1as4BjBhVzg6Sdwg PVTI_lAHOAHP1as4BjBhVzg6SdyQ PVTI_lAHOAHP1as4BjBhVzg6Sdzo PVTI_lAHOAHP1as4BjBhVzg6Sd1E PVTI_lAHOAHP1as4BjBhVzg6Sd2I PVTI_lAHOAHP1as4BjBhVzg6Sd3w PVTI_lAHOAHP1as4BjBhVzg6Sd5g PVTI_lAHOAHP1as4BjBhVzg6Sd7Q PVTI_lAHOAHP1as4BjBhVzg6Sd8Q PVTI_lAHOAHP1as4BjBhVzg6Sd9w

  Re-read Project #4 and record the exact snapshot.

---

### Task 8: Implement the 13 bilingual Quality Engineering NEW packages

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for quality-gate-design, quality-metrics-design, quality-dashboard-design, quality-debt-analysis, quality-maturity-assessment, test-effectiveness-analysis, automation-roi-analysis, testing-bottleneck-analysis, regression-optimization, ci-test-optimization, test-runtime-optimization, test-maintenance-cost-analysis, and quality-productivity-metrics.
- Every package creates the nine required files.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| quality-gate-design | QGD- | gate criteria, evidence prerequisites, owner, override path, and Human decision |
| quality-metrics-design | QMD- | metric definition, numerator/denominator, source, freshness, caveat, and anti-gaming concern |
| quality-dashboard-design | QDD- | audience, decision questions, panels, drill-down, freshness, access, and alert boundary |
| quality-debt-analysis | QDA- | debt item, origin, impact, age, evidence, priority, owner, and remediation trade-off |
| quality-maturity-assessment | QMA- | capability dimensions, rubric anchors, evidence sufficiency, gaps, and maturity uncertainty |
| test-effectiveness-analysis | TEA- | test signal, defect/risk relation, detection limits, false confidence, and validation plan |
| automation-roi-analysis | ARO- | automation candidate, setup/run/maintenance cost, benefit assumption, horizon, and sensitivity |
| testing-bottleneck-analysis | TBA- | queue, wait, dependency, capacity, handoff, constraint evidence, and improvement experiment |
| regression-optimization | RGO- | selection/order/parallelism/caching trade-off, risk preservation, and execution-cost evidence |
| ci-test-optimization | CTO- | pipeline stages, feedback latency, resource use, flakiness, cache/shard constraints, and rollback |
| test-runtime-optimization | TRO- | slow tests, profiling evidence, setup/teardown, parallelism, isolation, and baseline |
| test-maintenance-cost-analysis | TMC- | change frequency, repair effort, flake cost, ownership, maintainability evidence, and confidence |
| quality-productivity-metrics | QPM- | quality/delivery metrics, denominator, attribution limit, gaming risk, and Human-use boundary |

- Boundary: do not invent metric values, ROI, cost, maturity, pipeline timing, causal productivity conclusions, release gates, or individual performance rankings.

- [ ] **Step 1: Write 26 bilingual Eval files and trigger datasets with the table markers.**
- [ ] **Step 2: Validate all 26 files, then implement SKILL.md, Prompt, and metadata.**
- [ ] **Step 3: Run Batch 2 contract, Eval, independence, and diff checks.**

      for file in skills/zh/testing-types/{quality-gate-design,quality-metrics-design,quality-dashboard-design,quality-debt-analysis,quality-maturity-assessment,test-effectiveness-analysis,automation-roi-analysis,testing-bottleneck-analysis,regression-optimization,ci-test-optimization,test-runtime-optimization,test-maintenance-cost-analysis,quality-productivity-metrics}/evals/eval.yaml skills/en/testing-types/{quality-gate-design,quality-metrics-design,quality-dashboard-design,quality-debt-analysis,quality-maturity-assessment,test-effectiveness-analysis,automation-roi-analysis,testing-bottleneck-analysis,regression-optimization,ci-test-optimization,test-runtime-optimization,test-maintenance-cost-analysis,quality-productivity-metrics}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check

- [ ] **Step 4: Commit only QE package files.**

      git add skills/zh/testing-types/quality-gate-design skills/en/testing-types/quality-gate-design skills/zh/testing-types/quality-metrics-design skills/en/testing-types/quality-metrics-design skills/zh/testing-types/quality-dashboard-design skills/en/testing-types/quality-dashboard-design skills/zh/testing-types/quality-debt-analysis skills/en/testing-types/quality-debt-analysis skills/zh/testing-types/quality-maturity-assessment skills/en/testing-types/quality-maturity-assessment skills/zh/testing-types/test-effectiveness-analysis skills/en/testing-types/test-effectiveness-analysis skills/zh/testing-types/automation-roi-analysis skills/en/testing-types/automation-roi-analysis skills/zh/testing-types/testing-bottleneck-analysis skills/en/testing-types/testing-bottleneck-analysis skills/zh/testing-types/regression-optimization skills/en/testing-types/regression-optimization skills/zh/testing-types/ci-test-optimization skills/en/testing-types/ci-test-optimization skills/zh/testing-types/test-runtime-optimization skills/en/testing-types/test-runtime-optimization skills/zh/testing-types/test-maintenance-cost-analysis skills/en/testing-types/test-maintenance-cost-analysis skills/zh/testing-types/quality-productivity-metrics skills/en/testing-types/quality-productivity-metrics
      git commit -m "feat(v3-v4): add quality engineering skill batch"

---

### Task 9: Implement 11 AI Native NEW packages and enhance prompt-testing

**Files:**

- Create matching packages under skills/zh/testing-types/ and skills/en/testing-types/ for rag-quality-testing, rag-retrieval-testing, agent-loop-testing, agent-memory-testing, agent-permission-testing, agent-failure-recovery-testing, agent-long-running-testing, multi-agent-testing, llm-hallucination-testing, llm-consistency-testing, and ai-safety-testing.
- Modify both language prompt-testing SKILL.md, prompts/prompt-testing.md, evals/eval.yaml, evals/trigger-prompts.csv, and evals/local-rules.json.
- Add three prompt-regression-specific case files under both prompt-testing evals/cases directories.

**Interfaces:**

| Skill | Prefix | Minimum focus |
| --- | --- | --- |
| rag-quality-testing | RAGQ- | grounding, relevance, completeness, citation/support, abstention, and answer-level evidence |
| rag-retrieval-testing | RAGT- | query variants, chunking, filters, recall/precision proxy, ranking, freshness, and retrieval evidence |
| agent-loop-testing | ALT- | loop state, planning/action/observation cycle, stop condition, budget, repetition, and trace evidence |
| agent-memory-testing | AMT- | memory write/read/update/delete, retention, contamination, isolation, provenance, and forgetting |
| agent-permission-testing | AGP- | Agent identity, tool/resource scope, approval, deny path, escalation, and side-effect boundary |
| agent-failure-recovery-testing | AFR- | failure classification, retry/fallback/escalation, state consistency, user notice, and recovery evidence |
| agent-long-running-testing | ALR- | checkpoint, heartbeat, resume, cancel, duplicate submission, timeout, and resource lifecycle |
| multi-agent-testing | MAT- | delegation, coordination, shared state, conflict, ownership, termination, and traceability |
| llm-hallucination-testing | LHT- | claim/source relation, unsupported assertion, abstention, uncertainty, and evidence review |
| llm-consistency-testing | LCT- | repeat inputs, version/model/prompt factors, invariant, variance evidence, and comparison boundary |
| ai-safety-testing | AIS- | safety policy, abuse category, refusal/redirect, privacy, escalation, and Human risk decision |

- Prompt-regression enhancement: add prompt-regression mode and PRT-## findings to prompt-testing. Findings include baseline, candidate version, dataset/test-prompt identity, expected behavior, observed behavior, evidence state, difference, validation method, and Human decision. Preserve all existing prompt-testing modes and IDs.
- Boundary: no model call, retrieval call, Agent run, tool call, live prompt-injection attempt, safety approval, or semantic quality score.

- [ ] **Step 1: Write 22 NEW package Eval sets and trigger data plus three prompt-testing regression cases.**

  Regression cases use a prompt-regression prefix, are referenced by the existing eval.yaml, and keep local-rules.json.skill equal to prompt-testing. Do not create a prompt-regression-testing directory.

- [ ] **Step 2: Validate Evals and run the enhancement contract.**

      for file in skills/zh/testing-types/{rag-quality-testing,rag-retrieval-testing,agent-loop-testing,agent-memory-testing,agent-permission-testing,agent-failure-recovery-testing,agent-long-running-testing,multi-agent-testing,llm-hallucination-testing,llm-consistency-testing,ai-safety-testing}/evals/eval.yaml skills/en/testing-types/{rag-quality-testing,rag-retrieval-testing,agent-loop-testing,agent-memory-testing,agent-permission-testing,agent-failure-recovery-testing,agent-long-running-testing,multi-agent-testing,llm-hallucination-testing,llm-consistency-testing,ai-safety-testing}/evals/eval.yaml; do skill-up validate "$file" || exit 1; done
      skill-up validate skills/zh/testing-types/prompt-testing/evals/eval.yaml
      skill-up validate skills/en/testing-types/prompt-testing/evals/eval.yaml
      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v

- [ ] **Step 3: Write the 11 bilingual AI Native packages and prompt-testing enhancement.**

  Keep RAG quality distinct from retrieval mechanics, Agent permission distinct from tool-call mechanics, Agent failure recovery distinct from generic AI Agent testing, and LLM hallucination/consistency distinct from generic LLM testing. State the runtime-evidence boundary in each Prompt and entrypoint.

- [ ] **Step 4: Run checks and commit AI changes.**

      python3 -m unittest scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      bash scripts/validate_skill_evals.sh
      python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
      git diff --check
      git add skills/zh/testing-types/rag-quality-testing skills/en/testing-types/rag-quality-testing skills/zh/testing-types/rag-retrieval-testing skills/en/testing-types/rag-retrieval-testing skills/zh/testing-types/agent-loop-testing skills/en/testing-types/agent-loop-testing skills/zh/testing-types/agent-memory-testing skills/en/testing-types/agent-memory-testing skills/zh/testing-types/agent-permission-testing skills/en/testing-types/agent-permission-testing skills/zh/testing-types/agent-failure-recovery-testing skills/en/testing-types/agent-failure-recovery-testing skills/zh/testing-types/agent-long-running-testing skills/en/testing-types/agent-long-running-testing skills/zh/testing-types/multi-agent-testing skills/en/testing-types/multi-agent-testing skills/zh/testing-types/llm-hallucination-testing skills/en/testing-types/llm-hallucination-testing skills/zh/testing-types/llm-consistency-testing skills/en/testing-types/llm-consistency-testing skills/zh/testing-types/ai-safety-testing skills/en/testing-types/ai-safety-testing skills/zh/testing-types/prompt-testing skills/en/testing-types/prompt-testing
      git commit -m "feat(v3-v4): add ai native skill batch"

---

### Task 10: Complete Batch 2 governance, gates, and Done status

**Files:**

- Modify: Phase 3 documents and docs/governance/skill-governance-registry.yaml
- Regenerate: Matrix, Register, and docs/generated views
- Modify: both root/language READMEs, both catalog indexes, both graph files, and both governance roadmaps

**Interfaces:**

- Consumes: 24 Batch 2 NEW packages, prompt-testing enhancement, and Batch 1 current-state evidence.
- Produces: 24 new physical registry records, one ENHANCE candidate targeting prompt-testing, generated bilingual governance views, and current Project evidence for 25 cards.
- Boundary: no prompt-regression-testing physical registry Skill record; keep it only as an ENHANCE candidate targeting prompt-testing.

- [ ] **Step 1: Add Batch 2 physical and candidate registry records.**

  Add P2 roles, lifecycle stage, input/output evidence, related/workflow boundary, and all physical paths for the 24 NEW packages. Add prompt-regression-testing with decision_state REVIEWED, conclusion ENHANCE, target prompt-testing, existing_targets for both prompt-testing packages and Prompt, a regression-mode difference, target_evidence_paths for enhanced files, and no duplicate physical slug. Keep quality_score NOT_SCORED and eval_execution NOT_RUN.

- [ ] **Step 2: Add v3-v4 navigation compositions.**

  Add Reliability + Security, Quality Engineering, and AI Native rows to both indexes and graphs. Add a prompt-testing regression-mode note rather than a new catalog entry. Update root/language READMEs with actual physical NEW packages and update the roadmap and Phase 3 record with current batch states and the static-evidence boundary.

- [ ] **Step 3: Generate and run all local gates before Done.**

      python3 scripts/generate_skill_governance_matrix.py
      python3 scripts/generate_skill_governance_inventory.py
      python3 scripts/generate_skill_governance_matrix.py --check
      python3 scripts/generate_skill_governance_inventory.py --check
      python3 -m unittest scripts.tests.test_v3_v4_match_contracts scripts.tests.test_v3_v4_batch1_skill_contracts scripts.tests.test_v3_v4_batch2_skill_contracts scripts.tests.test_v3_v4_prompt_regression_contract -v
      python3 -m unittest discover -s scripts/tests -v
      bash scripts/check_skills_quality.sh
      git diff --check

- [ ] **Step 4: Move only the exact 25 Batch 2 cards from In Progress to Done.**

  Re-resolve live Status and Done option IDs, assert all 25 are In Progress and all 17 Batch 1 cards remain Done, then edit only the 25 exact IDs. Read Project #4 again and record current status and command/date evidence. Keep transition_audit UNASSESSED and acceptance_state INCOMPLETE unless an independent event-history source is available.

- [ ] **Step 5: Add final Project evidence, regenerate, and commit.**

  Add final Project evidence to the 25 candidate records, regenerate all views, run generator checks and the full quality gate again, then stage only governance/navigation paths and commit:

      git add docs/governance/PHASE_3_V3_V4.md docs/governance/PHASE_3_V3_V4_EN.md docs/governance/skill-governance-registry.yaml docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/generated README.md README_EN.md skills/zh/README.md skills/en/README.md docs/catalog docs/governance/SKILL_GOVERNANCE_ROADMAP.md docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
      git commit -m "feat(v3-v4): close batch2 governance evidence"

---

### Task 11: Final two-batch acceptance and delivery-boundary audit

**Files:**

- Read-only: all files changed by Tasks 1–10
- Modify only for a verified generated-file or bilingual-parity defect; do not broaden scope for cosmetic cleanup.

**Interfaces:**

- Consumes: both batch commits, final Project snapshot, registry, generated views, and contract reports.
- Produces: reproducible local acceptance evidence with exact counts and explicit unrun boundaries.
- Boundary: no push, Release, real-model Eval, external target execution, or historical-transition claim.

- [ ] **Step 1: Verify physical and logical counts.**

  With the expected Match result, verify 41 NEW slugs exist in both languages, prompt-regression-testing has no physical directory, and the current baseline of 121 packages per language became 162 per language and 324 physical directories total. If Match changes the number, report the actual count and explain it in Phase 3.

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

  Read Project #4 and assert the 17 Batch 1 and 25 Batch 2 cards are Done, no unrelated card changed, and the final record names the current-status limitation. Current Done does not prove the historical In Progress -> Done sequence.

- [ ] **Step 4: Inspect Git scope and report exact delivery state.**

      git status --short --branch
      git log --oneline --decorate -12
      git diff origin/main...HEAD --stat
      git diff origin/main...HEAD --check

  Report the phase-start snapshot 15c3804, the current PR review base origin/main@7f981931, v3-v4 design/plan and implementation commits, exact package/registry/doc counts, passing commands, current Project evidence, and NOT_RUN/NOT_SCORED/UNASSESSED boundaries. Do not call this a published release or pushed branch.
