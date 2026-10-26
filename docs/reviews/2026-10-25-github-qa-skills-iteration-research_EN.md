<div align="right"><a href="./2026-10-25-github-qa-skills-iteration-research.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# GitHub Landscape and QA Skills Iteration Research

> Research date: 2026-10-25
> Scope: GitHub projects related to Agent Skill catalogs, AI-assisted QA workflows, automated test execution, LLM/Agent evaluation, and QA discovery and distribution.
> Purpose: Identify transferable product and engineering practices and assess feasible, incremental directions. This is neither a market-sizing report nor an independent quality certification of the projects reviewed.

## Summary

The sampled projects broadly follow four product patterns:

1. **Catalogs and distribution:** Organize Skills by task and reduce first-use friction through search, plugins/bundles, and learning resources.
2. **Task workflows:** Break QA work into handoff stages and finish with structured reports, states, and evidence rather than conversation text alone.
3. **Execution adapters:** Use Playwright, CI, SAST, or specialized tools to perform real actions while retaining process details and artifacts.
4. **Behavior evaluation:** Compare behavior changes with versioned datasets, real traces, blind-test fixtures, and CI.

The most useful cross-project lesson is to **deliver inspectable quality artifacts for a few high-frequency tasks, then add execution and regression evidence incrementally**. This makes user value easier to validate than continuing to grow the catalog. The right workflow depends on the target repository's existing capabilities, real user tasks, and execution evidence.

## Method and evidence limits

This review used the GitHub plugin to search repositories, files, and commits, then read selected repositories' READMEs, Skill files, CI documentation, benchmark descriptions, and limitation notes. Searches used default branches; recent commit dates are recorded in UTC as returned by GitHub.

Projects were selected as relevant examples, not as a random sample. Product descriptions and self-reported scores in READMEs are treated as project claims. Except where code or contracts were explicitly reviewed, the projects were not cloned and run, and their metrics were not independently reproduced. Directory counts, Stars, download badges, and one-off Eval results are therefore not proof of effectiveness.

## Comparison with the current repository

This section avoids listing existing capabilities as new directions. Current-state observations come from repository files and dated records; historical run results do not mean the work was rerun for this report.

| Area | Existing foundation | Remaining gap or boundary |
| --- | --- | --- |
| Skill coverage and distribution | The current tree has 165 Skills in each language. The README/index and a fixed `skills@1.7.0` distribution compatibility gate are in place. | As of this research date, the README/index recorded 165 while the evolution roadmap still had an older count of 164; this count discrepancy was corrected on 2026-10-26. Broad discovery/installation is not a real compatibility matrix across all Agents and languages. |
| Routing and workflows | `discover-testing` has five Composition routes; `change-impact-analysis`, `regression-test-selection`, `root-cause-analysis`, `ui-test-playwright`, and `test-reporting` are reusable. | Composition is navigation metadata. The Router selects one primary Skill and at most one optional Skill; it is not a multi-stage automatic call chain or an executor. |
| Executable UI testing | `ui-test-playwright` has a local synthetic checkout fixture covering good, bug, and timeout modes, and requires judging business state rather than page titles. | A fixture's presence does not mean Playwright/runtime execution occurred. The current Pilot contract marks browser/runtime execution as `NOT_RUN`. |
| Skill behavior evaluation | In the 2026-10-03 Codex Pilot, bilingual cases for five core Skills scored 34/34 `PASS`; a second model was sampled only on 5/5 cases. On 2026-10-05, three Chinese benchmarks were extended to three runs per side. This supports limited observations about text behavior and state contracts, not general quality gains or formal ratings. [Pilot](../../evidence/skill-quality/2026-10-03-codex-pilot/README_EN.md) · [Repeated sampling](../../evidence/skill-quality/2026-10-05-codex-benchmark-repeat/README_EN.md) |
| Larger real-model run | A 2026-10-11 summary of 530 added cases recorded 94 `PASS`, 1 `FAIL`, 4 `ERROR`, and 431 `NOT_RUN`; 328 Eval configuration checks and 230 script tests passed at that time. | This is a bounded run against the then-current source, not a whole-repository behavior evaluation. Unrun cases, failures, and errors must remain visible. There is no need to rerun every case blindly just to make the report all green. [Runtime continuation](./2026-10-08-review-runtime-continuation_EN.md) |
| Real business validation and Router observation | Business acceptance checklists, state contracts, benchmarks, and evidence templates exist. | Real-project business acceptance remains `NOT_RUN`. The Router's canonical `skill.selection` observed event is missing, so natural selection and business routing effectiveness remain `BLOCKED`/unproven. [Business acceptance checklist](../../evidence/skill-quality/2026-10-03-codex-pilot/BUSINESS_ACCEPTANCE_EN.md) · [Pilot contract](../../docs/governance/SKILL_EVALUATION_PILOTS_EN.md) |

The next step is therefore not to add execution evaluation from scratch. It is to connect existing test assets and limited execution evidence to a real, acceptance-ready QA task, while addressing only the most important known evidence gaps. Cost and execution permissions are product constraints: the 2026-10-03 Pilot report's invocation cost had not yet been assessed for acceptability, so new model calls should use representative samples and an explicit budget.

## GitHub description, Topics, and README review (2026-10-26)

I checked GitHub's current main branch, repository About metadata and Topics, and the local develop branch's bilingual READMEs. GitHub documentation says Topics classify repositories by purpose and domain, with a limit of 20; the README is a primary entry point for visitors to understand a project and get started. [Repository Topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) · [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

| Area | Evidence at review time | Assessment |
| --- | --- | --- |
| GitHub About description | Before the update, it called the project an “open-source AI-native Quality Engineering skill system” and said it covered reasoning, design, execution, evaluation, and improvement across the SDLC. | **Updated.** The repository uses PolyForm Noncommercial 1.0.0, which restricts licensed purposes to noncommercial use; the OSI definition of Open Source does not allow licenses to restrict fields of endeavor. The About text therefore removed “open-source” and describes a bilingual collection of independently installable Agent Skills. [PolyForm license](https://polyformproject.org/licenses/noncommercial/1.0.0) · [OSI FAQ](https://opensource.org/faq) |
| Topics | The previous set had 10: agent-skills, ai-qa, ai-skills, ai-testing, ai-tools, awesome-list, prompt-engineering, qa, qa-skills, and skills. | **Refined for testing and host relevance.** Removed ai-qa, ai-skills, ai-tools, awesome-list, and skills; retained relevant core tags and added more specific testing, quality engineering, and host tags. [fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) · [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) |
| README content and state | The current GitHub main README already lists 330 bilingual directories, 165 Skills per language, and one-page-`test-strategy`; the counts need no change. The GitHub main and local develop bilingual READMEs both reference social-preview.jpg. | **No full rewrite is needed; the entry point can be tightened.** The bilingual home pages already include quick installation, representative scenarios, a full catalog, license information, and the Skills CLI validation boundary. The main opportunity is to make the first screen explain sooner that this is an installable Skill collection, not a universal execution platform, and to reduce secondary links near the top. Whether the repository Settings page has a separate GitHub Social preview was not checked. |

### Recommended changes

**1. About description (P0, low cost, completed):** Replace claims implying “open-source,” “system,” or “execute” with an accurate description:

> Bilingual Agent Skills for software testing and QA workflows from requirements through release. Independently installable for Codex, Claude Code, Cursor, and compatible coding agents. Licensed under PolyForm Noncommercial 1.0.0.

This copy highlights the deliverable, languages, purpose, host range, and license. Compatibility claims still need to be bounded by the fixed-version Skills CLI gate documented in the README; the description should not imply every platform has received equivalent verification.

**2. Topics (P1, low cost, completed):** Replace broad or repetitive tags with a semantically focused set:

~~~text
agent-skills, ai-testing, software-testing, test-automation,
quality-engineering, quality-assurance, qa-skills, qa,
claude-code, cursor, openai-codex, prompt-engineering
~~~

This set reflects the current product and tags used by comparable repositories. It is not a search-traffic or Stars-growth forecast. The 12 relevant tags do not need to fill GitHub's limit of 20; revisit them using GitHub traffic sources and user search feedback.

**3. README (P1, medium-low cost):** Keep the bilingual files and detailed catalog; do not rewrite the descriptions of all 165 Skills. Tighten the first screen:

- Put quick installation immediately after “what this is / who it is for,” and reduce top-level quick links to installation, task browsing, full catalog, and contribution. Move governance and long integration material into the later documentation map.
- Add a short boundary statement: “This repository provides Agent Skills and reusable QA workflows; it does not provide a universal test runner.” Add the equivalent clarification in Chinese.
- Keep the PolyForm Noncommercial badge and state the noncommercial license near the top so users do not find the restriction only at the end.
- If reducing README length, let the existing docs/catalog/skills-index files carry the detailed tables while the README keeps task entry points and representative Skills. This is an optional information-architecture change; first check its effect on GitHub browsing and site indexing. It need not be bundled with the About/Topics update.
- The social-preview.jpg reference is present on GitHub main. Check the repository Settings' Social preview separately because an embedded README image and the repository share card appear in different places.

**Acceptance:** GitHub About no longer claims OSI-defined open source; the description and README agree on the deliverable; Topics relate to Agent Skills, testing, and actually supported hosts; and both language home pages let new users find installation for an individual Skill, the complete catalog, and the license. Catalog counts should match the current index. Do not use a Stars change as proof that copy changes worked; observe GitHub traffic sources, landing-page clicks, installation-entry clicks, and first-install feedback instead.

**Execution result (2026-10-26):** After user confirmation, the GitHub About description and Topics were updated. GitHub REST API and gh repo view were both used to read back and verify the description and all 12 tags. The README and repository files were not changed by that GitHub metadata operation.

## Observations from adjacent projects

### 1. QA Skills and workflow catalogs

| Project | Observable GitHub implementation | Takeaway | Boundary |
| --- | --- | --- | --- |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Maintains Agents, Instructions, Skills, Hooks, Workflows, and Plugins separately. Its README points to a searchable/filterable site, Learning Hub, machine-readable llms.txt, and plugin installation. A 2026-10-22 commit continued to accept community Skills. | Organize curated paths, examples, and bundles around what users want to accomplish instead of only providing a long list. Machine-readable indexes can also help Agents search. | It is closely integrated with GitHub Copilot plugins and marketplace entry points; this does not mean the same distribution model suits every Agent. README resource volume and entry points do not prove adoption. |
| [anthropics/skills](https://github.com/anthropics/skills) | Provides Skill examples, templates, and a standards-oriented catalog; installation is through the Claude plugin marketplace. The README describes the repository as examples and education, and says users should validate actual behavior themselves. A 2026-10-09 commit included dynamic workflow and quickstart updates. | Complex Skills can include self-contained resources and an actionable quickstart. Distinguishing examples, standards, and runtime results helps avoid overclaiming. | An example catalog is not a production-effectiveness benchmark. Its Claude focus does not establish cross-tool compatibility. |
| [fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) | The README lists 12 Skills and a shared core/ knowledge base, with full installation through skills.sh. examples/README.md compares outputs for the same task with Skills on and off; it describes four paired runs at n=3 per side and a median sample, while noting that the full method and raw data are not distributed. A 2026-10-21 commit adjusted npm, skills.sh, and Git distribution. | Comparing the same task's artifacts before and after installation can be more useful than showing only Skill counts. A few representative cases can show assertion, input handoff, and evidence differences. | Public examples show output shape, but the complete raw evaluation chain is not in the repository. Its shared core/ installation requirement also couples Skills, which may not suit a project focused on independent installation. Historical README numbers were not independently rerun. |
| [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) | Provides a catalog site, CLI, Skill bundles, and an MCP server with tools to search, read metadata/content, install, list categories, and show rankings. A 2026-10-21 commit updated site activity information. | If the existing catalog already supports finding and installing Skills, first add task categories, curated bundles, and visual examples. Consider MCP search/install only if users have clear difficulty discovering Skills inside an Agent. | README quality scores and supported-Agent counts are project claims; this review did not find enough evidence to independently verify the scoring method or behavior on every host. MCP, CLI, and rankings add API, release, and maintenance costs. |

**External references:** [Awesome Copilot README](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/README.md), [Skill catalog](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/docs/README.skills.md), [Anthropic Skills README](https://github.com/anthropics/skills/blob/main/README.md), [FishZjp output comparison](https://github.com/fishzjp/qa-skills/blob/main/examples/README.md), and [QASkills MCP README](https://github.com/PramodDutta/qaskills/blob/6fc32e4adb7449fd5136746efc7f085357fca6c8/packages/mcp/README.md).

### 2. General development workflows

[obra/superpowers](https://github.com/obra/superpowers) organizes brainstorming, design, planning, TDD, incremental implementation, review, and wrap-up into composable Skills, with adapters for multiple coding Agents. Its README focuses on guiding Agents through stages and confirming with the user at key points. The 2026-10-21 v7.0.1 commit continued to adjust workflows and Skill recovery.

**Transferable practice:** Break a QA task into “input review → risk/acceptance → test design or selection → execution → result classification → evidence handoff,” with an artifact and exit condition at each stage. Start with a copyable task recipe instead of a general orchestration engine.

**Boundary:** This is a general software-development methodology, not a QA-specific evaluation. The full process may be too heavy for simple tasks; stage count should depend on task risk. [README](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/README.md) · [v7.0.1 commit](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b).

#### github/spec-kit: gated bugfix workflows and installable bundles

[Spec Kit](https://github.com/github/spec-kit) provides separate entry points for feature work, bug fixing, and idea assessment. Its [bugfix bundle](https://github.com/github/spec-kit/blob/main/docs/reference/bundles.md) combines a bug extension with an assess → human gate → fix → test workflow. Bundles install versioned components; the workflow itself remains a set of explicit steps and gates.

**Transferable practice:** Upgrade routes such as `change-regression` into a few task recipes, with human confirmation before a change or release. A recipe can combine existing Skills and use a common handoff/evidence manifest.

**Boundary:** Spec Kit is a development tool with a CLI, catalog, installation lifecycle, and workflow runtime. This repository should first adopt a lightweight “recipe + self-contained evidence template” layer. Evaluate CLI/bundles only after repeated use demonstrates a need for bundled installation; do not maintain a second package manager or automatic orchestrator. [Workflows documentation](https://github.github.io/spec-kit/reference/workflows.html) · [Bundles documentation](https://github.github.io/spec-kit/reference/bundles.html).

### 3. Focused QA delivery and evidence artifacts

#### openqa-cn/codexqa: a directly relevant QA verification Skill suite

[CodexQA](https://github.com/openqa-cn/codexqa) positions itself around testing and verification after code is written. Its README lists a router and specialized Skills for change impact, defect analysis, test cases, test data, root cause, and browser replay. Observable outputs include local HTML/Markdown/JSON reports and browser execution reports with step screenshots.

Its [inventory-service example](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/examples/inventory-service/README.md) provides a known-good baseline, a changed branch with seven defects and four decoys, an executable answer key, and blind-test instructions. The README reports one Agent run with 7/7 recall and 7/7 precision; it also says this is a project-built fixture and a single-model, single-run result, **not a benchmark**. Recent code changes also require visible page evidence before passing and fix false passes and missing cases: [require visible evidence](https://github.com/openqa-cn/codexqa/commit/7d81ca1d3baea84e8159352699731f01fc492476) · [fix false pass](https://github.com/openqa-cn/codexqa/commit/238b1521b55848b9bfd6528e923293014157d4b5). A recent commit on 2026-10-03 also generated an architecture wiki from a symbol graph.

Some limits are stated in its own docs: the symbol-graph analyzer uses a separately released closed-source CLI outside the repository; repository CI does not install or run that CLI; public host-Agent runs and an independent quality benchmark are absent; graph coverage also depends on the parser and is affected by dynamic calls and symbol collisions. [Code Analyzer limitations](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/skills/codexqa-code-analyzer/KNOWN_LIMITATIONS.md) · [Compatibility and validation matrix](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/docs/SUPPORT_MATRIX.md).

**Transferable practice:** Produce reports that can be reviewed offline; create focused known-good, known-bad, and decoy fixtures; distinguish structural analysis, model judgment, and real execution.

**Boundary:** Do not treat one README score as generalization evidence or infer analyzer effectiveness from a sample report. External closed-source runtimes add licensing, supply-chain, version compatibility, and reproducibility costs.

#### github/awesome-copilot's bug-receipt Skill: a verifiable completion contract

[bug-receipt](https://github.com/github/awesome-copilot/tree/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt) requires a Bug/Incident closeout to include Problem, Baseline, Root cause, Change, Proof, Gaps, and evidence sources. Its [JSON Schema](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt/references/receipt.schema.json) and [Node validator](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt/scripts/validate-receipt.mjs) check state invariants. For example, VERIFIED requires an observed baseline, root-cause evidence, a change, and passed verification; PARTIAL/`BLOCKED` must describe gaps. The upstream author says the Skill was originally published in another MIT project.

**Transferable practice:** Borrow machine-checkable completeness constraints and fields for who supplied evidence and when it was executed, so scripts can validate a workflow report rather than relying only on a model to remember the format.

**Boundary:** This is one Skill's contract, not a workflow orchestrator. If the target repository already has a state model, carry over invariants and field semantics rather than copying state names and creating a parallel vocabulary.

### 4. Automated test execution and repair

[Playwright Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md) defines three roles: Planner explores an application and writes a Markdown test plan; Generator creates Playwright tests from the plan and checks selectors/assertions during generation; Healer runs tests and attempts to repair failing tests. The documentation requires a seed test to initialize the environment and supports Agent loops for Codex, Claude, OpenCode, and others. A recent Playwright commit on 2026-10-25 mainly updated CI documentation.

**Transferable practice:** Keep test plans, generated code, and run results in separate reviewable stages. For existing UI automation, reuse native Playwright tools and fixtures instead of building another browser executor.

**Risk and control:** A Healer might remove a failure by changing the test rather than fixing the product. If repair is enabled, retain the original failure, the revision diff, and the rerun result; have a human check that assertions were not weakened. The documentation describes features and usage but does not provide general defect-detection or self-healing accuracy evidence.

To test whether generated tests catch behavior errors, projects using JavaScript/TypeScript may optionally try [StrykerJS](https://github.com/stryker-mutator/stryker-js). Mutation testing checks whether tests detect code mutations and supports incremental runs based on changes. It is an optional adapter for a particular test stack, not a cross-language quality score or a replacement for acceptance criteria.

### 5. LLM/Agent Eval and CI

| Project | Observable implementation | Takeaway for QA Skills | Cost and boundary |
| --- | --- | --- | --- |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | CLI/library for LLM Eval, model comparison, and red teaming. Official docs include a GitHub Action that compares Prompt changes in a PR and posts results to the PR; CI docs list JSON/HTML/JUnit outputs and failure thresholds. A 2026-10-25 commit changed dependencies and CI. | Let AI feature/Prompt/Agent testing Skills generate or configure promptfoo project files, CI examples, and evidence reports with commit/run IDs. Use the existing engine rather than building another Runner. | Real runs usually require provider credentials and incur cost and model variance; PR comments/shared results also raise data-privacy concerns. CI support in the tool does not prove a Skill's Eval design is correct. |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | README/docs offer pytest-style LLM Eval, datasets, single/multi-turn, end-to-end, and component-level testing. Agent Eval analyzes full traces as well as individual tool calls/steps; docs describe running evals in CI. A 2026-10-23 commit continued CLI/cloud integration work. | Turn real failures into committed, regression-ready datasets and tests. Choose trace-level or component assertions based on failure mode rather than looking only at the final answer. | LLM-as-judge needs calibration and can vary; latency, cost, and handling sensitive trace data also matter. Framework documentation does not show that a target system achieves the same quality. |

**External references:** [Promptfoo README](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/README.md), [Promptfoo GitHub Actions](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/site/docs/integrations/github-action.md), [Promptfoo CI/CD](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/site/docs/integrations/ci-cd.md), [DeepEval README](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/README.md), [DeepEval CI Eval docs](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/docs/content/docs/evaluation-unit-testing-in-ci-cd.mdx), and [DeepEval Agent Eval docs](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/docs/content/guides/guides-ai-agent-evaluation.mdx).

### 6. Broader runtime platforms

[proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) is a CLI/MCP quality engineering toolkit that configures several clients for coding Agents and offers test generation, coverage-gap analysis, flaky-behavior diagnosis, release-quality assessment, and a quality-pattern knowledge base. Its README lists Node.js 22, npm, SQLite, and optional native dependencies; a 2026-10-25 commit continued dependency maintenance.

[test-zeus-ai/testzeus-hercules](https://github.com/test-zeus-ai/testzeus-hercules) provides a browser-focused testing Agent that accepts Gherkin/natural language and uses Playwright and a Python sandbox to execute automation flows.

These projects show how a “Runtime/CLI/MCP + Agent + state/reporting” can form a more direct execution product. They also require installation, permissions, data handling, native dependencies, client adapters, versioning, and operational support. A safer path is to define reviewable workflow artifacts and an optional Runner interface first, and consider a platform only when user tasks demonstrate a need for persistent execution, state, or CI triggers.

## Comparison of feasible iteration directions

Benefit and feasibility ratings below are qualitative judgments based on the sample and common engineering dependencies, not measured commercial returns.

| Direction | Expected benefit | Feasibility | Main work | Acceptance evidence | Main risks |
| --- | --- | --- | --- | --- | --- |
| **A. Task-oriented QA delivery recipe + evidence receipt** | High | High | Select 1–2 high-frequency tasks such as bugfix verification or PR change regression; define inputs, stage handoffs, and exit criteria; make reports both human-readable and machine-readable, and validate state/evidence constraints. | Link baseline, change, acceptance criteria, actual execution, failure classification, and evidence paths. Missing evidence must prevent a complete passing conclusion; examples must be independently reproducible. | Building general orchestration too early, or reporting a guessed root cause as proven fact. |
| **B. Blind-test fixtures and outcome reports** | High | Medium | Reuse the checkout fixture and Codex Pilot; add cross-stage/multi-task known-good, known-bad, decoy, ambiguous/blocked cases without duplicating a large Eval set; record version, Agent, model, task, repetitions, and cost. | Publish runnable scripts and answer keys; report false positives/negatives, execution success, time/cost, and limits; distinguish one-off results from generalizable conclusions. | Fixture leakage or overfitting; uncalibrated semantic judges; mistaking structural gates for effectiveness. |
| **C. First-use task entry points and examples** | Medium-high | High | Organize a small number of “what do I need to do?” entries, Skill recipes, and installation guidance; provide same-task inputs, outputs, and boundaries; reuse the existing catalog site/CLI to validate search. | Track completion rate, time to first useful artifact, common mis-selections, and feedback. Examples must label facts and assumptions. | Adding another MCP/CLI/ranking system and taking on duplicate distribution and maintenance. |
| **D. Thin adapters for existing Eval/CI tools** | Medium-high for AI QA | Medium | Provide optional configuration generation, dataset structure, CI examples, and result interpretation for Promptfoo/DeepEval; standardize run metadata while retaining original tool reports. | The same dataset/config can run in development and CI; results can be compared by commit/run ID; summaries do not hide failures; cost and privacy boundaries are explicit. | Making a specific platform a hard dependency; CI noise/cost from judge variance and API credentials; maintaining a new Runner. |
| **E. Selective executor/host adapters** | Medium-high | Medium-low | Start from one mature tool (usually Playwright); define an execution interface, run states, and report references. Generated tests return to the user's project, and the user decides whether to run or repair them. | Execute the same limited scenario; retain original failures, assertion changes, and reruns; list only host/version combinations actually verified. | Permissions, environment, selector stability, and Agents changing tests in ways that hide product defects. |
| **F. Router-selection events and host observability** | Medium-high for routing validation | Medium-low | Record a minimal canonical `skill.selection` event for one observable host; never infer Skill invocation from the final answer. | Replayable route/primary/optional/`selected_skills` and run metadata; absence of an event remains `BLOCKED`. | The host may not expose invocation events; custom telemetry adds privacy and maintenance costs. |
| **G. Full Agent QE platform** | Potentially high | Low | Installer, MCP server, state storage, executor, retrieval, CI, and cross-Agent adapters. | Real users keep using it and measurable incremental value over Skills/CLI is shown; support and permission/update policies are clear. | High investment for a Skill-only repository and risk of duplicating existing execution tools. Defer until users prove they need persistent execution. |

## Recommended order for this repository

1. **P0: Build one reviewable Bugfix/PR verification recipe.** Start with bugfixes: defect, baseline, fix, and regression make before/after comparisons easy to define. Reuse existing root-cause, change-impact, regression-selection, Playwright, and reporting capabilities. Use a dedicated workflow Skill or recipe to connect stages; do not put a multi-step chain into the Router contract, which selects one primary and one optional Skill at most.
2. **P0: Define a minimal evidence receipt and exit states.** At minimum, link the issue/PR, baseline and target commit, acceptance criteria, selected tests, actual execution state, raw report path, failure category, uncovered risks, and human decision. The bug-receipt schema/validator is a reference; reuse this repository's `PASS`/`FAIL`/`BLOCKED`/`NOT_RUN` model rather than inventing new states.
3. **P1: Add cross-stage red/green validation on current fixtures, then run one authorized real-project pilot.** Existing good/bug/timeout modes cover local assertion sensitivity. Add or reuse baseline defect, fixed version, decoy, and environment-blocked cases. Require good to pass, a known product defect to be `FAIL`, and environment timeout to be `BLOCKED`/`NOT_RUN`; none may be reported as green. A real project needs an agreed target environment, permissions, budget, and acceptance owner; without any of these, keep the result unaccepted.
4. **P1: Triage existing evaluation debt instead of running every unexecuted case.** First review the attribution and handling of one `FAIL` and four `ERROR` cases, then select a small set of `NOT_RUN` representative cases by important Skill/risk. Evaluate natural Router selection only if the host emits a canonical event. Preserve date, source hash, target model/config, cost, and limits in baseline reports; do not present October evidence as current.
5. **P1: Make recipes task-oriented first-use entry points.** Show 3–5 tasks in the README, index, and website. Each should include an input example, installation command, expected artifact, state when not run, and applicability boundary. Measure first completion through feedback or a small pilot before building a ranking or MCP.
6. **P2: Add thin adapters from AI Native QA to external Eval tools.** For one real AI feature, generate runnable Promptfoo or DeepEval configuration; keep datasets and raw traces with the tool, while Skills own test design, interpretation, and limits. Do not promise continuous automation before the target, credentials, and CI budget are clear.
7. **Defer a full Agent QE platform, full host matrix, and custom Eval Engine.** Reconsider only after several pilots demonstrate a need for persistent state, team-level CI scheduling, or host events unavailable from current tools.

External research favors “recipe + receipt + task-first discovery.” Local evidence changes the initial priority from “run more models” to “complete an end-to-end business validation within a finite budget and address the most important `FAIL`/`ERROR`/selection observability gaps.” This ranking is an engineering judgment based on current assets and dependencies, not a quantified commercial-return estimate.

## Practices not to copy directly

- **Do not use catalog size, leaderboard scores, or download badges as proof of quality.** They can show project activity or presentation, not correct behavior on real tasks.
- **Do not define self-healing as “make the test green.”** Retain the original failure and confirm that product-contract assertions were not weakened.
- **Do not rewrite Promptfoo/DeepEval's Eval Engine.** Focus on domain cases, adapters, and evidence interpretation.
- **Do not introduce a full Runtime, database, vector retrieval, and all-host matrix too early.** These are more expensive and need stronger evidence than making one QA deliverable trustworthy.
- **Do not directly depend on a competitor's closed-source or host-specific engine.** Borrow output and workflow patterns without making proprietary runtimes an implicit requirement for cross-tool QA Skills.

## Main sources

- [github/spec-kit](https://github.com/github/spec-kit) · [Workflow docs](https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md) · [Bundle docs](https://github.com/github/spec-kit/blob/main/docs/reference/bundles.md)
- [github/awesome-copilot](https://github.com/github/awesome-copilot) · [Bug Receipt Skill](https://github.com/github/awesome-copilot/tree/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt)
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [microsoft/playwright Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md)
- [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js)
- [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa) · [Blind-eval fixture](https://github.com/openqa-cn/codexqa/tree/main/examples/inventory-service) · [Known limitations](https://github.com/openqa-cn/codexqa/blob/main/skills/codexqa-code-analyzer/KNOWN_LIMITATIONS.md)
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [GitHub Actions](https://github.com/promptfoo/promptfoo/blob/main/site/docs/integrations/github-action.md) · [CI/CD](https://github.com/promptfoo/promptfoo/blob/main/site/docs/integrations/ci-cd.md)
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval) · [CI Eval docs](https://github.com/confident-ai/deepeval/blob/main/docs/content/docs/evaluation-unit-testing-in-ci-cd.mdx)
- [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe)
- [test-zeus-ai/testzeus-hercules](https://github.com/test-zeus-ai/testzeus-hercules)
- [fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) · [Output comparisons](https://github.com/fishzjp/qa-skills/tree/main/examples)
- [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) · [MCP server tools](https://github.com/PramodDutta/qaskills/tree/main/packages/mcp)
