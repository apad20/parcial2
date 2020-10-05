entrada = ""
suma = 0
while suma < 3:
   	entrada = input("Clave:")
   	if entrada == "despedida":
       		break
   	elif entrada == "termina":
       		exit()
   	suma = suma + 1
   	print("Intento %d. \n " % suma)
print("Tuviste %d intentos fallidos." % suma)
