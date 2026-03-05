#!/usr/bin/env python3
import os
import subprocess
import sys
LOCAL = os.path.normpath(os.path.join(os.path.dirname(__file__), 'parse_formats.py'))
if __name__ == '__main__':
    raise SystemExit(subprocess.call([sys.executable, LOCAL, '--format', 'json'] + sys.argv[1:]))
