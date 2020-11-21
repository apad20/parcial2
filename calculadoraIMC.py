# Problema 1.
# El Indice de Masa muscular se calcula dividiendo los kilogramos de peso por el cuadrado de la estatura en metros.
# Si el resultado excede a 25 quiere decir que la persona tiene sobrepeso.
# Elabora un programa con interface gráfica que calcule el IMC de una persona, solicitando peso en kg y estatura en m,
# calcule el IMC y diga si tiene o no sobrepeso.

#DISEÑO DE INTERFACE
#Paso 1 - Importar libreria
import PySimpleGUI as sg

#OPERACIONES
#Función para calcular el IMC
def calcularIMC(v):
    # Proceso de cálculo IMC
    try:
        estatura = float(v['-ESTATURA-'])
        peso = float(v['-PESO-'])
        imc = peso / estatura ** 2
        msg0 = 'El índice de masa corporal es: ' + str(imc)
        if imc >= 25:
            msg1 = 'Tienes sobrepeso'
        else:
            msg1 = 'No tienes sobrepeso'
    except ValueError:
        msg0 = 'Los campos están vacíos'
        msg1 = 'o no hay valores numéricos'
    except ZeroDivisionError:
        msg0 = 'No es posible que la estatura sea 0m'
        msg1 = ''
    return msg0, msg1

#Función para limpiar campos
def limpiarCampos(w):
    w['-PESO-'].update('')
    w['-ESTATURA-'].update('')


#INTERFACE GRÁFICA
def main():
    #Paso 2 - Elegir tema
    sg.theme('SystemDefault')

    #Paso 3 - Definir Layout
    layout = [
                [ sg.Text('Estatura en metros'), sg.InputText(key='-ESTATURA-')], # ROW 1
                [ sg.Text('Peso en kilogramos'), sg.InputText(key='-PESO-')], # ROW 2
                [ sg.Button('Limpiar'), sg.Button('Calcular'), sg.Button('Salir')] #ROW 3
            ]

    #Paso 4 - Crear la ventana
    window = sg.Window('Calculadora IMC', layout)

    #Paso 5 - Loop de eventos
    while True:
        #Ejecución de nuestro programa
        event, values  = window.read()

        #Tratamiento de los eventos
        if event == sg.WIN_CLOSED or event=='Salir':    #Botón SALIR
            break
        elif event == 'Calcular':                       #Botón CALCULAR
            #Llamada a método de cálculo de IMC
            mensaje = calcularIMC(values)
            #Llamada a POPUP con resultados
            sg.popup(mensaje[0], mensaje[1])
            #Llamada al método limpieza de campos
            limpiarCampos(window)
        elif event == 'Limpiar':                        #Botón LIMPIAR
            #Llamada al método limpieza de campos
            limpiarCampos(window)


#FLUJO PRINCIPAL
main()