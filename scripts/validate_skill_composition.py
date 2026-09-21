#!/usr/bin/env python3
"""Validate the repository's JSON-compatible Skill Composition manifest.

The manifest is governance input, not an installation manifest.  This module
keeps parsing and validation in one place so generators and quality gates make
the same decisions without adding a YAML dependency or a runtime Skill
dependency.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


MANIFEST_RELATIVE_PATH = Path("docs/governance/skill-composition.yaml")
ALLOWED_RELATION_TYPES = frozenset(
    {"precedes", "recommended_with", "alternative_to", "conflicts_with"}
)
REQUIRED_ROUTE_FIELDS = ("label", "intent", "phase", "not_for", "handoff", "primary", "optional")
LOCALIZED_FIELDS = ("label", "intent", "phase", "not_for", "handoff")
LANGUAGES = ("zh", "en")
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
INTERNAL_SKILL_PATH_PATTERN = re.compile(
    r"(?:skills/(?:zh|en)/[^\s)\]>]+|(?:\.\./)+[^\s)\]>]*(?:SKILL\.md|(?:prompts|agents|evals)/))"
)


def load_manifest(path: Path) -> dict[str, Any]:
    """Load a JSON-compatible YAML file using only the standard library."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"manifest file is missing: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"manifest must be JSON-compatible YAML: {error}") from error
    if not isinstance(value, dict):
        raise ValueError("manifest root must be an object")
    return value


def _skill_dirs(repo_root: Path, language: str) -> dict[str, list[Path]]:
    root = repo_root / "skills" / language
    result: dict[str, list[Path]] = {}
    if not root.is_dir():
        return result
    for section in root.iterdir():
        if not section.is_dir():
            continue
        for skill_dir in section.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
                result.setdefault(skill_dir.name, []).append(skill_dir)
    return result


def bilingual_skill_slugs(repo_root: Path) -> set[str]:
    """Return canonical Skill slugs that have a source package in both languages."""
    zh = set(_skill_dirs(repo_root, "zh"))
    en = set(_skill_dirs(repo_root, "en"))
    return zh & en


def route_targets(manifest: dict[str, Any]) -> set[str]:
    """Return all primary and optional route targets represented as slugs."""
    targets: set[str] = set()
    for route in manifest.get("routes", []):
        if not isinstance(route, dict):
            continue
        for field in ("primary", "optional"):
            value = route.get(field)
            if isinstance(value, str) and value:
                targets.add(value)
    return targets


def _add(errors: list[str], location: str, reason: str) -> None:
    errors.append(f"{location}: {reason}")


def _validate_localized(
    value: Any,
    location: str,
    errors: list[str],
    *,
    list_value: bool = False,
) -> None:
    if not isinstance(value, dict):
        _add(errors, location, "must provide exactly zh and en language values")
        return
    keys = set(value)
    if keys != set(LANGUAGES):
        unknown = sorted(keys - set(LANGUAGES))
        missing = sorted(set(LANGUAGES) - keys)
        if unknown:
            _add(errors, location, "unknown language=" + ",".join(unknown))
        if missing:
            for language in missing:
                _add(errors, f"{location}.{language}", "is required")
    for language in LANGUAGES:
        if language not in value:
            continue
        localized = value[language]
        if list_value:
            if not isinstance(localized, list) or not localized or not all(
                isinstance(item, str) and item.strip() for item in localized
            ):
                _add(errors, f"{location}.{language}", "must be a non-empty list of strings")
        elif not isinstance(localized, str) or not localized.strip():
            _add(errors, f"{location}.{language}", "must be a non-empty string")


def _walk_strings(value: Any, location: str):
    if isinstance(value, str):
        yield location, value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from _walk_strings(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk_strings(child, f"{location}[{index}]")


def validate_manifest(manifest: dict[str, Any], repo_root: Path) -> list[str]:
    """Return actionable contract errors; an empty list means valid."""
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest: root must be an object"]

    if manifest.get("format") != "json-compatible-yaml":
        _add(errors, "format", "must be json-compatible-yaml")
    if manifest.get("version") != 1:
        _add(errors, "version", "must be integer 1")
    for forbidden in ("dependencies", "install_requires", "requires"):
        if forbidden in manifest:
            _add(errors, forbidden, "install dependencies are not allowed in a Composition manifest")

    routes = manifest.get("routes")
    if not isinstance(routes, list) or not routes:
        _add(errors, "routes", "must be a non-empty list")
        routes = []
    route_ids: set[str] = set()
    bilingual = bilingual_skill_slugs(repo_root)
    for index, route in enumerate(routes):
        location = f"routes[{index}]"
        if not isinstance(route, dict):
            _add(errors, location, "must be an object")
            continue
        route_id = route.get("id")
        route_label = route_id if isinstance(route_id, str) and route_id else f"routes[{index}]"
        if not isinstance(route_id, str) or not SLUG_PATTERN.fullmatch(route_id):
            _add(errors, f"{location}.id", "must be a lowercase canonical slug")
        elif route_id in route_ids:
            _add(errors, f"{location}.id", f"duplicate route ID {route_id}")
        else:
            route_ids.add(route_id)

        for field in REQUIRED_ROUTE_FIELDS:
            if field not in route:
                _add(errors, f"{route_label}.{field}", "is required")
        for field in LOCALIZED_FIELDS:
            if field in route:
                _validate_localized(
                    route[field],
                    f"{route_label}.{field}",
                    errors,
                    list_value=field == "not_for",
                )

        route_target_fields: list[tuple[str, str]] = []
        primary = route.get("primary")
        if not isinstance(primary, str) or not primary.strip():
            _add(errors, f"{route_label}.primary", "must select exactly one Skill")
        else:
            route_target_fields.append(("primary", primary))
        optional = route.get("optional")
        if optional is not None:
            if not isinstance(optional, str):
                _add(errors, f"{route_label}.optional", "must select at most one Skill")
            elif optional.strip():
                route_target_fields.append(("optional", optional))

        for field, target in route_target_fields:
            if not SLUG_PATTERN.fullmatch(target):
                _add(errors, f"{route_label}.{field}", f"invalid Skill slug {target!r}")
            elif target not in bilingual:
                _add(errors, f"{route_label}.{field}", f"unknown bilingual target Skill {target!r}")

    relations = manifest.get("relations")
    if not isinstance(relations, list):
        _add(errors, "relations", "must be a list")
        relations = []
    relation_directions: set[tuple[str, str]] = set()
    for index, relation in enumerate(relations):
        location = f"relations[{index}]"
        if not isinstance(relation, dict):
            _add(errors, location, "must be an object")
            continue
        source = relation.get("from")
        target = relation.get("to")
        relation_type = relation.get("type")
        for field, value in (("from", source), ("to", target)):
            if not isinstance(value, str) or not SLUG_PATTERN.fullmatch(value):
                _add(errors, f"{location}.{field}", "must be a canonical Skill slug")
            elif value not in bilingual:
                _add(errors, f"{location}.{field}", f"unknown bilingual target Skill {value!r}")
        if relation_type not in ALLOWED_RELATION_TYPES:
            _add(
                errors,
                f"{location}.type",
                "must use an allowed navigation relation: " + ", ".join(sorted(ALLOWED_RELATION_TYPES)),
            )
        if isinstance(source, str) and isinstance(target, str):
            if source == target:
                _add(errors, location, "relation cannot self-reference a Skill")
            direction = (source, target)
            if direction in relation_directions:
                _add(errors, location, f"duplicate relation direction {source}->{target}")
            relation_directions.add(direction)

    for location, value in _walk_strings(manifest, "manifest"):
        if INTERNAL_SKILL_PATH_PATTERN.search(value):
            _add(errors, location, "cross-Skill internal Skill path is not allowed")

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--manifest", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    manifest_path = (args.manifest or repo_root / MANIFEST_RELATIVE_PATH).resolve()
    try:
        manifest = load_manifest(manifest_path)
    except ValueError as error:
        print(f"manifest_error={error}")
        return 1
    errors = validate_manifest(manifest, repo_root)
    if errors:
        print("\n".join(f"composition_error={error}" for error in errors))
        return 1
    summary = {
        "manifest": str(manifest_path.relative_to(repo_root)) if manifest_path.is_relative_to(repo_root) else str(manifest_path),
        "routes": len(manifest["routes"]),
        "relations": len(manifest["relations"]),
        "target_skills": len(route_targets(manifest)),
    }
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
