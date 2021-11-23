from math import sin
from numpy import arange
from vpython import *


# from pylab import plot,xlabel,ylabel,show

def f(x, t):
    return -x ** 3 + sin(t)


a = 0.0  # Start of the interval
b = 10.0  # End of the interval
N = 1000  # Number of steps
h = (b - a) / N  # Size of a single step
x = 0.0  # Initial condition

tpoints = arange(a, b, h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x += h * f(x, t)

graph1 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>', ytitle='<i>Y[0]</i><sup>2</sup>')
funct1 = gcurve(color=color.blue)

for x, y in zip(tpoints, xpoints):
    funct1.plot(x, y)