"""
this script finds numerically the intersection between two polinomial functions:
f(x) and g(x)
"""
import numpy as np
from matplotlib import pyplot as plt


def span_x(min_x, max_x, bins):
    return np.linspace(min_x, max_x, bins)


def f_of_x(x, coefs):
    poly = np.poly1d(coefs)
    return poly(x)


def find_intersects(f1, f2):
    min_distances = sorted(np.abs(f1 - f2))[:2]
    condition = (min_distances[0] == np.abs(f1 - f2)) | (min_distances[1] == np.abs(f1 - f2))
    intersect_indexes = np.where(condition)[0]
    return intersect_indexes


def main():
    x = span_x(-10, 10, 50)
    f_x = f_of_x(x, [-5, 5, 2])
    g_x = f_of_x(x, [50, 5])
    plt.figure()
    plt.plot(x, f_x, 'k')
    plt.plot(x, g_x, 'k')
    intersect_indexes = find_intersects(f_x, g_x)
    plt.plot(x[intersect_indexes], f_x[intersect_indexes], 'r', marker='o', markersize=14, linewidth=0)
    plt.show()


if __name__ == "__main__":
    main2()
