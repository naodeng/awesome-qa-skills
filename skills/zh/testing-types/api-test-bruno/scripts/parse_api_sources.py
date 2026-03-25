#!/usr/bin/env python3
import argparse
import json
import re
import zipfile
from pathlib import Path
from typing import Dict, List, Optional
from xml.etree import ElementTree as ET

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}


def _safe_text(raw: bytes) -> str:
    return raw.decode("utf-8", errors="ignore")


def _append_endpoint(out: List[Dict], method: str, path: str, source: str, **extra) -> None:
    method = method.upper().strip()
    path = (path or "").strip()
    if method not in METHODS or not path:
        return
    rec = {"method": method, "path": path, "source": source}
    rec.update({k: v for k, v in extra.items() if v is not None})
    out.append(rec)


def _parse_curl(text: str, source: str) -> List[Dict]:
    out: List[Dict] = []
    for line in [x.strip() for x in text.splitlines() if "curl " in x]:
        m_method = re.search(r"-X\s+([A-Za-z]+)", line)
        method = m_method.group(1).upper() if m_method else "GET"
        m_url = re.search(r"(https?://[^\s'\"\\]+)", line)
        if not m_url:
            continue
        url = m_url.group(1)
        m_path = re.match(r"https?://[^/]+(.*)", url)
        path = m_path.group(1) if m_path else "/"
        if not path:
            path = "/"
        _append_endpoint(out, method, path, source, raw_url=url, format="curl")
    return out


def _parse_postman(obj: Dict, source: str) -> List[Dict]:
    out: List[Dict] = []

    def walk(items: List[Dict]) -> None:
        for it in items or []:
            if "request" in it:
                req = it.get("request", {})
                method = str(req.get("method", "GET")).upper()
                url_obj = req.get("url", {})
                path = "/"
                raw_url = None
                if isinstance(url_obj, dict):
                    raw_url = url_obj.get("raw")
                    path_parts = url_obj.get("path")
                    if isinstance(path_parts, list) and path_parts:
                        path = "/" + "/".join(str(p) for p in path_parts)
                    elif isinstance(raw_url, str):
                        m = re.match(r"https?://[^/]+(.*)", raw_url)
                        path = m.group(1) if m and m.group(1) else "/"
                elif isinstance(url_obj, str):
                    raw_url = url_obj
                    m = re.match(r"https?://[^/]+(.*)", url_obj)
                    path = m.group(1) if m and m.group(1) else "/"
                _append_endpoint(out, method, path, source, raw_url=raw_url, format="postman")
            if isinstance(it.get("item"), list):
                walk(it["item"])

    walk(obj.get("item", []))
    return out


def _parse_openapi(obj: Dict, source: str) -> List[Dict]:
    out: List[Dict] = []
    paths = obj.get("paths", {})
    if not isinstance(paths, dict):
        return out
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for m in methods.keys():
            method = str(m).upper()
            if method in METHODS:
                _append_endpoint(out, method, str(path), source, format="openapi")
    return out


def _parse_insomnia(obj: Dict, source: str) -> List[Dict]:
    out: List[Dict] = []
    resources = obj.get("resources", [])
    if not isinstance(resources, list):
        return out
    for r in resources:
        if not isinstance(r, dict):
            continue
        if r.get("_type") == "request":
            method = str(r.get("method", "GET")).upper()
            url = str(r.get("url", ""))
            path = "/"
            m = re.match(r"https?://[^/]+(.*)", url)
            if m and m.group(1):
                path = m.group(1)
            elif url.startswith("/"):
                path = url
            _append_endpoint(out, method, path, source, raw_url=url, format="insomnia")
    return out


def _parse_opencollection(obj: Dict, source: str) -> List[Dict]:
    out: List[Dict] = []
    requests = obj.get("requests")
    if isinstance(requests, list):
        for r in requests:
            if not isinstance(r, dict):
                continue
            method = str(r.get("method", "GET")).upper()
            path = str(r.get("path") or r.get("url") or "/")
            _append_endpoint(out, method, path, source, format="opencollection")
    return out


def _parse_wsdl(text: str, source: str) -> List[Dict]:
    out: List[Dict] = []
    try:
        root = ET.fromstring(text.encode("utf-8"))
    except Exception:
        return out
    ns = {
        "wsdl": "http://schemas.xmlsoap.org/wsdl/",
        "soap": "http://schemas.xmlsoap.org/wsdl/soap/",
    }
    soap_address = root.find(".//soap:address", ns)
    location = soap_address.attrib.get("location") if soap_address is not None else None
    for op in root.findall(".//wsdl:operation", ns):
        name = op.attrib.get("name")
        if not name:
            continue
        path = f"/soap/{name}"
        _append_endpoint(out, "POST", path, source, raw_url=location, format="wsdl", operation=name)
    return out


def _parse_bruno(text: str, source: str) -> List[Dict]:
    out: List[Dict] = []
    method = None
    url = None
    for line in text.splitlines():
        s = line.strip()
        block = re.match(r"^(get|post|put|patch|delete|head|options)\s*\{", s, re.IGNORECASE)
        if block:
            method = block.group(1).upper()
            continue
        m = re.match(r"method:\s*([A-Za-z]+)", s, re.IGNORECASE)
        if m:
            method = m.group(1).upper()
            continue
        u = re.match(r"url:\s*(.+)$", s, re.IGNORECASE)
        if u:
            url = u.group(1).strip()
    if method and url:
        m = re.match(r"https?://[^/]+(.*)", url)
        path = m.group(1) if m and m.group(1) else (url if url.startswith("/") else f"/{url}")
        _append_endpoint(out, method, path, source, raw_url=url, format="bruno")
    return out


def _load_structured(path: Path, raw: str) -> Optional[Dict]:
    if path.suffix.lower() == ".json":
        try:
            return json.loads(raw)
        except Exception:
            return None
    if path.suffix.lower() in {".yaml", ".yml"} and yaml is not None:
        try:
            obj = yaml.safe_load(raw)
            return obj if isinstance(obj, dict) else None
        except Exception:
            return None
    return None


def parse_file(path: Path, raw: str) -> List[Dict]:
    lower_name = path.name.lower()
    ext = path.suffix.lower()

    if ext == ".wsdl" or (ext == ".xml" and "<definitions" in raw and "wsdl" in raw.lower()):
        return _parse_wsdl(raw, str(path))
    if ext == ".bru":
        return _parse_bruno(raw, str(path))
    if ext in {".curl", ".sh", ".txt"}:
        return _parse_curl(raw, str(path))

    obj = _load_structured(path, raw)
    if obj is not None:
        if "openapi" in obj or "swagger" in obj:
            return _parse_openapi(obj, str(path))
        if lower_name.endswith(".postman_collection.json") or "info" in obj and "item" in obj:
            return _parse_postman(obj, str(path))
        if "resources" in obj:
            return _parse_insomnia(obj, str(path))
        if lower_name.endswith(".opencollection.json") or "requests" in obj:
            return _parse_opencollection(obj, str(path))
        return []

    return _parse_curl(raw, str(path))


def parse_zip(path: Path) -> List[Dict]:
    out: List[Dict] = []
    with zipfile.ZipFile(path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            p = Path(info.filename)
            raw = _safe_text(zf.read(info))
            if p.suffix.lower() == ".zip":
                continue
            out.extend(parse_file(p, raw))
    return out


def parse_input(path: Path) -> List[Dict]:
    if path.is_dir():
        out: List[Dict] = []
        for f in path.rglob("*"):
            if f.is_file():
                raw = f.read_text(encoding="utf-8", errors="ignore")
                out.extend(parse_file(f, raw))
        return out
    if path.suffix.lower() == ".zip":
        return parse_zip(path)
    raw = path.read_text(encoding="utf-8", errors="ignore")
    return parse_file(path, raw)


def dedupe(endpoints: List[Dict]) -> List[Dict]:
    seen = set()
    out = []
    for e in endpoints:
        key = (e.get("method"), e.get("path"), e.get("source"))
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse API sources into normalized endpoint inventory")
    parser.add_argument("--input", required=True, type=Path, help="Input file/folder/zip path")
    parser.add_argument("--output", type=Path, help="Output JSON path")
    args = parser.parse_args()

    endpoints = dedupe(parse_input(args.input))
    payload = {
        "input": str(args.input),
        "count": len(endpoints),
        "endpoints": endpoints,
    }

    if args.output:
        args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(str(args.output))
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
