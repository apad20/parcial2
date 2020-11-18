import PySimpleGUI as sg

#1 - DEFINIR EL TEMA
sg.theme('SystemDefault')   # Add a touch of color



#2.
# All the stuff inside your window.
layout = [
            [sg.Text('Clase GUI APAD 20')],   #row 1

            [sg.Text('Enter something on Row 2'), sg.InputText()],  #row2

            [sg.Text('Tercera línea'), sg.InputText()],  #row3

            [sg.Button('Ok'), sg.Button('Cancel')]  #row4
        ]

#3 Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0],values[1])

window.close()