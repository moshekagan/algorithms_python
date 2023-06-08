testList = [27, 3, 9, 1, 4, 5, 18]


def selection_sort(L):
    for i in range(len(L) - 1):
        indx_min = find_min(L, i)
        L[i], L[indx_min] = L[indx_min], L[i]
    return L


def find_min(L, i):
    indx_min = i
    for j in range(i + 1, len(L)):
        if L[indx_min] > L[j]:
            indx_min = j
    return indx_min


selection_sort(testList)


def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))
