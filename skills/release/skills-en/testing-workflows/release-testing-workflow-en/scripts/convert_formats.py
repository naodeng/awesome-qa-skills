#!/usr/bin/env python3
import argparse
import csv
import json
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


# ---- parsing ----
def parse_markdown(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    headings: list[dict[str, Any]] = []
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m:
            headings.append({"level": len(m.group(1)), "title": m.group(2).strip()})
    return {"title": headings[0]["title"] if headings else path.stem, "headings": headings, "text": text}


def parse_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    return {"title": path.stem, "data": data}


def parse_csv_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return {"title": path.stem, "columns": reader.fieldnames or [], "rows": rows}


def parse_docx(path: Path) -> dict[str, Any]:
    paragraphs: list[str] = []
    with zipfile.ZipFile(path) as zf:
        with zf.open("word/document.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    for p in root.findall(".//w:p", ns):
        texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
        s = "".join(texts).strip()
        if s:
            paragraphs.append(s)
    return {"title": path.stem, "paragraphs": paragraphs}


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    out: list[str] = []
    try:
        with zf.open("xl/sharedStrings.xml") as f:
            root = ET.fromstring(f.read())
        ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        for si in root.findall(".//a:si", ns):
            out.append("".join((t.text or "") for t in si.findall(".//a:t", ns)))
    except KeyError:
        pass
    return out


def parse_xlsx(path: Path) -> dict[str, Any]:
    rows: list[list[str]] = []
    with zipfile.ZipFile(path) as zf:
        shared = _shared_strings(zf)
        with zf.open("xl/worksheets/sheet1.xml") as f:
            root = ET.fromstring(f.read())
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    for row in root.findall(".//a:sheetData/a:row", ns):
        vals = []
        for c in row.findall("a:c", ns):
            t = c.attrib.get("t")
            v = c.find("a:v", ns)
            if v is None or v.text is None:
                vals.append("")
            elif t == "s":
                idx = int(v.text)
                vals.append(shared[idx] if 0 <= idx < len(shared) else "")
            else:
                vals.append(v.text)
        rows.append(vals)
    return {"title": path.stem, "rows": rows}


def parse_xmind(path: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        topics: list[str] = []
        if "content.json" in names:
            data = json.loads(zf.read("content.json").decode("utf-8", errors="ignore"))

            def walk(node: Any):
                if isinstance(node, dict):
                    t = node.get("title")
                    if isinstance(t, str) and t.strip():
                        topics.append(t.strip())
                    for k in ("children", "topics", "rootTopic", "attached"):
                        walk(node.get(k))
                elif isinstance(node, list):
                    for i in node:
                        walk(i)

            walk(data)
        elif "content.xml" in names:
            root = ET.fromstring(zf.read("content.xml"))
            topics = [e.text.strip() for e in root.findall(".//title") if e.text and e.text.strip()]
        else:
            raise ValueError("Unsupported XMind package structure")
    return {"title": topics[0] if topics else path.stem, "topics": topics}


def detect_in_format(path: Path, forced: str | None) -> str:
    if forced and forced != "auto":
        return forced
    return {
        ".md": "markdown",
        ".markdown": "markdown",
        ".json": "json",
        ".csv": "csv",
        ".docx": "word",
        ".xlsx": "excel",
        ".xmind": "xmind",
        ".tsv": "excel",
    }.get(path.suffix.lower(), "markdown")


def normalize(parsed: dict[str, Any]) -> dict[str, Any]:
    title = parsed.get("title") or "QA Output"
    sections: list[dict[str, Any]] = []

    if "text" in parsed:
        sections.append({"name": "content", "items": [{"key": "text", "value": parsed["text"]}]})
    if "headings" in parsed:
        sections.append({"name": "headings", "items": [{"key": "heading", "value": h.get("title", "")} for h in parsed["headings"]]})
    if "data" in parsed:
        data = parsed["data"]
        if isinstance(data, dict):
            items = [{"key": k, "value": v} for k, v in list(data.items())[:100]]
            sections.append({"name": "json_object", "items": items})
        elif isinstance(data, list):
            sections.append({"name": "json_array", "items": [{"key": "row", "value": v} for v in data[:200]]})
        else:
            sections.append({"name": "json_value", "items": [{"key": "value", "value": data}]})
    if "rows" in parsed:
        rows = parsed["rows"]
        sections.append({"name": "rows", "items": [{"key": f"row_{i+1}", "value": r} for i, r in enumerate(rows[:200])]})
    if "columns" in parsed:
        sections.append({"name": "columns", "items": [{"key": "column", "value": c} for c in parsed["columns"]]})
    if "paragraphs" in parsed:
        sections.append({"name": "paragraphs", "items": [{"key": f"p{i+1}", "value": p} for i, p in enumerate(parsed["paragraphs"][:200])]})
    if "topics" in parsed:
        sections.append({"name": "topics", "items": [{"key": "topic", "value": t} for t in parsed["topics"][:300]]})

    return {"title": title, "sections": sections}


# ---- writers ----
def write_json(model: dict[str, Any], output: Path) -> None:
    output.write_text(json.dumps(model, ensure_ascii=False, indent=2), encoding="utf-8")


def _scalar(v: Any) -> str:
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def write_csv(model: dict[str, Any], output: Path) -> None:
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["section", "key", "value"])
        for s in model.get("sections", []):
            for item in s.get("items", []):
                writer.writerow([s.get("name", ""), item.get("key", ""), _scalar(item.get("value", ""))])


def write_excel_tsv(model: dict[str, Any], output: Path) -> None:
    lines = ["Section\tKey\tValue"]
    for s in model.get("sections", []):
        for item in s.get("items", []):
            lines.append(f"{s.get('name','')}\t{item.get('key','')}\t{_scalar(item.get('value','')).replace(chr(9), ' ')}")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown(model: dict[str, Any], output: Path) -> None:
    lines = [f"# {model.get('title', 'QA Output')}", ""]
    for s in model.get("sections", []):
        lines.append(f"## {s.get('name', 'section')}")
        for item in s.get("items", []):
            lines.append(f"- **{item.get('key','key')}**: {_scalar(item.get('value',''))}")
        lines.append("")
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_word_md(model: dict[str, Any], output: Path) -> None:
    lines = [model.get("title", "QA Output"), "=" * len(model.get("title", "QA Output")), ""]
    idx = 1
    for s in model.get("sections", []):
        lines.append(f"{idx}. {s.get('name', 'section').replace('_', ' ').title()}")
        for item in s.get("items", []):
            lines.append(f"- {item.get('key','key')}: {_scalar(item.get('value',''))}")
        lines.append("")
        idx += 1
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_xmind_md(model: dict[str, Any], output: Path) -> None:
    lines = [f"# {model.get('title', 'QA Output')}", "", f"- {model.get('title', 'QA Output')}"]
    for s in model.get("sections", []):
        lines.append(f"  - {s.get('name', 'section')}")
        for item in s.get("items", []):
            lines.append(f"    - {item.get('key','key')}: {_scalar(item.get('value',''))}")
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def default_output(input_path: Path, to_fmt: str) -> Path:
    ext = {
        "json": ".json",
        "csv": ".csv",
        "excel": ".tsv",
        "markdown": ".md",
        "word": ".word.md",
        "xmind": ".xmind.md",
    }[to_fmt]
    return input_path.with_name(input_path.stem + ".converted" + ext)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert QA output files between common formats")
    parser.add_argument("input", type=Path, help="Input file path")
    parser.add_argument("--from", dest="from_fmt", default="auto", choices=["auto", "word", "excel", "xmind", "json", "csv", "markdown"])
    parser.add_argument("--to", required=True, choices=["word", "excel", "xmind", "json", "csv", "markdown"])
    parser.add_argument("--output", type=Path, help="Output file path")
    args = parser.parse_args()

    in_fmt = detect_in_format(args.input, args.from_fmt)
    if in_fmt == "word":
        parsed = parse_docx(args.input)
    elif in_fmt == "excel":
        if args.input.suffix.lower() == ".tsv":
            rows = [line.rstrip("\n").split("\t") for line in args.input.read_text(encoding="utf-8", errors="ignore").splitlines() if line]
            parsed = {"title": args.input.stem, "rows": rows}
        else:
            parsed = parse_xlsx(args.input)
    elif in_fmt == "xmind":
        parsed = parse_xmind(args.input)
    elif in_fmt == "json":
        parsed = parse_json(args.input)
    elif in_fmt == "csv":
        parsed = parse_csv_file(args.input)
    else:
        parsed = parse_markdown(args.input)

    model = normalize(parsed)
    output = args.output or default_output(args.input, args.to)

    if args.to == "json":
        write_json(model, output)
    elif args.to == "csv":
        write_csv(model, output)
    elif args.to == "excel":
        write_excel_tsv(model, output)
    elif args.to == "markdown":
        write_markdown(model, output)
    elif args.to == "word":
        write_word_md(model, output)
    else:
        write_xmind_md(model, output)

    print(str(output))


if __name__ == "__main__":
    main()
