# return True / False
def is_triangle(m, rows):
    A = ord("a")

    for i in range(rows):
        current = ord(m[i][i])  # Ascii of the current

        if current != A + i:
            return False

    return True


def is_triangle_rec(m, rows):
    A = ord("a")

    if rows == 0:
        return True

    current = ord(m[rows - 1][rows - 1])
    if current != A + rows - 1:
        return False

    result = is_triangle_rec(m, rows - 1)
    return result


def _num_to_letter(i):
    v = ord('a') + i
    return chr(v)


def is_triangle_rec_2(m, rows):
    if rows == 0:
        return True

    i = rows - 1

    # _num_to_letter:
    # 0->a
    # 1->b
    # 2->c
    # 3->d
    # 4->e
    if m[i][i] != _num_to_letter(i):
        return False

    return is_triangle_rec_2(m, rows - 1)


m = []

m1 = [['a']]

m1_2 = [['b']]

m1_2_2 = [['a', 'x'],
          ['x', 'b']]

m2 = [["a", "y", "d", "g", "b"],
      ["t", "b", "u", "k", "n"],
      ["i", "p", "c", "t", "l"],
      ["e", "v", "f", "d", "y"],
      ["b", "r", "e", "r", "e"]]

m3 = [["a", "y", "d", "g", "b"],
      ["t", "b", "u", "k", "n"],
      ["i", "p", "w", "t", "l"],
      ["e", "v", "f", "d", "y"],
      ["b", "r", "e", "r", "e"]]

print(is_triangle(m1, 1))
print(is_triangle(m1_2, 1))
print(is_triangle(m2, 5))
print(is_triangle(m3, 5))

print(is_triangle_rec(m1, 1))
print(is_triangle_rec(m1_2, 1))
print(is_triangle_rec(m2, 5))
print(is_triangle_rec(m3, 5))
