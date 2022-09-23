#definir una lista
lista=[] # esta lista esta vacia
lista2=[1,2,3,4]
print(lista2)
#acceder a una posicion especifica a traves del index
print(lista2[2])
#ultimo elemento de la lista
print(lista2[-1])
#penultimo elemento de una lista
print(lista2[-2])
#modificar un elemn¿ento d euna posicion especifica
lista2[0]=7
print(lista2)
#recorrer la lista2 y multiplicar por 2 sus elementos
for l in lista2:
    print(l*2)
#incluir el index en el recorrido, la interaccion
for index,l in enumerate(lista2):
    print(f"en la posisicion{index} se encuentra el valor {l}")


numeros=[5,9,10]
generos=["jazz","rock","djent"]
#recorrer en un ciclo las dos listas
for n,g in zip(numeros,generos):
    print(f"el numero {n} esta asociado con el genero {g}")

print(len(generos))
generos.sort()
print(generos)
numeros.sort()
print(numeros)