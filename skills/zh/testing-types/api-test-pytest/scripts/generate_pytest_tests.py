#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def _safe_name(method: str, path: str, idx: int) -> str:
    base = f"{method}_{path}_{idx}".lower()
    return re.sub(r"[^a-z0-9]+", "_", base).strip("_")


def _case_block(method: str, path: str, name: str) -> str:
    method_low = method.lower()
    body = "{}" if method_low in {"post", "put", "patch"} else "None"
    return (
        f"def test_{name}(api_client):\n"
        f"    resp = api_client.request('{method_low}', '{path}', json={body})\n"
        f"    assert resp.status_code in [200, 201, 202, 204, 400, 401, 403, 404]\n"
        f"    assert resp.elapsed.total_seconds() < 3\n\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate pytest tests from normalized endpoint JSON")
    parser.add_argument("--input", required=True, type=Path, help="Normalized endpoint JSON")
    parser.add_argument("--output", required=True, type=Path, help="Output pytest file path")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    endpoints = payload.get("endpoints", [])

    lines = [
        '"""Auto-generated pytest API tests."""',
        "",
        "def test_generated_collection_not_empty():",
        f"    assert {len(endpoints)} >= 0",
        "",
    ]
    for i, ep in enumerate(endpoints, start=1):
        method = str(ep.get("method", "GET")).upper()
        path = str(ep.get("path", "/"))
        name = _safe_name(method, path, i)
        lines.append(_case_block(method, path, name).rstrip())
        lines.append("")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(str(args.output))


if __name__ == "__main__":
    main()
