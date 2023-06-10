"""
Assignment 1: Algorithms and python programming
Recursions
Dictionaries
Author: Hadas Lapid
"""


# Q1.A.
def countCInList(l, c):
    if len(l) == 0:
        return 0

    s = 0

    if l[-1] == c:
        s = 1
    else:
        s = 0

    count = countCInList(l[:-1], c)

    return s + count


# Q1.B.
def isCNInList(l, c, n):
    return countCInList(l, c) == n


# Q2
def countNumsDict(l, d):
    if len(l) == 0:
        return d

    if l[-1] not in d:
        d[l[-1]] = countCInList(l, l[-1])

    return countNumsDict(l[:-1], d)


# Q3
def int2bin(num):  # ADD INPUT
    if num == 0: return 0

    if num < 2: return 1

    b = 0 if num % 2 == 0 else 1
    res = int2bin(int(num / 2))

    return int(f"{res}{b}")


# Q4
def _number_to_letter(n):
    v = ord('a') + n
    return chr(v)


def recDiagHelper(m, l):
    if l <= 0:
        return True

    i = l - 1
    if m[i][i].lower() != _number_to_letter(i):
        return False

    return recDiagHelper(m, l - 1)


def recDiag(m):
    return recDiagHelper(m, len(m))


def main():
    # Q1 test
    l = [1, 4, 7, 1, 2, 1]
    # Q1.A.
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

    # Q2 test
    print(countNumsDict(l, {}))
    ls = "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world"
    print(countNumsDict(ls.lower().split(), {}))

    # Q3 test
    print(int2bin(175), bin(175))
    print(int2bin(17), bin(17))
    print(int2bin(7), bin(7))
    print(int2bin(235), bin(235))

    # Q4 test
    l1 = [['a', 'g', 'd', 'y', 'b'],
          ['n', 'b', 'u', 'k', 't'],
          ['l', 't', 'c', 'p', 'i'],
          ['y', 'f', 'v', 'd', 'e'],
          ['e', 'r', 'b', 'r', 'e']]
    print(recDiag(l1))
    l2 = [['d', 'g', 'w', 'y', 'a'],
          ['n', 'c', 'u', 'k', 'j'],
          ['l', 's', 'b', 'p', 'l'],
          ['k', 'f', 'r', 'm', 'e'],
          ['q', 'r', 'b', 'r', 'n']]
    print(recDiag(l2))


if __name__ == "__main__":
    main()
