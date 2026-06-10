from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.cliente_service import (
    criar_cliente,
    listar_clientes
)

cliente_bp = Blueprint(
    "cliente",
    __name__
)


@cliente_bp.route("/cliente/novo")
def novo_cliente():

    return render_template(
        "cliente/novo.html"
    )


@cliente_bp.route(
    "/cliente/salvar",
    methods=["POST"]
)
def salvar_cliente():

    criar_cliente(
        nome=request.form["nome"],
        telefone=request.form["telefone"],
        email=request.form["email"],
        como_conheceu=request.form["como_conheceu"]
    )

    return redirect(
        url_for("cliente.listar_clientes_view")
    )


@cliente_bp.route("/clientes")
def listar_clientes_view():

    clientes = listar_clientes()

    return render_template(
        "cliente/lista.html",
        clientes=clientes
    )