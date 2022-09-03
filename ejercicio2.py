edad=int(input("ingresa tu edad en años \n"))
if 0<=edad<=4:
    print(F"El cliente ingresa gratis")
elif 4>edad<=18:
    print(f"su edad es igual {edad} años y debe pagar 20000")
elif 19>=edad<=60:
    print(f"su edad es {edad} años y debe pagar 15000")
else:
    print(f"su edad es {edad} años debe pagar 0")