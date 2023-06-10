import numpy as np


x = [1, 2, 3]
y = [4, 6, 7]

# XY = [[(1, 4), (1, 6), (1, 7)],
#       [(2, 4), (2, 6), (2, 7)],
#       [(3, 4), (3, 6), (3, 7)]]

X, Y = np.meshgrid(x, y)

Z = 2*X + 3*Y

print(X)