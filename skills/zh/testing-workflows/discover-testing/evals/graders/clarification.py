#!/usr/bin/env python3
"""检查信息不足时是否用文字澄清关键范围。"""
from __future__ import annotations

import os
import re
import sys


FEATURE = re.compile(r"功能|需求|用户流程")
SCOPE = re.compile(r"范围|产品|模块|页面|平台|PR|仓库|URL|系统|用户流程|用户旅程|场景|业务路径", re.IGNORECASE)
PHASE = re.compile(r"阶段|做到哪一步|当前进度|开发中|已部署|需求评审|设计阶段")
DELIVERABLE = re.compile(r"交付(?:物|什么|内容|哪些)|期望.{0,12}交付|用例|策略|方案|测试类型|执行|报告")
PREMATURE_ROUTE = re.compile(r"主推荐|唯一主\s*[Ss]kill|主\s*[Ss]kill\s*[:：]", re.IGNORECASE)


def grade(text: str, exit_code: object) -> None:
    if str(exit_code) != "0":
        raise ValueError("engine did not exit successfully")
    checks = (FEATURE, SCOPE, PHASE, DELIVERABLE)
    if any(not pattern.search(text) for pattern in checks):
        raise ValueError("clarification is missing feature, scope, phase, or deliverable questions")
    if PREMATURE_ROUTE.search(text):
        raise ValueError("selected a route before clarifying the underspecified goal")


if __name__ == "__main__":
    try:
        grade(os.environ.get("EVAL_FINAL_MESSAGE", ""), os.environ.get("EVAL_EXIT_CODE", ""))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print("已覆盖功能、范围、阶段和期望产出澄清")
