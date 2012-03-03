import unittest

def gerar_primos_ate(limite):
    return 2

class TestCrivoEratostenes(unittest.TestCase):
    def teste_primos_ate_2(self):
        self.assertEquals([2], gerar_primos_ate(2))