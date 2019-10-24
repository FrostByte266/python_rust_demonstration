import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np 
import math
import rustic

x = np.array([
    [1, 1],
    [2, 2.5],
    [3, 1]
])

def is_congruent(base: plt.Polygon, compare: plt.Polygon, return_match_mode=False) -> tuple:
    pass

def get_triangle_angles(triangle: plt.Polygon) -> tuple:
    points = triangle.get_xy()
    a, b, c = points[:-1]

    abc = rustic.get_angle(a, b, c)
    bac = rustic.get_angle(b, a, c)
    bca = rustic.get_angle(b, c, a)

    return abc, bac, bca


ax = plt.gca()
plt.scatter(x[:, 0], x[:, 1])
t1 = plt.Polygon(x)
coords = t1.get_xy()[:-1]
abc, bac, bca = get_triangle_angles(t1)
ang = '\u2220'
print(f'{ang} ABC: {abc:.2f}\n'
f'{ang} BAC: {bac:.2f}\n'
f'{ang} BCA: {bca:.2f}\n'
)
ax.add_patch(t1)
plt.show()
