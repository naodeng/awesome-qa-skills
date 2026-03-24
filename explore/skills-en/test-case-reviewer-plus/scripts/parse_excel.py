#!/usr/bin/env python3
import argparse
from pathlib import Path

from common_parser import parse_excel


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse Excel file")
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    print(parse_excel(args.input))


if __name__ == "__main__":
    main()
