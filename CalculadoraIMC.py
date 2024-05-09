# Solicitar al usuario que ingrese su peso en kg y altura en metros
peso = float(input("Ingresar peso en kg: "))
altura = float(input("Ingresar altura en metros: ")) 

# Calcular el IMC
IMC = peso / (altura * altura)
print("Tu IMC es:", IMC)

# Determinar en qué rango de IMC se encuentra y mostrar un mensaje correspondiente
if IMC < 18.5:
    print("Bajo peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
