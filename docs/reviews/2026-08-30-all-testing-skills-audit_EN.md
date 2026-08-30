<div align="right"><a href="./2026-08-30-all-testing-skills-audit.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# All Testing-Type Skills Audit Report

**Date:** 2026-08-30

**Scope:** All 130 Skill packages under `skills/{zh,en}/testing-types/` (65 topics, one Chinese and one English package each).

**Method:** The nine-phase `skill-review` audit, repository structural and independence validators, static eval-YAML validation, and official-documentation checks for executable k6, Selenium, and Appium examples.

## Executive Summary

**Result:** Pass, with one Medium and one Low maintenance item recommended for the next content update.

| Severity | Count | Result |
| --- | ---: | --- |
| Critical | 0 | No secret exposure, destructive execution, or unusable Skill package. |
| High | 0 | No issue blocks installation, invocation, or core delivery. |
| Medium | 1 | One k6 quick-reference command is not supported by the current CLI. |
| Low | 1 | One Selenium example pins plainly outdated dependencies. |

## Verified Passes

- Testing-type directories are fully paired: 65 topics and 130 packages; each has its entry, primary prompt, `agents/openai.yaml`, and `evals/` directory.
- Metadata, standalone-installation, cross-Skill links, integrity, and external-snapshot hygiene all returned zero findings.
- Static `skill-up` eval YAML validation: 156 passed and 0 failed, including all 130 packages in scope.
- Eval cases cover complete input, incomplete information, and risk/boundary scenarios. No TODO/FIXME placeholder remains in a user-executable entry or primary prompt. `TODO`/`TBD` occurrences in eval assertions deliberately require models to state information gaps.
- Sampled Playwright, Cypress, k6 module imports, and Appium `AppiumBy` usage remain compatible with current official documentation.

## Findings

### Medium: the k6 “run a specific scenario” command is invalid

**Location:** `skills/zh/testing-types/performance-testing/quick-start.md:260`

```bash
k6 run --scenario-name my_scenario script.js
```

**Evidence:** Current k6 documentation defines scenarios through `options.scenarios` in the script and runs the script with `k6 run scenario-example.js`; it does not provide a `--scenario-name` run flag. Selecting a named workload needs explicit script logic, for example an environment-variable-controlled scenario configuration, rather than a CLI flag.

**Impact:** A reader who copies this quick-reference command receives a CLI error. Its position in the common-command section makes that misleading.

**Recommended remediation:** Remove the command. State that scenarios are defined in `options.scenarios` and run with `k6 run script.js`; add a controlled environment-variable selection example only if that behavior is needed.

### Low: pinned Selenium example dependencies are outdated

**Location:** `skills/zh/testing-types/automation-testing/examples/selenium-pom-python/requirements.txt:1-6` and `README.md:277-281` in the same directory.

**Evidence:** The example pins `selenium` to `4.16.0` and `pytest` to `7.4.3`. Selenium’s current stable release is 4.48.0, and the official Selenium Manager handles browser drivers in most current setups; the example also retains the older third-party `webdriver-manager` dependency.

**Impact:** The example may still execute, but it misses current compatibility and maintenance improvements, and can imply that a separate driver manager is universally required.

**Recommended remediation:** Run it in an isolated environment, then update to verified current version ranges and prefer Selenium Manager. If `webdriver-manager` stays, document that it is only for specific restricted environments.

## Review Boundaries and Residual Risk

- Automated structural, metadata, independence, and eval-YAML checks ran over every package. Tool-specific examples received high-risk sampling and official-documentation verification; this was not a full live execution of every example environment.
- `examples/` and `references/` are on-demand material and do not require line-by-line bilingual mirroring. That follows the repository’s standalone-Skill and no-internal-language-switch conventions, so it is not a bilingual finding.
- The `description: Use this skill when ...` frontmatter in Chinese `SKILL.md` files is the repository’s discovery-metadata contract. Chinese bodies, prompts, and project-level entries remain Chinese-first, so it is not classified as English leakage.

## Conclusion

All testing-type Skills meet the project’s current structural, bilingual-pairing, standalone-installation, and static-evaluation quality gate. Resolving the two maintenance items will further improve copy-and-run reliability. This review intentionally did not modify Skill content so that the audit and any later remediation remain clearly separated.
