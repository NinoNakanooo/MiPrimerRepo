cantidad = float(input("Ingrese cantidad de dinero: "))
moneda_origen = input("Ingrese moneda de origen (USD o EUR): ")
tipos_de_cambio = {"USD-EUR": 0.85, "EUR-USD": 1.18}

if moneda_origen == "USD":
    cantidad_convertida = cantidad * tipos_de_cambio["USD-EUR"]
    print("f{cantidad} USD equivale a {cantidad_convertida} EUR.")
elif moneda_origen == "EUR":
    cantidad_convertida = cantidad * tipos_de_cambio["EUR-USD"]
    print("f{cantidad} EUR equivale a {cantidad_convertida} USD.")
else:
    print("Moneda de origen no válida. Por favor ingrese USD o EUR.")
