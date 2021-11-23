# implementing rk4 algorithm, 4th order Runger Kutta

from vpython import *
from numpy import zeros

# Initialization
a = 0.
b = 10.
n = 100
ydumb, y = zeros(2, float), zeros(2, float)
fReturn = zeros(2, float)
k1, k2, k3, k4 = zeros(2, float), zeros(2, float), zeros(2, float), zeros(2, float),

y[0], y[1] = 3., -5.
t = a
h = (b - a) / n


def f(t, y):  # Force function
    fReturn[0] = y[1]
    fReturn[1] = -100. * y[0] - 2. * y[1] + 10. * sin(3. * t)
    return fReturn


graph1 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[0]</i><sup>2</sup>')

funct1 = gcurve(color=color.blue)

graph2 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>',
               ytitle='<i>Y[1]</i><sup>2</sup>')

funct2 = gcurve(color=color.blue)


def rk4(t, h, n):
    k1 = [0] * (n)
    k2 = [0] * (n)
    k3 = [0] * (n)
    k4 = [0] * (n)
    fR = [0] * (n)
    ydumb = f(t, y)
    fR = f(t, y)
    for i in range(0, n):
        k1[i] = h * fR[i]
    for i in range(0, n):
        ydumb[i] = y[i] + k1[i] / 2.
    k2 = h * f(t + h / 2., ydumb)
    for i in range(0, n):
        ydumb[i] = y[i] + k2[i] / 2.
    k3 = h * f(t + h / 2., ydumb)
    for i in range(0, n):
        ydumb[i] = y[i] + k3[i]
    k4 = h * f(t + h / 2., ydumb)
    for i in range(0, 2):
        y[i] = y[i] + (k1[i] + 2. * (k2[i] + k3[i]) + k4[i]) / 6.
    return y


while t < b:  # time loop
    if (t + h) > b:
        h = b - t  # last step
    y = rk4(t, h, 2)
    t = t + h
    rate(30)
    funct1.plot(pos=(t, y[0]))
    funct2.plot(pos=(t, y[1]))
