from models import Atendimento
from models import db

from services.classifier import (
    classificar_cliente
)


def criar_atendimento(
    cliente_id,
    problema,
    necessidade,
    objetivo,
    interesse,
    prazo,
    observacoes
):

    classificacao = classificar_cliente(
        interesse,
        prazo
    )

    atendimento = Atendimento(
        cliente_id=cliente_id,
        problema=problema,
        necessidade=necessidade,
        objetivo=objetivo,
        interesse=interesse,
        prazo=prazo,
        observacoes=observacoes,
        classificacao=classificacao
    )

    db.session.add(atendimento)
    db.session.commit()

    return atendimento