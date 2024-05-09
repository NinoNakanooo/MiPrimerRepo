NumeroPositivo = int(input("Ingresar numero entero positivo: "))

# Verificar si el número ingresado es positivo
while NumeroPositivo < 1:
    print("Error: el número no es positivo.")
    NumeroPositivo = int(input("Ingresar numero entero positivo: "))

print(f"Tabla de multiplicar del {NumeroPositivo}:")
i = 1
while i <= 10:
    i += 1  # Incrementar el valor de i antes de imprimir
    print(f"{NumeroPositivo} x {i-1} = {NumeroPositivo * (i-1)}")
