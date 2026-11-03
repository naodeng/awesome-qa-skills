<div align="right"><a href="./AGENT_COMPATIBILITY_MATRIX.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Agent Compatibility and Distribution Matrix

This matrix separates repository/install evidence, Skills CLI discovery, and real invocation inside an Agent Host. Static source compatibility or `--dry-run` does not prove that a Host loaded or executed a Skill. The state is dated 2026-11-03; per-item install, upgrade, uninstall, and ZIP results are in the [machine-readable verification record](./agent-compatibility-evidence-2026-11-03.json).

| Capability | Codex | Claude Code | Cursor | Evidence boundary |
| --- | --- | --- | --- | --- |
| Install entry point | macOS/Linux installer | macOS/Linux installer | macOS/Linux installer | `--tool` target × five Workflow packages × two locales × two installs each: 60 isolated installs; recursive file SHA-256 matched the source |
| Canonical name / one Skill directory | Supported | Supported | Supported | `validate_agents_metadata.py`, independence checks, and installed file structure |
| Agent Skills CLI discovery | Repository gate on `skills@1.7.0` | Same; scoped to CLI behavior covered by the gate | Same; scoped to CLI behavior covered by the gate | CLI gate does not prove built-in Host Runtime compatibility |
| Chinese/English selection | `--lang zh|en` | `--lang zh|en` | `--lang zh|en` | All 60 installs used isolated temporary roots; recursive files match each source package, with no user config changed |
| References / Scripts | Distribute package-local resources | Distribute package-local resources | Distribute package-local resources | All five bilingual packages were compared file by file; ZIP members and contents matched the sources |
| Standalone Skill ZIP | Generic packager available | Generic packager available | Generic packager available | All 10 ZIPs have root-level `SKILL.md`, `agents/openai.yaml`, and Eval config, with exact file contents; this does not claim a native ZIP installation experience |
| Upgrade / uninstall / residue | Codex install target verified | Installer target selectable | Installer target selectable | On disposable Codex targets, 10 same-path upgrades, uninstall previews/applies, and zero-residue scans passed across five packages × two locales; Claude Code/Cursor Host upgrade execution is not claimed |
| Host auto-discovery / prompt execution | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | Requires separate acceptance in each real user environment |
| Automatic cross-stage Workflow orchestration / Host recovery | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | The repository provides and validates a file-based Run State CLI. It checks checkpoints and refuses stale or repeated stages, but it does not execute Skills or schedule Host stages |

## Reproduction

```bash
bash scripts/check_skills_cli_compatibility.sh
bash scripts/install-skills-mac.sh --tool codex --lang en --skill pr-quality-review --dest /tmp/qa-skills-install --dry-run
python3 scripts/manage_skill_packages.py pack --skill-dir skills/en/testing-workflows/pr-quality-review --output /tmp/pr-quality-review-en.zip
python3 scripts/manage_skill_packages.py check-residue --install-root /tmp/qa-skills-install --repo-root . --json
```

Real Host acceptance should record the Host name/version, Skill version, installation method, load evidence, input case, output, and time. Without those records, retain `NOT_RUN`.
