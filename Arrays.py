# Arreglos.
# -> En Python
# Como una lista de listas.

def cPromedioSemestre(c):
    for semestre in c:
        suma = 0
        for calificacion in semestre:
            suma += calificacion
        promedio = suma / len(semestre)
        semestre.append(promedio)

def cAcumulado(c):
    for semestre in c:
        semestre[-1]

def main():
    semestre1 = [8, 9, 7, 7]
    semestre2 = [9, 9, 8, 9]
    semestre3 = [7, 7, 9, 10]
    semestre4 = [8, 8, 9, 7]
    semestre5 = [9, 10, 9, 8]

    concentrado = [semestre1,
                   semestre2,
                   semestre3,
                   semestre4,
                   semestre5]

    # concentrado2=[[8, 9, 7, 7],
    #              [9, 9, 8, 9],
    #              [7, 7, 9, 10],
    #              [8, 8, 9, 7],
    #              [9, 10, 9, 8]]

    cPromedioSemestre(concentrado)
    print(concentrado)


main()
