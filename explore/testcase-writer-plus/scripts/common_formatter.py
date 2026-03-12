#!/usr/bin/env python3
import json
import zipfile
from xml.sax.saxutils import escape
from pathlib import Path
from typing import List, Dict


def format_markdown(cases: List[Dict]) -> str:
    chunks = []
    for c in cases:
        chunks.append(
            "\n".join(
                [
                    f"## {c['title']}",
                    "",
                    f"**优先级**: {c['priority']}",
                    f"**类型**: {c['type']}",
                    f"**前置条件**: {c['preconditions']}",
                    f"**测试步骤**: {c['steps']}",
                    "",
                    f"**测试数据**: {c['data']}",
                    "",
                    f"**预期结果**: {c['expected']}",
                    "",
                    f"**实际结果**: {c['actual']}",
                    f"**状态**: {c['status']}",
                    f"**备注**: {c['remark']}",
                ]
            )
        )
    return "# 测试用例输出\n\n" + "\n\n---\n\n".join(chunks) + "\n"


def format_word_text(cases: List[Dict]) -> str:
    lines = ["测试用例输出", "==========", ""]
    for idx, c in enumerate(cases, start=1):
        lines.extend(
            [
                f"{idx}. 用例标题: {c['title']}",
                f"优先级: {c['priority']}",
                f"类型: {c['type']}",
                f"前置条件: {c['preconditions']}",
                f"测试步骤: {c['steps']}",
                f"测试数据: {c['data']}",
                f"预期结果: {c['expected']}",
                f"实际结果: {c['actual']}",
                f"状态: {c['status']}",
                f"备注: {c['remark']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _paragraph_xml(text: str) -> str:
    return (
        "<w:p>"
        "<w:r>"
        "<w:t xml:space=\"preserve\">"
        f"{escape(text)}"
        "</w:t>"
        "</w:r>"
        "</w:p>"
    )


def _build_docx_xml(cases: List[Dict]) -> str:
    lines = ["测试用例输出", ""]
    for idx, c in enumerate(cases, start=1):
        lines.extend(
            [
                f"{idx}. 用例标题: {c['title']}",
                f"优先级: {c['priority']}",
                f"类型: {c['type']}",
                f"前置条件: {c['preconditions']}",
                f"测试步骤: {c['steps']}",
                f"测试数据: {c['data']}",
                f"预期结果: {c['expected']}",
                f"实际结果: {c['actual']}",
                f"状态: {c['status']}",
                f"备注: {c['remark']}",
                "",
            ]
        )
    body = "".join(_paragraph_xml(x) for x in lines)
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
        "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
        "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
        "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
        "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
        "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
        "xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" "
        "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
        "mc:Ignorable=\"w14 wp14\">"
        "<w:body>"
        f"{body}"
        "<w:sectPr><w:pgSz w:w=\"11906\" w:h=\"16838\"/><w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/></w:sectPr>"
        "</w:body>"
        "</w:document>"
    )


def write_word_docx(cases: List[Dict], path: Path) -> None:
    content_types = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
        "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
        "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
        "<Override PartName=\"/word/document.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>"
        "</Types>"
    )
    rels = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"word/document.xml\"/>"
        "</Relationships>"
    )
    document_xml = _build_docx_xml(cases)

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document_xml)


def format_json(cases: List[Dict]) -> str:
    payload = []
    for c in cases:
        payload.append(
            {
                "用例标题": c["title"],
                "优先级": c["priority"],
                "类型": c["type"],
                "前置条件": c["preconditions"],
                "测试步骤": c["steps"],
                "测试数据": c["data"],
                "预期结果": c["expected"],
                "实际结果": c["actual"],
                "状态": c["status"],
                "备注": c["remark"],
            }
        )
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def format_excel_tsv(cases: List[Dict]) -> str:
    rows = ["用例标题\t优先级\t类型\t前置条件\t测试步骤\t测试数据\t预期结果\t实际结果\t状态\t备注"]
    for c in cases:
        row = [
            c["title"],
            c["priority"],
            c["type"],
            c["preconditions"],
            c["steps"],
            c["data"],
            c["expected"],
            c["actual"],
            c["status"],
            c["remark"],
        ]
        rows.append("\t".join(x.replace("\t", " ").replace("\n", " ") for x in row))
    return "\n".join(rows) + "\n"


def write_output(content: str, path: Path) -> None:
    path.write_text(content, encoding="utf-8")
