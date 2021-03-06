import unittest

def funcaoFizzBuzz(entrada):

    if entrada % 6 == 0:
        return "fizzbuzz"
    if entrada % 2 == 0:
        return "fizz"
    if entrada % 3 == 0:
        return "buzz"
    return str(entrada)

    
class nomedaclassedeTest (unittest.TestCase) :
    def teste_fizz_2 (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(2))

    def teste_buzz_3 (self) :
        self.assertEquals("buzz",funcaoFizzBuzz(3))

    def teste_fizz_buzz_6 (self) :
        self.assertEquals("fizzbuzz",funcaoFizzBuzz(6))
        
    def teste_fizz_buzz_8 (self) :
        self.assertEquals("fizz",funcaoFizzBuzz(8))

    def teste_fizz_buzz_9 (self) :
        self.assertEquals("buzz",funcaoFizzBuzz(9))

    def teste_fizz_buzz_12(self):
        self.assertEquals("fizzbuzz", funcaoFizzBuzz(12))

    def teste_fizz_buzz_5(self):
        self.assertEquals("5", funcaoFizzBuzz(5))
       