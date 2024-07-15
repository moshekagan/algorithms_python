import random
import numpy as np

l1 = [3, 5, 2, 18, 9, 4]
s = "supercalifragilisticexpialidocious"
n0 = 4
n1 = 16
r = random.randint(n0, n1)


def q1_a(s, d={}):
    if len(s) <= 0:
        return d

    if s[-1] not in d:
        d[s[-1]] = 1
    else:
        d[s[-1]] += 1

    d = q1_a(s[:-1], d)

    return d


def q1_b():
    res = q1_a(s)
    max_char = None
    max_count = 0

    for val, count in res.items():
        if count > max_count:
            max_count = count
            max_char = val

    return max_char, max_count


# Bonus question
def q1_c(d):
    res = {}
    for val, count in d.items():
        if count not in res:
            res[count] = [val]
        else:
            res[count].append(val)

    return res


def q2_a(x0, x1, step):
    return [i for i in range(x0, x1 + 1, step)]


def q2_b(x0, x1, step, n):
    if n < x0 or x1 < n:
        return -1

    l = q2_a(x0, x1, step)
    if len(l) < 1:
        return -1

    diff = step / 2
    curr_i = 0

    for i in range(1, len(l)):
        if l[curr_i] + diff < n:
            curr_i = i

    return curr_i


# Bonus question
def q2_c(lst, low, high, n):
    if n < lst[low] or lst[high] < n or low > high or len(lst) < high+1:
        return -1

    if low == high:
        return low

    diff = (lst[low+1] - lst[low]) / 2

    if lst[low + 1] < n:
        return q2_c(lst, low+1, high, n)

    if lst[low] + diff < n:
        return low + 1
    else:
        return low


def q3_a(l, index):
    if index < 0 or index >= len(l):
        return None

    if index == 0 or index == len(l) -1:
        return l[index]

    s = 0
    for n in l[index-1:index+2]:
        s += n

    return s / 3


def q3_b(l):
    return [q3_a(l, i)for i in range(len(l))]


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

    print("\nq2_a:")
    print(f"initial number = {n0}\n"
          f"last number = {n1}\n"
          f"list span at step -1: {q2_a(n0, n1, -1)}\n"
          f"list span at step 3: {q2_a(n0, n1, 3)}\n"
          f"list span at step 5: {q2_a(n0, n1, 5)}\n")

    # assisting list
    l2 = [4, 7, 10, 13, 16]
    # iterative solution
    print("q2_b:")
    print(f"x0={n0}, x1={n1}, step=3")
    print(q2_a(n0, n1, 3))
    print(f"{r} is at index {q2_b(n0, n1, 3, r)}")
    print(f"{n0} is at index {q2_b(n0, n1, 3, n0)}")
    print(f"{n1} is at index {q2_b(n0, n1, 3, n1)}")
    print(f"-5 is at index {q2_b(n0, n1, 3, -5)}")
    print(f"20 is at index {q2_b(n0, n1, 3, 20)}\n")

    print("BONUS q2_c:")
    l2 = q2_a(n0, n1, 3)
    print(f"{r} is at index {q2_c(l2,0,len(l2)-1,r)}")
    print(f"{n0} is at index {q2_c(l2,0,len(l2)-1,n0)}")
    print(f"{n1} is at index {q2_c(l2,0,len(l2)-1,n1)}")
    print(f"-5 is at index {q2_c(l2,0,len(l2)-1,-5)}")
    print(f"20 is at index {q2_c(l2,0,len(l2)-1,20)}")

    print("\nq3_a:")
    print(f"original list {l1}")
    print(f"q3a at index 0: {q3_a(l1,0)}")
    print(f"q3a at index len(l1)-1: {q3_a(l1,len(l1)-1)}")
    print(f"q3a at index 2: {q3_a(l1,2)}\n")

    print("\nq3_b:")
    print(f"smoothed list {q3_b(l1)}")


if __name__ == "__main__":
    main()
