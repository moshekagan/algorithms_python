# iterative algorithm for calculation of multiplicity
def mult_fun(a, b):
    res = 0
    while b > 0:
        res += a
        b -= 1
    return res


print(mult_fun(10, 6))


# recursive algorithm for calculation of multiplicity
def mult_rec(a, b):
    if b == 1:
        return a
    else:
        return a + mult_rec(a, b - 1)


print(mult_rec(10, 6))


# recursive solution to factorial:
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(4))


# iterative solution to factorial"
def fact_it(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(fact_it(4))

# sanity check:
import math as m

print(m.factorial(4))


# recursion with two base cases and two recursive calls
def fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


fibonacci(4)


def parseS(s):
    return ''.join(s.lower().split(' '))


def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])


print(isPal(parseS("Was it a car or a cat I saw")))
