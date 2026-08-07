from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_skills_integrity import scan_skill


def test_optional_support_dirs_do_not_fail_minimal_skill(tmp_path: Path) -> None:
    skill = tmp_path / "skills" / "zh" / "testing-types" / "minimal-skill"
    (skill / "prompts").mkdir(parents=True)
    (skill / "agents").mkdir()
    (skill / "evals" / "cases").mkdir(parents=True)

    (skill / "SKILL.md").write_text(
        "---\nname: minimal-skill\ndescription: Use this skill when testing optional dirs.\n---\n",
        encoding="utf-8",
    )
    (skill / "prompts" / "minimal-skill.md").write_text("# Prompt\n", encoding="utf-8")
    (skill / "agents" / "openai.yaml").write_text("version: 1\n", encoding="utf-8")
    (skill / "evals" / "eval.yaml").write_text("schema_version: v1alpha1\n", encoding="utf-8")
    (skill / "evals" / "cases" / "basic-success.yaml").write_text("id: basic-success\n", encoding="utf-8")

    findings = scan_skill(skill, tmp_path)

    assert [f.detail for f in findings] == []
