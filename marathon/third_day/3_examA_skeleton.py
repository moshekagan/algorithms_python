import random
l1 = [3,5,2,18,9,4]
s = "supercalifragilisticexpialidocious"
n0 = 4
n1 = 16
r = random.randint(n0, n1)


def q1_a(s, d={}):
    if len(s) == 0:
        return d

    current = s[0]
    if current not in d:
        d[current] = 1
    else:
        d[current] += 1

    return q1_a(s[1:], d)


print(q1_a("", {}))     # {}
print(q1_a("a", {}))    # {"a": 1}
print(q1_a("aa", {}))    # {"a": 2}
print(q1_a("aab", {}))    # {"a": 2, "b": 1}


def q1_b():
    d = q1_a(s, {})

    max_char = None
    max_count = -1

    for char, count in d.items():
        if max_count < count:
            max_count = count
            max_char = char

    return (max_char, max_count)


# Bonus question
def q1_c(d):
    res = {}

    for char, count in d.items():
        if count not in res:
            res[count] = [char]
        else:
            res[count].append(char)

    return res
# s 3
# u 2
# p 2

# 3 -> [s]
# 3 -> [u, p]



def q2_a(x0, x1, step):
    l = []

    for i in range(x0, x1+1, step):
        l.append(i)

    return l

def q2_b():
    pass

# Bonus question
def q2_c():
    pass

def q3_a():
    pass

def q3_b():
    pass

def main():
    global s, l1, n0, n1, r
    print("q1_a:")
    print(q1_a(s, d={}))
    # assisting dictionary
    d = {'s': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'c': 3, 'a': 3, 'l': 3, 'i': 7, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1, 'o': 2}
    print("q1_b:")
    print(q1_b())
    print("BONUS q1_c:")
    print(q1_c(d))
    www = q1_c(d)
    www

    print("\nq2_a:")
    print(f"initial number = {n0}\n"
          f"last number = {n1}\n"
          f"list span at step -1: {q2_a(n0,n1,-1)}\n"
          f"list span at step 3: {q2_a(n0,n1,3)}\n"
          f"list span at step 5: {q2_a(n0,n1,5)}\n")

    # assisting list
    # l2 = [4, 7, 10, 13, 16]
    # iterative solution
    print("q2_b:")
    print(f"x0={n0}, x1={n1}, step=3")
    # print(f"{r} is at index {q2_b(n0,n1,3,r)}")
    # print(f"{n0} is at index {q2_b(n0,n1,3,n0)}")
    # print(f"{n1} is at index {q2_b(n0,n1,3,n1)}")
    # print(f"-5 is at index {q2_b(n0,n1,3,-5)}")
    # print(f"20 is at index {q2_b(n0,n1,3,20)}\n")

    print("BONUS q2_c:")
    # l2 = q2_a(n0, n1, 3)
    # print(f"{r} is at index {q2_c(l2,0,len(l2)-1,r)}")
    # print(f"{n0} is at index {q2_c(l2,0,len(l2)-1,n0)}")
    # print(f"{n1} is at index {q2_c(l2,0,len(l2)-1,n1)}")
    # print(f"-5 is at index {q2_c(l2,0,len(l2)-1,-5)}")
    # print(f"20 is at index {q2_c(l2,0,len(l2)-1,20)}")

    print("\nq3_a:")
    # print(f"original list {l1}")
    # print(f"q3a at index 0: {q3_a(l1,0)}")
    # print(f"q3a at index len(l1)-1: {q3_a(l1,len(l1)-1)}")
    # print(f"q3a at index 2: {q3_a(l1,2)}\n")

    print("\nq3_b:")
    # print(f"smoothed list {q3_b(l1)}")

if __name__=="__main__":
    main()