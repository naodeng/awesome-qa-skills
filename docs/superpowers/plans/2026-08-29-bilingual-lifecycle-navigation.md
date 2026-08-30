<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-08-29-bilingual-lifecycle-navigation_EN.md">🇬🇧 English</a></div>

# 双语生命周期导航实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在不改变任何 Skill 目录和安装路径的前提下，将全部 Skill 按“四层能力体系 × 研发测试阶段”纳入双语 README，并建立可持续的中英文文档配对校验。

**Architecture:** 使用现有物理目录作为唯一安装真相，README、路线图与索引只增加逻辑分类。新增独立文档校验脚本，对项目级文档和 Skill 维护文档执行镜像、语言切换与分类完整性检查，并接入现有质量门禁。

**Tech Stack:** Markdown、Python 3 标准库、Bash、现有仓库质量脚本。

**Spec:** `docs/superpowers/specs/2026-08-29-bilingual-lifecycle-navigation-design.md`

## Global Constraints

- 不移动、重命名或删除 `skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/` 下任何 Skill 目录。
- 中文 `README.md` 是默认入口，英文 `README_EN.md` 是完整镜像。
- 每个测试类型 Skill 在主分类中只出现一次；工作流和 Skill Engineering 分别作为编排层与治理层展示。
- 每种语言保持 78 个 Skill：10 workflows + 65 testing types + 3 Skill Engineering；双语共 156 个目录。
- `legacy-prompts/`、`docs/archive/`、外部快照、生成产物、第三方许可和评测运行产物不要求逐文件翻译。
- 保留当前工作区内与本任务无关的未提交改动，提交时只暂存确认属于本计划的文件。

---

### Task 1: 固化分类清单与失败校验

**Files:**
- Create: `scripts/check_docs_bilingual.py`
- Create: `scripts/tests/test_check_docs_bilingual.py`
- Modify: `scripts/check_skills_quality.sh`

**Interfaces:**
- Consumes: 实际 Skill 目录和 README 中 `data-skill` 标记。
- Produces: `check_docs_bilingual.py --repo-root PATH`，成功返回 0，发现缺失镜像、无语言切换、遗漏或重复分类时返回 1。

- [x] **Step 1:** 编写失败测试，临时仓库分别覆盖缺少英文镜像、缺少反向链接、Skill 分类重复、Skill 分类遗漏和目录快照变化。
- [x] **Step 2:** 运行 `python3 -m unittest scripts.tests.test_check_docs_bilingual -v`，确认失败原因来自脚本尚不存在。
- [x] **Step 3:** 实现仅使用 Python 标准库的校验器；项目文档通过显式维护清单检查，Skill 文档按 zh/en 相对路径检查 `SKILL.md`、`prompts/`、`README.md`、`quick-start.md`、`tutorial.md`、`output-formats.md` 与 `reference.md`。
- [x] **Step 4:** 在 `check_skills_quality.sh` 增加第七步，并避免改变原六项校验语义。
- [x] **Step 5:** 重跑 unittest，预期全部通过；在真实仓库运行校验器，预期先因尚未补齐文档而失败。

### Task 2: 重建根 README 的双层导航

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`

**Interfaces:**
- Consumes: 65 个测试类型目录、10 个工作流目录、3 个 Skill Engineering 目录。
- Produces: 中英文一致的“四层能力体系 × 研发测试阶段”目录，每个测试类型行包含唯一 `data-skill="<name>"` 标记供校验器计数。

- [x] **Step 1:** 记录变更前 `find skills/{zh,en} -mindepth 3 -maxdepth 3 -type d` 的 Skill 目录快照和数量。
- [x] **Step 2:** 修正徽章与说明中的 testing types 数量为 65，并移除“计划中”“候选 Skill”等过期表述。
- [x] **Step 3:** 保留工作流表，增加其覆盖研发测试阶段的说明。
- [x] **Step 4:** 将 65 个测试类型分别放入 Core、Engineering、Production、AI Native，并在每层按适用生命周期阶段细分。
- [x] **Step 5:** 完整同步英文 README 的表格、顺序、链接、说明和统计。
- [x] **Step 6:** 运行文档校验器，确认不存在遗漏、重复和无效 Skill 路径。

### Task 3: 同步索引、路线图与语言入口

**Files:**
- Modify: `skills-index.md`
- Create: `skills-index_EN.md`
- Modify: `skills/zh/README.md`
- Modify: `skills/en/README.md`
- Modify: `docs/QA_SKILLS_EVOLUTION_ROADMAP.md`
- Modify: `docs/QA_SKILLS_EVOLUTION_ROADMAP_EN.md`

**Interfaces:**
- Consumes: Task 2 的唯一分类映射。
- Produces: 同一分类术语、阶段顺序、统计和双向语言切换。

- [x] **Step 1:** 为 `skills-index.md` 增加中文默认语言切换和完整阶段映射，修复旧的“planned extensions”状态。
- [x] **Step 2:** 创建内容对等的 `skills-index_EN.md`，路径保持指向实际英文 Skill。
- [x] **Step 3:** 重写两份语言分区 README 的能力导航，使其与根 README 的主归属完全一致。
- [x] **Step 4:** 在两份路线图中加入八阶段细分、已完成状态和语言切换链接。
- [x] **Step 5:** 运行文档校验器，确认四个入口没有分类漂移。

### Task 4: 补齐核心维护文档双语镜像

**Files:**
- Create bilingual counterparts for: `docs/reviews/2026-08-29-new-skills-audit.md`, `docs/superpowers/specs/2026-08-29-four-stage-qa-skills-evolution-design.md`, `docs/superpowers/plans/2026-08-29-four-stage-qa-skills-evolution.md`.
- Modify both files in each pair to add two-way language switching.
- Create English mirrors for: `skills/DIRECTORY_GUIDE.md`, `skills/EXTERNAL_SNAPSHOT_POLICY.md`, `skills/SKILL_AUTHORING.md`, `skills/SKILL_STYLE_GUIDE.md`.
- Modify Chinese originals to add language switching.

**Interfaces:**
- Consumes: existing Chinese source documents.
- Produces: `_EN.md` English mirrors with matching headings, rules, commands, paths, counts, and status.

- [x] **Step 1:** Translate the active review, four-stage design, and four-stage implementation plan without changing commands or paths.
- [x] **Step 2:** Translate the four Skill governance guides and preserve all normative MUST/禁止 boundaries.
- [x] **Step 3:** Add relative two-way language links to every pair.
- [x] **Step 4:** Run the parity checker and `git diff --check`.

### Task 5: 补齐 Skill 维护文档路径镜像

**Files:**
- Create English mirrors for the 20 zh-only maintained documents under `skills/en/testing-types/`: quick-start files for accessibility, AI-assisted, API, automation, bug reporting, functional, manual, mobile, performance, requirements, security, case review, case writing, reporting, and strategy; tutorials for API, automation, functional, mobile, and performance.
- Chinese source documents remain unchanged; language selection happens at the root and language-directory README level.

**Interfaces:**
- Consumes: the Chinese document at the same relative path.
- Produces: an English document at `skills/en/<same-relative-path>` with equivalent workflow, commands, examples, and safety notes.

- [x] **Step 1:** Add English quick-start mirrors, preserving executable commands and replacing only language-specific prose and example labels.
- [x] **Step 2:** Add English tutorial mirrors, preserving code semantics, paths, placeholders, and expected results.
- [x] **Step 3:** Do not add per-file language switches inside Skill packages; verify only same-relative-path pairing.
- [x] **Step 4:** Run the parity checker and inspect at least one quick-start and one tutorial in each language tree.

### Task 6: 最终验证与交付

**Files:**
- Modify only files produced by Tasks 1–5 if verification finds defects.

**Interfaces:**
- Consumes: completed bilingual documentation and stable Skill directories.
- Produces: verified commit on `explore` and updated PR #4.

- [x] **Step 1:** Compare pre/post Skill directory snapshots; expected result is byte-for-byte identical sorted path lists.
- [x] **Step 2:** Run `python3 -m unittest scripts.tests.test_check_docs_bilingual -v`.
- [x] **Step 3:** Run `python3 scripts/check_docs_bilingual.py --repo-root .`.
- [x] **Step 4:** Run `bash scripts/check_skills_quality.sh` and `git diff --check`.
- [x] **Step 5:** Stage only plan files, documentation files, the new checker/test, and the one quality-gate edit; inspect `git diff --cached --name-only` for unrelated paths.
- [x] **Step 6:** Commit with `docs(readme): add lifecycle navigation and bilingual parity`, push `explore`, and verify PR #4 head commit and checks.
