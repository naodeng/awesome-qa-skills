#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CORE_TYPES = SKILLS_ROOT / "testing-types"
CORE_WORKFLOWS = SKILLS_ROOT / "testing-workflows"
RELEASE_ZH = SKILLS_ROOT / "release" / "skills-zh"
RELEASE_EN = SKILLS_ROOT / "release" / "skills-en"
VIEW_ZH = SKILLS_ROOT / "skills-zh"
VIEW_EN = SKILLS_ROOT / "skills-en"


def copy_dir_if_exists(src: Path, dst: Path) -> int:
    copied = 0
    if not src.exists():
        return copied
    dst.mkdir(parents=True, exist_ok=True)
    for child in sorted([p for p in src.iterdir() if p.is_dir()]):
        target = dst / child.name
        if not target.exists():
            shutil.copytree(child, target)
            copied += 1
    return copied


def ensure_core_from_release() -> tuple[int, int]:
    CORE_TYPES.mkdir(parents=True, exist_ok=True)
    CORE_WORKFLOWS.mkdir(parents=True, exist_ok=True)

    copied_types = 0
    copied_workflows = 0
    copied_types += copy_dir_if_exists(RELEASE_ZH / "testing-types", CORE_TYPES)
    copied_workflows += copy_dir_if_exists(RELEASE_ZH / "testing-workflows", CORE_WORKFLOWS)
    copied_types += copy_dir_if_exists(RELEASE_EN / "testing-types", CORE_TYPES)
    copied_workflows += copy_dir_if_exists(RELEASE_EN / "testing-workflows", CORE_WORKFLOWS)
    return copied_types, copied_workflows


def safe_symlink(target_rel: Path, link_path: Path) -> None:
    if link_path.exists() or link_path.is_symlink():
        if link_path.is_dir() and not link_path.is_symlink():
            shutil.rmtree(link_path)
        else:
            link_path.unlink()
    try:
        link_path.symlink_to(target_rel)
    except FileExistsError:
        # Make operation idempotent even if a path appears between checks.
        if link_path.is_dir() and not link_path.is_symlink():
            shutil.rmtree(link_path)
        elif link_path.exists() or link_path.is_symlink():
            link_path.unlink()
        link_path.symlink_to(target_rel)


def rebuild_language_views() -> tuple[int, int]:
    # Create symlink view directories if missing
    for view in (VIEW_ZH, VIEW_EN):
        (view / "testing-types").mkdir(parents=True, exist_ok=True)
        (view / "testing-workflows").mkdir(parents=True, exist_ok=True)

    zh_count = 0
    en_count = 0

    # zh view: map non -en names directly
    for section in ("testing-types", "testing-workflows"):
        src_base = SKILLS_ROOT / section
        view_base = VIEW_ZH / section
        for s in sorted([p for p in src_base.iterdir() if p.is_dir() and not p.name.endswith("-en")]):
            rel_target = Path("..") / ".." / section / s.name
            safe_symlink(rel_target, view_base / s.name)
            zh_count += 1

    # en view: map *-en source to names without -en
    for section in ("testing-types", "testing-workflows"):
        src_base = SKILLS_ROOT / section
        view_base = VIEW_EN / section
        for s in sorted([p for p in src_base.iterdir() if p.is_dir() and p.name.endswith("-en")]):
            alias_name = s.name[:-3]
            rel_target = Path("..") / ".." / section / s.name
            safe_symlink(rel_target, view_base / alias_name)
            en_count += 1

    return zh_count, en_count


def validate_structure() -> list[str]:
    issues: list[str] = []
    if not CORE_TYPES.exists():
        issues.append("missing skills/testing-types")
    if not CORE_WORKFLOWS.exists():
        issues.append("missing skills/testing-workflows")

    # Check language view links resolve
    for view in (VIEW_ZH / "testing-types", VIEW_ZH / "testing-workflows", VIEW_EN / "testing-types", VIEW_EN / "testing-workflows"):
        if not view.exists():
            issues.append(f"missing {view.relative_to(ROOT)}")
            continue
        for p in sorted([x for x in view.iterdir() if x.is_symlink()]):
            if not p.exists():
                issues.append(f"broken symlink: {p.relative_to(ROOT)}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Organize and optimize project skill directories.")
    parser.add_argument(
        "--repair-core-from-release",
        action="store_true",
        help="Recover missing core skill dirs from skills/release if needed",
    )
    parser.add_argument(
        "--rebuild-language-views",
        action="store_true",
        help="Rebuild symlink views under skills/skills-zh and skills/skills-en",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate structure and return non-zero if issues found",
    )
    args = parser.parse_args()

    # default behavior: do all
    do_repair = args.repair_core_from_release or not (args.repair_core_from_release or args.rebuild_language_views or args.check)
    do_rebuild = args.rebuild_language_views or not (args.repair_core_from_release or args.rebuild_language_views or args.check)
    do_check = args.check or not (args.repair_core_from_release or args.rebuild_language_views or args.check)

    if do_repair:
        copied_types, copied_workflows = ensure_core_from_release()
        print(f"core_repair_copied_types={copied_types}")
        print(f"core_repair_copied_workflows={copied_workflows}")

    if do_rebuild:
        zh_count, en_count = rebuild_language_views()
        print(f"rebuilt_view_links_zh={zh_count}")
        print(f"rebuilt_view_links_en={en_count}")

    if do_check:
        issues = validate_structure()
        print(f"issues={len(issues)}")
        for i in issues[:200]:
            print(f"- {i}")
        if issues:
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
