#!/usr/bin/env python3
"""Regenerate docs/smartpick-databricks-onboarding-guide.pdf from the markdown source.

Usage (with ~/pdf_env):
    source ~/pdf_env/bin/activate
    python docs/generate_onboarding_pdf.py
"""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

REPO_ROOT = Path(__file__).resolve().parent.parent
MD_PATH = REPO_ROOT / "docs" / "smartpick-databricks-onboarding-guide.md"
PDF_PATH = REPO_ROOT / "docs" / "smartpick-databricks-onboarding-guide.pdf"


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_pdf(md_path: Path, pdf_path: Path) -> None:
    lines = md_path.read_text(encoding="utf-8").splitlines()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocH1",
            parent=styles["Heading1"],
            fontSize=18,
            spaceAfter=12,
            spaceBefore=16,
        )
    )
    styles.add(
        ParagraphStyle(
            name="DocH2",
            parent=styles["Heading2"],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="DocH3",
            parent=styles["Heading3"],
            fontSize=12,
            spaceAfter=6,
            spaceBefore=8,
        )
    )
    styles.add(ParagraphStyle(name="DocBody", parent=styles["Normal"], fontSize=10, leading=14))
    styles.add(
        ParagraphStyle(
            name="DocCode",
            parent=styles["Normal"],
            fontName="Courier",
            fontSize=8,
            leading=10,
            backColor=colors.HexColor("#f5f5f5"),
        )
    )

    story: list = []
    in_code = False
    code_buf: list[str] = []

    def flush_code() -> None:
        nonlocal code_buf
        if code_buf:
            story.append(Preformatted("\n".join(code_buf), styles["DocCode"]))
            story.append(Spacer(1, 6))
            code_buf = []

    for line in lines:
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 6))
            continue
        if line.startswith("# "):
            story.append(Paragraph(esc(line[2:]), styles["DocH1"]))
            continue
        if line.startswith("## "):
            story.append(Paragraph(esc(line[3:]), styles["DocH2"]))
            continue
        if line.startswith("### "):
            story.append(Paragraph(esc(line[4:]), styles["DocH3"]))
            continue
        if line.startswith("|") and "---" in line:
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            story.append(
                Paragraph(
                    '<font name="Courier" size="9">' + esc(" | ".join(cells)) + "</font>",
                    styles["DocBody"],
                )
            )
            continue
        if line.startswith("- [ ]"):
            story.append(Paragraph("[ ] " + esc(line[5:].strip()), styles["DocBody"]))
            continue
        if line.startswith("- "):
            story.append(Paragraph("&bull; " + esc(line[2:]), styles["DocBody"]))
            continue
        if line.startswith("---"):
            story.append(Spacer(1, 8))
            continue
        text = esc(re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line.replace("`", "")))
        # Strip markdown links to plain text for PDF readability
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        story.append(Paragraph(text, styles["DocBody"]))

    if code_buf:
        flush_code()

    doc.build(story)


def main() -> None:
    build_pdf(MD_PATH, PDF_PATH)
    print(f"Wrote {PDF_PATH} ({PDF_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
