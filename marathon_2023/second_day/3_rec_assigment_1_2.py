def countCInList(l, c):
    if len(l) == 0:
        return 0

    # list l is *not* empty!
    if l[0] == c:
        return countCInList(l[1:], c) + 1
    else:
        return countCInList(l[1:], c)


def countNumsDict(l, d={}):
    if len(l) == 0:
        return d

    current = l[0]
    count = countCInList(l, current)

    if current not in d:
        # Update dict
        d[current] = count

    return countNumsDict(l[1:], d)


if __name__ == '__main__':
    # Q2 test
    print(countNumsDict([], {}))  # {}
    print(countNumsDict([7], {}))  # {7: 1}
    print(countNumsDict([1, 1], {}))  # {1: 2}

    l = [1, 4, 7, 1, 2, 1]
    print(countNumsDict(l, {}))
    ls = "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world"
    l1 = ls.lower().split()
    print(countNumsDict(l1, {}))
    print(countNumsDict(['a', 'b', 'c', 'b', 'd', 'b'], {}))
