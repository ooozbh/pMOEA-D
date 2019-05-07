import numpy as np
from DrawPicture import get_can


def calhy(x, y):
    l = len(x)
    res = 0.0
    for i in range(l):
        if i == 0:
            res = res + x[1] * (1 - y[0])
        elif i == l - 1:
            res = res + (1 - x[i]) * (1 - y[i])
        else:
            res = res + (x[i + 1] - x[i]) * (1 - y[i]);
    return res


def get_hv(filename):
    m1 = np.loadtxt(filename)
    x1, y1 = get_can(m1)
    return calhy(x1, y1)
