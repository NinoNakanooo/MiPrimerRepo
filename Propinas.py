Factura = float(input("Ingresar total de la factura: "))
Propina = float(input("Ingresar cantidad de propina que desea dejar: "))
CantidadPropina = Factura * (Propina / 100) 
CantidadTotal = CantidadPropina + Factura
print(f"Total de la factura con propina incluida sería: {CantidadTotal:.2f}")
