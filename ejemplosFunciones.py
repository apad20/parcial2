#Declaración o definición de un método
def metodo(argumento1, argumento2, nombre):
    print(argumento1)
    print(argumento2, nombre)

def suma(a,b):
    r = a + b
    return r

def main():
    #Llamada a un método
    saludo="¿Cómo están"
    metodo("Hola",saludo, "alumnos?")
    elemento1 = 7
    elemento2 = 2
    resultado = suma(elemento1,elemento2)
    print(resultado)

main()