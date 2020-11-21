#Un programa en el que se vayan acumulando las cantidades de gasto capturadas.
#La captura deberá seguir indefinidamente hasta que se capture un valor negativo.

acumulado = 0
cantidad = 0

while cantidad >= 0:
    acumulado += cantidad
    cantidad = float(input('Introduce la cantidad gastada: '))

print("El acumulado de gastos es: " + str(acumulado))
