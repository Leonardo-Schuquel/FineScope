from .financial import entries_list, outputs_list, cumulative_balance
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.colors import Color
from datetime import datetime
import os

# Generates a stylized FinScope financial report.
def gen_financial_pdf(entradas, saidas, saldo_anterior):    

    monthly_balance = sum(i["value"] for i in entradas) - sum(i["value"] for i in saidas)
    total_balance = monthly_balance + saldo_anterior
    now = datetime.now()
    month = now.strftime('%B').capitalize()
    formatted_date = now.strftime('%d/%m/%Y %H:%M')

    # path of the file to be generated and its generation
    os.makedirs("pdf", exist_ok=True)
    way_pdf = f"pdf/Relatório_{month}_{now.year}.pdf"

    # create pdf
    c = canvas.Canvas(way_pdf, pagesize=A4)
    width, height = A4

    # File presentation
    slogan = Color(0.6, 0.6, 0.6, alpha=0.4)
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(slogan)
    c.drawString(1.5 * cm, height - 1 * cm, "Controle inteligente começa com organização.")
    c.setFillColor(colors.black)

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 2.5 * cm, "FinScope — Relatório Financeiro")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 3.2 * cm, f"Mês: {month} de {now.year}")

    # current month's summary block
    y = height - 5 * cm
    c.setFont("Helvetica", 12)
    summary = [
        ("Mês", now.strftime('%m/%Y')),
        ("Entradas", f"R$ {sum(i['value'] for i in entradas):.2f}"),
        ("Saídas", f"R$ {sum(i['value'] for i in saidas):.2f}"),
        ("Saldo do Mês", f"R$ {monthly_balance:.2f}"),
        ("Saldo do Mês anterior", f"R$ {saldo_anterior:.2f}")
    ]
    
    for label, value in summary:
        features(c, label, value, y, width)
        y -= 0.6 * cm

    # input block
    y -= 0.4 * cm
    separator(c, y, width)
    y -= 1 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "Entradas:")
    y -= 0.6 * cm
    c.setFont("Helvetica", 12)
    for item in entradas:
        event = f"{item['name_event']}"
        value_event = str(f"R$ {item['value']:.2f}")
        features(c, event, value_event, y, width)
        y -= 0.6 * cm

    # Output block
    y -= 0.4 * cm
    separator(c, y, width)
    y -= 1 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "Saídas:")
    y -= 0.6 * cm
    c.setFont("Helvetica", 12)
    for item in saidas:
        event = f"{item['name_event']}"
        value_event = str(f"R$ {item['value']}")
        features(c, event, value_event, y, width)
        y -= 0.6 * cm

    # complete final summary
    y -= 0.4 * cm
    separator(c, y, width)
    y -= 1.2 * cm
    c.setFont("Helvetica-Bold", 12)
    summary_months = [
        ("Saldo do Mês", f"R$ {monthly_balance:.2f}"),
        ("Saldo Anterior", f"R$ {saldo_anterior:.2f}"),
        ("Saldo Total", f"R$ {total_balance:.2f}")
    ]
    for label, value in summary_months:
        features(c, label, value, y, width)
        y -= 0.6 * cm

    # plinth
    c.setFont("Helvetica-Oblique", 9)
    plinth = f"FinScope © 2025 • Criado por Leonardo Schuquel • Gerado em {formatted_date}"
    c.drawCentredString(width / 2, 1.5 * cm, plinth)

    c.save()
    print(f"✅ PDF gerado com sucesso: {way_pdf}")

def features(c, label, valor, y, largura, fonte="Helvetica", tamanho=12):
    label = str(label)
    valor = str(valor)
    c.setFont(fonte, tamanho)
    margin = 2 * cm
    total_width = largura - 4 * cm
    label_width = c.stringWidth(label, fonte, tamanho)
    width_value = c.stringWidth(valor, fonte, tamanho)
    avaliable_width = total_width - (label_width + width_value)
    num_strokes = max(3, int(avaliable_width / c.stringWidth("-", fonte, tamanho)) - 5)
    line = f"{label} " + "-" * num_strokes
    c.drawString(margin, y, line)
    c.drawRightString(largura - margin, y, valor)

def separator(c, y, largura, margem=2 * cm):
    c.line (margem, y, largura - margem, y)

