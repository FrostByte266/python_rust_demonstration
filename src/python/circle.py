import PySimpleGUI as sg 
import numpy as np 

import matplotlib.pyplot as plt

from io import BytesIO
from base64 import b64encode

import rustic

layout = [
    [sg.Text('Radius:'), sg.Input('1', key='r', size=(3, 1)), sg.Button('Plot', bind_return_key=True), sg.Button('Clear')],
    [
        sg.Checkbox('Offset the figure?', key='cb', enable_events=True),
        sg.Input('0', size=(3, 1), key='x', disabled=True), 
        sg.Input('0', size=(3, 1), key='y', disabled=True)
    ],
    [sg.Image('640x480.png', size=(640, 480), key='img')],
    [sg.Exit()]
]

window = sg.Window('Circle Plotter', layout=layout, finalize=True)

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
        r = float(window['r'].Get())

        x_off = float(window['x'].Get()) if checked else 0
        y_off = float(window['y'].Get()) if checked else 0

        x, y = rustic.circle_points_offset(r, x_off, y_off)
        plt.plot(x, y)
        plt.text(
            x_off,
            y_off,
            f'Circle\nRadius: {r:g}\nCenter: ({x_off:g}, {y_off:g})',
            horizontalalignment='center',
            verticalalignment='center',
            bbox={'edgecolor': 'red', 'facecolor': 'white'}
        )
        bio = BytesIO()
        plt.savefig(bio, facecolor='#D9D9D9')
        bio.seek(0)
        enc = b64encode(bio.read())
        window['img'].Update(data=enc)
    elif event == 'Clear':
        starting_plot()
        window['cb'].Update(0)
        