def rec_func1(x):
    if x != 0:
        rec_func1(x - 1)


x = 1
# rec_func1(x)

n = 5


# for i in range(1, n+1):
#     print(i)

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)


# print_numbers(n)

def rec_factorial(n):
    if n == 0:
        return 1
    return rec_factorial(n - 1) * n


print(rec_factorial(5))


def rec_sum(n):
    if n == 0:
        return 0
    return rec_sum(n - 1) + n
