# Lambda Functions in Python

Lambda functions in Python are small, anonymous functions defined with the `lambda` keyword. Unlike regular functions defined using `def`, lambda functions can have any number of arguments but only one expression. They are often used for short, throwaway functions, where using `def` would be overkill.

The basic syntax of a lambda function is:
```python
lambda arguments: expression
```

## Examples of Lambda Functions

### Example 1: Basic Usage
A simple example of a lambda function that adds two numbers:
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### Example 2: Sorting with Lambda
Lambda functions are often used as key functions in sorting. For instance, sorting a list of tuples based on the second element:
```python
points = [(1, 2), (4, 1), (5, -1), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, -1), (4, 1), (1, 2), (2, 3)]
```

### Example 3: Filtering with Lambda
Using a lambda function with `filter()` to filter out even numbers from a list:
```python
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]
```

### Example 4: Mapping with Lambda
Using a lambda function with `map()` to square each number in a list:
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### Example 5: Reducing with Lambda
Using a lambda function with `reduce()` to calculate the product of a list of numbers:
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

## Explanation

1. **Basic Usage**:
    - `add = lambda x, y: x + y`: Defines a lambda function that takes two arguments and returns their sum.
  
2. **Sorting with Lambda**:
    - `sorted(points, key=lambda point: point[1])`: Sorts a list of tuples based on the second element of each tuple.

3. **Filtering with Lambda**:
    - `filter(lambda x: x % 2 != 0, numbers)`: Filters out even numbers from the list `numbers`.

4. **Mapping with Lambda**:
    - `map(lambda x: x ** 2, numbers)`: Applies the lambda function to each element of the list `numbers` to get their squares.

5. **Reducing with Lambda**:
    - `reduce(lambda x, y: x * y, numbers)`: Applies the lambda function cumulatively to the items of the list `numbers` to compute their product.

