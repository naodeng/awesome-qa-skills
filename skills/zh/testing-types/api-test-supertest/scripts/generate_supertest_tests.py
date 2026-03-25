#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def _safe_name(method: str, path: str, i: int) -> str:
    base = f"{method}_{path}".lower()
    base = re.sub(r"[^a-z0-9]+", "_", base).strip("_")
    return f"api_{base}_{i}"


def _to_test(method: str, path: str, title: str) -> str:
    m = method.lower()
    call = f"request(app).{m}('{path}')"
    if m in {"post", "put", "patch"}:
        call += ".send({})"
    return (
        f"test('{title}', async () => {{\n"
        f"  const res = await {call};\n"
        f"  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);\n"
        f"}});\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Supertest tests from normalized endpoint JSON")
    parser.add_argument("--input", required=True, type=Path, help="Normalized endpoint JSON from parse_api_sources.py")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory for generated test file")
    args = parser.parse_args()

    obj = json.loads(args.input.read_text(encoding="utf-8"))
    endpoints = obj.get("endpoints", [])
    args.output_dir.mkdir(parents=True, exist_ok=True)

    lines = [
        "const request = require('supertest');",
        "const app = require(process.env.SUPERTEST_APP || '../app');",
        "",
        "describe('Generated API Tests', () => {",
    ]
    for i, ep in enumerate(endpoints, start=1):
        method = str(ep.get("method", "GET")).upper()
        path = str(ep.get("path", "/"))
        title = _safe_name(method, path, i)
        lines.append(_to_test(method, path, title).rstrip())
    lines.append("});")
    lines.append("")

    out = args.output_dir / "generated.api.test.js"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(str(out))


if __name__ == "__main__":
    main()
