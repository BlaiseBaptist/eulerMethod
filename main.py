# This is a sample Python script.
import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt


def f(both):
    a = 1.5
    b = .2
    d = .1
    g = 1
    return (a * both[0] - b * both[0] * both[1]), (d * both[1] * both[0] - g * both[1])


def forward(x, y, step, size):
    vals = []
    for i in range(size):
        both = [x, y]
        x, y = np.array(f([x, y])) * step + both
        vals.append([x, y])
    xs = np.linspace(0, step * size, size)
    ys = np.array(vals)
    return xs, ys


def backward(x, y, step=.1, size=100):
    vals = []
    for i in range(size):
        both = np.array([x, y])
        x, y = root(lambda n: both + np.array(f(n)) * step - n, both)['x']
        vals.append([x, y])
    xs = np.linspace(0, step * size, size)
    ys = np.array(vals)
    return xs, ys


def main():
    size = 10000
    step = .01
    xs, ys = forward(10, 10, step, size)
    # xs, ys = backward(.1, 0, step=step, size=size)
    plt.plot(xs, ys)
    plt.show()


main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
