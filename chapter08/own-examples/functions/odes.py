from numpy import linspace, arange


def euler(xpoints: [float], ypoints: [float], c: float = 0) -> [float]:
    '''
    This function finds derivative of the set of x and y points
    :param xpoints: set of x-axis datapoints
    :param ypoints: set of y-axis datapoints
    :param c: any constant
    :return: only set of y points
    '''
    n = len(xpoints)
    h = (xpoints[-1] - xpoints[0]) / n
    ypoints_d = []
    for y in ypoints:
        ypoints_d.append(c)
        c += y * h

    return ypoints_d


def func_to_array(func, a: float, b: float, n) -> tuple[[float], [float]]:
    '''

    :param func:
    :param a: start from
    :param b: end at
    :param n: how precise
    :return:
    '''
    xpoints, ypoints = [], []
    range_ = linspace(a, b, n)
    for x in range_:
        xpoints.append(x)
        ypoints.append(func(x))
    return xpoints, ypoints
