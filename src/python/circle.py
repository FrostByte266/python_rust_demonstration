import matplotlib.pyplot as plt 

import numpy as np 
import rustic
from math import cos, sin
from copy import deepcopy

t = np.linspace(0, np.pi*2)

r = 1

x = t.copy()
y = t.copy()

rustic.gen_circle_points(r, x, y)
plt.plot(x, y)
plt.show()