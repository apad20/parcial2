#Desarrolla un método que solicite un año y devuelva si es bisiesto o no.
#Un año bisiesto es múltiplo de 4, pero no es bisiesto si es múltiplo de 100
#excepto si también es múltiplo de 400.

#Análisis del problema, expresión lógica.

# ****  Si x MULTIPLO de 4 AND NOT MULTIPLO de 100 OR MULTIPLO de 400.
# Si x es múltiplo de 4, debemos evaluar que no sea múltiplo de 100,
# pero, si es el caso que si sea múltiplo de 100,

#Método llamado Múltiplo, este método recibe 2 variales, primera es el multiplo y
#la segunda es el año.

#Devuelve un booleano, T si un año es múltiplo de un número y F si no lo es.
def multiplo(mul, anyo):
    r = anyo % mul
    return r is 0

#Flujo principal
anyo = int(input("Introduce algún año"))

#Evaluación opcion 1
if multiplo(4,anyo) and not multiplo(100,anyo) or multiplo(400,anyo):
    print("bisiesto")
else:
    print("no es bisiesto")
