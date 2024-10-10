print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")

# Función que de un string, regrese la longitud de la última palabra. Las palabras tienen separación por uno o más espacios.

def longitud_ultima_palabra(cadena):
    palabras = cadena.strip().split()  # Elimina espacios extras y divide en palabras
    if len(palabras) == 0:
        return 0  # Si no hay palabras, devuelve 0
    return len(palabras[-1])

# Ejemplo de uso
cadena = input("Escribe una frase: ")
print(f"La longitud de la última palabra es: {longitud_ultima_palabra(cadena)}")