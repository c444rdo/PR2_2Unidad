print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")

# Definir una función (), que tome tres números como argumentos y devuelva el mayor de ellos.

def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

mayor = mayor_de_tres(num1, num2, num3)
print(f"El número mayor es: {mayor}")