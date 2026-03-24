#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def _metric_value(metrics: dict, name: str, key: str):
    m = metrics.get(name) or {}
    values = m.get("values") or {}
    return values.get(key)


def summarize(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    metrics = data.get("metrics") or {}
    return {
        "file": str(path),
        "p95_ms": _metric_value(metrics, "http_req_duration", "p(95)"),
        "p99_ms": _metric_value(metrics, "http_req_duration", "p(99)"),
        "error_rate": _metric_value(metrics, "http_req_failed", "rate"),
        "rps": _metric_value(metrics, "http_reqs", "rate"),
        "checks_rate": _metric_value(metrics, "checks", "rate"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize k6 summary json file")
    parser.add_argument("summary_json", type=Path, help="Path to k6 summary json")
    args = parser.parse_args()

    out = summarize(args.summary_json)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
