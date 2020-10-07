#Realiza un programa que lea 30 enteros, los guarde en una lista, calcule su promedio,
# determine la cantidad de elementos que están por encima del promedio
# y la cantidad de elementos que están por debajo del promedio, y muestre los resultados.

#Definición de función Enteros
def solicitaEneteros():
    #lista vacía
    enteros=[]
    for i in range(0,30):
        #solicitando al usuario un número entero
        entero = int(input("Introduce un entero:"))
        #agrego un elemento a la lista
        enteros.append(entero)
    return enteros

#Método para calcular el promedio
def promedio(lista):
    suma=0
    for i in lista:
        suma += i
        #Len es un método, que devuelve el tamaño o cantidad de
        # elemenos que conforma la lista
    return suma / len(lista)

#Elemenos superiores al promedio
def contadorElementos(lista, promedio):
    cmy=0
    cmn=0
    for i in lista:
        if i > promedio:
            cmy+=1
        elif i < promedio:
            cmn+=1
    #devuelvo una tupla
    return cmy,cmn

def mostrarResultados (promedio, mym):
    m=list(mym)
    print ("El promedio de los elmentos es ", promedio,
           "\nlos números mayores al promedio son ", m[0],
           "\nlos números menores al promedio son ", m[1])

#Flujo principal
l = solicitaEneteros()
p = promedio(l)
t = contadorElementos(l,p)
mostrarResultados(p,t)