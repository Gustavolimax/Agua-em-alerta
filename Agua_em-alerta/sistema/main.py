
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algoritmos.analise_consumo import analisar_consumo
from algoritmos.calculo_media import calcular_media
from algoritmos.deteccao_vazamento import detectar_vazamento

from algoritmos.historico_consumo import (
    registrar_consumo,
    buscar_consumos_anteriores,
    periodo_ja_registrado
)

from algoritmos.validacao import validar_data

from sistema.relatorios import (
    exibir_relatorio,
    exibir_matriz
)


# VETOR E MATRIZ
historico = []
matriz_consumo = []


def cadastrar_consumo():

    print("\n========== REGISTRAR CONSUMO ==========")

    try:

        data = input("Informe a data (DD/MM/AAAA): ")
        data = validar_data(data)

        print("\nSelecione o período:")
        print("1 - Manhã")
        print("2 - Tarde")
        print("3 - Noite")

        opcao_periodo = input("Período: ")

        periodos = {
            "1": "Manhã",
            "2": "Tarde",
            "3": "Noite"
        }

        if opcao_periodo not in periodos:
            print("Período inválido.")
            return

        periodo = periodos[opcao_periodo]

        if periodo_ja_registrado(
            matriz_consumo, data, periodo
        ):
            print("Já existe um registro para esse dia e período.")
            return

        consumo = float(input("Consumo em litros: "))

        if consumo < 0:
            print("O consumo não pode ser negativo.")
            return

        # BUSCA O HISTÓRICO DO MESMO PERÍODO
        consumos_anteriores = buscar_consumos_anteriores(
            matriz_consumo, data, periodo
        )

        # CALCULA A MÉDIA
        if len(consumos_anteriores) > 0:
            media = calcular_media(consumos_anteriores)
        else:
            media = None

        # ANALISA O CONSUMO
        if len(consumos_anteriores) > 0:

            diferenca, variacao = analisar_consumo(
                media, consumo
            )

            print("\nDiferença em relação à média:", diferenca, "litros")
            print("Variação:", variacao)

        # DETECTA POSSÍVEIS ANORMALIDADES
        situacao, mensagem = detectar_vazamento(
            consumo, media
        )

        print("\nResultado:", mensagem)

        # REGISTRA OS DADOS
        sucesso = registrar_consumo(
            historico,
            matriz_consumo,
            data,
            periodo,
            consumo,
            situacao
        )

        if sucesso:
            print("\nConsumo registrado com sucesso!")

    except ValueError as erro:

        print("\nErro:", erro)

    except Exception as erro:

        print("\nErro inesperado:", erro)


def consultar_relatorios():

    print("\n1 - Histórico completo")
    print("2 - Matriz de consumo")

    opcao = input("Escolha: ")

    if opcao == "1":
        exibir_relatorio(historico)

    elif opcao == "2":
        exibir_matriz(matriz_consumo)

    else:
        print("Opção inválida.")


def executar_sistema():

    while True:

        print("\n====================================")
        print("           ÁGUA EM ALERTA")
        print(" Sistema de detecção de vazamentos")
        print("====================================")

        print("\n1 - Registrar consumo")
        print("2 - Consultar relatórios")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            cadastrar_consumo()

        elif opcao == "2":

            consultar_relatorios()

        elif opcao == "3":

            print("\nSistema encerrado.")
            break

        else:

            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    executar_sistema()
