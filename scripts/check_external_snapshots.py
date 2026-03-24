#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


HASHY = re.compile(r".*__[0-9a-f]{8,40}\.md$")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check _external snapshot hygiene.")
    parser.add_argument("--skills-root", default="skills")
    parser.add_argument("--max-per-skill", type=int, default=5)
    args = parser.parse_args()

    root = Path(args.skills_root).resolve()
    bad_names = []
    over_limit = []

    for ext in root.rglob("references/_external"):
        if not ext.is_dir():
            continue
        files = [p for p in ext.iterdir() if p.is_file() and p.suffix == ".md"]
        if len(files) > args.max_per_skill:
            over_limit.append((str(ext), len(files)))
        for f in files:
            if HASHY.match(f.name) or f.name.startswith("dir_proxy__"):
                bad_names.append(str(f))

    print(f"snapshot_dirs_checked={sum(1 for _ in root.rglob('references/_external'))}")
    print(f"over_limit={len(over_limit)}")
    print(f"bad_names={len(bad_names)}")
    for path, count in over_limit[:50]:
        print(f"OVER_LIMIT {path} {count}")
    for path in bad_names[:50]:
        print(f"BAD_NAME {path}")

    return 2 if over_limit or bad_names else 0


if __name__ == "__main__":
    raise SystemExit(main())
