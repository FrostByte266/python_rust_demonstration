import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np 
import math
from rust_ext import get_angle

x = np.array([
    [1, 1],
    [2, 2.5],
    [3, 1]
])
 

def get_triangle_angles(triangle: plt.Polygon) -> tuple:
    points = triangle.get_xy()
    a = points[0]
    b = points[1]
    c = points[2]

    abc = get_angle(a, b, c)
    bac = get_angle(b, a, c)
    bca = get_angle(b, c, a)

    return abc, bac, bca



plt.figure()
plt.scatter(x[:, 0], x[:, 1])
t1 = plt.Polygon(x)
coords = t1.get_xy()[:-1]
abc, bac, bca = get_triangle_angles(t1)
ang = '\u2220'
print(f'{ang} ABC: {abc:.2f}\n'
f'{ang} BAC: {bac:.2f}\n'
f'{ang} BCA: {bca:.2f}\n'
)
plt.gca().add_patch(t1)
plt.show()
