"""
O(1)
"""
def foo():
    num = input("insert a number:")     # O(1)
    num = int(num)  # O(1)
    mul = num*num   # O(1)
    print(mul)  # O(1)

# O(1) + O(1) + O(1) + O(1) = O(4) = O(1)

foo()


def foo_X(x):
    num = input("insert a number:")  # O(1)
    num = int(num)  # O(1)
    mul = num * num  # O(1)

    for i in range(2):  # O(2)
        print(mul)  # O(1)
# O(1)

"""
O(n)
"""

def foo_2(x):
    num = input("insert a number:")  # O(1)
    num = int(num)  # O(1)
    mul = num * num  # O(1)

    for i in range(x):  # O(X)
        print(mul)  # O(1)


# O(1) + O(1) + O(1) + O(X) * O(1) = O(1) + O(X*1) = O(1) + O(X) = O(X) = O(n)
foo_2(3)


def foo_3(l):
    print("-- foo_3")  # O(1)

    for i in l:  # O(len(l)) = O(n)
        print(i)  # O(1)


# O(1) + O(1) * O(n) = O(1) + O(1*n) = O(1) + O(n) = O(n)


foo_3([1, 2, 3, 4, 5, 6, 7])

"""
O(n^2)
"""
def foo_4(l):
    print("-- foo_4") # O(1)

    for i in l:  # O(len(l)) = O(n)
        for j in l:  # O(len(l)) = O(n)
            print(i * j, end=" ")  # O(1)
        print()

# O(1) + O(n) * O(n) * O(1) = O(1) + O(n*n*1) = O(n^2)


foo_4([1, 2, 3, 4, 5, 6, 7])


"""
O(n*m)
"""
def foo_5(l1, l2):
    print("-- foo_5")  # O(1)

    for i in l1:  # O(len(l1)) = O(n)
        for j in l2:  # O(len(l2)) = O(m)
            print(i * j, end=" ")  # O(1)
        print()


# O(1) + O(n) * O(m) * O(1) = O(1) + O(n*m*1) = O(n*m)

#        len(l1) = n             len(l2) = m
foo_5([1, 2, 3, 4, 5, 6, 7, 8], [40, 50, 60])
