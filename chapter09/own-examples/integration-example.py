import numpy as np
from numpy import trapz
from vpython import *

# f = trapz([1, 2, 3])

graph1 = graph(width=400, height=400, title='<b>function</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[0]</i><sup>2</sup>')

funct1 = gcurve(color=color.blue)

graph2 = graph(width=400, height=400, title='<b>integ</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[1]</i><sup>2</sup>')

funct2 = gcurve(color=color.orange)


def f(x):
    return x ** 1


x_start, x_end = 0, 20
# x_axis = [x for x in range(x_start, x_end)]
# y_axis = [f(x) for x in x_axis]
# y_integrated_axis = trapz(y_axis, x_axis)

x_accumulated, y_accumuated = np.array([]), np.array([])
for x in range(x_start, x_end):
    x_accumulated = np.append(x_accumulated, x)
    y_accumuated = np.append(y_accumuated, f(x))
    funct1.plot(pos=(x, y_accumuated[-1]))
    funct2.plot(x, trapz(y_accumuated, x_accumulated))
