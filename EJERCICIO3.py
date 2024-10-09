print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Dar un entero positivo y resuelva su factorial.

def factorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = int(input("Escribe un número entero positivo: "))
print(f"El factorial de {numero} es {factorial(numero)}")