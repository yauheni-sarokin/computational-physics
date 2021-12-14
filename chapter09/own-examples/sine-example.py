import numpy as np
from numpy import trapz, diff, linspace, pi, add, delete, array, asarray
from vpython import *

graph1 = graph(width=400, height=400, title='<b>function</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[0]</i><sup>2</sup>')

funct1 = gcurve(color=color.blue)

graph2 = graph(width=400, height=400, title='<b>function 2</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[1]</i><sup>2</sup>')

funct2 = gcurve(color=color.orange)

graph3 = graph(width=400, height=400, title='<b>function 3</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[1]</i><sup>2</sup>')

funct3 = gcurve(color=color.magenta)


def f(x):
    return sin(x)


x_start, x_end = 0, 2 * pi
x_axis = linspace(x_start, x_end, num=100)
# x_axis = [x for x in range(x_start, x_end)]
y_axis = [f(x) for x in x_axis]
# y_axis = [f(x) for x in range(x_start, x_end)]

for x, y in zip(x_axis, y_axis):
    funct1.plot(x, y)

dx = x_axis[1] - x_axis[0]

y_axis_diff = diff(y_axis) / dx

for x, dy in zip(x_axis, y_axis_diff):
    funct2.plot(x, dy)

y_axis: np.array = asarray(y_axis)
print(type(y_axis))
y_axis = delete(y_axis, y_axis.size - 1)
y_plus_dy = add(y_axis, y_axis_diff)
# y_plus_dy = delete(y_plus_dy, y_plus_dy.size() - 1)

for x, y in zip(x_axis, y_plus_dy):
    funct3.plot(x, y)
