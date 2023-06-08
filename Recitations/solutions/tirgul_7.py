import numpy as np


def gen_mat(n):
    x = np.identity(n)
    returned_mat = np.logical_or(x, np.fliplr(x)).astype(int)
    returned_mat *= n
    print(returned_mat)


gen_mat(6)

tmp1 = np.reshape(np.arange(1, 31), (30, 1))
# print(tmp1)

tmp2 = np.random.uniform(15, 25, size=(30, 1))
# print(tmp2)
table = np.hstack([tmp1, tmp2])

print(table)
print(table.shape)

mask = table[:, 1] > 22
# print(np.where(mask))
table2 = table[mask]
print(table2)
