"""
Factorial Calculation:

Simple recursion: (n! = n imes (n-1)!)
Memoized recursion to avoid recalculating values.
"""

def factorial(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        res = 1
    else:
        res = n * factorial(n - 1, memo)

    memo[n] = res
    return res


print(factorial(1))
print(factorial(5))