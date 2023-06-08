import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

# array attributes:
print(f'the shape of a is {a.shape}')  # Tuple of array dim
print(f'the type of a is {type(a)}')
print(f'the type of a elements is {a.dtype}')
print(f'the size of a is {a.size}')  # Number of elements
print(f'number of dimensions of a is {a.ndim}')
print(f'itemsize is {a.itemsize}')

# array initiation:
a = np.zeros((3, 4))
print(a, '\n')
a = np.zeros((3, 4), dtype='int32')
print(a, '\n')
a = np.ones((2, 5))
print(a, '\n')
x = np.ones(2, dtype=np.int64)
print(x, '\n')
a = np.full((2, 2), 99)
print(a, '\n')
a = np.identity(5)
print(a, '\n')

# np.arange - range-like array initiation
a = np.arange(4)
print(a, '\n')
a = np.arange(2, 9, 2)
print(a, '\n')
a = np.arange(0, 2, 0.3)
print(a, '\n')

# np.linspace() - vector array spanning
a = np.linspace(0, 20, 10)
print(a)

# array slicing and indexing:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a, '\n')
print(f'a[0] = {a[0]}')
print(f'a[0,:] = {a[0, :]}')
print(f'a[1,3] = {a[1, 3]}')
print(f'a[:,2] = {a[:, 2]}')

# more slicing examples
b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(b[0, 1:6:2])
# 3D arrays slicing example
a = np.arange(18).reshape(2, 3, 3)
print(a[1, -1, 2])
print(a[1, -1])  # if a was a list a[1][-1]
print(a[1, -1, :])
#
print(a[1])
print(a[1, :, :])
print(a[1, ...])

# updating array values:
a = np.arange(10) ** 3
a[:6:2] = 1000  # equivalent to a[0:6:2] = 1000;
print(a)

b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
b[1, 5] = 1500
print(b, '\n')
b[:, 2] = [100, 200]
print(b)

# array manipulations
# reshape
b = np.arange(12).reshape(4, 3)
print(b, '\n')
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c, '\n')
print(np.arange(10000), '\n')
print(np.arange(10000).reshape(100, 100), '\n')

# flatten
y = np.array([[2, 3], [4, 5], [6, 7]])
print(y.flatten(), '\n')  # order='C' is the default
print(y.flatten(order='F'), '\n')

# array transpose
a = np.arange(6).reshape((2, 3))
print(a, '\n')
b = np.transpose(a)
print(b)

# Array randomization with np.random
x = np.random.randint(100, size=5)
print(x)
x = np.random.randint(100, size=(3, 5))
print(x)
x = np.random.rand(5)
print(x)
x = np.random.rand(3, 5, 2)
print(x)
x = np.random.uniform(2, 10, size=(2, 3))
print(x)
x = np.random.choice([3, 5, 7, 9])
print(x)
x = np.random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# array vector products
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b  # elementwise substraction
print(c)
print(a + 2)
print(b ** 2)
a = np.arange(12).reshape(4, 3)
b = np.array([10, 20, 30])
print(a + b)  # element-wise addition
print(np.add(a, b))  # element-wise addition
print(a * b)  # element-wise multiplication
print(np.multiply(a, b))
print(a / b)  # element-wise division
print(np.divide(a, b))
arr = np.arange(20).reshape(4, 5)
print(arr)
print(10 * np.sin(arr))

# Array filtration
print(arr < 5)  # array filtration
print(arr[arr < 5])  # slicing array indexes by filter
# complex condition filtering (c-based code)
mask = (arr > 15) | (arr % 2 == 0)  # in python 'or' in c '|', 'and' in c '&'
print(mask)
# get values of filter
print(arr[mask])
# get indexes of positive filter elements
print(np.where(mask))
# finding element indexes of filter using np.where
low_indexes1D = np.where(c <= 30)  # creating 1Darray of indexes by filter
print(low_indexes1D)
low_indexes2D = np.where(arr < 5)  # creating 2Darray of indexes by filter
print(low_indexes2D)

# Joining arrays
# concatenate
a = np.arange(10).reshape(2, 5)
b = np.arange(10, 20).reshape(2, 5)
c = np.concatenate((a, b))
print(c)
d = np.concatenate((a, b), axis=1)
print(d)

# Array stacking
# vstack, hstack
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

v = np.vstack([v1, v2])  # equivalent to np.concatenate(*,axis = 0)
print(v, '\n')

h = np.hstack([v1, v2])  # equivalent to np.concatenate(*,axis = 1)
print(h, '\n')
