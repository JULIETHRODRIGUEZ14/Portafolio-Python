sumanota=0
nota=0
cantidad=0
repetir1="si"
while repetir1=="si" or repetir1=="SI":
    nota=float(input("ingrese la nota \n "))
    cantidad=cantidad+1
    sumanota=sumanota+nota
    if nota>=0:
        repetir1=input(f"si desea ingresar mas calificaciones marque si o no \n")
    else:
        break
print("total suma de notas",sumanota,"camtidad de notas", cantidad)
notafinal=nota/cantidad
print(f"definitiva es {notafinal}")
if notafinal<=3.0:
    print(f"Reprobaste {notafinal}")
elif notafinal<=4.0 or notafinal>=3.1:
    print(f"Pasaste Raspando {notafinal}")
else:
    print(f"Aprobaste {notafinal}")