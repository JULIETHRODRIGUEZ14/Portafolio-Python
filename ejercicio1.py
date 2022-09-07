from random import randint, random
moneda=random(1,2)
eleccion=int(input( "Digite 1 para cara y 2 para cello"))
if moneda==1 and eleccion==1:
    print(" Salio cara, usted eliguio cara Ganaste....")
elif moneda==1 and eleccion==2:
    print(" Salio cara, usted eliguio sello Perdiste....")
elif moneda==2 and eleccion==2:
    print(" Salio sello, usted eliguio sello Ganaste....")
elif moneda==2 and eleccion==1:
    print(" Salio sello, usted eliguio cara perdiste....")
elif eleccion!=1 or eleccion!=2:
    print("Digitaste una opcion incorrecta")
else:
    print("sigue intentando")