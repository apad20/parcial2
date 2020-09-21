#Escribe un programa que responda a un usuario que quiere comprar
#un helado en una conocida marca de comida rápida,
#¿cuánto le costaría en función del topping que elija?

# el helado sin topping cuesta 1.90
# el topping de oreo cuesta 1
# el topping de KitKat cuesta 1.50
# el topping de brownie cuesta .75
# el topping de lacasitos cuesta .95

#En caso de no disponer del topping solicitado por el usuario, el programa
#escribirá por pantalla "NO TENEMOS ESTE TOPPING, LO SENTIMOS"
#y acontinuación informar el precio del helado sin ningún topping,
#al finalizar el programa muestra el precio del helado
#con el topping seleccionado (o ninguno)

#Inicialización de variables
#La Lista está conformada por la exitencia y el precio.
helado = 1.90 #precio del helado
#Lista, posición 0 = existencia, posición 1 = precio.
oreo = [3, 1]
kitkat = [0, 1.5]
brownie = [10, .75]
lucasitos = [2, .95]

#Mostrar el menú al usuario
print("Bienvenido a la Heladería \n"
      "Estos son nuestros toppings \n"
      "1. Oreo \n"
      "2. Kitkat \n"
      "3. Brownie \n"
      "4. Lucaciots \n"
      "5. Sin topping\n"
      "¿Cual eliges? introduce un número del 1 al 5")

#Solicitamos al usuario un número
respuesta = input()

#creamos una función
def topping (lista):
    if lista[0]>0:  #Si hay existencia
        lista[0] = lista[0] - 1   #descontamos 1 a la existencia
        return str(helado + lista[1])  #indicamos el total
    else:
        print("NO TENEMOS ESTE TOPPING, LO SENTIMOS")
        return str(helado)

#Trabajamos con la respuesta del usuario
#Estructura de control
if respuesta == "1":
    #OREO
    total = topping(oreo)
elif respuesta == "2":
    #Kitkat
    total = topping(kitkat)
elif respuesta == "3":
    #Brownie
    total = topping(brownie)
elif respuesta == "4":
    #Lucacitos
    total = topping(lucasitos)
else:
    #Sin topping
    total = str(helado)

print("EL Total de tu cumpra es " + total)


