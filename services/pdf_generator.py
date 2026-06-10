from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def gerar_pdf_atendimento(atendimento):

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=A4
    )

    y = 800

    pdf.setTitle(
        f"Relatorio_{atendimento.id}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        50,
        y,
        "Relatório de Atendimento"
    )

    y -= 40

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        50,
        y,
        f"Nome: {atendimento.cliente.nome}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Telefone: {atendimento.cliente.telefone}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Email: {atendimento.cliente.email}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Como conheceu: {atendimento.cliente.como_conheceu}"
    )

    y -= 40

    pdf.drawString(
        50,
        y,
        f"Problema: {atendimento.problema}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Necessidade: {atendimento.necessidade}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Objetivo: {atendimento.objetivo}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Interesse: {atendimento.interesse}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Prazo: {atendimento.prazo}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Classificação: {atendimento.classificacao}"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Observações: {atendimento.observacoes}"
    )

    pdf.save()

    buffer.seek(0)

    return buffer