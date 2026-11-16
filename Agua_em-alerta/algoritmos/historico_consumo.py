
PERIODOS = {
    "Manhã": 1,
    "Tarde": 2,
    "Noite": 3
}


def registrar_consumo(historico, matriz, data, periodo,
                      consumo, situacao):

    indice = PERIODOS[periodo]

    # Procura a data na matriz
    linha_encontrada = None

    for linha in matriz:
        if linha[0] == data:
            linha_encontrada = linha
            break

    # Cria uma nova linha se a data não existir
    if linha_encontrada is None:
        linha_encontrada = [data, None, None, None]
        matriz.append(linha_encontrada)

    # Impede dois registros no mesmo período e dia
    if linha_encontrada[indice] is not None:
        return False

    # Registra na matriz
    linha_encontrada[indice] = consumo

    # Registra no vetor
    registro = {
        "data": data,
        "periodo": periodo,
        "consumo": consumo,
        "situacao": situacao
    }

    historico.append(registro)

    return True


def buscar_consumos_anteriores(matriz, data, periodo):

    indice = PERIODOS[periodo]

    consumos = []

    for linha in matriz:

        if linha[0] < data and linha[indice] is not None:

            consumos.append(linha[indice])

    return consumos


def periodo_ja_registrado(matriz, data, periodo):

    indice = PERIODOS[periodo]

    for linha in matriz:

        if linha[0] == data and linha[indice] is not None:
            return True

    return False
