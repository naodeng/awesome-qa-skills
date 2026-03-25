#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def _get(metrics: dict, name: str, key: str):
    m = metrics.get(name) or {}
    values = m.get("values") or {}
    return values.get(key)


def _load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    metrics = data.get("metrics") or {}
    return {
        "path": str(path),
        "p95_ms": _get(metrics, "http_req_duration", "p(95)"),
        "p99_ms": _get(metrics, "http_req_duration", "p(99)"),
        "error_rate": _get(metrics, "http_req_failed", "rate"),
        "rps": _get(metrics, "http_reqs", "rate"),
    }


def _pct(base, curr):
    if base in (None, 0) or curr is None:
        return None
    return ((curr - base) / base) * 100.0


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two k6 summary json files")
    parser.add_argument("baseline_json", type=Path)
    parser.add_argument("candidate_json", type=Path)
    args = parser.parse_args()

    b = _load(args.baseline_json)
    c = _load(args.candidate_json)

    result = {
        "baseline": b["path"],
        "candidate": c["path"],
        "delta": {
            "p95_pct": _pct(b["p95_ms"], c["p95_ms"]),
            "p99_pct": _pct(b["p99_ms"], c["p99_ms"]),
            "error_rate_diff": None
            if b["error_rate"] is None or c["error_rate"] is None
            else c["error_rate"] - b["error_rate"],
            "rps_pct": _pct(b["rps"], c["rps"]),
        },
        "raw": {
            "baseline": b,
            "candidate": c,
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
