#mi solucion
Precio = float(input("Precio original del producto"))
DescuA = float(input("Descuento a aplicar"))
Descuento = (Precio*DescuA)/100
print("precio final",Descuento - Precio)

#Solucion mejorada
Precio = float(input("Precio original del producto: "))
DescuA = float(input("Descuento a aplicar: "))
Descuento = (Precio * DescuA) / 100
PrecioFinal = Precio - Descuento
print("Precio final:", PrecioFinal)
