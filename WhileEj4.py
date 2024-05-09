Numero = int(input("Ingresar Entero Positivo:"))

# Verificar si el número ingresado es positivo
while Numero < 1:
    print("Error: El número no es positivo.")
    Numero = int(input("Ingresar Entero Positivo:"))

# Inicializar un contador en 1
i = 1

# Imprimir los números desde 1 hasta el número ingresado
while i <= Numero:
    print(i)
    i += 1
