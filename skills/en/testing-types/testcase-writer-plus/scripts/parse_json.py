#!/usr/bin/env python3
import argparse
from pathlib import Path

from common_parser import parse_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse JSON file")
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    print(parse_json(args.input))


if __name__ == "__main__":
    main()
