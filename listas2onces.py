onces=["hamburguesa","sandwich","pizza"]
#agregue en una posiscion especifica de la lista un elemento
onces.insert(2,"empanadas")
#agrega un elemento al final de la lista un solo elemwnto
#onces.append("malteada")
onces.extend(["malteada","perro caliente"])
print(onces)

#onces.remove("empanadas")
#del onces[0:2]
#onces.pop()
onces.clear()

print(onces)

print(onces.index("malteada"))