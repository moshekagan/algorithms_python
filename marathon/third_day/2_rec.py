#    0 ......... 4
l = [1, 2, 3, 4, 5]


def rec_print_list(num):
    if 0 <= num < len(l):
        rec_print_list(num + 1)
        print(l[num])


rec_print_list(2)
# OUTPUT:
# 5
# 4
# 3
# 2
# 1
