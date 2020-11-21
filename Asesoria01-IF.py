#edad = int(input("Introduce tu edad"))

edad = input('Introduce tu edad')
edad = int(edad)

if edad >= 18: #Evaluación de una condición
    #Código que se ejecuta en caso de que la condición sea Verdadera
    print('Eres mayor de edad')
elif edad < 0:
    print('No puede haber edades negativas')
else:
    print('Eres menor de edad')