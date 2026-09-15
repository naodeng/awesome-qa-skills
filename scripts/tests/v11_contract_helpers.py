from __future__ import annotations

import csv
from pathlib import Path
import unittest


TRIGGER_MODES = {"explicit", "implicit", "contextual", "negative"}


def read_trigger_rows(package: Path) -> list[dict[str, str]]:
    with (package / "evals" / "trigger-prompts.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        return list(csv.DictReader(stream))


def assert_trigger_contract(test: unittest.TestCase, package: Path) -> list[dict[str, str]]:
    rows = read_trigger_rows(package)
    test.assertEqual({row.get("mode") for row in rows}, TRIGGER_MODES, package)
    test.assertEqual({row.get("should_trigger") for row in rows}, {"true", "false"}, package)
    test.assertEqual(len(rows), len({row.get("id") for row in rows}), package)
    test.assertTrue(all((row.get("prompt") or "").strip() for row in rows), package)
    return rows
