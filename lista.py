# Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
# dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
# número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
# de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
# otros programas.
#
# Las funciones que debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes cabeceras:
#
# def estaEnRango(valor, minimo, maximo)
# Devuelve True o False determinando que valor se encuentra entre el mínimo y elmáximo.
#
# def estaEnLista(valor, lista)
# Devuelve True o False determinando si el valor está en la lista

def estaEnRango(valor, minimo, maximo):
    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False

print(estaEnRango(6, 1, 20))

print(estaEnRango(14, 15, 20))

def estaEnLista(valor, lista):
    if valor in lista:
        return True
    else:
        return False

print(estaEnLista(6, [6,14,11,3,2,1,15,19]))