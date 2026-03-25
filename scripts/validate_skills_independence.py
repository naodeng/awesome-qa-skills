#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class Finding:
    kind: str
    source: str
    link: str
    resolved: str
    skill_root: str


def _skill_identity(path: Path) -> tuple[str, str] | None:
    parts = path.parts
    if "testing-types" in parts:
        i = parts.index("testing-types")
        if i + 1 < len(parts):
            return ("testing-types", parts[i + 1])
    if "testing-workflows" in parts:
        i = parts.index("testing-workflows")
        if i + 1 < len(parts):
            return ("testing-workflows", parts[i + 1])
    return None


def _is_allowed_cross_language_prompt_link(source: Path, target: Path) -> bool:
    # Allow direct zh/en counterpart links for prompt files only.
    if source.parent.name != "prompts" or target.parent.name != "prompts":
        return False
    sid = _skill_identity(source)
    tid = _skill_identity(target)
    if not sid or not tid:
        return False
    if sid[0] != tid[0]:
        return False
    s_name = sid[1]
    t_name = tid[1]
    # New canonical layout: same skill name across zh/en folders.
    if s_name == t_name:
        return True
    # Legacy layout: zh/en distinguished by -en suffix.
    if s_name.endswith("-en"):
        return s_name[:-3] == t_name
    if t_name.endswith("-en"):
        return t_name[:-3] == s_name
    return False


def iter_skill_markdown(skills_root: Path):
    canonical_bases = [
        skills_root / "zh" / "testing-types",
        skills_root / "zh" / "testing-workflows",
        skills_root / "en" / "testing-types",
        skills_root / "en" / "testing-workflows",
    ]
    if any(b.exists() for b in canonical_bases):
        bases = canonical_bases
    else:
        bases = [skills_root / "testing-types", skills_root / "testing-workflows"]

    for base in bases:
        if not base.exists():
            continue
        for skill_dir in sorted([p for p in base.iterdir() if p.is_dir() and not p.is_symlink()]):
            for md in skill_dir.rglob("*.md"):
                if "node_modules" in md.parts:
                    continue
                yield skill_dir, md


def scan(skills_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for skill_root, md in iter_skill_markdown(skills_root):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            raw = m.group(2).strip()
            if raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            link = raw.split("#", 1)[0].split("?", 1)[0]
            if not link:
                continue
            target = (md.parent / link).resolve()
            if not target.exists():
                findings.append(
                    Finding(
                        kind="broken",
                        source=str(md),
                        link=raw,
                        resolved=str(target),
                        skill_root=str(skill_root),
                    )
                )
                continue
            if not str(target).startswith(str(skill_root.resolve())):
                if _is_allowed_cross_language_prompt_link(md, target):
                    continue
                findings.append(
                    Finding(
                        kind="external",
                        source=str(md),
                        link=raw,
                        resolved=str(target),
                        skill_root=str(skill_root),
                    )
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate skills independence and link integrity.")
    parser.add_argument("--skills-root", default="skills", help="Skills root directory")
    parser.add_argument("--report-json", help="Write JSON report path")
    parser.add_argument("--report-md", help="Write Markdown report path")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit non-zero when findings exist")
    args = parser.parse_args()

    skills_root = Path(args.skills_root).resolve()
    findings = scan(skills_root)
    broken = [f for f in findings if f.kind == "broken"]
    external = [f for f in findings if f.kind == "external"]

    summary = {
        "skills_root": str(skills_root),
        "broken": len(broken),
        "external": len(external),
        "total_findings": len(findings),
    }

    if args.report_json:
        payload = {
            "summary": summary,
            "findings": [asdict(f) for f in findings],
        }
        out = Path(args.report_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.report_md:
        lines = [
            "# Skills Independence Validation Report",
            "",
            f"- Skills root: `{summary['skills_root']}`",
            f"- Broken links: **{summary['broken']}**",
            f"- External references: **{summary['external']}**",
            f"- Total findings: **{summary['total_findings']}**",
            "",
            "## Findings",
        ]
        if not findings:
            lines.append("No issues found.")
        else:
            for f in findings[:300]:
                lines.append(
                    f"- `{f.kind}`: `{f.source}` -> `{f.link}` (resolved: `{f.resolved}`)"
                )
        out = Path(args.report_md)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"broken={summary['broken']}")
    print(f"external={summary['external']}")
    print(f"total_findings={summary['total_findings']}")
    if args.fail_on_findings and summary["total_findings"] > 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
