# splineinteract spline fit with slide to control number of points

from vpython import *
from numpy import *

x = array([0., 0.12, 0.25, 0.37, 0.5, 0.62, 0.75, 0.87, 0.99])
y = array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
n, np = 9, 15

# Initialize
y2, u = zeros(n, float), zeros(n, float)
# graph = graph(width=600, height=600, x=0, y=0, xtitle='x', ytitle='y')
# graph = graph(x=0, y=0, xtitle='x', ytitle='y')

funct1 = gdots(color=color.yellow)


# funct2 = gdots(color=color.red)


def update(c):
    # Nfit = int(control)
    for i in range(0, n):
        funct1.plot(pos=(x[i] + c.value, y[i]))
        funct1.plot(pos=(1.01 * x[i], 1.01 * y[i]))
        funct1.plot(pos=(.99 * x[i], .99 * y[i]))
        # yp1 = (y[1] - y[0]) / (x[1] - x[0]) - (y[2] - y[1]) / (x[2] - x[1]) + (y[2] - y[0]) / (x[2] - x[0])


sl = slider(bind=update, min=1, max=50)
scene.append_to_caption('\n\n')
update(sl)
