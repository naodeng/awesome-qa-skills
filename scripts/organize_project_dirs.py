#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CANON_EN = SKILLS_ROOT / "en"
CANON_ZH = SKILLS_ROOT / "zh"


def ensure_canonical_layout() -> None:
    for lang in (CANON_EN, CANON_ZH):
        (lang / "testing-types").mkdir(parents=True, exist_ok=True)
        (lang / "testing-workflows").mkdir(parents=True, exist_ok=True)


def sync_canonical() -> tuple[int, int]:
    ensure_canonical_layout()
    # No external source to sync from.
    return (0, 0)


def cleanup_en_suffix_aliases() -> int:
    removed = 0
    for section in ("testing-types", "testing-workflows"):
        for root in (CANON_ZH / section, CANON_EN / section):
            if not root.exists():
                continue
            for p in sorted(root.iterdir()):
                if p.name.endswith("-en") and p.is_symlink():
                    p.unlink()
                    removed += 1
    return removed


def validate_structure() -> list[str]:
    issues: list[str] = []
    for path in (
        CANON_ZH / "testing-types",
        CANON_ZH / "testing-workflows",
        CANON_EN / "testing-types",
        CANON_EN / "testing-workflows",
    ):
        if not path.exists():
            issues.append(f"missing {path.relative_to(ROOT)}")

    # Check aliases resolve
    for section in ("testing-types", "testing-workflows"):
        for root in (CANON_ZH / section, CANON_EN / section):
            if not root.exists():
                continue
            for p in sorted([x for x in root.iterdir() if x.is_symlink()]):
                if not p.exists():
                    issues.append(f"broken symlink: {p.relative_to(ROOT)}")

    for lang_root, lang in ((CANON_ZH, "zh"), (CANON_EN, "en")):
        for section in ("testing-types", "testing-workflows"):
            base = lang_root / section
            if not base.exists():
                continue
            for skill_dir in sorted([p for p in base.iterdir() if p.is_dir() and not p.is_symlink()]):
                prompts = skill_dir / "prompts"
                if not prompts.exists():
                    continue
                if not any(prompts.glob("*.md")):
                    issues.append(f"missing prompt files: {prompts.relative_to(ROOT)}")
                if (prompts / "zh").exists() or (prompts / "en").exists():
                    issues.append(f"unexpected language prompt dir: {prompts.relative_to(ROOT)}")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Organize and optimize project skill directories.")
    parser.add_argument("--sync-canonical", action="store_true", help="Ensure canonical language directories exist")
    parser.add_argument("--rebuild-language-views", action="store_true", help="Cleanup legacy alias links")
    parser.add_argument("--check", action="store_true", help="Validate structure and return non-zero if issues found")
    args = parser.parse_args()

    do_sync = args.sync_canonical or not (args.sync_canonical or args.rebuild_language_views or args.check)
    do_rebuild = args.rebuild_language_views or not (args.sync_canonical or args.rebuild_language_views or args.check)
    do_check = args.check or not (args.sync_canonical or args.rebuild_language_views or args.check)

    if do_sync:
        copied_types, copied_workflows = sync_canonical()
        print(f"canonical_sync_copied_types={copied_types}")
        print(f"canonical_sync_copied_workflows={copied_workflows}")

    if do_rebuild:
        removed_aliases = cleanup_en_suffix_aliases()
        print(f"removed_legacy_en_suffix_aliases={removed_aliases}")

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
