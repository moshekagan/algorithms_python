# Q1
def _number_to_letter(n):
    v = ord('a') + n
    return chr(v)


def is_alpha_beta(m, l):
    if l <= 0:
        return True

    i = l - 1
    if m[i][i].lower() != _number_to_letter(i):
        return False

    return is_alpha_beta(m, l - 1)


# Q2
def dec_to_bin(num):
    if num == 0: return 0

    if num < 2: return 1

    b = 0 if num % 2 == 0 else 1
    res = dec_to_bin(int(num / 2))

    return int(f"{res}{b}")


# Q3
def bin_to_dec(num, pos=None):
    if num == 0:
        return 0

    if pos is None:
        pos = 0

    r = (num % 10) * 2 ** pos
    res = bin_to_dec(int(num / 10), pos + 1)

    return r + res


# Q4
def is_series(arr, num):
    if len(arr) < num: return False
    if len(arr) == 0: return True

    res1 = is_series(arr[:-1], num - 1) if arr[-1] == num else False
    res2 = is_series(arr[:-1], num)

    return res1 or res2


# Q5
def print_scale(l):
    if l <= 0: return

    print_scale(l - 1)
    print("- " * l)
    print_scale(l - 1)


# Q6
def print_number_to_string(num):
    if num <= 0: return

    A = ord('A')
    d = num % 10
    char = chr(A + d)
    print_number_to_string(int(num / 10))
    print(char, end="")


# Q7
def same_amount_in_list(l, num, amount):
    if len(l) == 0:
        if amount == 0: return True
        else: return False

    if l[-1] == num:
        return same_amount_in_list(l[:-1], num, amount - 1)

    return same_amount_in_list(l[:-1], num, amount)


if __name__ == '__main__':
    print("# Test - Q1")
    print(is_alpha_beta([["a", "y", "d", "g", "b"],
                         ["t", "b", "u", "k", "n"],
                         ["i", "p", "c", "t", "l"],
                         ["e", "v", "f", "d", "y"],
                         ["b", "r", "e", "r", "e"]], 5))  # True

    print(is_alpha_beta([["a", "y", "d", "g"],
                         ["t", "b", "u", "k"],
                         ["i", "p", "f", "t"],
                         ["e", "v", "f", "d"]], 4))  # False

    print()
    print("# Test - Q2")
    print(dec_to_bin(0))  # 0
    print(dec_to_bin(1))  # 1
    print(dec_to_bin(2))  # 10
    print(dec_to_bin(3))  # 11
    print(dec_to_bin(4))  # 100
    print(dec_to_bin(5))  # 101
    print(dec_to_bin(17))  # 10001
    print(dec_to_bin(175))  # 10101111

    print()
    print("# Test - Q3")
    print(bin_to_dec(0))  # 0
    print(bin_to_dec(1))  # 1
    print(bin_to_dec(10))  # 2
    print(bin_to_dec(11))  # 3
    print(bin_to_dec(100))  # 4
    print(bin_to_dec(101))  # 5
    print(bin_to_dec(10001))  # 17
    print(bin_to_dec(10101111))  # 175

    print()
    print("# Test - Q4")
    print(is_series([], 0))  # T
    print(is_series([], 1))  # F
    print(is_series([1], 1))  # T
    print(is_series([1, 2], 1))  # T
    print(is_series([1, 2], 2))  # T
    print(is_series([2, 1, 2], 1))  # T
    print(is_series([2, 1, 2], 2))  # T
    print(is_series([1, 2, 3], 2))  # T
    print(is_series([4, 2, 3], 2))  # F
    print(is_series([3, 1, 2, 3, 4, 6, 3], 4))  # T
    print(is_series([3, 1, 2, 1, 2, 3, 4], 4))  # T
    print(is_series([1, 2, 3, 4, 1, 5, 1], 4))  # T
    print(is_series([3, 1, 2, 1, 2, 3, 5], 4))  # F
    print(is_series([3, 1, 2, 3, 5, 6, 3], 4))  # F

    print()
    print("# Test - Q5")
    print("# 1:")
    print_scale(1)
    print()
    print("# 2:")
    print_scale(2)
    print()
    print("# 3:")
    print_scale(3)
    print()
    print("# 4:")
    print_scale(4)
    print()
    print("# 5:")
    print_scale(5)
    print()

    print()
    print("# Test Q6")
    print_number_to_string(123)     # BCD
    print()
    print_number_to_string(9054)    # JAFE
    print()
    print()

    print()
    print("# Test Q7")
    print(same_amount_in_list([], 1, 0))  # T
    print(same_amount_in_list([], 1, 1))  # F
    print(same_amount_in_list([1], 1, 1))     # T
    print(same_amount_in_list([1, 4, 7, 1, 2, 1], 1, 3))     # T
    print(same_amount_in_list([1, 4, 7, 1, 2, 1], 1, 2))     # F
    print(same_amount_in_list([1, 4, 7, 1, 2, 1], 8, 3))     # F
    print(same_amount_in_list([1, 4, 7, 1, 2, 1], 8, 0))     # T
