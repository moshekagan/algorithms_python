# print all items in list with recursion function
def print_list(l):
    if len(l) == 0:
        return

    print(l[0])
    print_list(l[1:])


# Tests
print_list([])
print("--")
print_list([1])
print("--")
print_list([1, 2])
print("--")

l = [1, 334, 56, 53, 345, 6345]
print_list(l)


