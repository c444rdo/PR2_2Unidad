print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Funcion que muestre el saludo Hey amigos! cada vez que se le pida.

def escuchar_comando(comando):
    if comando.lower() == "saludo":
        print("Hey amigos!")
    else:
        print("Comando no reconocido.")

# Ejemplo de uso
entrada_usuario = input("Escribe el comando: ")
escuchar_comando(entrada_usuario)