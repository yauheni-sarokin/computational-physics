# random walk page 75
from vpython import *
import random

random.seed(None)  # Seed generator, None => System clock
jmax = 60
x = 0.
y = 0.  # Start at origin
z = 0.  # Start at origin

c = curve(retain=15)
radius = 0.01
# for i in range(0, jmax + 1):
for i in range(jmax + 1):
    # rate(1)
    sleep(0.2)
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    z += (random.random() - 0.5) * 2
    radius += 0.001
    c.append(vector(x, y, z), radius=radius)
    print("i", i, "\tx ", x, "\ty ", y)
