def q2_a(l, bin=3):
    min_x = min(l) - 1
    max_x = max(l) + bin
    x = []
    for i in range(min_x, max_x + 1, bin):
        x.append(i)
    return x


l1 = [3, 5, 2, 18, 9, 4]

print(q2_a(l1))


def q2_b(l, bin):
    x = q2_a(l, bin)
    prob = [0] * (len(x) - 1)
    for elem in l:
        for i in range(len(x)):
            if elem >= x[i] and elem < x[i + 1]:
                prob[i] += 1
                break
    return x, prob


x, prob = q2_b(l1, 4)
print(x)
print(prob)
