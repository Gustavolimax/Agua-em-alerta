
def analisar_consumo(consumo_anterior, consumo_atual):

    diferenca = consumo_atual - consumo_anterior

    if diferenca > 0:
        situacao = "AUMENTO"

    elif diferenca < 0:
        situacao = "DIMINUICAO"

    else:
        situacao = "ESTAVEL"

    return diferenca, situacao
