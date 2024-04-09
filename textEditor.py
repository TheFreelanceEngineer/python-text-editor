import PySimpleGUI as sg

layout = [  [sg.Button('Ok'), sg.Button('Cancel')]  ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' :
        break
    print('You entered ', values[0])

window.close()