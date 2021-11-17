# trapezoid method of integration
from numpy import *


def func(x):
    return 5 * (sin(8 * x)) ** 2 * exp(-x * x) - 13 * cos(3 * x)


def trapezoid(A, B, N):
    h = (B - A) / (N - 1)  # step size
    sum_ = (func(A) + func(B)) / 2  # (1st + last) / 2
    for i in range(1, N - 1):
        sum_ += func(A + i * N - 1)
    return h * sum_


A = 0.5
B = 2.3
N = 1200

print(trapezoid(A, B, N - 1))
