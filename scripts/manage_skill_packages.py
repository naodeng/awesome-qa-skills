#!/usr/bin/env python3
"""Package, safely uninstall, and audit standalone Skill installs."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NAME_RE = re.compile(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", re.MULTILINE)
SECTIONS = ("testing-types", "testing-workflows", "skill-engineering")
IGNORED_PARTS = {"__pycache__", ".git"}


def read_skill_name(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_file}: SKILL.md frontmatter is missing")
    frontmatter = text.split("\n---", 1)[0]
    match = NAME_RE.search(frontmatter)
    if not match:
        raise ValueError(f"{skill_file}: canonical name field is missing or invalid")
    return match.group(1)


def package_skill(skill_dir: Path, output: Path) -> None:
    source = skill_dir.resolve(strict=True)
    if not source.is_dir():
        raise ValueError("--skill-dir must point to a Skill directory")
    if output.resolve(strict=False).is_relative_to(source):
        raise ValueError("--output must be outside the Skill directory")
    name = read_skill_name(source / "SKILL.md")
    if name != source.name or not SLUG_RE.fullmatch(name):
        raise ValueError(f"SKILL.md name {name!r} must match directory name {source.name!r}")
    for relative in ("agents/openai.yaml", "prompts", "evals/eval.yaml"):
        if not (source / relative).exists():
            raise ValueError(f"required standalone artifact is missing: {relative}")

    files: list[tuple[Path, str]] = []
    for path in sorted(source.rglob("*")):
        if any(part in IGNORED_PARTS for part in path.relative_to(source).parts):
            continue
        if path.name == ".DS_Store":
            continue
        if path.is_symlink():
            raise ValueError(f"symbolic links are not allowed in a standalone package: {path.relative_to(source)}")
        if path.is_file():
            relative = path.relative_to(source).as_posix()
            files.append((path, relative))
    if not any(relative == "SKILL.md" for _, relative in files):
        raise ValueError("SKILL.md is required")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            archive.write(path, relative)


def uninstall_skill(install_root: Path, skill: str, apply: bool) -> str:
    if not SLUG_RE.fullmatch(skill):
        raise ValueError("--skill must be a canonical lowercase slug")
    if install_root.is_symlink():
        raise ValueError("--install-root cannot be a symbolic link")
    root = install_root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("--install-root must be a directory")
    target = root / skill
    if target.is_symlink():
        raise ValueError("refusing to uninstall a symbolic link")
    if not target.exists() or not target.is_dir():
        raise ValueError(f"installed Skill directory not found: {target}")
    if target.parent != root or not (target / "SKILL.md").is_file():
        raise ValueError("target must be one Skill package directly inside --install-root")
    if not apply:
        return f"DRY_RUN: would remove {target}"
    shutil.rmtree(target)
    return f"REMOVED: {target}"


def repository_slugs(repo_root: Path) -> set[str]:
    slugs: set[str] = set()
    for language in ("zh", "en"):
        for section in SECTIONS:
            directory = repo_root / "skills" / language / section
            if directory.is_dir():
                slugs.update(
                    path.name for path in directory.iterdir()
                    if path.is_dir() and (path / "SKILL.md").is_file()
                )
    return slugs


def find_residue(install_root: Path, repo_root: Path) -> list[dict[str, str]]:
    known = repository_slugs(repo_root)
    if not install_root.exists():
        return []
    if install_root.is_symlink() or not install_root.is_dir():
        raise ValueError("--install-root must be a real directory")
    findings: list[dict[str, str]] = []
    root = install_root.resolve(strict=True)
    package_dirs: list[Path] = []
    pending = [root]
    while pending:
        directory = pending.pop()
        for child in sorted(directory.iterdir(), reverse=True):
            if child.is_symlink() or not child.is_dir():
                continue
            manifest = child / "SKILL.md"
            if manifest.is_file() or manifest.is_symlink():
                package_dirs.append(child)
            else:
                pending.append(child)

    for package in sorted(package_dirs):
        relative = package.relative_to(root).as_posix()
        slug = package.name
        if slug.endswith("-en"):
            findings.append({"path": relative, "kind": "legacy-language-suffix"})
        if slug not in known:
            findings.append({"path": relative, "kind": "not-in-repository"})
        try:
            if (package / "SKILL.md").is_symlink():
                raise ValueError("SKILL.md cannot be a symbolic link")
            declared = read_skill_name(package / "SKILL.md")
        except (OSError, ValueError):
            findings.append({"path": relative, "kind": "invalid-skill-manifest"})
        else:
            if declared != slug:
                findings.append({"path": relative, "kind": "manifest-directory-mismatch"})
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    pack_parser = subparsers.add_parser("pack", help="create an optional standalone Skill ZIP")
    pack_parser.add_argument("--skill-dir", type=Path, required=True)
    pack_parser.add_argument("--output", type=Path, required=True)

    uninstall_parser = subparsers.add_parser("uninstall", help="preview or remove one installed Skill")
    uninstall_parser.add_argument("--install-root", type=Path, required=True)
    uninstall_parser.add_argument("--skill", required=True)
    uninstall_parser.add_argument("--apply", action="store_true", help="perform deletion; default is preview only")

    residue_parser = subparsers.add_parser("check-residue", help="read-only scan for old or unknown Skill installs")
    residue_parser.add_argument("--install-root", type=Path, required=True)
    residue_parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    residue_parser.add_argument("--json", action="store_true", help="emit machine-readable findings")

    args = parser.parse_args(argv)
    try:
        if args.command == "pack":
            package_skill(args.skill_dir, args.output)
            print(f"PACKAGED: {args.output.resolve()}")
        elif args.command == "uninstall":
            print(uninstall_skill(args.install_root, args.skill, args.apply))
        else:
            findings = find_residue(args.install_root, args.repo_root.resolve(strict=True))
            if args.json:
                print(json.dumps(findings, ensure_ascii=False, indent=2))
            else:
                print(f"findings={len(findings)}")
                for finding in findings:
                    print(f"{finding['kind']}: {finding['path']}")
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
