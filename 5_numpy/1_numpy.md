# Numpy
```python
import numpy as np
```

#### 1. Array Attributes:
- `shape`: Returns the dimensions of an array.
- `type`: Returns the type of an array.
- `dtype`: Returns the data type of array elements.
- `size`: Returns the number of elements in an array.
- `ndim`: Returns the number of dimensions of an array.
- `itemsize`: Returns the size (in bytes) of each array element.

#### 2. Array Initialization and more:
- `np.zeros`: Creates an array filled with zeros.
- `np.ones`: Creates an array filled with ones.
- `np.full`: Creates an array filled with a specific value.
- `np.identity`: Creates an identity matrix.
- `np.arange`: Generates an array with a range of values.
- `np.linspace`: Generates an array with evenly spaced values.
- `np.poly1d`: is a function that creates a one-dimensional polynomial object from a sequence of coefficients.
- `np.abs`: is a function that returns the absolute values of the elements in an array.
- `np.where`: is a function that returns the indices where a specified condition is met in an array.
- `np.meshgrid`: is a function that generates coordinate matrices from coordinate vectors, which are commonly used for creating grids for evaluating functions over a specified range.
- `np.transpose`: is a function that returns a new array with the dimensions transposed, effectively swapping the rows and columns of a given array.
- `np.hstack`: is a function that horizontally stacks arrays, meaning it concatenates arrays along the column axis, allowing you to combine arrays side by side.
- `np.vstack`: is a function that vertically stacks arrays, which means it concatenates arrays along the row axis, allowing you to stack arrays on top of each other.
- `np.flipud`: is a function that flips an array vertically, reversing the order of rows in the array.
- `np.all`: is a function that returns True if all elements of an array evaluate to True, and False otherwise.
  
~ `plt.contourf`: is a __matplotlib__ function that creates filled contour plots based on a given array of data.




#### 3. Array Slicing and Indexing:
Array indexing allows accessing specific elements or subarrays of an array, while array slicing extracts portions of an array based on specified indices. Here are some examples:

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Accessing elements
print(a[0])          # [1, 2, 3, 4]
print(a[0, :])       # [1, 2, 3, 4]
print(a[1, 3])       # 8
print(a[:, 2])       # [3, 7, 11]

# Slicing subarrays
print(a[0, 1:6:2])   # [2, 4, 6]
print(a[1, -1, 2])   # 12
print(a[1, -1, :])   # [9, 10, 11, 12]
print(a[1])          # [5, 6, 7, 8]
print(a[1, :, :])    # [[5, 6, 7, 8]]
print(a[1, ...])     # [[5, 6, 7, 8]]
```

#### 4. Updating Array Values:
Array values can be updated by modifying elements using indexing or slicing. Here are some examples:

```python
a = np.arange(10) ** 3
a[:6:2] = 1000       # [1000, 1, 1000, 27, 1000, 125, 216, 343, 512, 729]

b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
b[1, 5] = 1500       # [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 1500, 14]]
b[:, 2] = [100, 200] # [[1, 2, 100, 4, 5, 6, 7], [8, 9, 200, 11, 12, 1500, 14]]
```
