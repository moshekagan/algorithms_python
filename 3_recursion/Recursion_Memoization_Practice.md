
# Recursion and Memoization in Python

## Simple Recursion Example: Fibonacci Sequence

The Fibonacci sequence is defined as:
- \(F(0) = 0\)
- \(F(1) = 1\)
- \(F(n) = F(n-1) + F(n-2)\) for \(n > 1\)

Here's a simple recursive implementation:

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10))  # Output: 55
```

## Memoized Recursion Example: Fibonacci Sequence

To optimize the recursive solution, we can use memoization. This involves storing the results of expensive function calls and returning the cached result when the same inputs occur again.

Here's the memoized version:

```python
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
    
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    
    memo[n] = result
    return result

# Example usage
print(fibonacci_memo(10))  # Output: 55
```

## Explanation

1. **Simple Recursion**:
    - The function `fibonacci(n)` calls itself to compute the Fibonacci number.
    - This approach has an exponential time complexity, \(O(2^n)\), because it recalculates the same values multiple times.

2. **Memoized Recursion**:
    - The function `fibonacci_memo(n, memo)` uses a dictionary `memo` to store previously computed results.
    - Before performing any computation, it checks if the result for the current `n` is already in `memo`. If so, it returns the cached result.
    - This reduces the time complexity to \(O(n)\), making it much more efficient.

## Practice Problems

To practice, try implementing the following problems using both simple recursion and memoized recursion:

1. **Factorial Calculation**:
    - Simple recursion: \(n! = n 	imes (n-1)!\)
    - Memoized recursion to avoid recalculating values.

2. **Climbing Stairs**:
    - You can climb 1 or 2 steps. How many distinct ways can you climb to the top if the staircase has `n` steps?

3. **Unique Paths in a Grid**:
    - You are given an `m x n` grid. Start at the top-left corner and move to the bottom-right corner. You can only move down or right. How many unique paths are there?

