#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def summarize(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))

    stats = data.get("stats", {})
    req = stats.get("requests", {})
    resp = stats.get("responseTime", {})

    def _pct_resp(name: str):
        return resp.get(name)

    return {
        "file": str(path),
        "total_requests": req.get("total"),
        "ok_requests": req.get("ok"),
        "ko_requests": req.get("ko"),
        "p95_ms": _pct_resp("percentiles3"),
        "p99_ms": _pct_resp("percentiles4"),
        "mean_ms": resp.get("mean"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize Gatling js stats file")
    parser.add_argument("stats_json", type=Path, help="Path to Gatling JSON stats file")
    args = parser.parse_args()
    print(json.dumps(summarize(args.stats_json), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
