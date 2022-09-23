from random import randint


Dado1=randint(1,6)
Dado2=randint(1,6)
total=Dado1+Dado2
print(f"el dado rojo cayo {Dado1} y dado blanco cayo {Dado2}")

if Dado1==1 and Dado2==1:
    print("si salio pares de unos, ganaste")
elif Dado1==1 and Dado2==2 or Dado1==2 and Dado2==1:
    print("su total es de tres en los dados, ganaste")
elif Dado1==6 and Dado2==5 or Dado1==5 and Dado2==6:
     print("tu resultado fue 11, ganaste")
elif Dado1==6 and Dado2==6:
    print("ganaste")
elif total==7:
    print("el resultado de su lanzamiento es 7,ganaste")
else:
    print("perdiste")

