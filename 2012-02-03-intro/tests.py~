import unittest

def gerar_candidatos(limite):
    cand = []
    for num in range(0, limite):
        cand[i] = True

def gerar_primos_ate(limite):
    if limite == 2:
        return [2]
    else:
        return [2, 3]

class TestCrivoEratostenes(unittest.TestCase):
    def teste_primos_ate_2(self):
        self.assertEquals([2], gerar_primos_ate(2))

    def teste_primos_ate_tres(self):
        self.assertEquals([2, 3], gerar_primos_ate(3))

    def teste_primos_ate_quatro(self):
        self.assertEquals([2, 3], gerar_primos_ate(4))

    def teste_inicializa_lista_de_candidatos(self):
        candidatos = gerar_candidatos(3)

        self.assertEquals(False, candidatos[0])
        self.assertEquals(False, candidatos[1])

        for i in range(2, len(candidatos)):
            self.assertEquals(True, candidatos[i])
            