# Write a Python program to calculate the sum of a list of numbers.


def sum_list(l):
    s = 0
    for i in l:
        s += i

    return s


l = [1, 34, 56, 7]
# print(sum_list(l))


def rec_sum_list(l):
    if len(l) == 0:
        return 0

    # l is not Empty!
    element = l[0]
    sum_smallest_list = rec_sum_list(l[1:])

    return element + sum_smallest_list


# print(rec_sum_list([]))  # 0 V
# print(rec_sum_list([4]))  # 4
# print(rec_sum_list([4, 5]))  # 9
print(rec_sum_list([1, 2, 3]))  # 6
# print(rec_sum_list(l))  # 98
