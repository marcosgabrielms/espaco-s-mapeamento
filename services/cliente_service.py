from models import Cliente
from models import db


def criar_cliente(
    nome,
    telefone,
    email,
    como_conheceu
):

    cliente = Cliente(
        nome=nome,
        telefone=telefone,
        email=email,
        como_conheceu=como_conheceu
    )

    db.session.add(cliente)
    db.session.commit()

    return cliente


def listar_clientes():

    return Cliente.query.all()


def buscar_cliente(cliente_id):

    return Cliente.query.get_or_404(cliente_id)