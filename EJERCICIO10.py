print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")

# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def validacion(vocal):
    return vocal in ('a', 'e', 'i', 'o', 'u')

while True:
    vocal = input("Ingresa una letra para verificar si es una vocal: ")
    if validacion(vocal):
        print("True. Es una vocal")
        break
    else:
        print("False. No es una vocal. Vuelve a ingresar una letra.")