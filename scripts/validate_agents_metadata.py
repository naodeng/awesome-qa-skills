#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIRS = sorted(
    [p for p in (ROOT / "skills").glob("testing-types/*") if p.is_dir()]
    + [p for p in (ROOT / "skills").glob("testing-workflows/*") if p.is_dir()]
)


@dataclass
class Finding:
    severity: str
    skill: str
    file: Path
    message: str


def read_skill_meta(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    name = re.search(r"^name:\s*(.+)$", text, re.M)
    desc = re.search(r"^description:\s*(.+)$", text, re.M)
    h1 = re.search(r"^#\s+(.+)$", text, re.M)
    return {
        "name": (name.group(1).strip() if name else ""),
        "description": (desc.group(1).strip() if desc else ""),
        "h1": (h1.group(1).strip() if h1 else ""),
    }


def read_openai_yaml(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    vals = {}
    patterns = {
        "version": r"^version:\s*(.+)$",
        "key": r"^\s*key:\s*(.+)$",
        "display_name": r"^\s*display_name:\s*(.+)$",
        "short_description": r"^\s*short_description:\s*(.+)$",
        "default_prompt": r"^\s*default_prompt:\s*(.+)$",
        "allow_implicit_invocation": r"^\s*allow_implicit_invocation:\s*(.+)$",
    }
    for k, p in patterns.items():
        m = re.search(p, text, re.M)
        vals[k] = m.group(1).strip() if m else ""
    for k in ("key", "display_name", "short_description", "default_prompt"):
        v = vals.get(k, "")
        if v.startswith('"') and v.endswith('"') and len(v) >= 2:
            vals[k] = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return vals


def validate() -> List[Finding]:
    findings: List[Finding] = []

    symlink_types = ROOT / ".agents" / "skills" / "testing-types"
    symlink_workflows = ROOT / ".agents" / "skills" / "testing-workflows"
    if not symlink_types.exists():
        findings.append(Finding("high", "GLOBAL", symlink_types, "Missing .agents/skills/testing-types"))
    if not symlink_workflows.exists():
        findings.append(Finding("high", "GLOBAL", symlink_workflows, "Missing .agents/skills/testing-workflows"))

    for d in SKILL_DIRS:
        skill_md = d / "SKILL.md"
        agent_yaml = d / "agents" / "openai.yaml"

        if not skill_md.exists():
            findings.append(Finding("high", d.name, skill_md, "Missing SKILL.md"))
            continue
        if not agent_yaml.exists():
            findings.append(Finding("high", d.name, agent_yaml, "Missing agents/openai.yaml"))
            continue

        sm = read_skill_meta(skill_md)
        ay = read_openai_yaml(agent_yaml)

        if ay.get("version") != "1":
            findings.append(Finding("medium", d.name, agent_yaml, "version should be 1"))

        if ay.get("key") != sm.get("name"):
            findings.append(Finding("high", d.name, agent_yaml, f"metadata.key mismatch: {ay.get('key')} != {sm.get('name')}"))

        if not ay.get("display_name"):
            findings.append(Finding("high", d.name, agent_yaml, "interface.display_name is empty"))

        sd = ay.get("short_description", "")
        if not sd:
            findings.append(Finding("high", d.name, agent_yaml, "interface.short_description is empty"))
        elif len(sd) > 160:
            findings.append(Finding("medium", d.name, agent_yaml, f"short_description too long ({len(sd)} > 160)"))

        dp = ay.get("default_prompt", "")
        if not dp:
            findings.append(Finding("high", d.name, agent_yaml, "interface.default_prompt is empty"))
        elif sm.get("name") and sm["name"] not in dp:
            findings.append(Finding("low", d.name, agent_yaml, "default_prompt does not mention skill name"))

        if ay.get("allow_implicit_invocation") not in {"true", "false"}:
            findings.append(Finding("medium", d.name, agent_yaml, "policy.allow_implicit_invocation should be true/false"))

    return findings


def write_report(findings: List[Finding], report_path: Path) -> None:
    total_skills = len(SKILL_DIRS)
    by_sev = {"high": 0, "medium": 0, "low": 0}
    for f in findings:
        by_sev[f.severity] = by_sev.get(f.severity, 0) + 1

    lines = [
        "# Skills Metadata Validation Report",
        "",
        "## Summary",
        f"- Total skills scanned: {total_skills}",
        f"- Total findings: {len(findings)}",
        f"- High: {by_sev['high']}",
        f"- Medium: {by_sev['medium']}",
        f"- Low: {by_sev['low']}",
        "",
    ]

    if not findings:
        lines.extend([
            "## Findings",
            "No issues found. All `agents/openai.yaml` files passed current validation rules.",
            "",
        ])
    else:
        lines.append("## Findings")
        lines.append("")
        for i, f in enumerate(findings, 1):
            rel = f.file.relative_to(ROOT)
            lines.append(f"{i}. [{f.severity.upper()}] `{f.skill}` - `{rel}` - {f.message}")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Codex skills metadata files.")
    parser.add_argument("--report", default="skills-metadata-report.md", help="Output report path")
    args = parser.parse_args()

    findings = validate()
    report_path = (ROOT / args.report).resolve()
    write_report(findings, report_path)

    print(f"report={report_path}")
    print(f"findings={len(findings)}")

    # return non-zero only on high severity
    if any(f.severity == "high" for f in findings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
