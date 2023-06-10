import numpy as np


if __name__ == "__main__":
    x = np.linspace(-10, 10, 50)

    mask1 = x > 1.5
    res = np.any(mask1)
    print(res)  # True

    res = np.all(mask1)
    print(res)  # False

    mask1 = x > -100    # [T, T, T, T....]
    res = np.any(mask1)
    print(res)  # True

    res = np.all(mask1)
    print(res)  # True

    mask1 = (x < -100)  # [F, F, F,...]
    res = np.any(mask1)
    print(res)  # False

    res2 = np.all(mask1)
    print(res)  # False

    arr = np.arange(10)
    mask = (arr % 2 == 0) | (arr == 3)

    filter_arr = arr[mask]
    print(filter_arr)