
import sys
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algoritmos.calculo_media import calcular_media
from algoritmos.deteccao_vazamento import detectar_vazamento
from algoritmos.historico_consumo import (
    registrar_consumo,
    buscar_consumos_anteriores
)
from algoritmos.validacao import validar_data


class TesteAguaEmAlerta(unittest.TestCase):

    def test_calculo_media(self):

        resultado = calcular_media([100, 200, 300])

        self.assertEqual(resultado, 200)

    def test_media_vazia(self):

        resultado = calcular_media([])

        self.assertEqual(resultado, 0)

    def test_detectar_vazamento(self):

        situacao, mensagem = detectar_vazamento(150, 100)

        self.assertEqual(situacao, "ALERTA")

    def test_consumo_normal(self):

        situacao, mensagem = detectar_vazamento(110, 100)

        self.assertEqual(situacao, "NORMAL")

    def test_consumo_baixo(self):

        situacao, mensagem = detectar_vazamento(40, 100)

        self.assertEqual(situacao, "ATENCAO")

    def test_sem_historico(self):

        situacao, mensagem = detectar_vazamento(100, None)

        self.assertEqual(situacao, "SEM BASE")

    def test_registro_na_matriz(self):

        historico = []
        matriz = []

        resultado = registrar_consumo(
            historico,
            matriz,
            "2026-11-01",
            "Manhã",
            100,
            "NORMAL"
        )

        self.assertTrue(resultado)
        self.assertEqual(matriz[0][1], 100)

    def test_buscar_historico(self):

        historico = []
        matriz = []

        registrar_consumo(
            historico, matriz,
            "2026-11-01", "Manhã", 100, "NORMAL"
        )

        registrar_consumo(
            historico, matriz,
            "2026-11-02", "Manhã", 200, "ALERTA"
        )

        resultado = buscar_consumos_anteriores(
            matriz, "2026-11-03", "Manhã"
        )

        self.assertEqual(resultado, [100, 200])

    def test_validar_data(self):

        resultado = validar_data("16/11/2026")

        self.assertEqual(resultado, "2026-11-16")


if __name__ == "__main__":
    unittest.main()
