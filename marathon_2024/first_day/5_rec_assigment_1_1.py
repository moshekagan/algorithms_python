# Q1.A.
def countCInList(l, c):
    if len(l) == 0:
        return 0

    count_small_l = countCInList(l[1:], c)

    element = l[0]
    if element == c:
        return 1 + count_small_l
    else:
        return 0 + count_small_l


def isCNInList(l, c):
    c_in_l = countCInList(l, c)
    if c_in_l == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    # Q1 test
    l = [1, 4, 7, 1, 2, 1]

    # Q1.A.
    print(countCInList([], 1))  # 0
    print(countCInList([2], 1))  # 0
    print(countCInList([1], 1))  # 1

    print(countCInList(l, 1))
    print(countCInList(l, 7))
    print(countCInList(l, 8))
    print(countCInList(l, 2))

    # Q1.B.
    # print(isCNInList(l, 1, 3))
    # print(isCNInList(l, 1, 2))
    # print(isCNInList(l, 7, 1))
    # print(isCNInList(l, 8, 3))
    # print(isCNInList(l, 8, 0))
