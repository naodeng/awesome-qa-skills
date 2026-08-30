<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-08-29-four-stage-qa-skills-evolution_EN.md">🇬🇧 English</a></div>

# Four-Stage QA Skills Evolution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reframe the repository around Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills without changing any existing Skill directory.

**Architecture:** Keep the physical layout as the installation and compatibility contract. Add a logical capability map to the public documentation and make `discover-testing` route by lifecycle capability before choosing an existing concrete Skill. Publish a bilingual roadmap that records the 29 future logical Skills as scoped, independently installable additions.

**Tech Stack:** Markdown, YAML metadata already present in Skill directories, Bash/Python repository validation scripts.

**Spec:** `docs/superpowers/specs/2026-08-29-four-stage-qa-skills-evolution-design.md`

## Global Constraints

- Do not move, rename, or delete any current directory under `skills/`.
- Keep Chinese and English documentation structurally aligned; Chinese is in `README.md` and English in `README_EN.md`.
- Use the verified count: 49 Skills per language (10 workflow + 36 testing-type + 3 skill-engineering), 98 bilingual directories.
- Preserve `skill-engineering` as a horizontal governance layer, not a fifth capability stage.
- Keep `ai-assisted-testing` explicitly defined as AI for QA; AI Native QA covers Testing for AI.
- Add no future Skill directory in this documentation/navigation change.
- Use `/Users/nao.deng/awsomeCode/awesome-qa-prompt` only as a content-quality and topic-coverage reference; never copy its Prompt Baseline directory model into `skills/`.
- For each future Skill, map the canonical Skill name to its closest Prompt Baseline before authoring; adapt input audit, no-fabrication, degradation, evidence and Human Task rules into the existing Skill package contract.
- Preserve unrelated working-tree changes and do not commit or push unless the user explicitly asks.

---

## File Structure

| File | Responsibility |
| --- | --- |
| `docs/QA_SKILLS_EVOLUTION_ROADMAP.md` | Chinese contributor-facing roadmap, 29-Skill backlog, delivery gates and anti-overlap rules |
| `docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md` | English equivalent of the roadmap |
| `README.md` / `README_EN.md` | Main repository positioning, accurate counts and capability-first catalog navigation |
| `skills-index.md` | Complete inventory with a logical-stage mapping and physical paths |
| `skills/zh/README.md` / `skills/en/README.md` | Language-local capability maps that retain direct install paths |
| `skills/DIRECTORY_GUIDE.md` | Explicit contract separating stable physical directory taxonomy from logical capability stages |
| `skills/{zh,en}/testing-workflows/discover-testing/{SKILL.md,prompts/discover-testing.md,reference.md}` | Bilingual lifecycle-first routing contract and routing map |
| `docs/QA_SKILLS_EVOLUTION_ROADMAP*.md` | Records the future-Skill to Prompt Baseline mapping; it never creates a runtime dependency on the other repository |

## Task 0: Establish the cross-repository reference map

**Files:**
- Create: `docs/QA_SKILLS_EVOLUTION_ROADMAP.md`
- Create: `docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md`
- Read-only source: `/Users/nao.deng/awsomeCode/awesome-qa-prompt/PROMPT_AUTHORING_STANDARD.md`
- Read-only source: `/Users/nao.deng/awsomeCode/awesome-qa-prompt/testing-types/{zh,en}/`

**Interfaces:**
- Consumes: the 29 accepted canonical Skill identifiers and Prompt Baseline modules.
- Produces: a per-Skill reference mapping used by every later Skill-authoring iteration; it does not create a cross-repository link or runtime dependency.

- [ ] **Step 1: Inventory exact and nearest Prompt Baseline equivalents.**

Create a `Reference baseline` column for every planned Skill. At minimum record these known mappings:

```text
acceptance-criteria-review → acceptance-criteria-reviewer
requirement-gap-analysis → requirement-gap-analyzer
api-contract-testing → api-contract-analysis
production-verification → production-verification-generation / production-verification-review
ai-feature-testing → ai-feature-test-design
llm-evaluation-design → ai-evaluation-design
ai-agent-testing → ai-agent-test-design
agent-tool-testing → agent-tool-call-test-design
prompt-injection-testing → prompt-injection-test-design
```

For exact-name modules such as `change-impact-analysis`, `flaky-test-analysis`, `root-cause-analysis`, `log-analysis`, `performance-result-analysis`, `capacity-planning-analysis`, `production-incident-analysis`, `distributed-trace-analysis` and `metrics-anomaly-analysis`, record the exact module name.

- [ ] **Step 2: Record adaptation rules, not copied structures.**

For each reference mapping, record the input audit, anti-fabrication rule, missing-input degradation path, evidence/Human Task boundary and required structured output to adapt. Explicitly prohibit copying `Standard-version/`, framework-variant directories and cross-repository relative links; the target remains a standalone `SKILL.md` + `prompts/` + metadata + evals package.

- [ ] **Step 3: Verify mapping completeness.**

Run:

```bash
rg -n '^\\| `?[a-z0-9-]+`? \\|' docs/QA_SKILLS_EVOLUTION_ROADMAP.md | wc -l
rg -n 'Prompt Baseline|输入审计|禁止编造|降级|Human Task' \
  docs/QA_SKILLS_EVOLUTION_ROADMAP.md docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md
```

Expected: the roadmap includes 29 planned-Skill mapping rows and both language versions state the five adaptation boundaries.

## Task 1: Complete the bilingual roadmap and backlog

**Files:**
- Modify: `docs/QA_SKILLS_EVOLUTION_ROADMAP.md`
- Modify: `docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md`

**Interfaces:**
- Consumes: The accepted stage and backlog definitions in the spec.
- Produces: The canonical public source for future-Skill scope; root README links to it.

- [ ] **Step 1: Add the Chinese roadmap with the four-stage map and directory-stability rule.**

Include this lifecycle line verbatim:

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

State that this is a logical classification only and that all installation paths remain under `skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}`.

- [ ] **Step 2: Add the six-iteration Chinese backlog table and reference column.**

Use these exact new-Skill groups and totals:

```text
Iteration 1 (4): acceptance-criteria-review, requirement-gap-analysis,
quality-risk-analysis, testability-analysis

Iteration 2 (4): change-impact-analysis, pr-test-impact-analysis,
regression-scope-analysis, regression-test-selection

Iteration 3 (5): test-data-generation, api-contract-testing,
flaky-test-analysis, root-cause-analysis, log-analysis

Iteration 4 (5): performance-workload-modeling, performance-result-analysis,
performance-bottleneck-analysis, performance-regression-analysis,
capacity-planning-analysis

Iteration 5 (4): production-verification, production-incident-analysis,
distributed-trace-analysis, metrics-anomaly-analysis

Iteration 6 (7): ai-feature-testing, llm-testing, llm-evaluation-design,
prompt-testing, ai-agent-testing, agent-tool-testing, prompt-injection-testing
```

For each iteration, state its capability stage, outcome, priority, existing-Skill relationship, Prompt Baseline reference and acceptance gate. State the final result as 29 logical Skills / 58 bilingual directories, raising the inventory from 98 to 156 directories only after all six iterations complete.

- [ ] **Step 3: Record deliberate non-additions and their owners.**

Add a compact table with:

```text
exploratory-testing → manual-testing mode
release-readiness-assessment → release-testing-workflow mode
prompt-regression-testing → prompt-testing mode
```

Explain that this prevents duplicate routing targets and duplicate installable packages.

- [ ] **Step 4: Add the English roadmap as a semantic counterpart.**

Translate headings, stage descriptions, all 29 canonical identifiers, the non-addition table, and the Definition of Done. Do not translate Skill directory identifiers. Ensure its iteration totals are 4 + 4 + 5 + 5 + 4 + 7 = 29.

- [ ] **Step 5: Validate roadmap parity and identifiers.**

Run:

```bash
rg -n 'acceptance-criteria-review|prompt-injection-testing|29|58|156' \
  docs/QA_SKILLS_EVOLUTION_ROADMAP.md docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md
```

Expected: both files contain all sampled identifiers and the 29/58/156 totals.

## Task 2: Update the root bilingual repository narrative

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`

**Interfaces:**
- Consumes: roadmap URLs and verified repository totals from Task 1.
- Produces: primary landing-page navigation into the four-stage model and roadmap.

- [ ] **Step 1: Correct all counts and badges.**

Replace every obsolete “92”, “46”, or “10 workflows + 36 testing types” total statement with text that includes all categories:

```text
49 Skills per language: 10 workflows + 36 testing types + 3 skill-engineering.
98 bilingual Skill directories in total.
```

The badges may show 98 Skills, 10 Workflows, 36 Testing Types, and 3 Skill Engineering items separately; do not imply the last category is absent from the total.

- [ ] **Step 2: Add a capability-evolution section before the detailed catalog.**

Write one compact table per language with stage, user problem, and representative existing assets. Include the following distinctions:

```text
Core QA Skills: foundational analysis, design, execution and reporting.
Engineering QA Skills: shift-left, change intelligence, diagnostic and performance decisions.
Production Quality Skills: release, production verification and observability evidence.
AI Native QA Skills: testing AI systems; distinct from AI-assisted-testing (AI for QA).
```

Link the final stage’s future work to the matching language section of the roadmap; do not link from one Skill package to another Skill package.

- [ ] **Step 3: Reframe the existing catalog without hiding implementation navigation.**

Keep current workflow/type/tool/Plus tables, but precede them with the capability map and state that these are physical package categories. Add a short `skill-engineering` entry instead of leaving the three existing packages invisible.

- [ ] **Step 4: Verify bilingual count and stage parity.**

Run:

```bash
rg -n '98|49|Core QA Skills|Engineering QA Skills|Production Quality Skills|AI Native QA Skills|skill-engineering' README.md README_EN.md
```

Expected: both README files expose all four stages, `skill-engineering`, and the verified totals.

## Task 3: Make indexes capability-first while retaining direct package paths

**Files:**
- Modify: `skills-index.md`
- Modify: `skills/zh/README.md`
- Modify: `skills/en/README.md`

**Interfaces:**
- Consumes: stage definitions and current 49-per-language inventory.
- Produces: index pages that answer both “what quality outcome?” and “what directory do I install?”.

- [ ] **Step 1: Correct the top-level index inventory.**

Change the opening inventory summary to list 10 workflow + 36 testing-type + 3 skill-engineering packages per language. Add both Chinese and English links for the three Skill Engineering packages.

- [ ] **Step 2: Add a logical capability map to `skills-index.md`.**

Before the physical inventories, create four sections mapping existing Skills to stages. Keep every entry as its actual Markdown path, for example:

```markdown
- Core QA Skills: [`functional-testing`](skills/zh/testing-types/functional-testing/)
- Engineering QA Skills: [`code-review`](skills/zh/testing-types/code-review/)
- Production Quality Skills: [`release-testing-workflow`](skills/zh/testing-workflows/release-testing-workflow/)
- AI Native QA Skills: roadmap planned; [`ai-assisted-testing`](skills/zh/testing-types/ai-assisted-testing/) is AI for QA, not this stage's testing-for-AI package.
```

Do not list planned packages as existing install paths.

- [ ] **Step 3: Apply the same map to each language-local README.**

Keep language-local paths only. In both files retain the `testing-workflows`, `testing-types`, and tool-specific lists after the map so users can browse by package family.

- [ ] **Step 4: Verify exact current-package coverage.**

Run:

```bash
for lang in zh en; do
  find "skills/$lang" -name SKILL.md -type f | wc -l
done
rg -n 'skill-engineering|Core QA Skills|Engineering QA Skills|Production Quality Skills|AI Native QA Skills' \
  skills-index.md skills/zh/README.md skills/en/README.md
```

Expected: the counts are `49` and `49`; every index includes governance and all capability-stage labels (localized wording is permitted in the Chinese README).

## Task 4: Document the stable-directory contract

**Files:**
- Modify: `skills/DIRECTORY_GUIDE.md`

**Interfaces:**
- Consumes: physical vs logical taxonomy decision.
- Produces: contributor rule preventing future capability-stage directories or accidental relocations.

- [ ] **Step 1: Add a “physical layout versus logical capability” section.**

State that `testing-types`, `testing-workflows`, and `skill-engineering` remain the only package-family directories. State that the four stages are documentation and routing classifications, and must not be encoded as a new directory prefix.

- [ ] **Step 2: Add contribution placement rules for all future roadmap Skills.**

Specify the placement decisions:

```text
Shift Left, Change Intelligence, Execution Intelligence, Performance, Production Quality and AI Native QA deliverables normally live in testing-types.
Cross-stage coordination and calendar/gate orchestration live in testing-workflows.
Skill authoring and repository governance live in skill-engineering.
```

Require authors to first check whether a proposed item is an existing Skill mode before creating a new directory.

- [ ] **Step 3: Verify no new capability directories were created.**

Run:

```bash
find skills/zh skills/en -mindepth 1 -maxdepth 1 -type d -print | sort
```

Expected: only `testing-types`, `testing-workflows`, and `skill-engineering` beneath each language root.

## Task 5: Upgrade bilingual `discover-testing` routing

**Files:**
- Modify: `skills/zh/testing-workflows/discover-testing/SKILL.md`
- Modify: `skills/zh/testing-workflows/discover-testing/prompts/discover-testing.md`
- Modify: `skills/zh/testing-workflows/discover-testing/reference.md`
- Modify: `skills/en/testing-workflows/discover-testing/SKILL.md`
- Modify: `skills/en/testing-workflows/discover-testing/prompts/discover-testing.md`
- Modify: `skills/en/testing-workflows/discover-testing/reference.md`

**Interfaces:**
- Consumes: current user request, lifecycle stage and package catalog.
- Produces: one primary existing Skill, at most one complementary Skill, and a reason that names the relevant stage.

- [ ] **Step 1: Amend both `SKILL.md` files with capability-first routing.**

Add the routing order: capability stage → existing primary Skill → optional workflow/tool/Plus specialization. Retain the existing “one primary, at most one complement” constraint. Explicitly say that future roadmap packages are not recommendable until their directories exist.

- [ ] **Step 2: Amend both main prompts with stage decisions and AI terminology.**

Add a first decision table:

```text
Foundational test design/execution/reporting → Core QA Skills
Requirements quality, code change, diagnosis or performance decision → Engineering QA Skills
Release/production evidence or incident follow-up → Production Quality Skills
Testing an LLM, prompt, agent or AI safety boundary → AI Native QA Skills
Using AI to help a conventional QA task → ai-assisted-testing (AI for QA)
```

For the last three rows that have no installed future package yet, return the existing nearest Skill plus an explicit “roadmap capability not yet installed” note; never invent a directory name as a primary recommendation.

- [ ] **Step 3: Replace the reference maps with a bilingual lifecycle map.**

Keep current actual Skill identifiers, add the four-stage classification, include `skill-engineering` as governance-only, and state the three non-additions:

```text
manual-testing owns exploratory-testing mode
release-testing-workflow owns release-readiness-assessment mode
prompt-testing will own prompt-regression-testing mode after it exists
```

- [ ] **Step 4: Add routing regression examples to the existing eval suites.**

Modify the existing `evals/cases/*.yaml` files for both language versions, adding concrete requests and expected primary-Skill behavior:

```text
“Review acceptance criteria for missing rules” → requirements-analysis today; identify Engineering QA / Shift Left.
“Need a go/no-go decision from release evidence” → release-testing-workflow; identify Production Quality.
“Use AI to draft API test data” → ai-assisted-testing; identify AI for QA, not AI Native QA.
“Evaluate an LLM’s hallucination and refusal behavior” → no nonexistent Skill; state AI Native QA is roadmap work and request/route to the nearest current capability.
```

- [ ] **Step 5: Validate route content and bilingual package integrity.**

Run:

```bash
rg -n 'Core QA Skills|Engineering QA Skills|Production Quality Skills|AI Native QA Skills|AI for QA|Testing for AI' \
  skills/{zh,en}/testing-workflows/discover-testing/{SKILL.md,prompts/discover-testing.md,reference.md}
bash scripts/check_skills_quality.sh
```

Expected: all route files include the appropriate terms and the repository quality gate passes.

## Task 6: Review the change set and validate navigation claims

**Files:**
- Verify: all files in Tasks 1–5

**Interfaces:**
- Consumes: completed documentation and routing changes.
- Produces: evidence that counts, terminology, language alignment and directory stability hold together.

- [ ] **Step 1: Scan for obsolete totals and unsupported future-package links.**

Run:

```bash
rg -n '\b92\b|10 个工作流 \+ 36 个测试类型|10 workflows \+ 36 testing types' \
  README.md README_EN.md skills-index.md skills/zh/README.md skills/en/README.md
rg -n '\]\(([^)]*acceptance-criteria-review|[^)]*llm-testing|[^)]*prompt-testing)' \
  README.md README_EN.md skills-index.md skills/zh/README.md skills/en/README.md \
  docs/QA_SKILLS_EVOLUTION_ROADMAP*.md
```

Expected: no obsolete total; no Markdown link points to a planned Skill directory.

- [ ] **Step 2: Check bilingual file pairs and formatting.**

Run:

```bash
git diff --check
git diff -- README.md README_EN.md skills-index.md skills/zh/README.md skills/en/README.md \
  skills/DIRECTORY_GUIDE.md skills/zh/testing-workflows/discover-testing \
  skills/en/testing-workflows/discover-testing docs/QA_SKILLS_EVOLUTION_ROADMAP.md \
  docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md
```

Expected: no whitespace errors; the diff contains only the planned documentation, routing and eval updates plus the approved planning artifacts.

- [ ] **Step 3: Report verification with explicit limits.**

Report the final current inventory as 49 per language / 98 total, that no directory moved, that no future Skill package was created, and that all 29 additions remain roadmap items. Include the exact quality-gate outcome and any pre-existing unrelated working-tree changes that were left untouched.
