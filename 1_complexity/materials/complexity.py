"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""
import time as t

testList = [1, 3, 4, 5, 9, 18, 27]


# constant # of operations :3
def c_to_f(c):
    return (c * 9 / 5) + 32  # 3 operations


t0 = t.time()
c_to_f(10)  # 10 or 1000000 are the same 0.0 secs
dt = t.time() - t0
print(dt)


# linear growth in # of operations:
# O(2+3*n) => O(n)
def ave(l):
    res = 0  # 1 op
    for i in l:  # n ops
        res += i  # 2*n ops
    return res / len(l)  # 1 op


t0 = t.time()
ave(1000000 * testList)
dt = t.time() - t0
print(f"ave function on test list takes {dt} secs")


# O versus # of Ops
# ops = 1+3*(n-1)
def fact(n):
    res = 1  # 1 Op
    for i in range(n, 1, -1):  # n-1 Ops
        res *= i  # 2*(n-1) ops
    return res


# O(2+2*n) => O(n)
def linear_search(L, e):
    found = False  # 1 op
    for i in range(len(L)):  # n ops
        if e == L[i]:  # n ops
            found = True  # 1 ops
    return found


linear_search(testList, 4)


# linearSearch on sorted list - O(n)
# O(n+(<n)) => O(n)
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


# O(n^2)
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]
print(f"{testSet1} is subset of {testSet}")
print(isSubset(testSet1, testSet))


# O(n^2)
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res


# iterative fibonacci
def itFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fi = 0
        fii = 1
        for i in range(n - 1):
            fi, fii = fii, fi + fii
        return fii


def recFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recFib(n - 1) + recFib(n - 2)
