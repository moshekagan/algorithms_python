# Program to implement min max selection sort.

def min_max_selection_sort(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while i < j:
        min = arr[i]
        max = arr[i]
        min_i = i
        max_i = i
        for k in range(i, j + 1, 1):
            if arr[k] > max:
                max = arr[k]
                max_i = k
            elif arr[k] < min:
                min = arr[k]
                min_i = k

            # shifting the min.
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp

        # Shifting the max. The equal condition
        # happens if we shifted the max to
        # arr[min_i] in the previous swap.
        if arr[min_i] == max:
            temp = arr[j]
            arr[j] = arr[min_i]
            arr[min_i] = temp
        else:
            temp = arr[j]
            arr[j] = arr[max_i]
            arr[max_i] = temp

        i += 1
        j -= 1

    print("Sorted array:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")

    # Driver code


if __name__ == '__main__':
    arr = ["Mystery", "Romance", "Fiction", "Science", "Thriller", "Science", "Fiction"]
    print(arr)

    min_max_selection_sort(arr)
