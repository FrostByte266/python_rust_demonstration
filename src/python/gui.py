import PySimpleGUI as sg 

import rustic

layout = [
    [sg.Checkbox('Offset the figure?', key='cb', enable_events=True), sg.Input('0', size=(3, 1), key='x', enable_events=True), sg.Input('0', size=(3, 1), key='y', enable_events=True)],
    [sg.Image('/src/python/640x480.png')],
    [sg.Exit()]
]

window = sg.Window('Test', layout=layout)

while True:
    event, values = window.Read()
    # print(values)
    if event in (None, 'Exit'):
        break
    checked = bool(window['cb'].Get())
    window['x'].Update(disabled= not checked)
    window['y'].Update(disabled= not checked)
    # print(window['cb'].Get())
