import PySimpleGUI as sg 
import numpy as np 

import matplotlib.pyplot as plt

from io import BytesIO
from base64 import b64encode

import rustic

layout = [
    [
        sg.Text('Height:'), sg.Input('1', key='h', size=(3, 1)),
        sg.Text('Width:'), sg.Input('1', key='w', size=(3, 1))
    ],
    [
        sg.Checkbox('Set custom origin point (default: (0, 0))?', key='cb', enable_events=True),
        sg.Input('0', size=(3, 1), key='x', disabled=True), 
        sg.Input('0', size=(3, 1), key='y', disabled=True)
    ],
    [sg.Button('Plot', bind_return_key=True), sg.Button('Clear')],
    [sg.Image('640x480.png', size=(640, 480), key='img')],
    [sg.Exit()]
]

window = sg.Window('Trainagle Plotter', layout=layout, finalize=True)

def starting_plot():
    plt.clf()
    plt.text(0.5, 0.5, 'Press plot to begin!', size=20, horizontalalignment='center', verticalalignment='center')
    bio = BytesIO()
    plt.savefig(bio, facecolor='#D9D9D9')
    bio.seek(0)
    enc = b64encode(bio.read())
    window['img'].Update(data=enc)
    plt.clf()

starting_plot()

while True:
    event, values = window.Read()
    # print(values)
    if event in (None, 'Exit'):
        break
    checked = bool(window['cb'].Get())
    elements = ['x', 'y']
    list(map(lambda i: window[i].Update(disabled=not checked), elements))
    if event == 'Plot':
        t = np.linspace(0, np.pi*2)
        # r = float(window['r'].Get())

        x = t.copy()
        y = t.copy()

        x_off, y_off = map(lambda i: float(window[i].Get() if checked else 0), elements)

        # rustic.linspace_to_circle_points_with_offset(r, x, y, x_off, y_off)
        # plt.plot(x, y)
        # plt.text(
        #     x_off,
        #     y_off,
        #     f'Circle\nRadius: {r:g}\nCenter: ({x_off:g}, {y_off:g})',
        #     horizontalalignment='center',
        #     verticalalignment='center',
        #     bbox={'edgecolor': 'red', 'facecolor': 'white'}
        # )
        # bio = BytesIO()
        # plt.savefig(bio, facecolor='#D9D9D9')
        # bio.seek(0)
        # enc = b64encode(bio.read())
        # window['img'].Update(data=enc)
    elif event == 'Clear':
        starting_plot()
        window['cb'].Update(0)
        