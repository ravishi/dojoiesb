import unittest

def gerar_candidatos(limite):
    cand = []
    for num in range(0, limite):
        cand.append(True)
    cand[0] = False
    cand[1] = False
    return cand

def gerar_primos_ate(limite):
    cand = gerar_candidatos(limite + 1)

    for primo in range(2, limite + 1):
        for multiplo in range(primo*2, limite + 1, primo):
            cand[multiplo] = False

    ret = []
    for num in range(limite + 1):
        if cand[num] == True:
            ret.append(num)
            
    return ret

class TestCrivoEratostenes(unittest.TestCase):
    def teste_primos_ate_2(self):
        self.assertEquals([2], gerar_primos_ate(2))

    def teste_primos_ate_tres(self):
        self.assertEquals([2, 3], gerar_primos_ate(3))

    def teste_primos_ate_quatro(self):
        self.assertEquals([2, 3], gerar_primos_ate(4))

    def teste_primos_ate_cinco(self):
        self.assertEquals([2, 3, 5], gerar_primos_ate(5))

    def teste_inicializa_lista_de_candidatos(self):
        candidatos = gerar_candidatos(3)

        self.assertEquals(False, candidatos[0])
        self.assertEquals(False, candidatos[1])

        for i in range(2, len(candidatos)):
            self.assertEquals(True, candidatos[i])
            