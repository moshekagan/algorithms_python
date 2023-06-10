# Q1.A.
def countCInList(l, c):
    if len(l) == 0:
        return 0

    # list l is *not* empty!
    if l[0] == c:
        return countCInList(l[1:], c) + 1
    else:
        return countCInList(l[1:], c)


def isCNInList(l, c, n):
    count = countCInList(l, c)

    if count == n:
        return True
    else:
        return False


if __name__ == '__main__':
    # Q1 test
    l = [1, 4, 7, 1, 2, 1]

    # Q1.A.
    print(countCInList([], 1))  # 0
    print(countCInList(l, 1))
    print(countCInList(l, 7))
    print(countCInList(l, 8))
    print(countCInList(l, 2))

    # Q1.B.
    print(isCNInList(l, 1, 3))
    print(isCNInList(l, 1, 2))
    print(isCNInList(l, 7, 1))
    print(isCNInList(l, 8, 3))
    print(isCNInList(l, 8, 0))
