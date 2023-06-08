import numpy as np
from matplotlib import pyplot as plt


# Q1
def create2Dfun(minScale, maxScale, nbins, a, b):
    x = np.linspace(minScale, maxScale, nbins)
    y = np.linspace(minScale, maxScale, nbins)
    xx, yy = np.meshgrid(x, y)
    f = a * xx + b * yy + (a ** 2 * b ** 2 * xx * yy)
    f = np.transpose(f)
    return x, y, f


# Q2
def frev(f):
    f_flip = np.flip(f, 1)
    f_rev = np.hstack([f, f_flip])
    return f_rev


# Q3
def fext(f):
    flip_f = np.flip(f, 0)
    rev_f = np.vstack([f, flip_f])
    return rev_f


# Q4
def fsym(f, i_min, i_max):
    return f[i_min:i_max, i_min:i_max]


# Q5
def is_symetric(f):
    return np.all(f == np.flip(f))


def main():
    pass
    # Q1 testing
    x_, y_, f_ = create2Dfun(-10, 10, 80, 1, -1)
    plt.figure("func3D")
    plt.contourf(x_, y_, f_)
    plt.savefig("func3D.png")
    plt.show()

    # Q2 testing
    f_adj = frev(f_)
    plt.figure("f_adj")
    plt.contourf(np.linspace(-20, 20, 160), y_, f_adj)
    plt.savefig("f_adj.png")
    plt.show()

    # Q3 testing
    f_ext = fext(f_adj)
    plt.figure("f_extended")
    plt.contourf(np.linspace(-20, 20, 160), np.linspace(-20, 20, 160), f_ext)
    plt.savefig("f_extended.png")
    plt.show()

    # Q4 testing
    f_symmetric = fsym(f_ext, 40, 120)
    plt.figure("f_symmetric")
    plt.contourf(x_, y_, f_symmetric)
    plt.savefig("f_symmetric.png")
    plt.show()

    # Q5 testing
    print(f"f_symmetric is symetric {is_symetric(f_symmetric)}")


if __name__ == "__main__":
    main()
