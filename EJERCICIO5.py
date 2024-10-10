print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Calcular el área de un círculo  y el volumen. Otra que calcule el volumen de un cilindro y utilice  primera función.

import math

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio**2

# Función para calcular el volumen de una esfera
def volumen_esfera(radio):
    return (4/3) * math.pi * radio**3

# Función para calcular el volumen de un cilindro usando el área del círculo
def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)  # Reutiliza la función del área
    return area_base * altura

# Ejemplo de uso
radio = float(input("Escribe el radio del círculo: "))
altura = float(input("Escribe la altura del cilindro: "))

print(f"El área del círculo es: {area_circulo(radio)}")
print(f"El volumen de la esfera es: {volumen_esfera(radio)}")
print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura)}")