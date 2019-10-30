import PySimpleGUI as sg 
import numpy as np 

import matplotlib.pyplot as plt

from io import BytesIO
from base64 import b64encode

import rustic

layout = [
    [
        sg.Text('Height:'), sg.Input('1', key='h', size=(3, 1)),
        sg.Text('Width:'), sg.Input('1', key='w', size=(3, 1)),
        sg.Checkbox('Make this figure a right triangle?', key='r')
    ],
    [
        sg.Checkbox('Set custom origin point (default: (0, 0))?', key='cb', enable_events=True),
        sg.Input('0', size=(3, 1), key='x', disabled=True), 
        sg.Input('0', size=(3, 1), key='y', disabled=True),
        sg.Text('Angles:')
    ],
    [sg.Button('Plot', bind_return_key=True), sg.Button('Clear'), sg.T(' ' * 70), sg.Text(' ' * 10, key='a0')],
    [sg.T(' '* 104), sg.Text(' ' * 10, key='a1')],
    [sg.T(' ' * 104), sg.Text(' ' * 10, key='a2')],
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

def get_triangle_angles(triangle: plt.Polygon) -> tuple:
    points = triangle.get_xy()
    a, b, c = points[:-1]

    abc = rustic.get_angle(a, b, c)
    bac = rustic.get_angle(b, a, c)
    bca = rustic.get_angle(b, c, a)

    return abc, bac, bca

starting_plot()

while True:
    event, values = window.Read()
    # print(values)
    if event in (None, 'Exit'):
        break
    checked = bool(window['cb'].Get())
    elements = ['x', 'y']
    params = ['h', 'w']
    boxes = ['cb', 'r']
    angles = ['a0', 'a1', 'a2']
    list(map(lambda i: window[i].Update(disabled=not checked), elements))
    if event == 'Plot':
        x_off, y_off = map(lambda i: float(window[i].Get() if checked else 0), elements)
        height, width = map(lambda i: float(window[i].Get()), params)
        right = bool(window['r'].Get())

        fig, ax = plt.subplots()
        x, y = rustic.make_triangle(x_off, y_off, width, height, right)
        plt.scatter(x, y, marker='None')
        t1 = plt.Polygon(np.concatenate((x, y), axis=1))
        ax.add_patch(t1)
        ang = get_triangle_angles(t1)
        list(map(lambda i: window[i].Update(f'{ang[int(i[-1])]:.2f}°'), angles))
        bio = BytesIO()
        plt.savefig(bio, facecolor='#D9D9D9')
        bio.seek(0)
        enc = b64encode(bio.read())
        window['img'].Update(data=enc)
    elif event == 'Clear':
        starting_plot()
        list(map(lambda i: window[i].Update(0), boxes))

        