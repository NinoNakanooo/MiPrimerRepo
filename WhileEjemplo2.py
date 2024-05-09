import random

NumeroAleatorio = random.randint(1, 100)
EntradaUsuario = int(input("Ingresa un numero entero del 1 al 100: "))

while EntradaUsuario != NumeroAleatorio:
    if EntradaUsuario > NumeroAleatorio:
        print("Estás adelante.")
    else:
        print("Estás atrás.")
    EntradaUsuario = int(input("Intenta de nuevo: "))

print("¡El número es correcto!")

 