#acumulador debe iniciar en 0 antes del ciclo
#contador debe iniciar en 0 antes del ciclo
hombre=0
mujer=0
for i in range (1,10,1):
     Genero=input("digite h si eres hombre, y m si eres mujer")
     if Genero=="h":
        hombre=hombre+1
     elif Genero=="m":
        mujer=mujer+1
     #acumulador viven dentro de un ciclo
     #aumentan en un valor variable
print(F"hay {hombre} y tantas{mujer}")
     

     