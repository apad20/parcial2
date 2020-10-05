suma = 0
while suma < 3:
   	entrada = input("Clave:")
   	#Si se ingresa la palabra "despedida, se termina el ciclo.
   	if entrada == "despedida":
       		break
   	suma = suma + 1
   	print("Intento %d. \n " % suma)
print("Tuviste %d intentos fallidos." % suma)
