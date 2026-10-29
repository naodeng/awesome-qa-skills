#!/usr/bin/env python3
"""Validate the small, stable Skills CLI distribution contract.

This checker validates the repository shape and Skill frontmatter before the
shell wrapper runs the pinned CLI discovery and installation smoke. Its YAML
parser is a pinned development dependency; it is not a Skill runtime dependency.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    import yaml
    from yaml.constructor import ConstructorError
    from yaml.nodes import MappingNode
except ModuleNotFoundError as exc:
    raise SystemExit(
        "PyYAML is required for Skill frontmatter validation. "
        "Install development dependencies with `python3 -m pip install -r requirements-dev.txt`."
    ) from exc


SECTIONS = ("testing-types", "testing-workflows", "skill-engineering")
LANGUAGES = ("en", "zh")
CANONICAL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


class SkillFrontmatterLoader(yaml.SafeLoader):
    """Safe YAML 1.2-style loader that rejects duplicate mapping keys."""


SkillFrontmatterLoader.yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)
for first_character, resolvers in tuple(SkillFrontmatterLoader.yaml_implicit_resolvers.items()):
    SkillFrontmatterLoader.yaml_implicit_resolvers[first_character] = [
        (tag, pattern)
        for tag, pattern in resolvers
        if tag not in {"tag:yaml.org,2002:bool", "tag:yaml.org,2002:timestamp"}
    ]
SkillFrontmatterLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
    list("tTfF"),
)


def _construct_unique_mapping(loader: SkillFrontmatterLoader, node: MappingNode, deep: bool = False):
    seen: set[str] = set()
    for key_node, _ in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            continue
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ConstructorError(
                "while constructing a frontmatter mapping",
                node.start_mark,
                "frontmatter mapping keys must be strings",
                key_node.start_mark,
            )
        if key in seen:
            raise ConstructorError(
                "while constructing a frontmatter mapping",
                node.start_mark,
                f"duplicate frontmatter key {key!r}",
                key_node.start_mark,
            )
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


SkillFrontmatterLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)
REPRESENTATIVE_NAMES = (
    "requirements-analysis",
    "functional-testing",
    "api-testing",
    "performance-testing",
    "ai-agent-testing",
    "release-testing-workflow",
    "skill-change-verification",
)


@dataclass(frozen=True)
class Finding:
    category: str
    kind: str
    skill: str
    source: str
    detail: str


@dataclass(frozen=True)
class SkillRecord:
    language: str
    section: str
    directory: Path

    @property
    def name(self) -> str:
        return self.directory.name


def discover_skill_dirs(skills_root: Path) -> list[SkillRecord]:
    """Discover direct leaf Skills under the supported language sections."""

    records: list[SkillRecord] = []
    if not skills_root.is_dir():
        return records
    for language in LANGUAGES:
        for section in SECTIONS:
            category = skills_root / language / section
            if not category.is_dir():
                continue
            for directory in sorted(category.iterdir()):
                if not directory.is_dir() or directory.is_symlink() or directory.name.endswith("-workspace"):
                    continue
                records.append(SkillRecord(language, section, directory.resolve()))
    return records


def parse_frontmatter(skill_md: Path) -> tuple[dict[str, str], str | None]:
    """Return frontmatter metadata and a deterministic parse error, if present."""

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "frontmatter must start with ---"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, "frontmatter closing --- is missing"

    try:
        document = yaml.load("\n".join(lines[1:end]), Loader=SkillFrontmatterLoader)
    except yaml.YAMLError as exc:
        problem = getattr(exc, "problem", None) or str(exc).splitlines()[0]
        mark = getattr(exc, "problem_mark", None)
        location = f" at line {mark.line + 2}" if mark else ""
        return {}, f"invalid YAML frontmatter{location}: {problem}"
    if not isinstance(document, dict):
        return {}, "frontmatter must be a YAML mapping"

    values: dict[str, str] = {}
    for key in ("name", "description", "license", "compatibility"):
        if key in document:
            value = document[key]
            if not isinstance(value, str):
                return {}, f"frontmatter field {key!r} must be a string"
            values[key] = value

    if "metadata" in document:
        metadata = document["metadata"]
        if not isinstance(metadata, dict):
            return {}, "frontmatter field 'metadata' must be a mapping"
        for key, value in metadata.items():
            if not isinstance(key, str):
                return {}, "frontmatter metadata keys must be strings"
            if not isinstance(value, str):
                return {}, f"frontmatter field 'metadata.{key}' must be a string"
            values[f"metadata.{key}"] = value
    return values, None


def _relative(path: Path, base: Path) -> str:
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except ValueError:
        return str(path.resolve())


def _format_skill(record: SkillRecord, skills_root: Path) -> str:
    return _relative(record.directory, skills_root)


def scan(skills_root: Path) -> list[Finding]:
    skills_root = skills_root.resolve()
    records = discover_skill_dirs(skills_root)
    findings: list[Finding] = []

    if not skills_root.is_dir():
        findings.append(
            Finding(
                "DISCOVERY",
                "missing-skills-root",
                "skills",
                str(skills_root),
                "skills root is missing",
            )
        )
        return findings
    if not records:
        findings.append(
            Finding(
                "DISCOVERY",
                "empty-skills-root",
                "skills",
                str(skills_root),
                "skills root contains no supported leaf Skills",
            )
        )

    names_by_language: dict[str, dict[str, list[SkillRecord]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        names_by_language[record.language][record.name].append(record)

    for language, names in names_by_language.items():
        for name, duplicates in names.items():
            if len(duplicates) < 2:
                continue
            locations = ", ".join(_format_skill(item, skills_root) for item in duplicates)
            for record in duplicates:
                findings.append(
                    Finding(
                        "BILINGUAL",
                        "duplicate-name",
                        _format_skill(record, skills_root),
                        str(record.directory / "SKILL.md"),
                        f"duplicate canonical name '{name}' within {language}: {locations}",
                    )
                )

    names_by_language_set = {language: set(names) for language, names in names_by_language.items()}
    en_names = names_by_language_set.get("en", set())
    zh_names = names_by_language_set.get("zh", set())
    for name in sorted(en_names - zh_names):
        findings.append(
            Finding(
                "BILINGUAL",
                "missing-zh-name",
                f"en/{name}",
                str(skills_root / "zh"),
                f"canonical name '{name}' exists in en but not zh",
            )
        )
    for name in sorted(zh_names - en_names):
        findings.append(
            Finding(
                "BILINGUAL",
                "missing-en-name",
                f"zh/{name}",
                str(skills_root / "en"),
                f"canonical name '{name}' exists in zh but not en",
            )
        )

    for representative in REPRESENTATIVE_NAMES:
        if representative not in en_names:
            findings.append(
                Finding(
                    "DISCOVERY",
                    "missing-representative",
                    representative,
                    str(skills_root / "en"),
                    f"representative English Skill '{representative}' is missing",
                )
            )

    for record in records:
        skill_label = _format_skill(record, skills_root)
        skill_md = record.directory / "SKILL.md"
        if not skill_md.exists():
            findings.append(
                Finding("CONTRACT", "missing-skill-md", skill_label, str(skill_md), "SKILL.md is missing")
            )
            continue

        metadata, parse_error = parse_frontmatter(skill_md)
        if parse_error:
            findings.append(Finding("CONTRACT", "frontmatter", skill_label, str(skill_md), parse_error))
            continue

        name = metadata.get("name", "").strip()
        description = metadata.get("description", "").strip()
        if not name:
            findings.append(Finding("CONTRACT", "missing-name", skill_label, str(skill_md), "frontmatter name is missing"))
        elif not CANONICAL_NAME_RE.fullmatch(name):
            findings.append(Finding("CONTRACT", "invalid-name", skill_label, str(skill_md), f"invalid canonical name: {name!r}"))
        elif name != record.name:
            findings.append(
                Finding(
                    "CONTRACT",
                    "name-directory-mismatch",
                    skill_label,
                    str(skill_md),
                    f"frontmatter name {name!r} != directory {record.name!r}",
                )
            )
        if not description:
            findings.append(Finding("CONTRACT", "missing-description", skill_label, str(skill_md), "frontmatter description is empty"))
        elif len(description) > 1024:
            findings.append(
                Finding(
                    "CONTRACT",
                    "description-too-long",
                    skill_label,
                    str(skill_md),
                    f"description is {len(description)} characters; maximum is 1024",
                )
            )

        if not metadata.get("license", "").strip():
            findings.append(Finding("CONTRACT", "missing-license", skill_label, str(skill_md), "frontmatter license is missing"))

        version = metadata.get("metadata.version", "")
        if not SEMVER_RE.fullmatch(version):
            findings.append(Finding("CONTRACT", "invalid-metadata-version", skill_label, str(skill_md), "metadata.version must be a semantic version such as 1.0.0"))

        if "metadata.compatibility" not in metadata:
            findings.append(Finding("CONTRACT", "invalid-metadata-compatibility", skill_label, str(skill_md), 'metadata.compatibility must be a string; use "" when unknown'))

        for field in ("author", "source", "license-url"):
            value = metadata.get(f"metadata.{field}", "").strip()
            if not value:
                findings.append(Finding("CONTRACT", f"missing-metadata-{field}", skill_label, str(skill_md), f"metadata.{field} is missing"))
            elif field in {"source", "license-url"} and not re.fullmatch(r"https?://[^\s/]+\S*", value):
                findings.append(Finding("CONTRACT", f"invalid-metadata-{field}", skill_label, str(skill_md), f"metadata.{field} must be an HTTP(S) URL"))

        expected_language = "zh-CN" if record.language == "zh" else "en"
        for field, expected in (("language", expected_language), ("category", record.section)):
            if metadata.get(f"metadata.{field}") != expected:
                findings.append(Finding("CONTRACT", f"invalid-metadata-{field}", skill_label, str(skill_md), f"metadata.{field} must match the package: {expected}"))

    return findings


def _report_payload(skills_root: Path, findings: list[Finding], records_count: int) -> dict[str, object]:
    categories = ("CONTRACT", "BILINGUAL", "DISCOVERY")
    by_category = {category: sum(1 for item in findings if item.category == category) for category in categories}
    return {
        "summary": {
            "skills_root": str(skills_root.resolve()),
            "skills_scanned": records_count,
            "findings": len(findings),
            "by_category": by_category,
        },
        "findings": [asdict(item) for item in findings],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Skills CLI compatibility for this repository.")
    parser.add_argument("--skills-root", default="skills", help="Root containing en/ and zh/ Skill trees")
    parser.add_argument("--report-json", help="Write a JSON report")
    parser.add_argument("--report-md", help="Write a Markdown report")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit 2 when findings exist")
    args = parser.parse_args()

    skills_root = Path(args.skills_root).resolve()
    records = discover_skill_dirs(skills_root)
    findings = scan(skills_root)
    payload = _report_payload(skills_root, findings, len(records))

    if args.report_json:
        output = Path(args.report_json)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.report_md:
        output = Path(args.report_md)
        output.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Skills CLI Compatibility Report",
            "",
            f"- Skills scanned: **{len(records)}**",
            f"- Findings: **{len(findings)}**",
            "",
            "## Findings",
        ]
        lines.extend(
            f"- [{item.category}] `{item.kind}` `{item.skill}` — {item.detail}"
            for item in findings[:500]
        )
        if not findings:
            lines.append("No findings.")
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"skills_scanned={len(records)}")
    print(f"findings={len(findings)}")
    for item in findings[:500]:
        print(f"[{item.category}] {item.kind}: {item.skill}: {item.detail}")
    if len(findings) > 500:
        print(f"[REPORT] output truncated; {len(findings) - 500} additional finding(s) are in the report file when requested")
    return 2 if args.fail_on_findings and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
