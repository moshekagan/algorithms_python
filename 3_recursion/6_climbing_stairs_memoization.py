"""
Climbing Stairs Problem
You can climb 1 or 2 steps at a time. How many distinct ways can you climb to the top if the staircase has n steps?

"""


# Simple Recursion
def climb_stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)

# Example usage
print(climb_stairs(5))  # Output: 8


# Memoization
def climb_stairs_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        result = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)

    memo[n] = result
    return result

# Example usage
print(climb_stairs_memo(5))  # Output: 8


"""
Explanation

Simple Recursion:
--------------------
The function climb_stairs(n) calls itself to compute the number of ways to climb to the top.
This approach has an exponential time complexity, O(2^n), because it recalculates the same values multiple times.

Memoized Recursion:
--------------------
The function climb_stairs_memo(n, memo) uses a dictionary memo to store previously computed results.
Before performing any computation, it checks if the result for the current n is already in memo. If so, it returns the cached result.
This reduces the time complexity to 𝑂(𝑛)
O(n), making it much more efficient.
"""