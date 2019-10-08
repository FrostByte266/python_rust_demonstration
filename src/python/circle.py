import matplotlib.pyplot as plt 

import numpy as np 
import rustic
from math import cos, sin
from copy import deepcopy

t = np.linspace(0,np.pi*2)

r = 1
# x = r*np.cos(t)
# y = r*np.sin(t)

x = deepcopy(t)
y = deepcopy(t)

# x = t
# y = t

rustic.gen_circle_points(r, x, y)
plt.plot(x, y)
plt.show()