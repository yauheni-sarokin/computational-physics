from math import sin
from numpy import arange
# from pylab import plot,xlabel,ylabel,show
from vpython import *


def f(x, t):
    return -x + sin(t)


a = 0.0
b = 10.0
N = 100
h = (b - a) / N

tpoints = arange(a, b, h)
xpoints = []
original_xpoints = []
x = 0.0
x_original = 0.

for t in tpoints:
    xpoints.append(x)
    original_xpoints.append(f(0, t))
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# plot(tpoints, xpoints)
# xlabel("t")
# ylabel("x(t)")
# show()


graph1 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>', ytitle='<i>Y[0]</i><sup>2</sup>')
funct1 = gcurve(color=color.blue)

graph2 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>', ytitle='<i>Y[0]</i><sup>2</sup>')
funct2 = gcurve(color=color.blue)

for x, y in zip(tpoints, xpoints):
    funct1.plot(x, y)
    # f()
    # funct2.plot(x, y)
    # rate(30)

for x, y in zip(tpoints, original_xpoints):
    funct2.plot(x, y)
