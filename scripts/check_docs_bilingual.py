#!/usr/bin/env python3
"""Validate bilingual project docs and README Skill classification."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote


PROJECT_PAIRS = (
    ("README.md", "README_EN.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING_EN.md"),
    ("FAQ.md", "FAQ_EN.md"),
    ("docs/catalog/skills-index.md", "docs/catalog/skills-index_EN.md"),
    ("docs/catalog/skills-graph.md", "docs/catalog/skills-graph_EN.md"),
    (
        "docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md",
        "docs/governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md",
    ),
    (
        "docs/governance/DOCUMENTATION_POLICY.md",
        "docs/governance/DOCUMENTATION_POLICY_EN.md",
    ),
    ("docs/reviews/2026-08-29-new-skills-audit.md", "docs/reviews/2026-08-29-new-skills-audit_EN.md"),
    (
        "docs/superpowers/specs/2026-08-29-four-stage-qa-skills-evolution-design.md",
        "docs/superpowers/specs/2026-08-29-four-stage-qa-skills-evolution-design_EN.md",
    ),
    (
        "docs/superpowers/plans/2026-08-29-four-stage-qa-skills-evolution.md",
        "docs/superpowers/plans/2026-08-29-four-stage-qa-skills-evolution_EN.md",
    ),
    (
        "docs/superpowers/specs/2026-08-29-bilingual-lifecycle-navigation-design.md",
        "docs/superpowers/specs/2026-08-29-bilingual-lifecycle-navigation-design_EN.md",
    ),
    (
        "docs/superpowers/plans/2026-08-29-bilingual-lifecycle-navigation.md",
        "docs/superpowers/plans/2026-08-29-bilingual-lifecycle-navigation_EN.md",
    ),
    (
        "docs/superpowers/specs/2026-08-29-project-structure-and-bilingual-docs-design.md",
        "docs/superpowers/specs/2026-08-29-project-structure-and-bilingual-docs-design_EN.md",
    ),
    (
        "docs/superpowers/plans/2026-08-29-project-structure-and-bilingual-docs.md",
        "docs/superpowers/plans/2026-08-29-project-structure-and-bilingual-docs_EN.md",
    ),
    ("skills/DIRECTORY_GUIDE.md", "skills/DIRECTORY_GUIDE_EN.md"),
    ("skills/EXTERNAL_SNAPSHOT_POLICY.md", "skills/EXTERNAL_SNAPSHOT_POLICY_EN.md"),
    ("skills/SKILL_AUTHORING.md", "skills/SKILL_AUTHORING_EN.md"),
    ("skills/SKILL_STYLE_GUIDE.md", "skills/SKILL_STYLE_GUIDE_EN.md"),
)

MAINTAINED_NAMES = {
    "SKILL.md",
    "README.md",
    "quick-start.md",
    "tutorial.md",
    "output-formats.md",
    "reference.md",
}

SKILL_MARKER = re.compile(r"<!--\s*data-skill:([a-z0-9-]+)\s*-->")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)


def maintained_skill_markdown(root: Path, lang: str) -> set[Path]:
    base = root / "skills" / lang
    found: set[Path] = set()
    for path in base.rglob("*.md"):
        rel = path.relative_to(base)
        parts = rel.parts
        if len(parts) < 3:
            continue
        package_tail = parts[2:]
        if set(package_tail[:-1]) & {"examples", "references", "output-templates", "reports", "evals"}:
            continue
        if path.name in MAINTAINED_NAMES or package_tail[0] == "prompts":
            found.add(rel)
    return found


def check_project_pairs(root: Path) -> list[str]:
    findings: list[str] = []
    for primary_rel, english_rel in PROJECT_PAIRS:
        primary = root / primary_rel
        english = root / english_rel
        if not primary.is_file():
            findings.append(f"missing primary document: {primary_rel}")
            continue
        if not english.is_file():
            findings.append(f"missing English mirror: {english_rel}")
            continue
        if Path(english_rel).name not in primary.read_text(encoding="utf-8"):
            findings.append(f"missing English switch link: {primary_rel}")
        if Path(primary_rel).name not in english.read_text(encoding="utf-8"):
            findings.append(f"missing Chinese switch link: {english_rel}")
    return findings


def check_relative_links(root: Path, paths: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    for rel in paths:
        document = root / rel
        if not document.is_file():
            continue
        text = FENCED_CODE.sub("", document.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            if not target or target.startswith(("#", "/", "http://", "https://", "mailto:")):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if path_part and not (document.parent / path_part).resolve().exists():
                findings.append(f"broken relative link in {rel}: {target}")
    return findings


def check_skill_parity(root: Path) -> list[str]:
    zh = maintained_skill_markdown(root, "zh")
    en = maintained_skill_markdown(root, "en")
    findings = [f"missing English Skill document: {p}" for p in sorted(zh - en)]
    findings.extend(f"missing Chinese Skill document: {p}" for p in sorted(en - zh))
    return findings


def check_catalog(root: Path) -> list[str]:
    findings: list[str] = []
    actual_zh = {p.name for p in (root / "skills/zh/testing-types").iterdir() if p.is_dir()}
    actual_en = {p.name for p in (root / "skills/en/testing-types").iterdir() if p.is_dir()}
    if actual_zh != actual_en:
        findings.append("zh/en testing-type directory names differ")
    for readme_rel in ("README.md", "README_EN.md"):
        readme = root / readme_rel
        if not readme.is_file():
            findings.append(f"missing catalog: {readme_rel}")
            continue
        markers = SKILL_MARKER.findall(readme.read_text(encoding="utf-8"))
        duplicates = sorted({name for name in markers if markers.count(name) > 1})
        missing = sorted(actual_zh - set(markers))
        unknown = sorted(set(markers) - actual_zh)
        if duplicates:
            findings.append(f"duplicate Skill markers in {readme_rel}: {', '.join(duplicates)}")
        if missing:
            findings.append(f"missing Skill markers in {readme_rel}: {', '.join(missing)}")
        if unknown:
            findings.append(f"unknown Skill markers in {readme_rel}: {', '.join(unknown)}")
        if len(markers) != len(actual_zh):
            findings.append(
                f"catalog count mismatch in {readme_rel}: markers={len(markers)} actual={len(actual_zh)}"
            )
    return findings


def check_chinese_readme_metadata_leak(root: Path) -> list[str]:
    readme = root / "README.md"
    if not readme.is_file():
        return ["missing catalog: README.md"]
    if re.search(r"\bUse this skill when\b|\btriggers include\b", readme.read_text(encoding="utf-8")):
        return ["English Skill metadata leaked into README.md"]
    return []


def validate(root: Path) -> list[str]:
    project_paths = tuple(path for pair in PROJECT_PAIRS for path in pair)
    return (
        check_project_pairs(root)
        + check_relative_links(root, project_paths)
        + check_skill_parity(root)
        + check_catalog(root)
        + check_chinese_readme_metadata_leak(root)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    findings = validate(root)
    for finding in findings:
        print(f"- {finding}")
    print(f"bilingual_docs_findings={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
