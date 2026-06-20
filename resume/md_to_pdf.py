from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import re

INPUT_FILE = "/Users/syedibrahim/Documents/Syed_Ibrahim_CV_2026_Dublin.md"
OUTPUT_FILE = "/Users/syedibrahim/Documents/Syed_Ibrahim_CV_2026_Dublin.pdf"

def parse_md_to_pdf():
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    doc = SimpleDocTemplate(OUTPUT_FILE, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=15*mm, bottomMargin=15*mm)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Name', fontSize=20, leading=24, alignment=TA_CENTER, spaceAfter=2))
    styles.add(ParagraphStyle(name='Subtitle', fontSize=11, leading=14, alignment=TA_CENTER, textColor=HexColor('#444444')))
    styles.add(ParagraphStyle(name='Contact', fontSize=9, leading=12, alignment=TA_CENTER, textColor=HexColor('#555555')))
    styles.add(ParagraphStyle(name='SectionHead', fontSize=13, leading=16, spaceBefore=10, spaceAfter=4, textColor=HexColor('#1a1a1a'), fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='SubHead', fontSize=11, leading=14, spaceBefore=8, spaceAfter=2, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='SubSubHead', fontSize=10, leading=13, spaceBefore=6, spaceAfter=2, fontName='Helvetica-BoldOblique'))
    styles.add(ParagraphStyle(name='Body', fontSize=9.5, leading=13, spaceAfter=2))
    styles.add(ParagraphStyle(name='CVBullet', fontSize=9.5, leading=13, leftIndent=12, spaceAfter=2, bulletIndent=0))
    styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

    story = []

    def fmt(text):
        """Convert markdown bold/italic to reportlab markup"""
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
        return text

    i = 0
    in_table = False
    table_rows = []

    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Horizontal rule
        if line.strip() == '---':
            story.append(Spacer(1, 3*mm))
            story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#cccccc')))
            story.append(Spacer(1, 3*mm))
            i += 1
            continue

        # Table handling
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            # Skip separator rows
            if all(re.match(r'^[-:]+$', c) for c in cells):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append([Paragraph(fmt(c), styles['TableCell']) for c in cells])
            i += 1
            # Check if next line is still table
            if i >= len(lines) or '|' not in lines[i] or not lines[i].strip().startswith('|'):
                in_table = False
                if table_rows:
                    t = Table(table_rows, colWidths=[35*mm, None])
                    t.setStyle(TableStyle([
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('TOPPADDING', (0, 0), (-1, -1), 2),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                    ]))
                    story.append(t)
                    story.append(Spacer(1, 3*mm))
            continue

        # H1 - Name
        if line.startswith('# ') and not line.startswith('## '):
            story.append(Paragraph(line[2:].strip(), styles['Name']))
            i += 1
            continue

        # H2 - Section headers
        if line.startswith('## '):
            story.append(Paragraph(fmt(line[3:].strip()), styles['SectionHead']))
            i += 1
            continue

        # H3 - Company/Role
        if line.startswith('### '):
            story.append(Paragraph(fmt(line[4:].strip()), styles['SubHead']))
            i += 1
            continue

        # H4 - Sub-roles
        if line.startswith('#### '):
            story.append(Paragraph(fmt(line[5:].strip()), styles['SubSubHead']))
            i += 1
            continue

        # Bullet points
        if line.strip().startswith('- '):
            text = fmt(line.strip()[2:])
            story.append(Paragraph(f"• {text}", styles['CVBullet']))
            i += 1
            continue

        # Bold subtitle line (like **Senior Java...**)
        if line.strip().startswith('**') and line.strip().endswith('**'):
            text = line.strip()[2:-2]
            story.append(Paragraph(text, styles['Subtitle']))
            i += 1
            continue

        # Regular paragraph
        story.append(Paragraph(fmt(line.strip()), styles['Body']))
        i += 1

    doc.build(story)
    print(f"PDF generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    parse_md_to_pdf()
