#Objetos iterables
cuadernos = ["Matemáticas","Español","Historia","Geografía"]

#Ejemplo de recorrido de un elemento iterable (lista)
for cuaderno in cuadernos:
    print (cuaderno)

#Ejemplo de un rango, con límite inferío 0 implícito,
# límite superior 30 explícito con incremento de 1 en 1 implícito.
for i in range(31):
    print(i)

#Ejemplo de un rango, con límite inferío 1,
# límite superior 30 con incremento de 2 en 2.
for i in range(1,31,2):
    print(i)

#Ejemplo de un rango, con límite inferío 1,
# límite superior 30 con incremento de 1 en 1 implícito.
for i in range(1,31):
    print(i)

#Ejemplo de un rango, con límite inferío 30,
# límite superior 1 con decremento de 1 en 1.
for i in range(30,0,-1):
    print(i)