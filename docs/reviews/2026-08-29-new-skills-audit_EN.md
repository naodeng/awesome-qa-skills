<div align="right"><a href="./2026-08-29-new-skills-audit.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# New QA Skills Audit Report

**Date:** 2026-08-29

**Scope:** The 29 Skills added on `explore` relative to `main`, covering 58 Chinese and English Skill packages.

**Method:** The nine-phase `skill-review` audit, repository authoring and style guides, and the complete quality gate.

## Executive Summary

**Result:** Pass after remediation

- Critical: 0
- High: 3 categories
- Medium: 2 categories
- Low: 1 category

The reviewed Skills contain no versioned external APIs, SDKs, or executable dependency examples, so upstream API and version-drift checks were not applicable. The material risks were underspecified content, incomplete cross-file contracts, and generic eval cases that could not demonstrate domain behavior.

## Findings and Remediation

### High: Skill entry files were shells

All 58 new `SKILL.md` files originally had only six lines. Every entry now covers invocation, output options, execution flow, reference loading, constraints, delivery checks, pitfalls, and domain-specific practices.

### High: Primary prompts lacked executable contracts

Forty-eight prompts had fewer than ten lines, including forty with only two lines. All 58 prompts now define real input sources, domain analysis dimensions, execution rules, minimum coverage, deliverables, operational boundaries, and evidence requirements.

### High: Eval cases were generic

Many cases reused the same commerce scenarios. All 174 Chinese and English cases now use domain-specific scenarios for complete context, incomplete input, and constrained risk or authorization boundaries.

### Medium: Bilingual depth was only structurally aligned

Chinese and English now align on folder names, frontmatter, section sequence, and evaluation intent while using natural language rather than literal translation.

### Medium: Production and AI-native safety boundaries were incomplete

The prompts now require least privilege, masked data, mocks, dry runs, isolated environments, stop conditions, human handoff, and side-effect verification. Unauthorized production writes are prohibited.

### Low: Output naming and order varied

Outputs now follow task understanding, input audit, risks and priorities, core execution items, residual risk, and next actions while retaining domain-specific deliverables.

## Verification

```bash
bash scripts/check_skills_quality.sh
git diff --check
```

- Directory organization: passed
- Agent metadata: 0 findings
- Skill independence: 0 findings
- Skill integrity: 156 scanned, 0 findings
- External snapshot hygiene: passed
- skill-up YAML: 156 passed, 0 failed
- New prompts: all at least 80 lines with required sections
- Bilingual Skill pairs: all 29 complete
- Git whitespace validation: passed

## Residual Risk

- The 174 cases were validated statically but not each executed through a model. Results may vary by engine, model version, and randomness.
- Real usage feedback should become regression cases under the relevant `evals/cases/` directory.

## Conclusion

The new Skills now have executable entry files, domain-specific prompt contracts, and meaningful domain evals. They meet the repository's pre-review quality threshold.
