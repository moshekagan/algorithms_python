"""
O(1)
"""
def foo():
    num = input("insert a number:") # O(1)
    num = int(num) # O(1)
    mul = num*num # O(1)
    print(mul)   # O(1)

foo() # 1 + 1 + 1 + 1 = O(1000) = O(1)


def foo_X(x):
    num = input("insert a number:")  # O(1)
    num = int(num) # O(1)
    mul = num * num # O(1)

    for i in range(2): # O(2)
        print(mul)  # O(1)
# 1 + 1+ 1+ (2*) = 3 + 2 = O(5) = O(1)

"""
O(n)
"""

def foo_2(x):
    num = input("insert a number:")  # O(1)
    num = int(num)  # O(1)
    mul = num * num / 2 ** 5 - 4 # O(5) = O(1)

    for i in range(x):  # O(x)
        print(mul) # O(1)
    for i in range(x):  # O(x)
        print(mul)  # O(1)
    for i in range(x):  # O(x)
        print(mul)  # O(1)

# 1 + 1+ 1+ (x*1) = 3 + x = O(3) + O(n) +O(n) +O(n) = O(3n) = O(n)
foo_2(3)
foo_2(300000000)


def foo_3(l):
    print("-- foo_3")

    for i in l: # O(len(l)) = O(n)
        print(i) # O(1)

# O(n)
foo_3([1, 2, 3, 4, 5, 6, 7])
foo_3([1, 2, 3, 4, 5, 6, 7, 9, 1,1,1,1,1,1,1,1,1])


"""
O(n^2)
"""
def foo_4(l):
    print("-- foo_4")

    for i in l:
        for j in l:
            print(i * j, end=" ")
        print()

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

#        len(l1) = n                  len(l2) = m
foo_5([1, 2, 3, 4, 5, 6, 7, 8], [40, 50, 60])
