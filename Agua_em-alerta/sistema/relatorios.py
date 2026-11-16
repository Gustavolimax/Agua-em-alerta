
def exibir_relatorio(historico):

    print("\n========== RELATÓRIO DE CONSUMO ==========")

    if len(historico) == 0:
        print("Nenhum consumo registrado.")
        return

    for registro in historico:

        data = registro["data"]
        data_formatada = "/".join(data.split("-")[::-1])

        print("\nData:", data_formatada)
        print("Período:", registro["periodo"])
        print("Consumo:", registro["consumo"], "litros")
        print("Situação:", registro["situacao"])

    print("\n==========================================")


def exibir_matriz(matriz):

    print("\n========== MATRIZ DE CONSUMO ==========")

    print("Data          | Manhã | Tarde | Noite")

    for linha in matriz:

        data = "/".join(linha[0].split("-")[::-1])

        manha = linha[1] if linha[1] is not None else "-"
        tarde = linha[2] if linha[2] is not None else "-"
        noite = linha[3] if linha[3] is not None else "-"

        print(f"{data} | {manha} | {tarde} | {noite}")

    print("=======================================")
