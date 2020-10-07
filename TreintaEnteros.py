#Realiza un programa que lea 30 enteros, los guarde en una lista, calcule su promedio,
# determine la cantidad de elementos que están por encima del promedio
# y la cantidad de elementos que están por debajo del promedio, y muestre los resultados.

#Definición de función Enteros
def solicitaEneteros(n):
    #lista vacía
    enteros=[]
    for i in range(0,n):
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

#Método para calcular elemenos superiores e inferiores al promedio
#devuelve una tupla
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
    print ("El promedio de los elmentos es ", promedio,
           "\nlos números mayores al promedio son ", mym[0], #Al llamar un elemento de tupla para imprimir utilizamos []
           "\nlos números menores al promedio son ", mym[1])

#Podemos agrupar el flujo principal en un método llamado Main para después llamarlo llamarlo.
def main():
    n = int(input("¿De cuántos números enteros deseas calcular el promedio?"))
    l = solicitaEneteros(n)
    p = promedio(l)
    t = contadorElementos(l, p)
    mostrarResultados(p, t)

#Flujo principal
main()

