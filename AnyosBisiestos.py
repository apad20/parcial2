#Desarrolla un método que solicite un año y devuelva si es bisiesto o no.
#Un año bisiesto es múltiplo de 4, pero no es bisiesto si es múltiplo de 100
#excepto si también es múltiplo de 400.

#Análisis del problema, expresión lógica.

# Si x es MULTIPLO de 4 AND no es MULTIPLO de 100 pero AND  MULTIPLO de 400.

#Método llamado Múltiplo, este método recibe 2 variales, primera es el multiplo y
#la segunda es el año.

#Devuelve un booleano, T si un año es múltiplo de un número y F si no lo es.
def multiplo(mul, anyo):
    r = anyo % mul
    return r is 0

#Flujo principal
anyo = int(input("Introduce algún año"))
#Pregunto si el anyo es múltiplo de 4
multiplo(4,anyo)
multiplo(100,anyo)
multiplo(400,anyo)


#Evaluación opcion 1
if multiplo(4,anyo):
    if not multiplo(100,anyo) and multiplo(400,anyo):
        print("bisiesto")
    else:
        print("no es bisiesto")

#Evaluación opción 2
if multiplo(4,anyo) and not multiplo(100,anyo):
        print("bisiesto")
elif multiplo(400,anyo):
        print("bisiesto")
else:
    print("no es bisiesto")

#Evaluación 3
if multiplo(4,anyo) and ( multiplo(100,anyo) or multiplo(400,anyo)):

