import unittest

def funcaoFizzBuzz(entrada):
    if (entrada == 2):
        return "fizz"

    return "buzz"

class nomedaclassedeTest (unittest.TestCase) :
    def teste_fizz (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(2))

    def teste_buzz (self) :
        self.assertEquals("buzz",funcaoFizzBuzz(3))

    #def teste_fizz_buzz (self) :
        #self.assertEquals("fizzbuzz",funcaoFizzBuzz(6))

        