import numpy as np


# v = [1,2,4]
# num = 3
# res = [ [1,2,4],
#         [1,2,4],
#         [1,2,4]]


def rec_concat_v(v, num):
    if num <= 1:
        return v

    res = rec_concat_v(v, num - 1)

    return np.vstack((v, res))


# test
r = rec_concat_v([1, 2, 3], 0)
r = rec_concat_v([1, 2, 3], 1)
r = rec_concat_v([1, 2, 3], 2)
r = rec_concat_v([1, 2, 3], 4)

print()
