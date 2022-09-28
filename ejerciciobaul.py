baul=[]
seguir="s"
while seguir=="S" or seguir=="S":
    print("seleccione 1. agregar un elemnto a la lista \n 2. listar articulos del baul \n 3. borrar ultimo elemento del baul \n 4. borrar articulo especifuco del baul")
    decision=int(input("que posicion deseas realizar"))
    if decision==1:
        baul.append(input("ingresa el nombre de tu articulo"))
    elif decision==2:
        print("estos son los articulos de tu baul \n")
        baul.sort()
        print(baul)
    elif decision==3:
        print(f"vas a eliminar el articulo {baul[-1]}")
        baul.pop()
        print(baul)
    elif decision==4:
        for index,articulo in enumerate(baul):
            print(f"#{index} => {articulo}")
            baul.remove(int(input("ingrese el numero del articulo que desee borrar")))
            #print("el baul quedo asi", baul)
    else:
        print("opcion incorrecta")
        
        seguir=input("deseas regresar al menu S/s o N para terminar")

        
        
    
        
