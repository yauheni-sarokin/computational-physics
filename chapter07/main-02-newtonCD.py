# Newton search with central difference
from math import cos

x, dx, eps = 4, 3.e-1, 0.2  # Parameters
imax = 100  # max no of iterations


def f(x):  # function
    return 2 * cos(x) - x


for it in range(0, imax + 1):
    F = f(x)
    if (abs(F) <= eps):
        print('\n Root found, F=', F, ', tolerance eps = ', eps)
        break

    print('Iteration #= ', it, ' x = ', ' f(x) = ', F)
    df = (f(x + dx / 2) - f(x - dx / 2)) / dx  # central diff
    dx = -F / df
    x += dx  # new guess

