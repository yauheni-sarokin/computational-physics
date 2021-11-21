# Bisection is a simple implementation of the bisection algorithm for finding a zero of a function,
# in this case '2 cos x - x'
# actually to put nicw comment press ctrl+alt+ö 🍉


from vpython import *


def f(x):
    return 2 * cos(x) - x


def bisection(xminus, xplus, Nmax, eps):  # x+, x-, Nmax, error
    for it in range(0, Nmax):
        x = (xplus + xminus) / 2.  # mid point
        print(' it ', it, ' x ', x, ' f(x) ', f(x))
        if (f(xplus) * f(x) > 0.):  # root in other half
            xplus = x  # change x+ to x
        else:
            xminus = x  # change x- to x
        if (abs(f(x)) < eps):
            print('\n Root found with precision eps = ', eps)
            break
        if it == Nmax - 1:
            print('\n Root NOT found after Nmax iterations\n')
    return x


eps = 1e-6              # Precision of zero
a, b = 0.0, 7.0         # Root in [a, b]
imax = 100              # Max no. iterations
root = bisection(a, b, imax, eps)
print(' Root =', root)
