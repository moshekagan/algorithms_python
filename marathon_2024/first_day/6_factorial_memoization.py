"""
Factorial Calculation:

Simple recursion: (n! = n imes (n-1)!)
Memoized recursion to avoid recalculating values.
"""

# 5! = + 5 * 4! = 5 * 4 *3!

# 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1 * 0! = 4 * 3 * 2 * 1 * 1
# 4! = 4 * 3! = 4 * 6

# memo = { 3: 6, 4: 24 }
def factorial(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 1
        return 1

    #            factorial(3)
    prev_n_fac = factorial(n-1, memo)
    res = n * prev_n_fac
    memo[n] = res

    return res


print(factorial(1))
print(factorial(5))