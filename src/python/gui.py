import PySimpleGUI as sg 
import numpy as np 

import matplotlib.pyplot as plt

from io import BytesIO
from base64 import b64encode

import rustic

layout = [
    [sg.Text('Radius:'), sg.Input('1', key='r', size=(3, 1), enable_events=True), sg.Button('Plot', bind_return_key=True), sg.Button('Clear')],
    [
        sg.Checkbox('Offset the figure?', key='cb', enable_events=True), sg.Input('0', size=(3, 1), key='x', enable_events=True, disabled=True), 
        sg.Input('0', size=(3, 1), key='y', enable_events=True, disabled=True)
    ],
    [sg.Image('/src/python/640x480.png', key='img')],
    [sg.Exit()]
]

def starting_plot():
    plt.clf()
    plt.text(0.5, 0.5, 'Press plot to begin!', size=20, horizontalalignment='center', verticalalignment='center')
    bio = BytesIO()
    plt.savefig(bio, facecolor='#D9D9D9')
    bio.seek(0)
    enc = b64encode(bio.read())
    window['img'].Update(data=enc)
    plt.clf()

window = sg.Window('Circle Plotter', layout=layout, finalize=True)
starting_plot()

while True:
    event, values = window.Read()
    # print(values)
    if event in (None, 'Exit'):
        break
    checked = bool(window['cb'].Get())
    window['x'].Update(disabled=not checked)
    window['y'].Update(disabled=not checked)
    if event == 'Plot':
        t = np.linspace(0, np.pi*2)
        r = float(window['r'].Get())

        x = t.copy()
        y = t.copy()

        x_off = float(window['x'].Get()) if checked else 0
        y_off = float(window['y'].Get()) if checked else 0

        rustic.linspace_to_circle_points_with_offset(r, x, y, x_off, y_off)
        plt.plot(x, y)
        plt.text(
            x_off,
            y_off,
            f'Circle\n{r:g} radius\nCenter {x_off:g}, {y_off:g}',
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
        