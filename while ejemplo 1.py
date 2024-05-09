suma = 0
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if numero < 1:
    print("El número ingresado no es positivo.")
else:
    contador = 2  # Comenzar desde el primer número par (2)
    while contador <= numero:
        suma += contador
        contador += 2  # Incrementar en 2 para obtener el siguiente número par

    print("La suma de los números pares hasta", numero, "es:", suma)
