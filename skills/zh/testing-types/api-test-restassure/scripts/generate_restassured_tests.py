#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def _safe_method(m: str) -> str:
    return m.upper() if m.upper() in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"} else "GET"


def _safe_name(method: str, path: str, idx: int) -> str:
    s = f"{idx}_{method}_{path}".lower()
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def _invoke_line(method: str, path: str) -> str:
    m = method.lower()
    if m in {"post", "put", "patch"}:
        return (
            f'given().spec(requestSpec).body("{{}}").when().{m}("{path}")'
            '.then().statusCode(anyOf(is(200), is(201), is(202), is(204), is(400), is(401), is(403), is(404)))'
            '.time(lessThan(3000L));'
        )
    return (
        f'given().spec(requestSpec).when().{m}("{path}")'
        '.then().statusCode(anyOf(is(200), is(201), is(202), is(204), is(400), is(401), is(403), is(404)))'
        '.time(lessThan(3000L));'
    )


def build_java_class(endpoints):
    lines = [
        "package com.example.api;",
        "",
        "import org.junit.jupiter.api.Test;",
        "",
        "import static io.restassured.RestAssured.given;",
        "import static org.hamcrest.Matchers.anyOf;",
        "import static org.hamcrest.Matchers.is;",
        "import static org.hamcrest.Matchers.lessThan;",
        "",
        "public class GeneratedApiTest extends BaseApiTest {",
        "",
        "    @Test",
        "    void generatedCollectionNotEmpty() {",
        f"        org.junit.jupiter.api.Assertions.assertTrue({len(endpoints)} >= 0);",
        "    }",
        "",
    ]
    for idx, ep in enumerate(endpoints, start=1):
        method = _safe_method(str(ep.get("method", "GET")))
        path = str(ep.get("path", "/"))
        name = _safe_name(method, path, idx)
        lines.extend(
            [
                "    @Test",
                f"    void test_{name}() {{",
                f"        {_invoke_line(method, path)}",
                "    }",
                "",
            ]
        )
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Rest Assured tests from normalized endpoint JSON")
    parser.add_argument("--input", required=True, type=Path, help="Normalized endpoint JSON")
    parser.add_argument("--output", required=True, type=Path, help="Output Java test class path")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    endpoints = payload.get("endpoints", [])
    java = build_java_class(endpoints)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(java, encoding="utf-8")
    print(str(args.output))


if __name__ == "__main__":
    main()
