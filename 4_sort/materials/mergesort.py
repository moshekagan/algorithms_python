def merge(left, right):
    res = []
    i_left, i_right = 0, 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            res.append(left[i_left])
            i_left += 1
        else:
            res.append(right[i_right])
            i_right += 1
    if i_right < len(right):
        res.extend(right[i_right:])
    else:
        res.extend(left[i_left:])
    print('merge: ' + str(left) + '&' + str(right) + ' to ' + str(res))
    return res


def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]
print(merge_sort(testList))
