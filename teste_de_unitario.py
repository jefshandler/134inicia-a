import unittest

import calculador


class MyTestCase(unittest.TestCase):
    def test_something(self):
        resultado_esperado = 14
        resultado_obtido = calculador.soma(5, 9)
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here


if __name__ == '__main__':
    unittest.main()
