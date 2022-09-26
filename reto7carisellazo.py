from random import randint
from timeit import repeat
saldo=0
repeat="SI"
repeat="si"
juego=0
while repeat=="SI" or repeat=="si":
    dinero=int(input("digita el saldo que deseas recargar"))
    saldo=saldo+dinero
    print("su saldo global es de",saldo)
    if saldo>=0:
        repeat=input("si deseas ingresar mas dinero digite s, de lo contrario digite n \n")
    else:
        break
apuesta=int(input("ingrese el valor a apostar \n"))
while repeat=="si" or repeat=="SI":
        moneda=randint(1,2)
        eleccion=int(input("digite 1 para escoger cara o 2 para sello"))
        if moneda==1 and eleccion==1:
            saldo=saldo+apuesta
            juego=juego+1
            print("salio cara, usted escogio cara Ganaste! DUPLICA tu apuesta")
        elif moneda==1 and eleccion==2:
          saldo=saldo+apuesta
          juego=juego+1
        print("salio cara, usted escogio sello perdiste...")
        elif moneda==2 and eleccion==2:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio sello, usted escogio sello Ganaste! DUPLICA tu apuesta")
        elif moneda==2 and eleccion==1:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio sello,usted escogio cara perdiste...")
        elif eleccion==1 and eleccion==2:
print("digitaste una opcion incorrecta")
print("datos incorrectos")
print(f"su saldo actual es",saldo)
repeat=input(f"quieres jugar de nuevo digite S, de lo contrario digite N \n")
if repeat=="SI" or repeat=="si":
    apuesta=int(input("digita el valor a apostar \n"))
else:
    break
print("el dinero acumulado fue {saldo} las veces jugadas fue {juego}")