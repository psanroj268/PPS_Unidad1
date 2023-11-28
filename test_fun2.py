# 5. Realiza el ejercicio 4 pero utilizando esta vez cualquier otro framework de terceros
# como por ejemplo pytest

from binario import esBinario
from lista import estaEnRango

def test_esBinario():
    assert esBinario("1001")
    assert not esBinario("Hola")
    assert not esBinario("1000000000h")
    assert not esBinario("Buenos10dias")

def test_estaEnRango():
    assert estaEnRango(6, 1, 20)
    assert not estaEnRango(14, 15, 20)
    assert not estaEnRango(100, 1, 20)
    assert estaEnRango(100, 1, 100)
