
from random import randint, random

bolita=randint(1, 4)

total=int(input("ingresa tu valor a pagar\n"))
if total>=50000:
    print("si tu compra es mayor a 50000 te obsequiamos un descuento,depende de tu suerte.\n")
    print("bolita roja,obtienes 10%")
    print("bolita azul,obtienes 30%")
    print("bolita amarilla,obtienes 50%")
    print("bolita blanca,llevas tu compra gratis.")
if bolita==1:
    total=total*10/100
    print("la bolita que sacaste fue roja")
    print("tu valor a pagar en tu compra es",total,)
elif bolita==2:
    total=total*30/100
    print("la bolita que sacaste fue azul")
    print("tu valor a pagar en tu compra es",total,)
elif bolita==3:
     total=total*50/100
     print("la bolita que sacaste es amarilla")
     print("tu valor a pagar en tu compra es",total,)
elif bolita==4:
    print("te la rifaste, llevas tu compra totalmente gratis,Felicidades...")
else:
    print("su total a pagar es",total,)