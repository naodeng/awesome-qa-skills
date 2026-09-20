#!/usr/bin/env python3
"""Validate the small, stable Skills CLI distribution contract.

This checker intentionally stays independent of the Skills CLI and third-party
YAML packages. It validates the repository shape before the shell wrapper runs
the pinned CLI discovery and installation smoke.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path


SECTIONS = ("testing-types", "testing-workflows", "skill-engineering")
LANGUAGES = ("en", "zh")
CANONICAL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
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


def _unquote_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value) if value[0] == '"' else value[1:-1].replace("''", "'")
            return str(parsed)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def _parse_block_scalar(lines: list[str], start: int, end: int, folded: bool) -> tuple[str, int]:
    """Parse a small YAML block scalar without pulling in a YAML dependency."""

    raw_lines: list[str] = []
    index = start
    while index < end:
        line = lines[index]
        if line.strip() and not line[0].isspace():
            break
        raw_lines.append(line)
        index += 1

    non_empty_indents = [len(line) - len(line.lstrip()) for line in raw_lines if line.strip()]
    indent = min(non_empty_indents, default=0)
    values = [line[indent:] if line.strip() else "" for line in raw_lines]
    if not folded:
        return "\n".join(values).rstrip("\n"), index

    folded_lines: list[str] = []
    for value in values:
        if not value:
            folded_lines.append("\n")
        elif folded_lines and folded_lines[-1] != "\n":
            folded_lines.append(" ")
            folded_lines.append(value)
        else:
            folded_lines.append(value)
    return "".join(folded_lines).rstrip("\n"), index


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

    values: dict[str, str] = {}
    index = 1
    while index < end:
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        match = FRONTMATTER_KEY_RE.match(line)
        if not match:
            return {}, f"invalid frontmatter line: {line.strip()}"
        key, raw = match.groups()
        raw = (raw or "").strip()
        if raw.startswith(("|", ">")):
            values[key], index = _parse_block_scalar(lines, index + 1, end, raw.startswith(">"))
        else:
            values[key] = _unquote_scalar(raw)
            index += 1
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
