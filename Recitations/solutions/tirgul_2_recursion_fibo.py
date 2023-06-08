# index:    0, 1, 2, 3, 4, 5, 6 ...
# fibonaci: 0, 1, 1, 2, 3, 5, 8 ...


def fib(n):  # no recursion
    first = 0
    second = 1
    if n == 0 or n == 1:
        return n
    for i in range(2, n + 1):
        tmp = second
        second += first
        first = tmp
    return second


def rec_fib(n):
    if n == 1 or n == 0:
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


print(fib(17))
print(rec_fib(5))
