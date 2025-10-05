# report.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.colors import Color
from datetime import datetime
from pathlib import Path
import utils

def gen_financial_pdf(saldo_anterior: float | None = None):
    """
    Generates a PDF with the entries in the JSON file (supports formats:
    - list of entries (old MVP)
    - dictionary by month -> { “MM/YYYY”: [ ... ] }

    previous_balance: if None, utils.total_balance() will be attempted
    """
    # Loads data (can be list or dict)
    transactions = utils.loadJson()

    # Normalizes to a list of entries
    all_transactions = []
    if transactions is None:
        transactions = {}

    if isinstance(transactions, dict):
        for month, launches in transactions.items():
            if isinstance(launches, list):
                all_transactions.extend(launches)
    elif isinstance(transactions, list):
        all_transactions = list(transactions)
    else:
        all_transactions = []

    # Ensures that values are floats
    normalized = []
    for t in all_transactions:
        item = dict(t)
        if 'title' not in item and 'name_event' in item:
            item['title'] = item.get('name_event')

        raw_value = item.get('value', 0)
        try:
            item['value'] = float(str(raw_value).replace(',', '.'))
        except Exception:
            item['value'] = 0.0

        item['event'] = item.get('event', '')
        item['date_time'] = item.get('date_time', '')
        item['id'] = item.get('id', '')
        normalized.append(item)

    entradas = [t for t in normalized if t.get('event') == "Entrada"]
    saidas = [t for t in normalized if t.get('event') == "Saida"]

    total_entradas = sum(i['value'] for i in entradas)
    total_saidas = sum(i['value'] for i in saidas)
    monthly_balance = total_entradas - total_saidas

    if saldo_anterior is None:
        try:
            saldo_anterior = float(str(utils.total_balance()).replace(',', '.'))
        except Exception:
            saldo_anterior = 0.0

    total_balance = monthly_balance + saldo_anterior

    now = datetime.now()
    month = now.strftime('%B').capitalize()
    formatted_date = now.strftime('%d/%m/%Y %H:%M')

    # Output folder: Documents/FineScope/Reports
    documentos = Path.home() / "Documentos" / "FineScope" / "Relatorios"
    documentos.mkdir(parents=True, exist_ok=True)
    way_pdf = documentos / f"Relatorio_{month}_{now.year}.pdf"

    # Create PDF
    c = canvas.Canvas(str(way_pdf), pagesize=A4)
    width, height = A4

    # Header
    slogan = Color(0.6, 0.6, 0.6, alpha=0.4)
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(slogan)
    c.drawString(1.5 * cm, height - 1 * cm, "Controle inteligente começa com organização.")
    c.setFillColor(colors.black)

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 2.5 * cm, "FineScope — Relatório Financeiro")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 3.2 * cm, f"Mês: {month} de {now.year}")

    # Summary
    y = height - 5 * cm
    c.setFont("Helvetica", 12)
    summary = [
        ("Mês", now.strftime('%m/%Y')),
        ("Entradas", f"R$ {total_entradas:.2f}"),
        ("Saídas", f"R$ {total_saidas:.2f}"),
        ("Saldo do Mês", f"R$ {monthly_balance:.2f}"),
        ("Saldo do Mês anterior", f"R$ {saldo_anterior:.2f}")
    ]

    for label, value in summary:
        features(c, label, value, y, width)
        y -= 0.6 * cm

    # Entries
    if entradas:
        y = print_section(c, "Entradas:", entradas, y, width, height)

    # Outings
    if saidas:
        y = print_section(c, "Saídas:", saidas, y, width, height)

   # Final summary
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

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    plinth = f"FineScope © {now.year} • Criado por Leonardo Schuquel • Gerado em {formatted_date}"
    c.drawCentredString(width / 2, 1.5 * cm, plinth)

    c.save()
    print(f"✅ PDF gerado em: {way_pdf}")
    return str(way_pdf)


def features(c, label, valor, y, largura, fonte="Helvetica", tamanho=12):
    """Line with label, separator, and value on the right"""
    label = str(label)
    valor = str(valor)
    c.setFont(fonte, tamanho)
    margin = 2 * cm
    total_width = largura - 4 * cm
    label_width = c.stringWidth(label, fonte, tamanho)
    width_value = c.stringWidth(valor, fonte, tamanho)
    avaliable_width = total_width - (label_width + width_value)

    if avaliable_width < 6:
        num_strokes = 3
    else:
        num_strokes = max(3, int(avaliable_width / c.stringWidth("-", fonte, tamanho)) - 5)

    line = f"{label} " + "-" * num_strokes
    c.drawString(margin, y, line)
    c.drawRightString(largura - margin, y, valor)


def separator(c, y, largura, margem=2 * cm):
    """Separator line"""
    c.line(margem, y, largura - margem, y)


def print_section(c, title, items, y, width, height):
    """Prints a section of entries (incoming or outgoing)"""
    y -= 0.4 * cm
    separator(c, y, width)
    y -= 1 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, title)
    y -= 0.6 * cm
    c.setFont("Helvetica", 12)

    for item in items:
        event = str(item.get('title', item.get('name_event', '')))
        value_event = f"R$ {item.get('value', 0.0):.2f}"
        features(c, event, value_event, y, width)
        y -= 0.6 * cm
        if y < 3.5 * cm:
            c.showPage()
            y = height - 2.5 * cm
    return y
