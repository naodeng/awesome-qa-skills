#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class Finding:
    severity: str
    kind: str
    skill: str
    file: str
    detail: str


def discover_skill_dirs(repo_root: Path) -> list[Path]:
    bases = [
        repo_root / "skills" / "zh" / "testing-types",
        repo_root / "skills" / "zh" / "testing-workflows",
        repo_root / "skills" / "en" / "testing-types",
        repo_root / "skills" / "en" / "testing-workflows",
    ]
    result: list[Path] = []
    for b in bases:
        if not b.exists():
            continue
        for d in sorted([p for p in b.iterdir() if p.is_dir() and not p.is_symlink()]):
            result.append(d.resolve())
    # de-dup while preserving order
    seen: set[str] = set()
    deduped: list[Path] = []
    for p in result:
        key = str(p)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(p)
    return deduped


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
    # Keep existing policy: allow direct zh/en counterpart links for prompt files.
    if source.parent.name != "prompts" or target.parent.name != "prompts":
        return False
    sid = _skill_identity(source)
    tid = _skill_identity(target)
    if not sid or not tid or sid[0] != tid[0]:
        return False
    s_name = sid[1]
    t_name = tid[1]
    # New canonical layout: same skill name under zh/en folders.
    if s_name == t_name:
        return True
    # Legacy layout: language split by -en suffix.
    if s_name.endswith("-en"):
        return s_name[:-3] == t_name
    if t_name.endswith("-en"):
        return t_name[:-3] == s_name
    return False


def scan_skill(skill_dir: Path, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    rel_skill = str(skill_dir.relative_to(repo_root))

    # Completeness checks
    if not (skill_dir / "SKILL.md").exists():
        findings.append(Finding("high", "missing", rel_skill, rel_skill, "Missing SKILL.md"))

    prompts = skill_dir / "prompts"
    if not prompts.exists() or not any(prompts.glob("*.md")):
        findings.append(Finding("high", "missing", rel_skill, rel_skill, "Missing prompts/*.md"))
    if (prompts / "zh").exists() or (prompts / "en").exists():
        findings.append(
            Finding(
                "medium",
                "layout",
                rel_skill,
                rel_skill,
                "prompts/ should not contain zh/ or en/ subdirectories",
            )
        )

    scripts = skill_dir / "scripts"
    if not scripts.exists() or not any(scripts.iterdir()):
        findings.append(Finding("high", "missing", rel_skill, rel_skill, "Missing scripts/"))

    templates = skill_dir / "output-templates"
    if not templates.exists() or not any(templates.iterdir()):
        findings.append(Finding("high", "missing", rel_skill, rel_skill, "Missing output-templates/"))

    # In this repository, skills generally include agents/openai.yaml
    if not (skill_dir / "agents" / "openai.yaml").exists():
        findings.append(Finding("medium", "missing", rel_skill, rel_skill, "Missing agents/openai.yaml"))

    # Independence checks for markdown links
    for md in skill_dir.rglob("*.md"):
        if "node_modules" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            raw = m.group(2).strip()
            if raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            link = raw.split("#", 1)[0].split("?", 1)[0]
            if not link:
                continue
            target = (md.parent / link).resolve()
            rel_md = str(md.relative_to(repo_root))
            if not target.exists():
                findings.append(Finding("high", "broken_link", rel_skill, rel_md, f"{raw} -> {target}"))
                continue
            if not str(target).startswith(str(skill_dir)):
                if _is_allowed_cross_language_prompt_link(md, target):
                    continue
                findings.append(
                    Finding(
                        "medium",
                        "external_link",
                        rel_skill,
                        rel_md,
                        f"{raw} -> {target}",
                    )
                )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate all skills for integrity and independence.")
    parser.add_argument("--report-json", help="Write JSON report path")
    parser.add_argument("--report-md", help="Write Markdown report path")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit non-zero when findings exist")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    skill_dirs = discover_skill_dirs(repo_root)
    findings: list[Finding] = []
    for d in skill_dirs:
        findings.extend(scan_skill(d, repo_root))

    high = sum(1 for f in findings if f.severity == "high")
    medium = sum(1 for f in findings if f.severity == "medium")
    summary = {
        "repo_root": str(repo_root),
        "skills_scanned": len(skill_dirs),
        "total_findings": len(findings),
        "high": high,
        "medium": medium,
    }

    if args.report_json:
        out = Path(args.report_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "summary": summary,
                    "findings": [asdict(f) for f in findings],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    if args.report_md:
        out = Path(args.report_md)
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Skills Integrity Validation Report",
            "",
            f"- Skills scanned: **{summary['skills_scanned']}**",
            f"- Total findings: **{summary['total_findings']}**",
            f"- High: **{summary['high']}**",
            f"- Medium: **{summary['medium']}**",
            "",
            "## Findings",
        ]
        if not findings:
            lines.append("No issues found.")
        else:
            for i, f in enumerate(findings[:500], 1):
                lines.append(f"{i}. [{f.severity.upper()}] `{f.kind}` `{f.skill}` `{f.file}` - {f.detail}")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"skills_scanned={summary['skills_scanned']}")
    print(f"total_findings={summary['total_findings']}")
    print(f"high={summary['high']}")
    print(f"medium={summary['medium']}")
    if args.fail_on_findings and findings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
