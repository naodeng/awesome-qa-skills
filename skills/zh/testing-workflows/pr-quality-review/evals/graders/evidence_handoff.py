#!/usr/bin/env python3
"""检查中文工作流交接是否保留证据和原待验证动作。"""
from __future__ import annotations

import os
import re
import sys


REQUIRED_SIGNALS = {
    "证据 ID": re.compile(r"\bE-91\b", re.IGNORECASE),
    "来源路径": re.compile(r"\bbilling/retry\.py\b", re.IGNORECASE),
    "重试重复扣款风险": re.compile(
        r"(?:重复(?:扣款|收费|支付)|(?:扣款|收费|支付)[^。.!?\n]{0,24}重复)",
        re.IGNORECASE,
    ),
    "重试范围": re.compile(r"重试", re.IGNORECASE),
    "推断状态": re.compile(r"推断"),
    "输入 SHA": re.compile(r"\babc123\b", re.IGNORECASE),
    "待验证动作": re.compile(r"(?:待验证|待跟进|后续动作)"),
    "支付沙箱": re.compile(r"支付沙箱"),
    "相同幂等键": re.compile(r"相同幂等键"),
    "单次扣款结果": re.compile(r"(?:只|仅)?(?:产生|发生)?一次(?:扣款|收费|支付)|(?:只|仅)扣款一次"),
}


def grade(text: str, exit_code: object) -> None:
    if str(exit_code) != "0":
        raise ValueError("engine did not exit successfully")
    missing = [name for name, marker in REQUIRED_SIGNALS.items() if not marker.search(text)]
    if missing:
        raise ValueError("handoff follow-up not preserved: " + ", ".join(missing))


if __name__ == "__main__":
    try:
        grade(os.environ.get("EVAL_FINAL_MESSAGE", ""), os.environ.get("EVAL_EXIT_CODE", ""))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print("证据交接和待验证动作已保留")
