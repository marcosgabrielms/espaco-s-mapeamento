from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from models import Atendimento
from flask import send_file

from services.pdf_generator import (
    gerar_pdf_atendimento
)

from services.cliente_service import (
    buscar_cliente
)

from services.atendimento_service import (
    criar_atendimento
)

atendimento_bp = Blueprint(
    "atendimento",
    __name__
)


@atendimento_bp.route(
    "/atendimento/novo/<int:cliente_id>"
)
def novo_atendimento(cliente_id):

    cliente = buscar_cliente(
        cliente_id
    )

    return render_template(
        "atendimento/novo.html",
        cliente=cliente
    )

@atendimento_bp.route(
    "/atendimento/salvar",
    methods=["POST"]
)
def salvar_atendimento():

    atendimento = criar_atendimento(

        cliente_id=request.form["cliente_id"],

        problema=request.form["problema"],

        necessidade=request.form["necessidade"],

        objetivo=request.form["objetivo"],

        interesse=request.form["interesse"],

        prazo=request.form["prazo"],

        observacoes=request.form["observacoes"]
    )

    return redirect(
        url_for(
            "atendimento.relatorio",
            atendimento_id=atendimento.id
        )
    )

@atendimento_bp.route(
    "/relatorio/<int:atendimento_id>"
)
def relatorio(atendimento_id):

    atendimento = Atendimento.query.get_or_404(
        atendimento_id
    )

    return render_template(
        "atendimento/relatorio.html",
        atendimento=atendimento
    )

@atendimento_bp.route(
    "/relatorio/pdf/<int:atendimento_id>"
)
def gerar_pdf(atendimento_id):

    atendimento = Atendimento.query.get_or_404(
        atendimento_id
    )

    pdf = gerar_pdf_atendimento(
        atendimento
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name=f"relatorio_{atendimento.id}.pdf",
        mimetype="application/pdf"
    )