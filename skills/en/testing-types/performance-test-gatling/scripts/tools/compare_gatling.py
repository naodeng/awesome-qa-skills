#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def _load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    stats = data.get("stats", {})
    req = stats.get("requests", {})
    resp = stats.get("responseTime", {})
    return {
        "path": str(path),
        "total": req.get("total"),
        "ok": req.get("ok"),
        "ko": req.get("ko"),
        "p95_ms": resp.get("percentiles3"),
        "p99_ms": resp.get("percentiles4"),
        "mean_ms": resp.get("mean"),
    }


def _pct(base, curr):
    if base in (None, 0) or curr is None:
        return None
    return ((curr - base) / base) * 100.0


def _ko_rate(m: dict):
    total = m.get("total")
    ko = m.get("ko")
    if total in (None, 0) or ko is None:
        return None
    return ko / total


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two Gatling stats json files")
    parser.add_argument("baseline_json", type=Path)
    parser.add_argument("candidate_json", type=Path)
    args = parser.parse_args()

    b = _load(args.baseline_json)
    c = _load(args.candidate_json)

    b_ko = _ko_rate(b)
    c_ko = _ko_rate(c)

    out = {
        "baseline": b["path"],
        "candidate": c["path"],
        "delta": {
            "p95_pct": _pct(b["p95_ms"], c["p95_ms"]),
            "p99_pct": _pct(b["p99_ms"], c["p99_ms"]),
            "mean_pct": _pct(b["mean_ms"], c["mean_ms"]),
            "ko_rate_diff": None if b_ko is None or c_ko is None else c_ko - b_ko,
        },
        "raw": {
            "baseline": b,
            "candidate": c,
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
