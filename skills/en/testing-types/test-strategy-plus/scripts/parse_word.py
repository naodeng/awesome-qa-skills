#!/usr/bin/env python3
import argparse
from pathlib import Path

from common_parser import parse_word


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse Word file (.docx)")
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    print(parse_word(args.input))


if __name__ == "__main__":
    main()
