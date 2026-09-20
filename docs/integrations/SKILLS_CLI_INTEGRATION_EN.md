<div align="right"><a href="./SKILLS_CLI_INTEGRATION.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skills CLI / Agent Skills Distribution Contract

Status: V2 delivered in one iteration. The `skills` CLI is the default distribution entry point, and `skills@1.7.0` is the fixed compatibility version used by repository CI.

This contract covers distribution, discovery, installation paths, and repository boundaries. It does not make the CLI a Skill runtime dependency, and it does not replace `skill-up` behavioral evaluation, business acceptance, release approval, or production verification.

## Quick start

The repository-level entry point is English-first and installs a leaf Skill by canonical name:

```bash
# Install English functional-testing
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# Optional: target Codex explicitly
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# Install the full English collection
npx skills add naodeng/awesome-qa-skills
```

Chinese requires explicit source selection; install one language per target by default:

```bash
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

## V2 distribution contract

1. The leaf directory, the `SKILL.md` frontmatter `name`, and the CLI `--skill` ID must be identical.
2. A new Skill must be discoverable from the repository-level entry point; it must not depend on hidden leaf paths or undocumented aliases.
3. A leaf Skill must be independently installable or copyable, with a self-contained `SKILL.md`, prompts, metadata, and resources.
4. `skills/en` and `skills/zh` keep the same canonical names; names must not repeat within one language.
5. `description` serves both triggering and discovery, so it must state capability, trigger intent, and QA differentiation.
6. The CLI is a distribution layer, not a Skill runtime dependency; installation must not implicitly execute Skill scripts.

The repository-level source maps to English by default. Select the explicit `skills/zh` source for Chinese; do not rely on implicit CLI deduplication or namespacing for same-named Skills.

## Fixed version and advanced commands

README keeps the everyday commands simple and unpinned. Reproduce CI or require a deterministic tool version with `skills@1.7.0`:

```bash
# Install fixed-version English functional-testing into a global Codex target
npx --yes skills@1.7.0 add naodeng/awesome-qa-skills --skill functional-testing -g -a codex -y

# Explicitly install fixed-version Chinese functional-testing
npx --yes skills@1.7.0 add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing -g -a codex -y

# Inspect records, update, and remove
npx --yes skills@1.7.0 list --json
npx --yes skills@1.7.0 update -g -y
npx --yes skills@1.7.0 remove functional-testing -g -y
```

`use`, `update`, `remove`, and Agent targets are CLI-version behavior. Before changing the pin, run `npx --yes skills@<version> --help`, then update the script, CI, and this document together.

## Compatibility gate

Run before submitting:

```bash
bash scripts/check_skills_cli_compatibility.sh
```

This entry point performs a small, stable set of checks:

- Local static contract: `SKILL.md`, frontmatter, `name`, directory alignment, same-language duplicates, and EN/ZH canonical-name alignment.
- Representative discovery: `requirements-analysis`, `functional-testing`, `api-testing`, `performance-testing`, `ai-agent-testing`, `release-testing-workflow`, and `skill-change-verification`.
- Repository-level `--list` discovery with fixed `skills@1.7.0`.
- English-first `functional-testing` global Codex smoke, including the installed `SKILL.md`, canonical name, and English heading.

CI runs one `skills-cli-compatibility` job in the existing `project-quality.yml` and sets `SKILLS_CLI_PACKAGE` to the current checkout, so a PR validates its changes instead of a fixed remote default branch. When run manually without that variable, the script defaults to `naodeng/awesome-qa-skills`; reproduce the CI source locally with `SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh`. It does not run a latest Canary and does not use total Skill count as a contract. The gate does not claim full real installation coverage, model replay, browser runtime coverage, business acceptance, or release evidence.

## Tested and Ecosystem compatible

- **Tested by this repository**: fixed `skills@1.7.0`, repository-level English discovery, the representative names above, and the English `functional-testing` Codex installation smoke.
- **Ecosystem compatible**: an Agent, version, or path declared usable by the upstream CLI but not covered by this repository's continuous gate evidence. Do not present it as project-tested support.

## Legacy installers and manual paths

The CLI is the preferred distribution layer, but existing paths remain supported:

```bash
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
bash scripts/install-skills-mac.sh --tool codex --lang zh
```

The Windows installer and manual copying are not removed because the CLI exists. They are compatibility fallbacks and do not change canonical names or directory layout.

## Explicit V2 non-goals

- Do not add `skills-manifest.json`, `package.json`, a CLI runtime dependency, or a custom package manager.
- Do not restructure `skills/en` / `skills/zh`, rename canonical names, or introduce `-en` / `-zh` suffixes.
- Do not delete legacy installers, add a separate canary workflow, or build a complex Canary or full multi-Agent matrix.
- Do not require real installation of all 162 Skills, expand trigger evals, or change `skill-up` architecture in this iteration.

## Troubleshooting

- Static failure: fix the reported `CONTRACT`, `BILINGUAL`, or `DISCOVERY` finding, then rerun the full quality gate.
- Missing discovery representative: check the repository root, canonical name, and remote branch content instead of bypassing the check with a leaf URL.
- EN/ZH overwrite: clean the target's existing language before installing one language collection; do not assume same-named Skills are automatically isolated.
- Upstream CLI breakage: keep the static contract and legacy installers, pause release-facing CLI claims, and never upgrade the fixed pin automatically.
