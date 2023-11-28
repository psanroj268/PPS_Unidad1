# Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
# introduzca un número binario e imprima por pantalla el número en formato decimal.
# Para desarrollar el programa, es necesario que desarrolles una función con la
# siguiente cabecera:
#
# def esBinario(strbinario)
#
# Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
# como parámetro contiene una cadena binaria.
#
# Ejemplo de esBinario:
#
# print(esBinario(“1001”))
# True
#
# print(esBinario(“Hola”))
# False

def esBinario(strbinario):
    user_response = strbinario
    cambio = 0

    for char in user_response:
        if char!= '0' and char!= '1':
            cambio += 1
            return False

    if cambio == 0:
        return True

print(esBinario("1001"))
print(esBinario("Hola"))