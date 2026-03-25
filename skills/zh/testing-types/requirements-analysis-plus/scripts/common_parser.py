#!/usr/bin/env python3
import json
import re
import zipfile
from pathlib import Path
from html.parser import HTMLParser
from typing import Callable, Dict
from xml.etree import ElementTree as ET


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self._parts.append(text)

    def get_text(self) -> str:
        return "\n".join(self._parts)


def parse_word(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        with zf.open("word/document.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    lines = []
    for p in root.findall(".//w:p", ns):
        texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
        line = "".join(texts).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def parse_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    parser = _HTMLTextExtractor()
    parser.feed(raw)
    return parser.get_text()


def _flatten_json(prefix: str, value, out: list) -> None:
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            _flatten_json(key, v, out)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten_json(key, v, out)
    else:
        out.append(f"{prefix}: {value}")


def parse_json(path: Path) -> str:
    obj = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    out = []
    _flatten_json("", obj, out)
    return "\n".join(out)


def parse_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Keep heading context but remove markdown emphasis markers.
    text = re.sub(r"[*_`>#-]", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _read_shared_strings(zf: zipfile.ZipFile) -> list:
    try:
        with zf.open("xl/sharedStrings.xml") as f:
            root = ET.fromstring(f.read())
    except KeyError:
        return []
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    strings = []
    for si in root.findall(".//a:si", ns):
        parts = [t.text or "" for t in si.findall(".//a:t", ns)]
        strings.append("".join(parts))
    return strings


def parse_excel(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        shared = _read_shared_strings(zf)
        with zf.open("xl/worksheets/sheet1.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rows = []
    for row in root.findall(".//a:sheetData/a:row", ns):
        values = []
        for c in row.findall("a:c", ns):
            ctype = c.attrib.get("t")
            v = c.find("a:v", ns)
            if v is None or v.text is None:
                values.append("")
            elif ctype == "s":
                idx = int(v.text)
                values.append(shared[idx] if 0 <= idx < len(shared) else "")
            else:
                values.append(v.text)
        joined = " | ".join(x for x in values if x)
        if joined:
            rows.append(joined)
    return "\n".join(rows)


PARSERS: Dict[str, Callable[[Path], str]] = {
    "word": parse_word,
    "html": parse_html,
    "json": parse_json,
    "markdown": parse_markdown,
    "excel": parse_excel,
}


def detect_format(path: Path) -> str:
    ext = path.suffix.lower()
    mapping = {
        ".docx": "word",
        ".html": "html",
        ".htm": "html",
        ".json": "json",
        ".md": "markdown",
        ".markdown": "markdown",
        ".xlsx": "excel",
        ".xlsm": "excel",
    }
    if ext not in mapping:
        raise ValueError(f"Unsupported file extension: {ext}")
    return mapping[ext]

