def multiplo(mul, anyo):
    r = anyo % mul
    return r == 0

#Flujo principal
anyo = input("Introduce algun año: ")

multiplo(4,int(anyo)) # P
multiplo(100,int(anyo)) # Q
multiplo(400, int(anyo)) # R

# La expresión sería P ^ (¬Q v R)
if multiplo(4, int(anyo)) and (not multiplo(100, int(anyo)) or multiplo(400, int(anyo))):
    print(f"El {anyo} es bisiesto")
else:
    print(f"El {anyo} no es bisiesto")
