print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")

# Que saque la distancia dirigida entre dos puntos.

def verificar_distancia(punto1, punto2):
    distancia_total = abs(punto1 - punto2)
    return f"La distancia entre los dos puntos es de {distancia_total} km."


# Solicitar distancias al usuario
try:
    punto1 = float(input("Ingrese la distancia del punto 1 (en km): "))
    punto2 = float(input("Ingrese la distancia del punto 2 (en km): "))

    # Llamar a la función y mostrar el resultado
    resultado = verificar_distancia(punto1, punto2)
    print(resultado)

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")