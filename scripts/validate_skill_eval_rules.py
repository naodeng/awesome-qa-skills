#!/usr/bin/env python3
"""Validate the repository's stable local Skill eval rule catalog."""

from __future__ import annotations

try:
    from .skill_eval_rules import RULE_IDS, validate_rule_catalog
except ImportError:  # pragma: no cover - supports direct script execution
    from skill_eval_rules import RULE_IDS, validate_rule_catalog


def main() -> int:
    errors = validate_rule_catalog()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"local Skill eval rule catalog valid: {len(RULE_IDS)} rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
