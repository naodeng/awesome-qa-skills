#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def normalize_name(name: str) -> str:
    stem, ext = os.path.splitext(name)
    stem = stem.replace("__", "-")
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", stem).strip("-_.")
    if not stem:
        stem = "snapshot"
    if not ext:
        ext = ".md"
    return f"{stem}{ext}"


def ensure_localized_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    txt = src.read_text(encoding="utf-8", errors="ignore")
    if not txt.startswith("# Local Reference"):
        txt = (
            "# Local Reference\n\n"
            "This file is an in-skill formal reference migrated from `_external`.\n\n"
            f"Original file: `{src.name}`\n\n"
            "---\n\n"
            + txt
        )
    dst.write_text(txt, encoding="utf-8")


def main() -> int:
    updated_files = 0
    moved_refs = 0

    for section in ("testing-types", "testing-workflows"):
        base = SKILLS / section
        if not base.exists():
            continue
        for skill_root in [p for p in base.iterdir() if p.is_dir()]:
            ext_dir = skill_root / "references" / "_external"
            if not ext_dir.exists():
                continue

            # gather markdown files in this skill
            md_files = [p for p in skill_root.rglob("*.md") if "node_modules" not in p.parts]

            # find referenced external files in this skill
            refs: set[Path] = set()
            for md in md_files:
                txt = md.read_text(encoding="utf-8", errors="ignore")
                for m in LINK_RE.finditer(txt):
                    raw = m.group(2).strip().split("#", 1)[0].split("?", 1)[0]
                    if not raw:
                        continue
                    target = (md.parent / raw).resolve()
                    if ext_dir.resolve() in target.parents and target.is_file():
                        refs.add(target)

            # move referenced _external files into references/local
            mapping: dict[Path, Path] = {}
            local_dir = skill_root / "references" / "local"
            for src in sorted(refs):
                target_name = normalize_name(src.name)
                dst = local_dir / target_name
                n = 2
                while dst.exists() and dst.resolve() != src.resolve():
                    dst = local_dir / target_name.replace(".md", f"-{n}.md")
                    n += 1
                ensure_localized_file(src, dst)
                mapping[src] = dst
                moved_refs += 1

            # rewrite links in this skill
            for md in md_files:
                txt = md.read_text(encoding="utf-8", errors="ignore")
                orig = txt
                for src, dst in mapping.items():
                    rel_old = os.path.relpath(src, start=md.parent).replace("\\", "/")
                    rel_new = os.path.relpath(dst, start=md.parent).replace("\\", "/")
                    txt = txt.replace(f"]({rel_old})", f"]({rel_new})")
                if txt != orig:
                    md.write_text(txt, encoding="utf-8")
                    updated_files += 1

            # remove _external dir entirely
            if ext_dir.exists():
                shutil.rmtree(ext_dir)

    print(f"updated_files={updated_files}")
    print(f"moved_refs={moved_refs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
