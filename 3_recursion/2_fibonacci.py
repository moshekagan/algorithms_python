"""
In this example, the fibonacci function calculates the Fibonacci number at a given position n in the Fibonacci sequence.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and 1.

The function uses recursion to break down the problem into smaller subproblems. The base cases are defined when n is 0 or 1,
where the Fibonacci number is known to be 0 and 1, respectively. For any other value of n, the function recursively calls
itself with n - 1 and n - 2 to calculate the Fibonacci number at the desired position.

When you run this code, it will output the Fibonacci number at position 6, which is 8. You can modify the input value
passed to the fibonacci function to calculate the Fibonacci number at a different position.
"""

# 0  1  2 3 4 5 6  7  8
# 0  1   ....

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and Fibonacci of (n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
result = fibonacci(0)
print(result)

result = fibonacci(1)
print(result)

result = fibonacci(2)
print(result)

result = fibonacci(3)
print(result)

result = fibonacci(6)
print(result)

result = fibonacci(16)
print(result)