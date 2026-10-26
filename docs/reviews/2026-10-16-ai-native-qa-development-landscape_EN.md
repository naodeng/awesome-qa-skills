<div align="right"><a href="./2026-10-16-ai-native-qa-development-landscape.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# GitHub Project Iteration Directions and AI-Native QA Opportunities

**Research date: 2026-10-16**

**Scope:** Compare prominent AI development workflows, Skill directories, test automation, and LLM Eval projects, then assess possible extensions in light of this repository's existing capabilities.

This report captures a one-time research snapshot as of 2026-10-16; it is not a long-term policy. An English mirror is provided under the current bilingual documentation policy. For later changes, refer to review records with newer dates.

## Executive summary

The project does not currently lack Skill volume or QA lifecycle coverage. The README records 165 Skills per language and 330 directories in total, covering Core QA, Engineering QA, Production Quality, and AI Native QA. The 29 extensions in the evolution roadmap are also marked complete. [README](../../README_EN.md#capability-layers) · [Evolution roadmap](../governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md)

The next major gap is moving existing Skills from “discoverable, installable, and independently usable” to “able to hand work off across a real development task and deliver reviewable execution evidence.” Composition in this repository is navigation metadata, not an enforced execution chain. Routing governance also identifies automatic target execution and validation in a real project as evidence boundaries that remain open. [Evaluation contract](../governance/SKILL_EVALUATION_CONTRACT_EN.md#evidence-states) · [Skill governance roadmap](../governance/SKILL_GOVERNANCE_ROADMAP_EN.md)

The recommended positioning is an **AI Native Quality Engineering workflow system for AI-assisted software delivery**. Its core promise is to start from a requirement, PR/Diff, or AI feature change and produce test decisions, optional execution, an evidence package, and a risk conclusion. The project can extend into AI Native Development, but should add quality checkpoints to the development process rather than become a general-purpose code-generation Skill collection.

## Research method and limits

- The sample includes prominent GitHub projects in engineering workflows, the Skill ecosystem, testing, and LLM Eval, as well as one directly comparable QA Skills project.
- Star counts are approximate snapshots from GitHub pages/API on 2026-10-16, rounded for readability. Stars indicate attention, not quality, usage, or effectiveness.
- The review focused on project READMEs, official documentation, and recent development direction. The projects were not run or independently validated.
- This is a representative sample, not a basis for estimating the size of the overall QA Skills market.

## Project comparison

| Project | Star snapshot | Observable direction | Takeaway for this project |
| --- | ---: | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | ~300k | Organizes development into explicit stages: brainstorming, planning, incremental implementation, TDD, review, and wrap-up. Recent work continues to improve core workflows, cross-tool support, and reliability. | Large Skill projects create value through process guidance as well as catalog size. Borrow stage contracts and deliverables without expanding into a general development assistant. |
| [anthropics/skills](https://github.com/anthropics/skills) | ~181k | Provides official Skill examples, templates, and development materials; the project describes itself as an example and education resource. | Simple entry points and copyable examples help ecosystem adoption. This project's differentiation should remain QA depth, bilingual content, and evidence governance. |
| [github/spec-kit](https://github.com/github/spec-kit) | ~141k | Makes Spec-Driven Development an optional workflow and provides extensions, presets, and composition. Recent work improves evaluation contracts, artifact capture, and Agent command integration. | Outcome-oriented workflow bundles can help teams get started more easily than a longer Skill list alone. |
| [microsoft/playwright](https://github.com/microsoft/playwright) | ~97.8k | Official documentation presents Planner, Generator, and Healer test Agents that explore an application, generate tests, validate selectors and assertions, execute tests, and handle failures. | Keep intermediate artifacts and execution results reviewable. Self-healing must not turn skipped tests or apparent success into a green result. |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | ~40.1k | Community Skills, Agents, instructions, Hooks, and plugins are paired with a searchable site, learning entry points, and installation discovery. Recent commits mainly maintain the community catalog. | Discovery, filtering, and first-use experience are product capabilities of their own. Offer a few curated task paths and demos instead of showing only totals. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | ~25.5k | Uses a brainstorm-plan-build-simplify-review-capture loop so one task can improve the next. Recent work improves multi-model collaboration and workflow reliability. | Retrospectives can become reusable test assets, defect patterns, and Eval cases, provided they retain evidence sources and human review. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | ~26k | Provides Eval, red teaming, model comparison, and CI/CD integration for LLM applications. | Do not rebuild a general-purpose evaluation runner in the Skill repository. Offer optional adapters for configuration generation, test design, and result interpretation. |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | ~18.9k | Provides an LLM Eval framework for Agent traces, tool calls, retrieval, and synthetic data. Its Skill guides users to create repeatable pytest Eval suites and analyze traces. | A Skill can turn one-off analysis into committed, regression-ready quality assets, which has more lasting value than advice alone. |
| [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa) | ~180 | A closer QA Skills comparison: its README describes local-first Router/Worker Skills, execution, evidence collection, and reporting. Recent changes emphasize visible browser evidence and reducing false positives. | This direct comparison is worth watching. Focused execution paths can feel immediately useful. This project can retain broader bilingual coverage and governance while deepening one end-to-end scenario. |
| [naodeng/awesome-qa-skills](https://github.com/naodeng/awesome-qa-skills) | ~260 | A bilingual, cross-tool QA Skill catalog. The README records 165 Skills per language across requirements through production and AI Native QA; governance emphasizes independent installation, Eval, and evidence boundaries. | Catalog breadth and lifecycle coverage are an established foundation. The next step is to connect a small number of existing capabilities into a verifiable task loop and validate their value with real-project evidence. |

Across this sample, high-star projects focus on **development workflows, tool ecosystems, test execution, or model evaluation**. Specialized QA Skills repositories are smaller in this set. That suggests this project should connect clearly to development workflows, but it does not show that demand for QA itself is small.

## Strengths and bottlenecks

### Existing strengths

- Covers requirements, design, testing, release, production, and AI feature validation; maintains Chinese and English versions; and supports independent Skill installation.
- Skill metadata, Eval cases, repository quality gates, and evidence states form a governance foundation.
- Existing capabilities in change impact, regression scope, regression test selection, Playwright, test reporting, release workflows, and AI/LLM/Agent testing can serve as building blocks for vertical workflows. [README capability catalog](../../README_EN.md#complete-skill-catalog) · [Evolution roadmap](../governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md)

### Main bottlenecks

- The capability map and Skill catalog are already substantial; adding similar Skills may have diminishing returns.
- Workflow composition is closer to routing and navigation than a generally executable “input → selection → execution → evidence → conclusion” chain.
- Real target execution, cross-model/tool performance, real-project regression, and user outcomes need separate evidence. They cannot be inferred from structural checks or Eval configuration. [Skill governance roadmap](../governance/SKILL_GOVERNANCE_ROADMAP_EN.md)
- At the time of this report, the repository had a catalog-count discrepancy: the README recorded 165 per language, while the evolution roadmap still recorded 164. The current directory and generator should be checked before updating the roadmap.

The sense of stagnation is therefore more likely a transition from a catalog-oriented project to a workflow product than a need for another list of Skill ideas.

## Four workflow structures

These are not four unrelated new Skills. They are four entry points that reuse one delivery backbone:

~~~text
Input and version confirmation → risk analysis → acceptance criteria → test design/generation → execution → failure triage → evidence package → conclusion and next steps
~~~

Each stage should produce a structured handoff. The next stage needs the requirement or defect, commit, assumptions, and evidence behind a summary. When information is missing, unaffected work can continue, but affected conclusions must be marked **BLOCKED**, **NOT_RUN**, or **INSUFFICIENT_EVIDENCE**; these states must not be treated as passing.

| Workflow entry | Inputs | Stages and reusable Skills | Completion and blocking rules |
| --- | --- | --- | --- |
| **New feature delivery** (new-feature-quality) | Issue/PRD, design/API contract, code PR, target environment, and existing tests | requirements-analysis → quality-risk-analysis / testability-analysis → acceptance-criteria-review → test-strategy / test-case-writing → API/UI/functional testing → test-reporting | Map every critical acceptance criterion to one or more tests and observable evidence. If business rules are unconfirmed, return questions rather than inventing rules. Without an implementation or environment, deliver test preparation only and mark it NOT_RUN. |
| **Bugfix verification** (bugfix-verification, proposed composition route) | Defect, reproduction steps, expected/actual behavior, logs, fix PR, baseline and target commits | Reproduction review → root-cause-analysis (hypotheses only) / change-impact-analysis → acceptance-criteria-review → test-case-writing (capture the reproduction first) → regression-test-selection → relevant test execution → test-reporting | Ideally, the reproduction fails before the fix and passes after it, with affected regression tests passing. If the defect cannot be reproduced on the baseline, do not claim the fix is verified. Distinguish product fixes, reproduction-test problems, environment issues, and failures to reproduce. |
| **AI-generated code verification** (ai-code-verification, proposed composition route) | Development task and acceptance criteria, AI-generated code/test diff, target commit; Agent/model/tool version and execution trace when available | code-review / change-impact-analysis → acceptance-criteria-review → relevant test design and generation → ai-generated-test-review to check whether assertions catch real defects → test execution → result report | First verify that generated implementation meets acceptance criteria, then verify that tests protect that behavior. Coverage or an all-green result alone is insufficient. If tests still pass after a critical behavior is broken, classify the evidence as insufficient or the test as failed. Preserve missing generation metadata as unknown; do not guess. |
| **Release readiness** (release-readiness) | RC/tag, PR/commit list, CI/build, environment, known defects, deployment and rollback plan | release-testing-workflow → regression-test-selection based on changes → focused security/performance/API/AI Eval execution → production-verification when applicable → test-reporting | Deliver a gate view with evidence links, open items, residual risks, and a Go/No-Go recommendation. Mark missing evidence for critical gates as BLOCKED/NOT_RUN. Final release authorization remains with an authorized person; the Skill can only make an evidence-backed recommendation. |

Two scopes are easy to confuse: the existing ai-feature-validation checks AI features in a product; ai-code-verification checks code and tests generated by a coding Agent. The former does not replace the latter. Current Composition includes routes such as new-feature-quality, change-regression, and ai-feature-validation, but routing does not execute tests. Release testing already has a [release-testing-workflow](../../skills/en/testing-workflows/release-testing-workflow/SKILL.md); the need is to connect it to execution and consistent evidence, not rewrite it.

### Failure triage and final evidence

A test failure does not automatically mean a product defect. Classify each failure and retain its original evidence:

- **Product behavior failure:** Reproducibly violates an approved acceptance criterion. Mark **FAIL** and link the case, version, and expected/actual difference.
- **Test problem:** The assertion, data, isolation, or cleanup is faulty. Fix and rerun, but retain the initial failure.
- **Flaky test:** Limit retries and preserve the first and retry results. Do not hide flakiness because one retry passed.
- **Environment/permission/dependency problem:** Without sufficient execution evidence, mark **BLOCKED** or **NOT_RUN**; do not show green.
- **Requirement or acceptance ambiguity:** Mark affected conclusions **BLOCKED**; unaffected tests may continue.

A minimum evidence package can include run_id, scenario, input issue/PR, baseline and target SHA, acceptance-criterion IDs, selected tests and selection rationale, command and environment, raw log/report paths, evidence state for each assertion, failure category, uncovered risks, recommended conclusion, and next owner. Reports must distinguish “test assertions passed” from “release is authorized”; these are different decisions.

**Bugfix example:** A defect says, “Submitting an order twice deducts inventory twice.” First confirm that this is the approved inventory contract and fix a reproducible input. The baseline should fail the reproduction; the fixed version should pass the same case, followed by affected inventory/order regression tests. If the baseline case does not fail, the conclusion is “reproduction not established.” If the fixed-version test does not run because the database service is unavailable, mark it **BLOCKED**. Only when reproduction, fix, and regression evidence are complete can the report say, “The version tested passed these assertions.”

## Recommended expansion path

### P0: Build one flagship QA delivery loop

Start with existing assets and build **PR/Diff → change-risk analysis → regression scope and test recommendations → optional test execution → evidence package and conclusion**. This is a natural meeting point for QA and development, and reuses change-impact-analysis, regression-scope-analysis, regression-test-selection, ui-test-playwright, and test-reporting.

The workflow should deliver a machine-readable, reviewable handoff/evidence manifest containing items such as workflow_id, code version or PR, stage, selected Skills/tests, execution state, evidence paths, uncovered risks, open questions, next steps, and exit conditions. Without execution evidence, use NOT_RUN, BLOCKED, or another explicit state; do not claim “regression passed.”

The first version does not need a general orchestration platform. Start with a copyable workflow definition and optional Runner/CI adapter, then complete the loop in a sample repository. Include at least known-good, known-bad, and known-ambiguous end-to-end cases to check normal evidence, real defects, and insufficient evidence for false greens.

### P1: Move AI Native QA from test design to continuous Eval

Build regression-ready Eval assets for real AI features: dataset versions, Prompt/model/Agent versions, tool traces, metrics and assertions, human review items, red-team cases, CI quality gates, and version comparisons. Offer optional configuration or workflow adapters for mature runners such as promptfoo and DeepEval. Skills should design inputs, state evidence requirements, interpret results, and identify risks; they should not replace a specialized Runner.

### P2: Extend quality checkpoints into AI Native Development

For developers, add or strengthen capabilities for requirement and Spec testability, coding-Agent acceptance criteria, test impact of code changes, review of generated tests, post-fix regression, and PR/release evidence summaries. Each capability should answer “How do we show the change meets expectations?” rather than generalizing into “write more code for the user.”

### P3: Improve first use and distribution

Offer 3–5 curated task paths, such as “review a PR,” “ship an AI feature,” “investigate a flaky test,” and “prepare a release.” Each path should include a real sample repository, installation instructions, expected artifacts, and failure handling. Organize Skill bundles and the website by user task to reduce the effort of choosing among 330 directories.

## How to measure whether an iteration works

Measure real tasks and version regressions:

1. Defect detection, false-positive, and false-negative rates, plus whether the workflow correctly blocks when evidence is insufficient.
2. Time and human effort from a change input to a credible quality judgment.
3. Completeness and reproducibility of execution evidence, and portability across Agents/Runners.
4. Behavior changes before and after Skill updates, and whether real users can complete a first task.

Stars, directory counts, static checks, one Eval score, or one local run cannot by themselves establish real quality gains. Report each result with evidence appropriate to its type. [Skill Eval state contract](../governance/SKILL_EVALUATION_CONTRACT_EN.md#evidence-states)

## Near-term decisions

1. Pause growth in general-purpose Skills and choose **Bugfix verification** as the smallest vertical slice. Defect input, baseline reproduction, post-fix verification, and regression evidence are easier to review; expand to arbitrary PR/Diff change regression once stable.
2. Define workflow inputs, handoff data, evidence package, and exit conditions before deciding whether to build a Runner or CI integration.
3. Keep AI Native Development within quality assurance during development; do not expand into a general coding Agent or a large multi-Agent orchestration platform.
4. Validate the workflow with three real-project cases, then use failures and user feedback to decide the next investment.

## Main sources

- [obra/superpowers](https://github.com/obra/superpowers)
- [anthropics/skills](https://github.com/anthropics/skills)
- [github/spec-kit](https://github.com/github/spec-kit)
- [Playwright Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md)
- [github/awesome-copilot](https://github.com/github/awesome-copilot)
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [promptfoo](https://github.com/promptfoo/promptfoo)
- [DeepEval Skill](https://github.com/confident-ai/deepeval/blob/main/skills/deepeval/SKILL.md)
- [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa)
