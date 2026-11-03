<div align="right"><a href="./WORKFLOW_RELIABILITY_ENHANCEMENT_V1.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Workflow Reliability Enhancement v1.0

## Goal and scope

Compose existing QA Skills into traceable, evaluable workflows while preserving canonical names, bilingual directories, and standalone installation. Workflows define routing, stages, handoffs, evidence, and gates. This repository does not implement a scheduler, persistent workflow state, or host-tool permission engine.

This is one continuous delivery. The four iterations show dependency order; they are not checkpoints that require a new authorization. New orchestration packages compose existing specialist Skills instead of copying their analysis prompts.

## Pre-implementation audit (2026-10-30 workspace)

| Capability | Current state and evidence | Decision |
| --- | --- | --- |
| Workflow directories | There are 10 tracked `testing-workflows` packages, plus an untracked `tdd-quality-workflow` in the workspace (11 directories on disk). They include a router, timeline workflows, and quality-perspective prompt collections; perspective packages are not fixed stage pipelines. | Preserve paths and canonical names; distinguish routers, workflows, and prompt collections in governance records. |
| Router | Before implementation, `discover-testing` had a 166-entry capability snapshot, five Composition routes, one-primary/at-most-one-optional rules, and routing Evals. This pass updates the snapshot to 169 and adds three end-to-end routes. A directory does not prove Host installation; missing installation evidence is `UNKNOWN`. | Keep and extend the Router; add explicit end-to-end workflow routes and missing-dependency, wrong-route, and conflict cases. |
| Specialist capabilities | The repository already has code review, change impact, regression selection, requirement analysis, testability, test strategy, test design, test effectiveness, release testing, quality gate, and production verification Skills. | Reuse existing Skills; add only three orchestration packages: `pr-quality-review`, `requirement-to-test`, and `change-to-regression`. |
| Release readiness | `release-testing-workflow` already covers T-N, Go/No-Go recommendations, evidence packs, specialist handoffs, and human approval. The roadmap explicitly advises against splitting readiness into a duplicate package. | Add standard Workflow/Evidence Contract support to the existing package; do not create another release Skill. |
| Eval and quality gates | Skill-level `eval.yaml`, cases, Skill-up validation/run scripts, integrity/independence/bilingual/CLI gates already exist. `skill_eval_evidence.py` records Skill Eval run metadata. The current quality script has 11 check groups. | Keep Skill Evals; add Workflow contract checks and cross-stage handoff, permission, and recovery scenarios. Structural validation must not be presented as model behavior Eval. |
| State and evidence | No generic `workflow.yaml`, `evidence.json` schema, or persistent Workflow Runtime exists. | Add versioned JSON Schemas, examples, and dependency-free validation; define checkpoint/staleness/replay rules while leaving runtime state to an external Workbench. |
| Lifecycle | Before implementation, the governance registry covered 166 bilingual Skill pairs; this pass extends it to 169 and adds a separate lifecycle state to every record. Real invocation volume and usage value are unavailable. | Define lifecycle and retirement/migration policy. Keep usage value `UNASSESSED` without adoption evidence; do not infer popularity from directories or static Evals. |
| Agent distribution | Installers support Codex, Claude Code, Cursor, and others; a pinned `skills@1.7.0` CLI gate exists. Install previews do not prove in-host execution. | Add a compatibility matrix, standalone ZIP packaging, and safe uninstall/residue checks; report install structure, CLI compatibility, and real host execution separately. |

## Implementation and acceptance plan

| # | Work item | Implementation decision and deliverable | Acceptance evidence |
| --- | --- | --- | --- |
| 01 | Existing capability audit · P0 | Maintain workflow-to-capability mapping; record overlap, Router conflicts, Eval and gate coverage; label retain/enhance/merge/add decisions. | Auditable table with repository paths; static inventory is not described as runtime behavior. |
| 02 | `discover-testing` v2 · P0 | Preserve the canonical name; route one step by default and select a Workflow when the user specifies an end state; report availability evidence, missing dependencies, conflicts, and only necessary clarification. | Bilingual positive, reverse, boundary, and missing-Skill Evals; one primary and at most one optional Skill. |
| 03 | Workflow standard contract · P0 | JSON Schema for id/version/kind, inputs/outputs, stages, dependencies, skip/failure, permissions, handoff, and evidence references; add `workflow.yaml` to workflow packages. | All workflow contracts validate and bilingual packages match. |
| 04 | PR Quality Review · P0 | Add a thin orchestration package composing `code-review`, `pr-test-impact-analysis`, `test-code-review` / `ai-generated-test-review`, and quality-gate capabilities. | Diff context, test obligations, weak tests, severity findings, blockers, and human approval boundary are covered by Evals. |
| 05 | Requirement-to-Test · P1 | Add requirement-to-case orchestration using existing requirement quality, testability, strategy, test design, and gap-analysis capabilities. | Testability gaps, risk strategy, cases and traceability, and coverage gaps cross stage handoffs. |
| 06 | Change-to-Regression · P1 | Add change-to-regression orchestration using impact analysis, regression scope, test selection, and flaky analysis. | Required/deferred tiers, exclusion rationale, uncovered risk, and execution state are traceable. |
| 07 | Release Readiness · P1 | Enhance the existing `release-testing-workflow` with the shared evidence contract and preserve human authority for final approval. | Scope, evidence, defects, residual risk, and Go/No-Go recommendations have sources; absent approval records stay pending. |
| 08 | State and recovery · P1 | Define Run ID, input fingerprint, commit SHA, stage state, checkpoint, idempotency key, resume, and invalidation rules. | Changed inputs or SHA make old checkpoints STALE; side-effect stages are never silently replayed. |
| 09 | Evidence Contract · P0 | Define fact/inference/plan/execution, source, time, version, scope, confidence state, and expiry. | PASS/FAIL/BLOCKED/UNKNOWN validate; static analysis cannot substantiate a real test execution pass. |
| 10 | Workflow Eval · P0 | Add routing, handoff, negative, permission, recovery, injection, and with/without-dependency scenarios; produce machine-readable reports. | Every new workflow has normal, boundary, failure/permission, and regression cases; reports distinguish structure checks from model execution. |
| 11 | Skill lifecycle · P2 | Define Experimental/Stable/Maintenance/Deprecated, overlap review, migration rules, low-frequency/high-risk exception, and read-only residue checks. | Value claims require usage evidence; missing data stays `UNASSESSED`; deprecated items have replacements and migration notes. |
| 12 | Multi-Agent distribution · P2 | Record Codex, Claude Code, and Cursor install/compatibility evidence; provide optional standalone ZIP, previewable uninstall, and old-package residue checks. | Independent zh/en packaging and install previews pass; upgrade, uninstall, and residue checks run; host execution is separately marked. |

## One-pass delivery order

1. **Baseline and contracts:** finish the audit, Router behavior inventory, Workflow/Evidence/Run State schemas, bilingual compatibility matrix, and lifecycle rules.
2. **P0 pilot:** extend `discover-testing` and implement `pr-quality-review`, then connect contract validation, handoff Evals, permission checks, and evidence gates.
3. **P1 workflows:** add `requirement-to-test` and `change-to-regression`, extend the existing `release-testing-workflow`, and standardize checkpoint/recovery rules.
4. **Governance and delivery:** update Skill indexes, lifecycle and compatibility records; run focused Evals, install previews, the full quality gate, and review the Git diff.

## Definition of Done

- Add only distinct orchestration capabilities; preserve existing canonical names, install layout, and specialist boundaries.
- Use TDD for behavior changes: write and observe a failing test first, implement, refactor, then rerun.
- User-facing docs and Skill packages have Chinese and English versions; leaf-package relative resources work after copying the package alone.
- Each new or behaviorally changed Skill has normal, boundary, failure/permission, and regression Evals; record structural validation and actual model runs separately.
- Evidence includes source, time, version, input fingerprint, and execution type; unknown facts remain UNKNOWN/NOT_RUN.
- Schema, contract, bilingual, independence, and quality checks pass; any unrun host validation is reported as unverified.
- Commit or push only on explicit user request; before delivery, verify the target branch, remote SHA, PR state, and worktree.

## Status convention

This document is the execution checklist. Mark an item complete only after its code, Eval/verification evidence, and documentation sync are complete. Listing a command is not proof that it has run.

## Current delivery status (2026-11-03)

All 12 work items have been implemented and checked within this repository's delivery scope: the existing Router and release workflow are enhanced; three thin orchestration Skills are added; standard contracts, evidence and Run State tooling, bilingual Evals, lifecycle governance, and distribution artifacts are in place. The Run State CLI writes stages and checkpoints to files, validates the input fingerprint, commit SHA, and Workflow package fingerprint, refuses resume after changes, and prevents silent stage replay. It does not schedule Skills or perform automatic cross-stage Host execution. Host auto-discovery and prompt execution, including Claude Code and Cursor in-host workflow runs, remain `NOT_RUN`.

Final Codex behavior Evals used skill-up 0.12.0 and Codex CLI 0.166.0. With-Skill suites passed **106/106 cases** (53/53 per locale); the current no-Skill suites passed **38/38** (19 per locale), covering routing, handoff, checkpoint recovery, permission boundaries, and release evidence. These are scenario checks, not a population-level estimate of effectiveness or improvement. Reports preserve raw-output hashes, runner versions, and input fingerprints:

Here, no-Skill means each `evals/without-skill/eval.yaml` explicitly sets `skills: []`, so skill-up does not install the evaluated Skill; the run configuration label alone does not mean a Skill was installed.

| Workflow | Chinese with Skill | English with Skill | Chinese no-Skill | English no-Skill |
| --- | --- | --- | --- | --- |
| `discover-testing` | [22/22](eval-runs/workflow-reliability-v1/runs/discover-testing-zh-20261103-final-v2.json) | [22/22](eval-runs/workflow-reliability-v1/runs/discover-testing-en-20261103-final-v2.json) | [3/3](eval-runs/workflow-reliability-v1/runs/discover-testing-zh-20261103-pr43-no-skill-full.json) | [3/3](eval-runs/workflow-reliability-v1/runs/discover-testing-en-20261103-pr43-no-skill-full.json) |
| `pr-quality-review` | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-final.json) | [4/4](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-pr43-no-skill-full.json) | [4/4](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-pr43-no-skill-full.json) |
| `requirement-to-test` | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-final.json) | [4/4](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-pr43-no-skill-full.json) | [4/4](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-pr43-no-skill-full.json) |
| `change-to-regression` | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-final.json) | [4/4](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-pr43-no-skill-full.json) | [4/4](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-pr43-no-skill-full.json) |
| `release-testing-workflow` | [7/7](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-zh-20261103-final.json) | [7/7](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-en-20261103-final.json) | [4/4](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-zh-20261103-pr43-no-skill-full.json) | [4/4](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-en-20261103-pr43-no-skill-full.json) |

This pass fixed two Eval false negatives: the PR comparison no longer requires a literal heading, and the Router clarification graders now accept plural English `behaviors` and Chinese “用户流程”. Both fixes started with failing regression tests. The final English and Chinese full Router Evals passed **22/22** each; their expanded no-Skill suites passed **3/3** each. The table links only to final runs for the current package version. Other Workflow results are listed above.

### PR #43 review follow-up verification (2026-11-03)

After the review fixes, the three affected Workflows' full bilingual Skill-up Evals were rerun: **48/48 passed** across six runs, each with 8/8 cases. These are follow-up regressions for existing scenarios, not 48 new unique cases; the cases and graders were tightened based on review findings. Each record preserves the run-time commit, Skill package fingerprint, and raw report hash:

| Workflow | Chinese with Skill | English with Skill | Commit at evaluation |
| --- | --- | --- | --- |
| `change-to-regression` | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-pr43-followup.json) | `306a57c0` |
| `pr-quality-review` | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-pr43-followup.json) | `a7b516ab` |
| `requirement-to-test` | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-pr43-followup.json) | `4495dee7` |

Follow-up fixes tightened Change-to-Regression's SHA summary, Skill availability status, and production/data-cleanup permission boundary; corrected the PR stale-checkpoint grader to recognize “重新运行”; and made bilingual Requirement-to-Test comparison language, headings, and traceability requirements explicit. Model responses and rule assertions are recorded separately; grader repairs are not evidence of Skill behavior passing.

The review also found that no-Skill suites selected only one comparison case per Workflow and locale. Both locales now cover Router routing/injection, handoff, recovery, permission boundaries, and release handoff/approval/evidence freshness. The complete no-Skill suites passed **38/38** (**19 per locale**) on commit `12c5b8f1`; the table above links the ten path-sanitized run records.

Final quality gates: Workflow Contract validation covered **14 packages, 28 Workflow files, and 0 errors**; `skill-up validate` passed **348/348**; bilingual documentation checks reported **0 findings**; and the latest full quality script's Python unit suite passed **407/407**. The local-source `skills@1.7.0` compatibility gate discovered **169 Skills** and passed the isolated English `functional-testing` install smoke. Distribution verification passed **60** isolated bilingual installs, **10** same-target upgrades, **10** uninstall previews/applies with zero-residue scans, and exact file checks on **10** standalone ZIPs, with **0 failures**. See the [compatibility verification record](../integrations/agent-compatibility-evidence-2026-11-03.json).

This evidence covers repository contracts, the listed Codex CLI cases, and isolated installer behavior. It does not prove Claude Code or Cursor Host loading/execution, nor does this repository provide a continuously running cross-stage scheduler. Humans retain the final release decision.

These review fixes have been committed and pushed to PR #43's branch; the PR remains open and unmerged. The worktree is clean at delivery.

## Change log

- **2026-10-30 · v1.0.0**: Added bilingual Workflow, Evidence, and Run State contracts; enhanced the Router; added PR quality, requirement-to-test, and change-to-regression orchestration packages; extended the existing release workflow; and added Eval, lifecycle, package-install, and quality-gate records.
- **2026-11-03 · v1.0 closeout**: Completed the bilingual Router behavior Evals, expanded no-Skill routing/handoff/recovery/permission coverage, and clarification-grader regression fixes; rechecked repository gates, CLI compatibility, isolated installs, upgrades/uninstalls, and standalone ZIP evidence. Host execution and automatic scheduling remain `NOT_RUN`.
