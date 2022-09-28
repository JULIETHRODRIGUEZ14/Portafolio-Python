#acumulador debe iniciar en 0 antes del ciclo
total=0
#contador debe iniciar en 0 antes del ciclo
minutos=0
for i in range (1,4,1):
     precio= int(input("ingrese el precio del prodcuto"))
     cantidad=int(input("ingrese la cantidad del producto"))   
     subtotal=precio*cantidad
     #acumulador viven dentro de un ciclo
     #aumentan en un valor variable
     total=total+subtotal

     print(F"el costo del desayuno es {total}")
     #contador vive dentro de un ciclo
     #aumenta en un valor fijo
     minutos=minutos+1
     #minutos+=1

     print(f"por esta compra obtuviste {minutos}minutops para recargar tu movil exito")
     print("adios")