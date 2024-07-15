def dec_to_bin(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    prefix = dec_to_bin(num // 2)

    if num % 2 == 0:
        b = 0
    else:
        b = 1

    return f"{prefix}{b}"

"""
2 -> 10
2 / 2 = 1 (0)
1 / 2 = 0 (1)

3 -> 11
3 / 2 = 1 (1)
1 / 2 = 0 (1)

4 -> 100
4 / 2 = 2 (0)
2 / 2 = 1 (0)
1 / 2 = 0 (1)

5 -> 101
5 / 2 = 2 (1)
2 / 2 = 1 (0)
1 / 2 = 0 (1)
"""

print(dec_to_bin(0))    # 0 v
print(dec_to_bin(1))    # 1 v
print(dec_to_bin(2))    # 10
print(dec_to_bin(3))    # 11
print(dec_to_bin(4))    # 100
print(dec_to_bin(5))    # 101
print(dec_to_bin(7))    # 10001
print(dec_to_bin(176))  # 10101111


