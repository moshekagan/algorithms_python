"""
this script finds numerically the intersection between two polinomial functions:
f(x) and g(x)
"""
import numpy as np
from matplotlib import pyplot as plt


def span_x(min_x, max_x, bins):
    return np.linspace(min_x, max_x, bins)


def f_of_x(x, cofes):
    poly = np.poly1d(cofes)
    print(poly)
    res = poly(x)

    return res


#       0 1 2
# f1 = [1,2,3]
# f2 = [5,2,8]
# d =  [4,0,5]

# min1 = 0
# min1 == d
#
# m =  [F,T,F]
def find_intersects(f1, f2):
    distance = np.abs(f1 - f2)
    two_mins = sorted(distance)[:4]
    min_1 = two_mins[0]
    min_2 = two_mins[1]

    mask = (min_1 == distance) | (min_2 == distance)
    a = np.where(mask)

    return a[0]

    #### iterative solution:
    # pot_index = []
    # for i in range(len(distance)):
    #     if min_1 == distance[i] or min_2 == distance[i]:
    #         pot_index.append(i)
    #
    # return pot_index


def main():
    x = span_x(-10, 10, 50)
    f_x = f_of_x(x, [-5, 5, 2])
    g_x = f_of_x(x, [50, 5])
    plt.figure()
    plt.plot(x, f_x, 'k')
    plt.plot(x, g_x, 'k')
    intersect_indexes = find_intersects(f_x, g_x)
    plt.plot(x[intersect_indexes], g_x[intersect_indexes], 'r', marker='o', markersize=14, linewidth=0)
    plt.show()


if __name__ == "__main__":
    main()
