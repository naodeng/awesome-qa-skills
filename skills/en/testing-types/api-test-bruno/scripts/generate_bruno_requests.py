#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def _safe_slug(method: str, path: str, i: int) -> str:
    base = f"{i:03d}_{method}_{path}".lower()
    return re.sub(r"[^a-z0-9]+", "_", base).strip("_")


def _to_bru(method: str, path: str, name: str) -> str:
    method_lower = method.lower()
    body_mode = "none" if method_lower in {"get", "delete", "head", "options"} else "json"
    body_block = ""
    if body_mode == "json":
        body_block = 'body:json {\n  {\n    "sample": true\n  }\n}\n'
    return (
        "meta {\n"
        f"  name: {name}\n"
        "  type: http\n"
        "  seq: 1\n"
        "}\n\n"
        f"{method_lower} {{\n"
        f"  url: {{baseUrl}}{path}\n"
        f"  body: {body_mode}\n"
        "}\n\n"
        f"{body_block}\n"
        "headers {\n"
        "  Content-Type: application/json\n"
        "  Authorization: Bearer {{token}}\n"
        "}\n\n"
        "tests {\n"
        "  test(\"status should be expected\", function() {\n"
        "    const status = res.getStatus();\n"
        "    expect([200, 201, 202, 204, 400, 401, 403, 404]).to.include(status);\n"
        "  });\n"
        "}\n"
    )


def _bruno_json() -> str:
    return '{\n  "version": "1",\n  "name": "generated-bruno-collection",\n  "type": "collection"\n}\n'


def _env_bru() -> str:
    return (
        "vars {\n"
        "  baseUrl: https://api.example.com\n"
        "  token: replace-me\n"
        "}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Bruno requests from normalized endpoint JSON")
    parser.add_argument("--input", required=True, type=Path, help="Normalized endpoint JSON")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output Bruno collection folder")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    endpoints = payload.get("endpoints", [])

    out_dir = args.output_dir
    req_dir = out_dir / "requests"
    env_dir = out_dir / "environments"
    req_dir.mkdir(parents=True, exist_ok=True)
    env_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "bruno.json").write_text(_bruno_json(), encoding="utf-8")
    (env_dir / "staging.bru").write_text(_env_bru(), encoding="utf-8")

    for i, ep in enumerate(endpoints, start=1):
        method = str(ep.get("method", "GET")).upper()
        path = str(ep.get("path", "/"))
        name = _safe_slug(method, path, i)
        content = _to_bru(method, path, name)
        (req_dir / f"{name}.bru").write_text(content, encoding="utf-8")

    print(str(out_dir))


if __name__ == "__main__":
    main()
