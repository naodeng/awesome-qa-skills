# Phase 0 Skill Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce validated bilingual governance records for all 79 logical Skill pairs without turning static evidence into runtime-quality claims.

**Architecture:** `docs/governance/skill-governance-registry.yaml` is the single source of truth. `scripts/generate_skill_governance_matrix.py` validates it against physical Skill directories and renders both Matrix and Matching Register language pairs. `generate_skill_inventory.py` remains a physical-only snapshot.

**Tech Stack:** Python 3 standard library, YAML, Markdown, Bash, `unittest`.

**Spec:** `docs/superpowers/specs/2026-09-13-phase-0-skill-governance-design.md`

## Global Constraints

- Cover exactly 79 logical bilingual pairs; do not create, rename, or delete `skills/` directories.
- Preserve the v1.0 inventory generator and its source-only boundary.
- Score states: `NOT_SCORED`, `PARTIALLY_SCORED`, `SCORED`. Eval execution defaults to `NOT_RUN`.
- Candidate conclusions: `EXISTING`, `MATCH`, `ENHANCE`, `MERGE`, `NEW`; all require six evidence fields: name, purpose, inputs, outputs, decision logic, Workflow role.
- Keep Chinese-first generated documents, English mirrors, and reciprocal links.

---

### Task 1: Add a testable registry contract

**Files:**
- Create: `scripts/generate_skill_governance_matrix.py`
- Create: `scripts/tests/test_generate_skill_governance_matrix.py`
- Create: `docs/governance/skill-governance-registry.yaml`

**Interfaces:** `discover_physical_skills(root: Path) -> set[str]`; `load_registry(path: Path) -> GovernanceRegistry`; `validate_registry(registry, physical) -> list[str]`; `validate_candidate(candidate) -> list[str]`.

- [ ] **Step 1: Write failing tests for missing/extra Skills, invalid enums, unpaired paths, incomplete `NEW` boundaries, and score evidence.**

```python
def test_rejects_new_candidate_without_scope_and_non_goals(self):
    candidate = {"slug": "new-capability", "conclusion": "NEW", "evidence": SIX_MATCH_FIELDS}
    self.assertEqual(matrix.validate_candidate(candidate), ["scope", "non_goals"])

def test_rejects_score_without_nine_dimensions_and_evidence(self):
    skill = {"slug": "sample", **REQUIRED_SKILL, "quality_score": {"state": "SCORED", "dimensions": {}}}
    self.assertIn("nine dimensions", matrix.validate_skill(skill))
```

- [ ] **Step 2: Run `python3 -m unittest scripts.tests.test_generate_skill_governance_matrix -v`; expect `ModuleNotFoundError`.**
- [ ] **Step 3: Implement validation using these exact constants.**

```python
VALID_STATUSES = {"Existing", "Enhance", "Merge", "Match", "Planned-P0", "Planned-P1", "Planned-P2", "Experimental", "Deprecated", "Archived"}
VALID_CONCLUSIONS = {"EXISTING", "MATCH", "ENHANCE", "MERGE", "NEW"}
VALID_SCORE_STATES = {"NOT_SCORED", "PARTIALLY_SCORED", "SCORED"}
MATCH_FIELDS = ("name", "purpose", "inputs", "outputs", "decision_logic", "workflow_role")
```

- [ ] **Step 4: Re-run the focused tests until passing, then commit.**

```bash
git add scripts/generate_skill_governance_matrix.py scripts/tests/test_generate_skill_governance_matrix.py docs/governance/skill-governance-registry.yaml
git commit -m "feat(governance): validate skill governance registry"
```

### Task 2: Populate 79 evidence-bounded records

**Files:**
- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`

**Interfaces:** physical slug union is input; registry produces 79 `skills` records plus candidate records from the current Matching Register.

- [ ] **Step 1: Add the coverage test.**

```python
def test_repository_registry_covers_each_logical_skill_once(self):
    registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
    self.assertEqual(matrix.validate_registry(registry, matrix.discover_physical_skills(ROOT)), [])
    self.assertEqual(len(registry.skills), 79)
```

- [ ] **Step 2: Run it; expect an incomplete-registry failure.**
- [ ] **Step 3: Add every physical slug once, with actual paths and conservative state.**

```yaml
- slug: requirements-analysis
  zh_path: skills/zh/testing-types/requirements-analysis
  en_path: skills/en/testing-types/requirements-analysis
  virtual_domain: D01
  sdlc_stage: requirements
  roles: [QA, BA]
  status: Existing
  priority: P0
  governance_evidence: skills/zh/testing-types/requirements-analysis/SKILL.md
  quality_score: {state: NOT_SCORED, reason: "No nine-dimension review evidence recorded"}
  eval_execution: {state: NOT_RUN, reason: "Structural cases exist; no execution result recorded"}
```

- [ ] **Step 4: Record each existing candidate with six target-Skill evidence references. `NEW` additionally requires explicit scope and non-goals.**
- [ ] **Step 5: Run focused tests; expect exactly 79 covered pairs; commit.**

```bash
python3 -m unittest scripts.tests.test_generate_skill_governance_matrix -v
git add docs/governance/skill-governance-registry.yaml scripts/tests/test_generate_skill_governance_matrix.py
git commit -m "docs(governance): record phase 0 skill decisions"
```

### Task 3: Generate bilingual Matrix and Register

**Files:**
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`
- Modify: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`
- Modify: `docs/SKILL_MATCHING_REGISTER.md`, `docs/SKILL_MATCHING_REGISTER_EN.md`

**Interfaces:** `render_matrix(registry, locale) -> str`; `render_matching_register(registry, locale) -> str`; CLI `--check` returns nonzero for stale files.

- [ ] **Step 1: Add failing renderer and drift tests.**

```python
def test_check_returns_nonzero_for_stale_output(self):
    output.write_text("stale\n", encoding="utf-8")
    self.assertEqual(matrix.check_outputs(root), 1)
```

- [ ] **Step 2: Render all governance fields, explicit score/eval states, reciprocal links, candidate conclusion/target/six evidence references/next action.**
- [ ] **Step 3: Generate, check, test, and commit.**

```bash
python3 scripts/generate_skill_governance_matrix.py
python3 scripts/generate_skill_governance_matrix.py --check
python3 -m unittest scripts.tests.test_generate_skill_governance_matrix -v
git add scripts/generate_skill_governance_matrix.py scripts/tests/test_generate_skill_governance_matrix.py docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md
git commit -m "feat(governance): generate skill matrix views"
```

### Task 4: Enforce freshness and document operation

**Files:**
- Modify: `scripts/check_skills_quality.sh`
- Modify: `docs/SKILL_LIFECYCLE.md`, `docs/SKILL_LIFECYCLE_EN.md`
- Modify: `docs/SKILL_QUALITY_GATE.md`, `docs/SKILL_QUALITY_GATE_EN.md`
- Modify: `docs/SKILL_MATCHING_GUIDE.md`, `docs/SKILL_MATCHING_GUIDE_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [ ] **Step 1: Add a failing test that requires the Matrix freshness command in the quality gate.**
- [ ] **Step 2: Add it as gate four and renumber later labels without removing commands.**

```bash
echo "[4/10] Check generated governance matrix"
python3 scripts/generate_skill_governance_matrix.py --check
```

- [ ] **Step 3: Update both language guides: registry is authoritative, views are generated, and `NOT_SCORED`, `NOT_RUN`, `UNASSESSED` are evidence states.**
- [ ] **Step 4: Run focused tests, full gate, and diff check; commit.**

```bash
python3 -m unittest scripts.tests.test_generate_skill_governance_matrix -v
bash scripts/check_skills_quality.sh
git diff --check
git commit -am "chore(governance): enforce phase 0 registry freshness"
```

### Task 5: Close Phase 0 with bounded evidence

**Files:**
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [ ] **Step 1: Record that all 79 pairs are covered, generated outputs are fresh, and focused/full gates passed; retain Prompt/model/runtime effectiveness as `UNASSESSED`.**
- [ ] **Step 2: Run final verification.**

```bash
python3 scripts/generate_skill_inventory.py
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
python3 -m unittest scripts.tests.test_generate_skill_governance_inventory scripts.tests.test_generate_skill_governance_matrix -v
bash scripts/check_skills_quality.sh
git diff --check
git status --short
```

- [ ] **Step 3: Commit the evidence record.**

```bash
git add docs/governance/SKILL_GOVERNANCE_ROADMAP.md docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md
git commit -m "docs(governance): close phase 0 evidence review"
```

## Plan self-review

- Tasks 1–3 implement the source, validation, candidates, and generated bilingual views.
- Task 4 makes freshness enforceable and synchronizes operation guidance.
- Task 5 closes only source-governance evidence; it does not claim runtime effectiveness.
