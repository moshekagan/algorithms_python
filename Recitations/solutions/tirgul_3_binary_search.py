l = sorted([2, 4, 1, 6, 8, 12, -2, -8])

n = 6

for i, v in enumerate(l):
    if v == n:
        print(f'{n} is in index {i}')


def binary_search(n):
    first = 0
    last = len(l) - 1
    mid = (first + last) // 2
    while l[mid] != n and last >= first:
        if l[mid] < n:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if last < first:
        return -1
    return mid


'from the mudele'

l = sorted([2, 4, 1, 6, 8, 12, -2, -8])
print(l)

n = 6
for i, v in enumerate(l):
    if v == n:
        print(f'{n} is in index {i}')


def binary_search(l, n):
    first = 0
    last = len(l) - 1
    mid = (first + last) // 2
    while l[mid] != n and last >= first:
        if l[mid] < n:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if last < first:
        return -1
    return mid


print(binary_search(l, 5))
