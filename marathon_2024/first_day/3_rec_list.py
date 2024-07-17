# print all items in list with recursion function

# regular function
def print_list(l):
    for i in l:
        print(i)


def print_list_rec(l):
    if len(l) == 0:
        return

#     l is not empty!
    print(l[0])
    # l =[1,2,3,4,5]
    s_l = l[1:]
    # s_l = [2,3,4,5]
    print_list_rec(s_l)

# Tests
print_list_rec([])
print("--")
print_list_rec([1])
print("--")
print_list_rec([1, 2])
print("--")

l = [1, 334, 56, 53, 345, 6345]
print_list_rec(l)


