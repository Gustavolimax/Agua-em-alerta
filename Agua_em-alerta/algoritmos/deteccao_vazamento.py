
def detectar_vazamento(consumo_atual, media_consumo):

    if media_consumo is None:
        return "SEM BASE", "Histórico insuficiente para análise."

    if media_consumo <= 0:
        return "SEM BASE", "Não existe média válida para comparação."

    limite_superior = media_consumo * 1.30
    limite_inferior = media_consumo * 0.50

    if consumo_atual > limite_superior:

        return "ALERTA", "Possível vazamento identificado!"

    elif consumo_atual < limite_inferior:

        return "ATENCAO", "Consumo muito abaixo da média."

    else:

        return "NORMAL", "Consumo dentro do padrão."
