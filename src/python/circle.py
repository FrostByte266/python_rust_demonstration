import matplotlib.pyplot as plt 

import numpy as np 
import rustic
from math import cos, sin

t = np.linspace(0,np.pi*2)

r = 0.2
# x = r*np.cos(t)
# y = r*np.sin(t)

x = t
y = t 

# x = [r * cos(i) for i in t]
# y = [r * sin(i) for i in t]


print(x)
rustic.gen_circle_points(r, x, y)
print(x)
plt.plot(x, y)
plt.show()