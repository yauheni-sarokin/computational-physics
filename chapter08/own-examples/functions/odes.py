from numpy import linspace


def euler2(xpoints: [float], ypoints: [float], c: float, n: int):
    h = (xpoints[0] - xpoints[-1]) / n
    ypoints_d = []
    for y in ypoints:
        ypoints_d.append(c)
        c += y * h

    return xpoints, ypoints


def func_to_array(func, a, b, n):
    xpoints, ypoints = [], []
    range_ = linspace(a, b, n)
    # print(arange(0, 10, 100))
    for x in range_:
        xpoints.append(x)
        ypoints.append(func(x))
    return xpoints, ypoints


def euler(c: float, a: float, b: float, n: int, function):
    """
    a # Start of the interval
    b # End of the interval
    n # Number of steps
    h = (b - a) / N  # Size of a single step
    c = 0.0  # Initial condition
    """
    h = (b - a) / n
    xpoints = arange(a, b, h)
    ypoints = []

    for x in xpoints:
        ypoints.append(c)
        c += h * function(x)
        # c += 1

    # print(function(1))
    # function('s')
    return xpoints, ypoints
