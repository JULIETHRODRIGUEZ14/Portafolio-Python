repetir="S"
alcancia=0
while repetir=="S" or repetir=="s":
  plata=int(input("ingrese el valor a ahorrar"))
  alcancia=alcancia+plata
  if alcancia<=100000:
   repetir=input("desea ingresar mas dinero s o n para terminar")
  else:
   break; 
  print("el total ahorrado es {alcancia}")