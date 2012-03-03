import unittest

def funcaoFizzBuzz(entrada):
    saida = "";
    if (entrada == 2):
        return "fizz"
    if(entrada == 3):
        return "buzz"
    if(entrada % 2 == 0):
        saida = "fizz"
        
    return saida

class nomedaclassedeTest (unittest.TestCase) :
    def teste_fizz_2 (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(2))

    def teste_buzz_3 (self) :
        self.assertEquals("buzz",funcaoFizzBuzz(3))

    def teste_fizz_buzz_6 (self) :
        self.assertEquals("fizzbuzz",funcaoFizzBuzz(6))
        
    def teste_fizz_buzz_8 (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(8))
        