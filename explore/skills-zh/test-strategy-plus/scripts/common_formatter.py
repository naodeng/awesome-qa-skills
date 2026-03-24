#!/usr/bin/env python3
import json
import zipfile
from xml.sax.saxutils import escape
from pathlib import Path
from typing import Dict


def strategy_to_lines(strategy: Dict[str, str]) -> list[str]:
    ordered_keys = [
        "策略标题",
        "质量目标",
        "范围_包含",
        "范围_不包含",
        "测试类型与覆盖",
        "环境与工具",
        "测试数据策略",
        "准入准出标准",
        "风险与缓解",
        "里程碑与角色",
        "交付物与度量",
    ]
    lines = ["测试策略输出", ""]
    for k in ordered_keys:
        lines.append(f"{k}: {strategy.get(k, '')}")
    return lines


def format_markdown(strategy: Dict[str, str]) -> str:
    return "\n".join(
        [
            "# 测试策略输出",
            "",
            f"## {strategy['策略标题']}",
            "",
            "### 质量目标",
            f"- {strategy['质量目标']}",
            "",
            "### 范围定义",
            f"- In Scope: {strategy['范围_包含']}",
            f"- Out of Scope: {strategy['范围_不包含']}",
            "",
            "### 测试类型与覆盖",
            f"- {strategy['测试类型与覆盖']}",
            "",
            "### 环境与工具",
            f"- {strategy['环境与工具']}",
            "",
            "### 测试数据策略",
            f"- {strategy['测试数据策略']}",
            "",
            "### 准入/准出标准",
            f"- {strategy['准入准出标准']}",
            "",
            "### 风险与缓解",
            f"- {strategy['风险与缓解']}",
            "",
            "### 里程碑与角色",
            f"- {strategy['里程碑与角色']}",
            "",
            "### 交付物与度量",
            f"- {strategy['交付物与度量']}",
            "",
        ]
    )


def format_json(strategy: Dict[str, str]) -> str:
    return json.dumps(strategy, ensure_ascii=False, indent=2) + "\n"


def format_excel_tsv(strategy: Dict[str, str]) -> str:
    rows = ["模块\t内容"]
    for key, value in strategy.items():
        rows.append(f"{key}\t{str(value).replace('\t', ' ').replace('\n', ' ')}")
    return "\n".join(rows) + "\n"


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


def _build_docx_xml(strategy: Dict[str, str]) -> str:
    body = "".join(_paragraph_xml(x) for x in strategy_to_lines(strategy))
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


def write_word_docx(strategy: Dict[str, str], path: Path) -> None:
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
    document_xml = _build_docx_xml(strategy)

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document_xml)


def write_output(content: str, path: Path) -> None:
    path.write_text(content, encoding="utf-8")
