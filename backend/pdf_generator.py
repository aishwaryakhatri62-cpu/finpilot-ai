from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import fonts
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def generate_payslip(name, base, overtime, bonus, deductions, gross, tax, net):
    file_name = f"{name}_payslip.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    elements.append(Paragraph("<b>FinPilot AI - Salary Payslip</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    data = [
        ["Employee Name", name],
        ["Base Salary", base],
        ["Overtime Hours", overtime],
        ["Bonus", bonus],
        ["Deductions", deductions],
        ["Gross Salary", gross],
        ["Tax (10%)", tax],
        ["Net Salary", net],
    ]

    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph("Authorized Signature: ____________________", styles["Normal"]))

    doc.build(elements)
    return file_name
