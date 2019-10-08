from rustic import cosine, gen_circle_points
from numpy import linspace, array, pi
from math import cos

num = 2.8
print(f'Python cos of {num}: {cos(num)}')
print(f'Rust cos of {num}: {cosine(num)}')
assert cos(num) == cosine(num)

t = linspace(0, pi*2)
x = linspace(0, pi*2)
y = linspace(0, pi*2)

print(f'First index of X before mutation: {x[0]}')
print(f'First index of Y before mutation: {y[0]}')
gen_circle_points(0.2, x, y)
print(f'First index of X after mutation: {x[0]}')
print(f'First index of Y after mutation: {y[0]}')

