from random import randint


moneda=randint(1,2)
eleccion=int(input("digite 1 para escoger cara o 2 para sello"))

if moneda==1 and eleccion==1:
    print("salio cara, usted escogio cara Ganaste...")
elif moneda==1 and eleccion==2:
    print("salio cara, usted escogio sello perdiste...")
elif moneda==2 and eleccion==2:
     print("salio sello, usted escogio sello ganaste...")
elif moneda==2 and eleccion==1:
     print("salio sello,usted escogio cara perdiste...")
elif eleccion==1 and eleccion==2:
    print("digitaste una opcion incorrecta")
else:
    print("datos incorrectos")
print(f"la moneda cayo{moneda}")