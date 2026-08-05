#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def detect_from(file: Path) -> str:
    ext = file.suffix.lower()
    if file.name.endswith('.word.md'):
        return 'markdown'
    return {
        '.md': 'markdown',
        '.markdown': 'markdown',
        '.json': 'json',
        '.csv': 'csv',
        '.tsv': 'excel',
        '.docx': 'word',
        '.xlsx': 'excel',
        '.xmind': 'xmind',
    }.get(ext, 'markdown')


def run_convert(convert_script: Path, src: Path, to_fmt: str, out: Path) -> int:
    cmd = [sys.executable, str(convert_script), str(src), '--from', detect_from(src), '--to', to_fmt, '--output', str(out)]
    return subprocess.call(cmd)


def main() -> None:
    parser = argparse.ArgumentParser(description='Batch convert all template files into target formats.')
    parser.add_argument('--templates-dir', type=Path, default=Path('output-templates'))
    parser.add_argument('--artifacts-dir', type=Path, default=Path('artifacts'))
    parser.add_argument('--targets', default='word,excel,xmind,json,csv,markdown', help='comma-separated target formats')
    parser.add_argument('--skip-same', action='store_true', help='skip conversion when source format equals target format')
    args = parser.parse_args()

    cwd = Path.cwd()
    templates_dir = (cwd / args.templates_dir).resolve()
    artifacts_dir = (cwd / args.artifacts_dir).resolve()
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    local_convert = (Path(__file__).resolve().parent / 'convert_formats.py').resolve()
    targets = [t.strip() for t in args.targets.split(',') if t.strip()]

    if not templates_dir.exists():
        raise SystemExit(f'templates directory not found: {templates_dir}')

    files = [p for p in sorted(templates_dir.iterdir()) if p.is_file()]
    total = 0
    failed = 0

    for src in files:
        src_fmt = detect_from(src)
        for to_fmt in targets:
            if args.skip_same and src_fmt == to_fmt:
                continue
            out_ext = {
                'json': '.json',
                'csv': '.csv',
                'excel': '.tsv',
                'markdown': '.md',
                'word': '.word.md',
                'xmind': '.xmind.md',
            }[to_fmt]
            out = artifacts_dir / f"{src.stem}.to-{to_fmt}{out_ext}"
            total += 1
            rc = run_convert(local_convert, src, to_fmt, out)
            if rc != 0:
                failed += 1
                print(f'[FAILED] {src.name} -> {to_fmt}')
            else:
                print(f'[OK] {src.name} -> {out.name}')

    print(f'\nDone. total={total}, failed={failed}, artifacts={artifacts_dir}')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
