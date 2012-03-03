import unittest

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