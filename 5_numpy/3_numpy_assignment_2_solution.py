import numpy as np
from matplotlib import pyplot as plt


# Q1
def create2Dfun(min_scale, max_scale, nbins, a, b):  # ADD INPUT
    """ create a 2D matrix, f """
    x = np.linspace(min_scale, max_scale, nbins)
    y = np.linspace(min_scale, max_scale, nbins)
    X, Y = np.meshgrid(x, y)
    f = a * X + b * Y + a ** 2 * b ** 2 * X * Y
    f = np.transpose(f)
    return x, y, f


# Q2
def frev(f):  # ADD INPUT
    """ create frev, a mirror image of f matrix in x dimension
    concatenate f and frev in the column axis
    to give f_adj, a 80X160 array
    """
    f_rev = np.hstack((f, np.fliplr(f)))
    return f_rev


# Q3
def fext(a):  # ADD INPUT
    """
    add a mirror image of f_adj in the rows dimension to f_adj itself
    i.e., the dimension of the new matrix should be 160X160
    hint: use np.append in the right axis
    """
    b = np.flipud(a)
    f_rev = np.vstack((a, b))
    return f_rev


# Q4
def fsym(arr, i_min, i_max):  # ADD INPUT
    """ slice out the core of f_extended matrix,
    to include only 80X80 array points with full symmetry
    in both the row and column dimensions
    hint: see figure to advice for the slicing boundaries
    """
    return arr[i_min:i_max, i_min:i_max]


# Q5
def is_symetric(arr):  # ADD INPUT
    """
    check a matrix's symmetry:
    test if all points in the upper and in the lower half
    of the array in the row's dimension are identical.
    hint: you should compare all values from the beginning of a row
    to the middle of the row, with all values from the end of the row
    to the middle of it for every column,
    and then test if equality holds in all columns
    """
    return np.all(arr == np.flip(arr))


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
    print(f"f_symmetric is symetric {is_symetric(f_ext)}")


if __name__ == "__main__":
    main()
