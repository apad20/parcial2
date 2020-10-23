calif=[87,89,78,92,100]
datos=["Javier","Dominguez",20,"Faja de Oro 100", "javier.dominguez@iest.edu.mx",False]

print("mostrando lista de calificaciones\n", calif)
print("mostrando lista de datos\n", datos)

print("Mostrando el primer elemento de lista datos\n", datos[0])

print("Mostrando el último elemento de lista calif\n", calif[-1])

print ("Mostrar un rango de la lista", calif[1:4])
print ("Mostrar un rango de la lista", calif[-3:-1])

calif[2]=[]
print (calif)
calif[2]=100
print (calif)
calif[-1]=70
print (calif)
#calif[:]=[]
#print (calif)
print(len(calif))

anidada=["IEST","Tampico","México",datos, calif]
print(anidada)

anidada[3][1]

print(anidada[0:3])
print(anidada[3])
print(anidada[4])

#buscar = input("Qué deseas buscar en la lista")

if "IEST" in anidada:
    print("Si se encuentra")
else:
    print("No se encuentra")

lista=["Juan",19, 92.3, True, "jdd@gmail.com"]
lista.append(77)
print(lista)

lista.extend(["IEST",100])
print(lista)

lista.