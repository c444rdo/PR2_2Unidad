print("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
# Capturar dirección de email. Desplegar mensaje si la dirección es válida o no, siendo que una función lo revisa por tener el "@", entonces solo así es valido.

def validacion(email):
    return '@' in email

while True:
    correo = input("Ingresa tu correo electrónico: ")
    if validacion(correo):
        print("Tu correo es válido. Puedes seguir.")
        break
    else:
        print("Tu correo no es válido. Vuelve a ingresarlo.")
