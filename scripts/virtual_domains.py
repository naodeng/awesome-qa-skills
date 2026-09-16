#!/usr/bin/env python3
"""Load and apply the repository's stable D01-D16 Virtual Domain taxonomy."""
from __future__ import annotations

from dataclasses import dataclass
import json
import re
from pathlib import Path


LANGUAGES = ("zh", "en")
SECTIONS = ("testing-workflows", "testing-types", "skill-engineering")
EXPECTED_DOMAIN_IDS = tuple(f"D{index:02d}" for index in range(1, 17))


@dataclass(frozen=True)
class VirtualDomain:
    id: str
    name_zh: str
    name_en: str
    description_zh: str
    description_en: str


@dataclass(frozen=True)
class VirtualDomainCatalog:
    domains: tuple[VirtualDomain, ...]
    section_defaults: dict[str, str]
    catalog_heading_defaults: dict[str, str]
    ambiguous_catalog_headings: tuple[str, ...]
    slug_overrides: dict[str, str]

    def domain_ids(self) -> tuple[str, ...]:
        return tuple(domain.id for domain in self.domains)

    def _domain(self, domain_id: str) -> VirtualDomain:
        for domain in self.domains:
            if domain.id == domain_id:
                return domain
        raise ValueError(f"Unknown virtual Domain ID: {domain_id}")

    def label(self, domain_id: str, locale: str) -> str:
        domain = self._domain(domain_id)
        if locale == "zh":
            return f"{domain.id} {domain.name_zh}"
        if locale == "en":
            return f"{domain.id} {domain.name_en}"
        raise ValueError(f"Unsupported virtual Domain locale: {locale}")

    def classify(self, section: str, slug: str, catalog_heading: str | None) -> str:
        domain_id = self.slug_overrides.get(slug)
        if domain_id is None and catalog_heading:
            if catalog_heading in self.ambiguous_catalog_headings:
                raise ValueError(
                    "Ambiguous catalog heading requires an explicit slug override: "
                    f"section={section!r}, slug={slug!r}, heading={catalog_heading!r}"
                )
            domain_id = self.catalog_heading_defaults.get(catalog_heading)
        if domain_id is None:
            domain_id = self.section_defaults.get(section)
        if domain_id is None:
            raise ValueError(
                "No virtual Domain mapping for "
                f"section={section!r}, slug={slug!r}, heading={catalog_heading!r}"
            )
        return domain_id


def _validate_mapping_values(values: dict[str, str], domain_ids: set[str], label: str) -> None:
    unknown = sorted(set(values.values()) - domain_ids)
    if unknown:
        raise ValueError(f"{label} contains unknown Domain IDs: {', '.join(unknown)}")


def load_catalog(path: Path) -> VirtualDomainCatalog:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Virtual Domain catalog is not valid JSON-compatible YAML: {path}") from error
    if not isinstance(data, dict):
        raise ValueError("Virtual Domain catalog must be an object")

    raw_domains = data.get("domains")
    if not isinstance(raw_domains, list):
        raise ValueError("Virtual Domain catalog requires a domains list")
    ids = tuple(str(entry.get("id", "")) for entry in raw_domains if isinstance(entry, dict))
    if ids != EXPECTED_DOMAIN_IDS:
        raise ValueError("Virtual Domain catalog must contain exactly D01-D16 in order")

    domains: list[VirtualDomain] = []
    for entry in raw_domains:
        if not isinstance(entry, dict):
            raise ValueError("Each Virtual Domain entry must be an object")
        fields = {
            field: str(entry.get(field, "")).strip()
            for field in ("id", "name_zh", "name_en", "description_zh", "description_en")
        }
        if any(not value for value in fields.values()):
            raise ValueError(f"Virtual Domain {fields['id'] or '<unknown>'} has an empty field")
        domains.append(VirtualDomain(**fields))

    domain_ids = set(EXPECTED_DOMAIN_IDS)
    section_defaults = data.get("section_defaults", {})
    heading_defaults = data.get("catalog_heading_defaults", {})
    ambiguous_headings = data.get("ambiguous_catalog_headings", [])
    slug_overrides = data.get("slug_overrides", {})
    if not all(isinstance(value, dict) for value in (section_defaults, heading_defaults, slug_overrides)):
        raise ValueError("Virtual Domain mappings must be objects")
    if not isinstance(ambiguous_headings, list) or any(
        not isinstance(value, str) or not value.strip() for value in ambiguous_headings
    ):
        raise ValueError("ambiguous_catalog_headings must be a list of non-empty strings")
    section_defaults = {str(key): str(value) for key, value in section_defaults.items()}
    heading_defaults = {str(key): str(value) for key, value in heading_defaults.items()}
    slug_overrides = {str(key): str(value) for key, value in slug_overrides.items()}
    _validate_mapping_values(section_defaults, domain_ids, "section_defaults")
    _validate_mapping_values(heading_defaults, domain_ids, "catalog_heading_defaults")
    _validate_mapping_values(slug_overrides, domain_ids, "slug_overrides")
    return VirtualDomainCatalog(
        tuple(domains),
        section_defaults,
        heading_defaults,
        tuple(value.strip() for value in ambiguous_headings),
        slug_overrides,
    )


def load_required_catalog(root: Path) -> VirtualDomainCatalog:
    path = root / "docs/governance/virtual-domains.yaml"
    if not path.is_file():
        raise ValueError(f"Virtual Domain catalog is required: {path}")
    return load_catalog(path)


def catalog_skill_headings(path: Path) -> dict[str, str | None]:
    """Return the nearest catalog `####` heading for each listed Skill slug."""
    headings: dict[str, str | None] = {}
    current: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") or (line.startswith("### ") and not line.startswith("#### ")):
            current = None
            continue
        if line.startswith("#### "):
            current = line[5:].strip()
            continue
        match = re.match(r"\| `([a-z0-9-]+)` \|", line)
        if match:
            headings[match.group(1)] = current
    return headings


def repository_mapping(root: Path) -> dict[tuple[str, str], str]:
    """Classify every logical repository Skill once, using both language trees."""
    catalog = load_catalog(root / "docs/governance/virtual-domains.yaml")
    headings = catalog_skill_headings(root / "docs/catalog/skills-index.md")
    mapping: dict[tuple[str, str], str] = {}
    for section in SECTIONS:
        slugs: set[str] = set()
        for language in LANGUAGES:
            section_root = root / "skills" / language / section
            if section_root.is_dir():
                slugs.update(path.name for path in section_root.iterdir() if path.is_dir())
        for slug in sorted(slugs):
            mapping[(section, slug)] = catalog.classify(section, slug, headings.get(slug))
    return mapping
