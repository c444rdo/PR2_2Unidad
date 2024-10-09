print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Calcular total de una factura luego del IVA. Primero obtener la cantidad sin IVA, luego el porcentaje de IVA a aplicar, por ultimo devolver el total de la factura. 
# Si se da la función sin pasarle un porcentaje de IVA, deberá aplicar un 21%.

def calcular_factura(cantidad_sin_iva, iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * iva / 100)
    return total

# Ejemplo de uso
cantidad = float(input("Escribe la cantidad sin IVA: "))
iva = input("Escribe el porcentaje de IVA (o presiona Enter para usar 21%): ")

if iva:
    iva = float(iva)  # Si el usuario ingresa un IVA, se convierte a número
    total = calcular_factura(cantidad, iva)
else:
    total = calcular_factura(cantidad)  # Si no, se usa el 21% por defecto

print(f"El total de la factura con IVA es: {total}")