
def calcular_media(consumos):

    if len(consumos) == 0:
        return 0

    soma = 0

    for consumo in consumos:
        soma += consumo

    media = soma / len(consumos)

    return media
