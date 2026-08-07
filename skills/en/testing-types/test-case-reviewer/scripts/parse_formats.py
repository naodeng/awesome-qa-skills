#!/usr/bin/env python3
import argparse
import csv
import json
import re
import subprocess
import zipfile
import zlib
from pathlib import Path
from typing import Any, Optional
from xml.etree import ElementTree as ET


def parse_markdown(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    headings = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m:
            headings.append({"level": len(m.group(1)), "title": m.group(2).strip()})
    return {"format": "markdown", "headings": headings, "preview": text[:500]}


def parse_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    if isinstance(data, dict):
        shape = {"type": "object", "keys": list(data.keys())[:50]}
    elif isinstance(data, list):
        shape = {"type": "array", "size": len(data)}
    else:
        shape = {"type": type(data).__name__}
    return {"format": "json", "shape": shape, "data": data}


def parse_csv_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return {
        "format": "csv",
        "columns": reader.fieldnames or [],
        "row_count": len(rows),
        "sample_rows": rows[:10],
    }


def parse_docx(path: Path) -> dict[str, Any]:
    paragraphs = []
    with zipfile.ZipFile(path) as zf:
        with zf.open("word/document.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    for p in root.findall(".//w:p", ns):
        texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
        joined = "".join(texts).strip()
        if joined:
            paragraphs.append(joined)
    return {"format": "word", "paragraph_count": len(paragraphs), "paragraphs": paragraphs[:100]}


def _pdf_unescape(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        token = match.group(1)
        if token.isdigit() and len(token) <= 3:
            try:
                return chr(int(token, 8))
            except ValueError:
                return ""
        mapping = {
            "n": "\n",
            "r": "\r",
            "t": "\t",
            "b": "\b",
            "f": "\f",
            "(": "(",
            ")": ")",
            "\\": "\\",
        }
        return mapping.get(token, token)

    return re.sub(r"\\([0-7]{1,3}|.)", repl, text)


def _extract_pdf_text_builtin(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    page_count = len(re.findall(rb"/Type\s*/Page\b", data))
    text_blocks: list[str] = []

    streams = re.findall(rb"stream\r?\n(.*?)\r?\nendstream", data, flags=re.S)
    for raw in streams:
        candidates = [raw]
        for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS):
            try:
                candidates.append(zlib.decompress(raw, wbits))
                break
            except Exception:
                continue

        for chunk in candidates:
            content = chunk.decode("latin1", errors="ignore")
            for m in re.finditer(r"\(((?:\\.|[^\\()])*)\)\s*Tj", content):
                text_blocks.append(_pdf_unescape(m.group(1)))
            for arr in re.finditer(r"\[(.*?)\]\s*TJ", content, flags=re.S):
                parts = re.findall(r"\(((?:\\.|[^\\()])*)\)", arr.group(1))
                if parts:
                    text_blocks.append("".join(_pdf_unescape(p) for p in parts))

    merged = "\n".join(t.strip() for t in text_blocks if t.strip())
    return merged, page_count


def parse_pdf(path: Path) -> dict[str, Any]:
    module_errors: list[str] = []
    for mod_name in ("pypdf", "PyPDF2"):
        try:
            pdf_mod = __import__(mod_name)
            reader = pdf_mod.PdfReader(str(path))
            texts = []
            for page in reader.pages:
                text = page.extract_text() or ""
                if text.strip():
                    texts.append(text.strip())
            merged = "\n\n".join(texts)
            return {
                "format": "pdf",
                "engine": mod_name,
                "page_count": len(reader.pages),
                "text_length": len(merged),
                "preview": merged[:2000],
            }
        except Exception as exc:
            module_errors.append(f"{mod_name}: {exc}")

    try:
        proc = subprocess.run(
            ["pdftotext", "-q", str(path), "-"],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            text = proc.stdout or ""
            page_count = text.count("\f") + (1 if text else 0)
            return {
                "format": "pdf",
                "engine": "pdftotext",
                "page_count": page_count,
                "text_length": len(text),
                "preview": text[:2000],
            }
    except FileNotFoundError:
        pass

    fallback_text, fallback_pages = _extract_pdf_text_builtin(path)
    if fallback_text or fallback_pages > 0:
        return {
            "format": "pdf",
            "engine": "builtin",
            "page_count": fallback_pages,
            "text_length": len(fallback_text),
            "preview": fallback_text[:2000],
        }

    detail = "; ".join(module_errors) if module_errors else "No PDF parser available"
    raise RuntimeError(
        "Unable to parse PDF text in current environment. "
        f"Details: {detail}"
    )


def _read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    strings = []
    try:
        with zf.open("xl/sharedStrings.xml") as f:
            root = ET.fromstring(f.read())
        ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        for si in root.findall(".//a:si", ns):
            parts = [t.text or "" for t in si.findall(".//a:t", ns)]
            strings.append("".join(parts))
    except KeyError:
        pass
    return strings


def parse_xlsx(path: Path) -> dict[str, Any]:
    rows_out: list[list[str]] = []
    with zipfile.ZipFile(path) as zf:
        shared = _read_shared_strings(zf)
        with zf.open("xl/worksheets/sheet1.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    for row in root.findall(".//a:sheetData/a:row", ns):
        vals = []
        for c in row.findall("a:c", ns):
            cell_type = c.attrib.get("t")
            v = c.find("a:v", ns)
            if v is None or v.text is None:
                vals.append("")
                continue
            if cell_type == "s":
                idx = int(v.text)
                vals.append(shared[idx] if 0 <= idx < len(shared) else "")
            else:
                vals.append(v.text)
        rows_out.append(vals)
    return {"format": "excel", "row_count": len(rows_out), "sample_rows": rows_out[:20]}


def parse_xmind(path: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        if "content.json" in names:
            data = json.loads(zf.read("content.json").decode("utf-8", errors="ignore"))
            titles: list[str] = []

            def walk(node: Any):
                if isinstance(node, dict):
                    title = node.get("title")
                    if isinstance(title, str) and title.strip():
                        titles.append(title.strip())
                    for k in ("children", "topics", "rootTopic", "attached"):
                        walk(node.get(k))
                elif isinstance(node, list):
                    for i in node:
                        walk(i)

            walk(data)
            return {"format": "xmind", "topic_count": len(titles), "topics": titles[:200]}
        if "content.xml" in names:
            root = ET.fromstring(zf.read("content.xml"))
            titles = [el.text.strip() for el in root.findall(".//title") if el.text and el.text.strip()]
            return {"format": "xmind", "topic_count": len(titles), "topics": titles[:200]}
    raise ValueError("Unsupported XMind package structure")


def detect_format(path: Path, forced: Optional[str]) -> str:
    if forced and forced != "auto":
        return forced
    ext = path.suffix.lower()
    return {
        ".md": "markdown",
        ".markdown": "markdown",
        ".json": "json",
        ".csv": "csv",
        ".docx": "word",
        ".pdf": "pdf",
        ".xlsx": "excel",
        ".xmind": "xmind",
    }.get(ext, "markdown")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse common QA output formats into normalized JSON")
    parser.add_argument("input", type=Path, help="Input file path")
    parser.add_argument("--format", default="auto", choices=["auto", "word", "pdf", "excel", "xmind", "json", "csv", "markdown"])
    parser.add_argument("--output", type=Path, help="Output JSON path (default: stdout)")
    args = parser.parse_args()

    fmt = detect_format(args.input, args.format)
    if fmt == "word":
        result = parse_docx(args.input)
    elif fmt == "pdf":
        result = parse_pdf(args.input)
    elif fmt == "excel":
        result = parse_xlsx(args.input)
    elif fmt == "xmind":
        result = parse_xmind(args.input)
    elif fmt == "json":
        result = parse_json(args.input)
    elif fmt == "csv":
        result = parse_csv_file(args.input)
    else:
        result = parse_markdown(args.input)

    result["source"] = str(args.input)
    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(out, encoding="utf-8")
    else:
        print(out)


if __name__ == "__main__":
    main()
