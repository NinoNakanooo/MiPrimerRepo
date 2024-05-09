# Solicitar al usuario que elija el tipo de conversión
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = input("Seleccione el tipo de conversión (1 o 2): ")

# Verificar la opción seleccionada y realizar la conversión
if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en Fahrenheit es:", fahrenheit)
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura en Celsius es:", celsius)
else:
    print("Opción no válida. Por favor seleccione 1 o 2.")


 
