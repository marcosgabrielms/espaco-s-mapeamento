from flask import (
    Blueprint,
    render_template
)

from models import (
    Cliente,
    Atendimento
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/dashboard")
def dashboard():

    total_clientes = Cliente.query.count()

    prioritarios = Atendimento.query.filter_by(
        classificacao="Cliente Prioritário"
    ).count()

    acompanhamento = Atendimento.query.filter_by(
        classificacao="Cliente em Acompanhamento"
    ).count()

    analise = Atendimento.query.filter_by(
        classificacao="Cliente em Análise"
    ).count()

    return render_template(
        "dashboard/index.html",

        total_clientes=total_clientes,

        prioritarios=prioritarios,

        acompanhamento=acompanhamento,

        analise=analise
    )