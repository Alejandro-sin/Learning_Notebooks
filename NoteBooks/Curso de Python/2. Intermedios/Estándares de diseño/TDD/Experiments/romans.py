'''

Este archivo tiene como propósito estudiar el TDD en python.
Y la conversión de los números romanos.


'''


import unittest

class RomanNumber(object):
    def int_to_roman(self, n):
        # 1. Aqui es donde añadimos la linea nueva diciendole que rerotne la I mayuscula de una vez.
        # return 'I'
    # 4. Hago refactor.
    #     if n == 1:
    #         return 'I'
    #     elif n ==2:
    #         return  'II'
        # 6. Hago el refactor para los 3 primeros numeros romanos.
        roman_number =''
        for x in range(n):
            roman_number +='I'
        return roman_number



class RomanNumberTest(unittest.TestCase):

    def setUp(self):
        self.roman_number = RomanNumber()

    def test_one_to_roman(self):
        roman_number = self.roman_number.int_to_roman(1)
        self.assertEqual('I',roman_number)

    #3.  Creo test para lso demás numeros. como el 2, lo corro y falla.
    def test_two_to_roman(self):
        roman_number = self.roman_number.int_to_roman(2)
        self.assertEqual('II', roman_number)

    # Creo otra función para el 3. Corro el test y falla, así que paso a la nueva iteración del refactor.
    def test_tree_to_roman(self):
        roman_number = self.roman_number.int_to_roman(3)
        self.assertEqual('III', roman_number)


if __name__ == '__main__':
    unittest.main()