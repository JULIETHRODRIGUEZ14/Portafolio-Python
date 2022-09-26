
from random import randint, random
eleccion=int(input("ingrese 1 para registar precio o 2 para ver cantidad de productos adquiridos \n"))
if eleccion==1:
    compra=int(input("registra el valor de tu compra \n"))
else:
    cantidadproductos=int(input("ingrese la cantidad de productos adquiridos \n"))
    precioproducto=200000
    total=cantidadproductos*precioproducto

descuento=randint(1, 4)

if total>=50000:
    print("si tu compra es mayor a 50000 te obsequiamos un descuento,depende de tu suerte.\n")
    print("bolita roja,obtienes 10%")
    print("bolita azul,obtienes 30%")
    print("bolita amarilla,obtienes 50%")
    print("bolita blanca,llevas tu compra gratis.")
if descuento==1:
    total=total*10/100
    print("la bolita que sacaste fue roja")
    print("tu valor a pagar en tu compra es",total,)
elif descuento==2:
    total=total*30/100
    print("la bolita que sacaste fue azul")
    print("tu valor a pagar en tu compra es",total,)
elif descuento==3:
     total=total*50/100
     print("la bolita que sacaste es amarilla")
     print("tu valor a pagar en tu compra es",total,)
elif descuento==4:
    print("te la rifaste, salio bolitablanca,llevas tu compra totalmente gratis,Felicidades...")
else:
    print(f"que bien el juego escogio {descuento}")
else:
print("no fuiste elegido para nuestra promocion, su total a pagar es ",compra)
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("ingresa el valor con el que deseas cancelar"))
    cambio=precioproducto-total
    print("su compra fue de ",total,"productos que realizo, el pago con ",valorrecibido," su cambio es ",cambio)
else:
    descuento==4
    print("ganaste")

