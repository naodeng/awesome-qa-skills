#!/usr/bin/env python3
"""Render the v1.0 source-governance inventory for every bilingual Skill pair.

This is an inventory of repository declarations.  It intentionally does not run
Skill prompts, model evaluations, package scripts, or quality scoring.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

try:
    from .virtual_domains import catalog_skill_headings, load_required_catalog
except ImportError:  # pragma: no cover - direct script execution
    from virtual_domains import catalog_skill_headings, load_required_catalog


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("testing-workflows", "testing-types", "skill-engineering")
LANGUAGES = ("zh", "en")
GENERATED = {
    "zh": ROOT / "docs/generated/skill-governance-inventory.md",
    "en": ROOT / "docs/generated/skill-governance-inventory_EN.md",
}


@dataclass(frozen=True)
class Record:
    section: str
    slug: str
    domain: str
    description_zh: str
    description_en: str
    status: str
    relation: str
    eval_summary: str
    evidence: str


def frontmatter_value(path: Path, key: str) -> str:
    if not path.is_file():
        return "UNASSESSED (file missing)"
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"') if match else "UNASSESSED (field missing)"


def catalog_domains() -> dict[str, str | None]:
    """Use the current catalog's capability headings as classifier input."""
    return catalog_skill_headings(ROOT / "docs/catalog/skills-index.md")


def virtual_domain(
    section: str,
    slug: str,
    domains: dict[str, str | None],
    catalog=None,
) -> str:
    if catalog is None:
        return "UNASSESSED (virtual-domain manifest missing)"
    return catalog.classify(section, slug, domains.get(slug))


def related(slug: str, all_slugs: set[str]) -> str:
    base = slug.removesuffix("-plus")
    if slug.endswith("-plus") and base in all_slugs:
        return f"Plus variant of `{base}`"
    aliases = {"testcase-writer-plus": "test-case-writing"}
    if slug in aliases and aliases[slug] in all_slugs:
        return f"Plus variant of `{aliases[slug]}`"
    families = ("api-test-", "ui-test-", "performance-test-")
    for prefix in families:
        if slug.startswith(prefix):
            siblings = sorted(candidate for candidate in all_slugs if candidate.startswith(prefix) and candidate != slug)
            return "Comparable tool-specific family: " + ", ".join(f"`{item}`" for item in siblings)
    return "No explicit Plus/similar relation recorded; semantic similarity UNASSESSED"


def eval_structure(skill_dir: Path) -> tuple[bool, str]:
    config = skill_dir / "evals/eval.yaml"
    cases = sorted((skill_dir / "evals/cases").glob("*.yaml")) if (skill_dir / "evals/cases").is_dir() else []
    listed: list[str] = []
    if config.exists():
        config_text = config.read_text(encoding="utf-8", errors="replace")
        listed.extend(re.findall(r"^\s*-\s+evals/cases/([^\s]+\.yaml)", config_text, re.MULTILINE))
        inline_files = re.search(r"^\s*files:\s*\[([^]]*)\]", config_text, re.MULTILINE | re.DOTALL)
        if inline_files:
            listed.extend(re.findall(r"evals/cases/([^,\]\s]+\.yaml)", inline_files.group(1)))
    present = bool(config.exists() and cases)
    return present, f"eval.yaml={'present' if config.exists() else 'missing'}; cases={len(cases)}; declared={len(listed)}"


def records() -> list[Record]:
    domain_catalog = load_required_catalog(ROOT)
    domains = catalog_domains()
    packages = {
        section: {
            path.name
            for lang in LANGUAGES
            for path in (ROOT / "skills" / lang / section).iterdir()
            if path.is_dir()
        }
        for section in SECTIONS
    }
    all_slugs = set().union(*packages.values())
    result: list[Record] = []
    for section in SECTIONS:
        for slug in sorted(packages[section]):
            zh_dir, en_dir = (ROOT / "skills/zh" / section / slug, ROOT / "skills/en" / section / slug)
            zh_skill, en_skill = zh_dir / "SKILL.md", en_dir / "SKILL.md"
            zh_agent, en_agent = zh_dir / "agents/openai.yaml", en_dir / "agents/openai.yaml"
            zh_eval_ok, zh_eval = eval_structure(zh_dir)
            en_eval_ok, en_eval = eval_structure(en_dir)
            structural = all((en_dir.is_dir(), zh_skill.exists(), en_skill.exists(), zh_agent.exists(), en_agent.exists(), zh_eval_ok, en_eval_ok))
            names_match = frontmatter_value(zh_skill, "name") == frontmatter_value(en_skill, "name") == slug
            status = "STRUCTURALLY_RECORDED" if structural and names_match else "UNASSESSED (structural gap)"
            evidence = (
                f"zh=`skills/zh/{section}/{slug}`; en=`skills/en/{section}/{slug}`; "
                f"frontmatter-name={'aligned' if names_match else 'not-aligned'}; "
                f"agent-metadata={'present' if zh_agent.exists() and en_agent.exists() else 'missing'}; "
                f"zh[{zh_eval}]; en[{en_eval}]; semantic/effectiveness=UNASSESSED"
            )
            result.append(Record(section, slug, virtual_domain(section, slug, domains, domain_catalog), frontmatter_value(zh_skill, "description"), frontmatter_value(en_skill, "description"), status, related(slug, all_slugs), f"zh[{zh_eval}] / en[{en_eval}]", evidence))
    return result


def render(language: str, rows: list[Record]) -> str:
    zh = language == "zh"
    domain_catalog = load_required_catalog(ROOT)
    title = "v1.0 Skill 治理逐项清单" if zh else "v1.0 Skill Governance Per-Package Inventory"
    switch = "English" if zh else "中文"
    switch_target = "skill-governance-inventory_EN.md" if zh else "skill-governance-inventory.md"
    intro = (
        "此文件由 `python3 scripts/generate_skill_governance_inventory.py` 生成。它只核对仓库声明、目录和 Eval 文件结构；不执行 Skill、脚本或模型，不产生 Quality Score，也不证明运行效果。"
        if zh else
        "Generated by `python3 scripts/generate_skill_governance_inventory.py`. It inspects only repository declarations, directories, and Eval file structure; it does not run Skills, scripts, or models, calculate a Quality Score, or prove runtime effectiveness."
    )
    columns = ("| Skill | Virtual Domain | 状态 | Scope 边界 | 相似/Plus 关系 | Eval 结构 | Capability Match 证据 |" if zh else "| Skill | Virtual Domain | Status | Scope boundary | Similar/Plus relation | Eval structure | Capability Match evidence |")
    lines = [f'<div align="right"><a href="./{switch_target}">{switch}</a></div>', "", f"# {title}", "", intro, "", f"- {'记录数' if zh else 'Records'}: `{len(rows)}` bilingual Skill pairs", "- Virtual Domains: `D01`–`D16`, sourced from `docs/governance/virtual-domains.yaml`.", "- `UNASSESSED` means evidence is unavailable or outside this source-only review; it is not a negative quality result.", "", columns, "| --- | --- | --- | --- | --- | --- | --- |"]
    boundary = "仅限包声明与文件结构；运行行为、模型评测、质量效果均为 UNASSESSED" if zh else "Package declarations and file structure only; runtime behavior, model evaluation, and quality effectiveness are UNASSESSED"
    for row in rows:
        description = row.description_zh if zh else row.description_en
        domain_label = domain_catalog.label(row.domain, language) if domain_catalog and row.domain in domain_catalog.domain_ids() else row.domain
        lines.append(f"| `{row.slug}` | {domain_label} | `{row.status}` | {boundary}. Source: {description} | {row.relation} | {row.eval_summary} | {row.evidence} |")
    lines.extend(["", "## Reproduce" if not zh else "## 复现", "", "```bash", "python3 scripts/generate_skill_governance_inventory.py --check", "```", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated inventories are stale")
    args = parser.parse_args()
    try:
        rendered = {language: render(language, records()) for language in LANGUAGES}
    except (OSError, ValueError) as error:
        print(f"virtual_domain_catalog_error={error}")
        return 1
    stale = [language for language, path in GENERATED.items() if not path.exists() or path.read_text(encoding="utf-8") != rendered[language]]
    if args.check:
        if stale:
            print("stale_governance_inventory=" + ",".join(stale))
            return 1
        print("governance_inventory=up-to-date")
        return 0
    for language, path in GENERATED.items():
        path.write_text(rendered[language], encoding="utf-8")
        print(f"generated={path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
