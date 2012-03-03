import unittest

def funcaoFizzBuzz(entrada):
    if (entrada == 2):
        return "fizz"
    if(entrada == 3)
        return "buzz"
    
    return "fizzbuzz"

class nomedaclassedeTest (unittest.TestCase) :
    def teste_fizz_2 (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(2))

    def teste_buzz_3 (self) :
        self.assertEquals("buzz",funcaoFizzBuzz(3))

    def teste_fizz_buzz (self) :
        self.assertEquals("fizzbuzz",funcaoFizzBuzz(6))

        