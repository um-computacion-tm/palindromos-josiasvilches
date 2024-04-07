#con una lista por ejemplo una como esta: milista = ['h', 'o', 'l', 'a']
#otra forma es haciendo strings -> mistring = 'hola'
#milista[1:] -> muestra desde el elemento 1 en adelante
#si quiero mostrar x cantidad de elementos y saltearlos de uno a otro cada 2 elementos hacemos lo sig: milista[3:8:2]
#print(range(6)) -> range(0, 6)
#print(list(range(6))) -> [0, 1, 2, 3, 4, 5]
#print(list(range(0, 6, 2))) -> [0, 2, 4]

import unittest

def is_palindrome(mystring):
    print(mystring)
    for indice in range (0, len(mystring)):
        print(mystring[indice]+ " -> " + mystring[-(indice +1)])
        if mystring[indice] != mystring[-(indice +1)]:
            print("no es palíndromo")
            return False
    return True

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)
    def test_b(self):
        resultado = is_palindrome('hipopótamo')
        self.assertEqual(resultado, False)
    def test_c(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)
    def test_d(self):

        self.assertEqual(is_palindrome('quequen'), False)
    def test_e(self):
        resultado = is_palindrome('abbc')
        self.assertEqual(resultado, False)
    def test_f(self):
        resultado = is_palindrome('acbbca')
        self.assertEqual(resultado, True)

unittest.main()