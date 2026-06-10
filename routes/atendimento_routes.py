from flask import (
    Blueprint,
    render_template
)

from services.cliente_service import (
    buscar_cliente
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