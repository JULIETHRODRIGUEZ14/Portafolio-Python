from random import randint,random

juguemos=randint(1, 3)

eleccion=int(input( " digite 1 para piedra, 2 para papel o 3 para tijera\n"))
if juguemos==1 and eleccion==1:
    print(" salio piedra, usted eligio piedra, intentalo de nuevo...")
elif juguemos==1 and eleccion==2 or juguemos==2 and eleccion==1:
    print(" salio piedra,usted elgio papel, Ganaste...")
elif juguemos==1 and eleccion==3 or juguemos==3 and eleccion==1:
    print(" salio piedra, usted elgio tijera, Perdiste...")
elif juguemos==2 and eleccion==2:
    print(" salio papel,usted elgio papel, intentalo de nuevo...")
elif juguemos==2 and eleccion==3 or juguemos==3 and eleccion==2:
    print(" salio tijeras, usted eligio tijeras, Ganaste...")
elif juguemos==3 and eleccion==3:
    print(" salio tijeras, usted elgio tijeras, intentalo de nuevo...")
else:
    print(" Vamos de nuevo")
