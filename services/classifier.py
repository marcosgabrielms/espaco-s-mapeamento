CLASSIFICACOES = {

    ("Alto", "Imediato"):
        "Cliente Prioritário",

    ("Médio", "Curto prazo"):
        "Cliente em Acompanhamento",

    ("Baixo", "Sem urgência"):
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