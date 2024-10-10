print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")

# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

# Función para sumar todos los números de una lista
def sum():
    lista = [1, 2, 3, 4]
    total = 0
    for num in lista:
        total += num
    return total

# Función para multiplicar todos los números de una lista
def multip():
    lista = [1, 2, 3, 4]
    total = 1
    for num in lista:
        total *= num
    return total

# Ejecución y resultados
resultado_suma = sum()
resultado_multiplicacion = multip()

print("Suma de la lista:", resultado_suma)
print("Multiplicación de la lista:", resultado_multiplicacion)