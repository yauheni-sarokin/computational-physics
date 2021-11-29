from functions.odes import euler, func_to_array
from functions.plotter import plot


def func(x):
    return -1


xp, yp = func_to_array(func, 0, 10, 1000)

plot(xp, yp, 'euler ODE')
yp = euler(xp, yp, 5)

plot(xp, yp, 'first derivative')

yp = euler(xp, yp, 0)

plot(xp, yp, 'second derivative')
