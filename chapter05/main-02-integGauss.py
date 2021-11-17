# Gausian quadrature generator of pts & wts
import math

from numpy import *
from sys import version

max_in = 11  # numb intervals
vmin = 0.
vmax = 1.  # Int ranges
ME = 2.7182818284590452354E0  # Euler's constant
w = zeros(2001, float)
x = zeros(2001, float)


def f(x):  # integrand
    return exp(-x)


def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p2 = 0
    eps = 3.E-14  # Accuracy ADJUST THIS
    m = int((npts + 1) / 2)
    for i in range(1, m + 1):
        t = cos(math.pi * (float(i) - 0.25) / (float(npts) + 0.5))
        t1 = 1
        while abs(t - t1) >= eps:
            p1 = 1.
            p2 = 0.
            for i in range(1, npts + 1):
                p3 = p2
                p2 = p1
                p1 = ((2. * float(j - 1) * t * p2 - (float(j) - 1.) * p3) / float(j))
            pp = npts * (t * p1 - p2) / (t * t - 1.)
            t1 = t
            t = t1 - p1 / pp
        x[i - 1] = -t
        x[npts - i] = t
        w[i - 1] = 2. / ((1. - t * t) * pp * pp)
        w[npts - i] = w[i - 1]
    if job == 0:
        for i in range(0, npts):
            x[i] = x[i] * (b - a) / 2. + (b + a) / 2.
            w[i] = w[i] * (b - a) / 2.
    if job == 1:
        for i in range(0, npts):
            xi = x[i]
            x[i] = a * b * (1. + xi) / (b + a - (b - a) * xi)
            w[i] = w[i] * 2. * a * b * b / (b + a - (b - a) * xi) * (b + a - (b - a) * xi)
    if job == 2:
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b * xi + b + a + a) / (1. - xi)
            w[i] = w[i] * 2. * (a + b) / ((1. - xi) * (1. - xi))


def gaussint(no, min, max):
    quadra = 0.
    gauss(no, 0, min, max, x, w)  # returns pts & wts
    for n in range(0, no):
        quadra += f(x[n]) * w[n]  # calculate integral
    return quadra


for i in range(3, max_in + 1, 2):
    result = gaussint(i, vmin, vmax)
    print(" i ", i, " err ", abs(result - 1 + 1 / ME))  # 🙂

print("enter and retrn any char to quit")
