CLASSIFICACOES = {

    ("Alto", "Imediato"):
        "Cliente Prioritário",

    ("Médio", "Curto Prazo"):
        "Cliente em Acompanhamento",

    ("Baixo", "Sem Urgência"):
        "Cliente em Análise"
}


def classificar_cliente(
    interesse,
    prazo
):

    chave = (
        interesse,
        prazo
    )

    return CLASSIFICACOES.get(
        chave,
        "Cliente em Análise"
    )