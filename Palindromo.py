palabra = input("Ingresar palabra: ")

# Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
palabra = palabra.lower()

# Invertir la palabra
palabra_invertida = palabra[::-1]

# Verificar si la palabra original es igual a su versión invertida
if palabra == palabra_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
