from __future__ import annotations

import os
from pathlib import Path
import subprocess
import unittest


VALID_ARTIFACT = """```javascript
import { test, expect } from '@playwright/test';

test('checkout', async ({ page }) => {
  await page.goto('/checkout');
  await expect(page.getByRole('heading')).toBeVisible();
});
```"""

INVALID_MARKERS = """```javascript
// Playwright
test( page.goto( expect(
```"""


class PlaywrightArtifactJudgeTest(unittest.TestCase):
    def test_judge_requires_a_valid_javascript_artifact(self) -> None:
        repo_root = Path(__file__).resolve().parents[2]
        scripts = [
            repo_root / "skills" / "en" / "testing-types" / "ui-test-playwright" / "evals" / "fixtures" / "scripts" / "check_playwright_output.sh",
            repo_root / "skills" / "zh" / "testing-types" / "ui-test-playwright" / "evals" / "fixtures" / "scripts" / "check_playwright_output.sh",
        ]
        for script in scripts:
            with self.subTest(script=script):
                valid = subprocess.run(
                    ["bash", str(script)],
                    cwd=repo_root,
                    env={**os.environ, "EVAL_FINAL_MESSAGE": VALID_ARTIFACT, "EVAL_EXIT_CODE": "0"},
                    capture_output=True,
                    text=True,
                    check=False,
                )
                invalid = subprocess.run(
                    ["bash", str(script)],
                    cwd=repo_root,
                    env={**os.environ, "EVAL_FINAL_MESSAGE": INVALID_MARKERS, "EVAL_EXIT_CODE": "0"},
                    capture_output=True,
                    text=True,
                    check=False,
                )

                self.assertEqual(valid.returncode, 0, valid.stderr or valid.stdout)
                self.assertNotEqual(invalid.returncode, 0, invalid.stdout)


if __name__ == "__main__":
    unittest.main()
