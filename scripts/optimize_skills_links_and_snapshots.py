#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HASH_TAIL_RE = re.compile(r"__(?:[0-9a-f]{8,40})$")


def is_markdown(path: Path) -> bool:
    return path.suffix.lower() == ".md"


def rewrite_cross_language_prompt_links() -> int:
    changed = 0
    for p in SKILLS.rglob("*.md"):
        if "node_modules" in p.parts:
            continue
        if p.parent.name != "prompts":
            continue

        skill_dir = p.parent.parent.name
        txt = p.read_text(encoding="utf-8", errors="ignore")
        orig = txt

        def repl(m: re.Match[str]) -> str:
            label, raw = m.group(1), m.group(2).strip()
            if "_external/" not in raw:
                return m.group(0)
            # only recover cross-language pointer in prompt files
            if skill_dir.endswith("-en"):
                target_skill = skill_dir[:-3]
                current_name = p.name
                target_name = current_name.replace("_EN.md", ".md")
                target = f"../../{target_skill}/prompts/{target_name}"
                return f"[{label}]({target})"
            else:
                target_skill = f"{skill_dir}-en"
                current_name = p.name
                if current_name.endswith(".md") and not current_name.endswith("_EN.md"):
                    target_name = current_name[:-3] + "_EN.md"
                else:
                    target_name = current_name
                target = f"../../{target_skill}/prompts/{target_name}"
                return f"[{label}]({target})"

        txt = LINK_RE.sub(repl, txt)
        if txt != orig:
            p.write_text(txt, encoding="utf-8")
            changed += 1
    return changed


def readable_snapshot_name(old_file: Path, source_hint: str | None, index: int) -> str:
    if source_hint:
        norm = source_hint.strip().replace("`", "").replace("\\", "/")
        norm = norm.lstrip("/")
        base = re.sub(r"[^a-zA-Z0-9._/-]+", "-", norm)
        base = base.replace("/", "-").replace("..", "up")
    else:
        stem = old_file.stem
        core = HASH_TAIL_RE.sub("", stem)
        core = re.sub(r"[^a-zA-Z0-9._-]+", "-", core)
        base = core
    base = base.strip("-_.") or f"snapshot-{index}"
    if not base.endswith(".md"):
        base = f"{base}.md"
    if len(base) > 140:
        base = base[:136] + ".md"
    return base


def normalize_snapshot_file(path: Path, source_hint: str | None) -> None:
    txt = path.read_text(encoding="utf-8", errors="ignore")
    header = [
        "# Snapshot Reference",
        "",
        "This file is a localized snapshot for skill portability.",
    ]
    if source_hint:
        header.extend(["", f"Source: `{source_hint}`"])
    header.extend(["", "---", ""])

    # remove markdown links in snapshot body to avoid introducing dependency graph noise
    body = LINK_RE.sub(lambda m: f"{m.group(1)} ({m.group(2)})", txt)

    if body.startswith("# Snapshot Reference"):
        # already normalized
        path.write_text(body, encoding="utf-8")
        return
    path.write_text("\n".join(header) + body, encoding="utf-8")


def rename_external_snapshots() -> int:
    renamed = 0
    mapping: dict[Path, Path] = {}

    for ext_dir in SKILLS.rglob("references/_external"):
        if not ext_dir.is_dir():
            continue
        files = sorted([f for f in ext_dir.iterdir() if f.is_file() and is_markdown(f)])
        used = set()
        for i, f in enumerate(files, start=1):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            source_match = re.search(r"Original path:\s*`([^`]+)`", txt)
            source_hint = source_match.group(1) if source_match else None
            new_name = readable_snapshot_name(f, source_hint, i)
            candidate = ext_dir / new_name
            n = 2
            while candidate.exists() and candidate.resolve() != f.resolve():
                candidate = ext_dir / new_name.replace(".md", f"-{n}.md")
                n += 1
            normalize_snapshot_file(f, source_hint)
            if candidate != f:
                mapping[f] = candidate
                used.add(candidate.name)
            else:
                used.add(f.name)

    # apply renames
    for old, new in mapping.items():
        old.rename(new)
        renamed += 1

    if not mapping:
        return renamed

    # rewrite links to renamed files
    for md in SKILLS.rglob("*.md"):
        if "node_modules" in md.parts:
            continue
        txt = md.read_text(encoding="utf-8", errors="ignore")
        orig = txt
        for old, new in mapping.items():
            rel_old = os.path.relpath(old, start=md.parent).replace("\\", "/")
            rel_new = os.path.relpath(new, start=md.parent).replace("\\", "/")
            txt = txt.replace(f"]({rel_old})", f"]({rel_new})")
        if txt != orig:
            md.write_text(txt, encoding="utf-8")

    return renamed


def cleanup_unreferenced_external(max_keep: int = 5) -> tuple[int, list[str]]:
    removed = 0
    warnings: list[str] = []

    # collect references to _external files
    referenced: set[Path] = set()
    for md in SKILLS.rglob("*.md"):
        if "node_modules" in md.parts:
            continue
        txt = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(txt):
            raw = m.group(2).strip().split("#", 1)[0].split("?", 1)[0]
            if not raw:
                continue
            target = (md.parent / raw).resolve()
            if "/references/_external/" in str(target):
                referenced.add(target)

    for ext_dir in SKILLS.rglob("references/_external"):
        if not ext_dir.is_dir():
            continue
        files = sorted([f for f in ext_dir.iterdir() if f.is_file()])
        keep = [f for f in files if f.resolve() in referenced]
        for f in files:
            if f.resolve() not in referenced:
                f.unlink(missing_ok=True)
                removed += 1
        if len(keep) > max_keep:
            warnings.append(f"{ext_dir}: referenced snapshots {len(keep)} > limit {max_keep}")
        # remove empty dir
        if not any(ext_dir.iterdir()):
            ext_dir.rmdir()

    return removed, warnings


def main() -> None:
    c1 = rewrite_cross_language_prompt_links()
    c2 = rename_external_snapshots()
    removed, warnings = cleanup_unreferenced_external(max_keep=5)

    print(f"rewrote_prompt_links={c1}")
    print(f"renamed_snapshots={c2}")
    print(f"removed_unreferenced_snapshots={removed}")
    if warnings:
        print("snapshot_warnings:")
        for w in warnings:
            print(f"  - {w}")


if __name__ == "__main__":
    main()
