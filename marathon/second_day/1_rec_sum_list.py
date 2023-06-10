# Write a Python program to calculate the sum of a list of numbers.


def sum_list(l):
    s = 0
    for i in l:
        s += i

    return s

l = [1, 34, 56, 7]
print(sum_list(l))


def rec_sum_list(l):
    if len(l) == 0:
        return 0

    # at least 1 element in list l
    x = rec_sum_list(l[1:])
    return l[0] + x



print(rec_sum_list([]))      # 0
print(rec_sum_list([4]))     # 4
print(rec_sum_list([4, 5]))  # 9
print(rec_sum_list(l))       # 98



