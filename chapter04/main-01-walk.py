# random walk, page 75
from vpython import *

import random

random.seed(None)
jmax = 200
x = 0.
y = 0.

scene = canvas(title='Random walk',
     width=600, height=600,
     center=vector(0,0,0), background=color.cyan)

c = curve(vector(-1,-1,0), vector(1,-1,0))
for i in range(0, jmax + 1):
    rate(10)
    c.append(vector(x, y, 0))
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
