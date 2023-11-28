# 4. Crea una suite de tests mediante UnitTest que comprueben las 3 funciones que has
# desarrollado en los ejercicios anteriores. Procura que los tests unitarios cubran lo
# mejor posible la aparición de comportamientos no deseados.

import unittest

import binario
import lista

class TestBinario(unittest.TestCase):
    def test_esBinario(self):
        self.assertTrue(binario.esBinario("1001"))
        self.assertFalse(binario.esBinario("Hola"))
        self.assertFalse(binario.esBinario("1000000000h"))
        self.assertFalse(binario.esBinario("Buenos10dias"))

class TestLista(unittest.TestCase):
    def test_estaEnRango(self):
        self.assertTrue(lista.estaEnRango(6, 1, 20))
        self.assertFalse(lista.estaEnRango(14, 15, 20))
        self.assertFalse(lista.estaEnRango(100, 1, 20))
        self.assertTrue(lista.estaEnRango(100, 1, 100))

if __name__ == '__main__':
    unittest.main()