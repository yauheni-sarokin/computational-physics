from functions.odes import euler, euler2, func_to_array
from functions.plotter import plot
import numpy as np
from vpython import *

np.random.random()


def func(x):
    return -1


xp, yp = func_to_array(func, 0, 10, 100)
print(xp)
print(yp)

xp, yp = euler2(xp, yp, 0, 100)
# xp, yp = euler(0, 0, 10, 20, func)


plot(xp, yp)
