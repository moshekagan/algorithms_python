# print all items in list with recursion function

# regular function
def print_list(l):
    for i in l:
        print(i)


# recursive function
def print_list_rec(l):
    if len(l) == 0:
        return

    print(l[0])
    print_list_rec(l[1:])


# Tests
print_list_rec([])
print("--")
print_list_rec([1])
print("--")
print_list_rec([1, 2])
print("--")

l = [1, 334, 56, 53, 345, 6345]
print_list_rec(l)


