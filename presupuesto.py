from re import S

sumagastos=0
presupuesto=100000
repetir="S"
for i in range(1,4,1):
 while repetir=="S" or repetir=="s":
  if presupuesto<=100000:
   repetir=input("desea registrar un gasto ingrese s \n")
   gasto=int(input("ingrese el gasto \n"))
   sumagastos=sumagastos+gasto
   presupuesto=presupuesto-gasto
  break;
else:

 print(f"el gasto fue {sumagastos}")
 print(f"el presupuesto es {presupuesto}")