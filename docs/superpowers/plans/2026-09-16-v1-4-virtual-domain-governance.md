# v1.4 Virtual Domain Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 v1.4 的首张治理卡“16 个虚拟 Domain 分类”落地为可复现、可校验、双语可读的 D01–D16 分类契约，并同步现有 162 个逻辑 Skill 对的 Matrix 与治理清单。

**Architecture:** `docs/governance/virtual-domains.yaml` 是 16 个 Domain、当前目录分组默认值和必要 slug 覆盖的单一事实源。`scripts/virtual_domains.py` 负责加载、分类和渲染标签；Inventory 与 Matrix 复用同一分类器，避免两套 Domain 逻辑漂移。现有物理 Skill 目录不迁移、不重命名、不新增。

**Tech Stack:** JSON-compatible YAML、Python 3 标准库、Markdown、`unittest`、现有 `check_skills_quality.sh`。

**Spec:** `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`，以及 v1.4 当前 P0 Project 卡 `v1.0｜治理｜16 个虚拟 Domain 分类`。

## Global Constraints

- Domain ID 必须固定为 `D01`–`D16`；每个当前 Skill 只能有一个主要 Domain。
- 分类只用于导航和治理，不表示安装依赖、执行顺序、语义等价或运行质量。
- 以当前 162 个逻辑 Skill 对为基线；新增、删除或重命名后，缺失映射必须让校验失败。
- 保留 `NOT_SCORED`、`NOT_RUN`、`UNASSESSED` 等证据边界；不执行 Prompt、模型或外部测试目标。
- 同步中文和英文治理文档及生成视图；不修改无关 Skill 内容。

---

### Task 1: 建立 D01–D16 分类源和共享分类器

**Files:**
- Create: `docs/governance/virtual-domains.yaml`
- Create: `scripts/virtual_domains.py`
- Create: `scripts/tests/test_virtual_domains.py`

**Interfaces:**
- `load_catalog(path: Path) -> VirtualDomainCatalog`
- `VirtualDomainCatalog.domain_ids() -> tuple[str, ...]`
- `VirtualDomainCatalog.label(domain_id: str, locale: str) -> str`
- `VirtualDomainCatalog.classify(section: str, slug: str, catalog_heading: str | None) -> str`

- [x] **Step 1: Record the exact taxonomy.** Add each of these IDs once, with Chinese and English labels: `D01 Requirement Quality`, `D02 Engineering Quality`, `D03 Test Analysis & Strategy`, `D04 Test Design`, `D05 Functional & Exploratory Testing`, `D06 API & Integration Quality`, `D07 UI & E2E Quality`, `D08 Automation Engineering`, `D09 Performance Quality`, `D10 Security Quality`, `D11 Reliability & Resilience`, `D12 Release & Production Quality`, `D13 Observability & Incident Quality`, `D14 Quality Engineering & Productivity`, `D15 AI for QA`, and `D16 AI / LLM / Agent Quality`.
- [x] **Step 2: Add deterministic defaults and overrides.** Map workflow packages to `D03`, Skill Engineering packages to `D14`, map catalog headings to their primary Domain, and explicitly override mixed groups such as API (`D06`), UI/E2E (`D07`), security (`D10`), reliability (`D11`), AI for QA (`D15`), and AI/LLM/Agent quality (`D16`).
- [x] **Step 3: Write failing tests before implementation.** The tests reject duplicate/missing IDs, unknown IDs, an unmapped current slug, and a catalog assignment that is not one of `D01`–`D16`; they also assert that all 16 IDs are used by the current repository mapping.
- [x] **Step 4: Implement the standard-library loader and classifier.** Parse the JSON-compatible YAML, validate the exact ID set, apply slug overrides before heading defaults, then section defaults, and raise a clear `ValueError` when no mapping exists.
- [x] **Step 5: Run the focused tests.**

```bash
python3 -m unittest scripts.tests.test_virtual_domains -v
```

Expected: all taxonomy and mapping contract tests pass.

### Task 2: Apply the taxonomy to registry and generated views

**Files:**
- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `scripts/generate_skill_governance_inventory.py`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`
- Modify: `scripts/tests/test_generate_skill_governance_inventory.py`
- Regenerate: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`
- Regenerate: `docs/generated/skill-governance-inventory.md`, `docs/generated/skill-governance-inventory_EN.md`

**Interfaces:** Matrix validation accepts only a known Domain ID or an explicit `UNASSESSED` value for isolated incomplete fixtures; repository validation requires every current registry record to use `D01`–`D16`. Both renderers resolve the same ID through `VirtualDomainCatalog.label()`.

- [x] **Step 1: Add regression assertions.** Verify the repository registry has 162 unique Skill records, exactly 16 used Domain IDs, no unknown/unmapped IDs, and matching zh/en rendered labels.
- [x] **Step 2: Replace each registry record’s current high-level Domain with the classifier’s stable ID.** Keep all other governance fields unchanged, including status, priority, score, Eval state, and evidence paths.
- [x] **Step 3: Update both generators.** Load `virtual-domains.yaml`; the inventory must stop deriving only four high-level layers, and the Matrix must render `Dxx` plus the locale-specific label while retaining the source-governance boundary text.
- [x] **Step 4: Regenerate and check freshness.**

```bash
python3 scripts/generate_skill_governance_inventory.py
python3 scripts/generate_skill_governance_matrix.py
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
```

Expected: both `--check` commands report up-to-date and both generated language pairs contain the same 162 slugs and 16 Domain IDs.

### Task 3: Synchronize bilingual governance documentation

**Files:**
- Modify: `docs/governance/SKILL_GOVERNANCE_V1.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_V1_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [x] **Step 1: Document the 16-Domain contract and link the source manifest.** State that IDs are navigation classifications, not execution order or quality evidence.
- [x] **Step 2: Correct stale inventory counts from 79 to the current 162 logical Skill records where the v1.0 baseline describes the current tree.** Preserve historical 79-pair context only where it is explicitly identified as historical.
- [x] **Step 3: Add the exact mapping/reproduction commands and note that semantic/runtime/model evidence remains unassessed.** Keep the Chinese and English structures equivalent.
- [x] **Step 4: Run the bilingual documentation check.**

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
git diff --check
```

Expected: zero bilingual findings and zero whitespace errors.

### Task 4: Verify the first v1.4 card and update Project state

**Files:**
- External state: Project #4 card `v1.0｜治理｜16 个虚拟 Domain 分类`.
- Read-only reference: Project #4 Status field `PVTSSF_lAHOAHP1as4BjBhVzhh3bSA`, `Done` option `98236657`.

- [x] **Step 1: Run the focused tests, the full quality gate, generated-view checks, and `git status --short`.**

```bash
python3 -m unittest scripts.tests.test_virtual_domains scripts.tests.test_generate_skill_governance_inventory scripts.tests.test_generate_skill_governance_matrix -v
bash scripts/check_skills_quality.sh
python3 scripts/check_docs_bilingual.py --repo-root .
git diff --check
git status --short
```

- [x] **Step 2: Confirm the implementation is limited to the taxonomy, governance generators, generated views, registry, and bilingual governance docs; do not claim runtime quality or release completion.**
- [x] **Step 3: After all checks pass, move only this completed card to `Done`; leave the remaining v1.4 cards in `In Progress`.**
- [x] **Step 4: Re-read Project #4 and record the exact card status and repository verification result in the handoff.**

## Plan self-review

- Task 1 defines the exact 16-domain source and makes unmapped additions fail early.
- Task 2 makes Inventory and Matrix consume one classifier and updates all current records without touching physical Skill packages.
- Task 3 fixes bilingual governance context and stale current-tree counts.
- Task 4 gates the card transition on local evidence and preserves the remaining v1.4 execution scope.
