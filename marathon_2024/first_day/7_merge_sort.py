"""
Merge sort is a popular sorting algorithm that follows the divide-and-conquer approach.
It recursively divides the input list into smaller halves, sorts them individually,
and then merges them back together to obtain the sorted result.

1. The merge_sort function takes an array (arr) as input and performs the merge sort algorithm on it.
2. The base case of the recursive function is when the length of the array is less than or equal to 1. In this case, the array is already considered sorted, so it is returned as is.
3. If the length of the array is greater than 1, it is divided into two halves. The middle index (mid) is computed, and the left and right halves are obtained accordingly.
4. The merge_sort function is called recursively on both halves to sort them individually. This step continues until the base case is reached.
5. The sorted left and right halves are then merged back together by calling the merge function.
6. The merge function takes two sorted arrays (left and right) as input and merges them into a single sorted array.
7. It initializes an empty merged list and two indices (i for the left half and j for the right half) to track the current positions in the respective halves.
8. The elements from both halves are compared, and the smaller element is appended to the merged list. The corresponding index is then incremented.
9. The process continues until all elements from either the left or the right half have been added to the merged list.
10. If there are any remaining elements in either half, they are added to the merged list.
11. Finally, the merged list containing the sorted elements is returned.


Merge sort has a time complexity of O(n log n) in the average and worst case, where n is the number of elements in the array
This complexity makes merge sort one of the most efficient sorting algorithms for large datasets.

The O(n log n) time complexity of merge sort can be explained as follows:

1. Divide Phase: The array is divided into halves recursively until the base case is reached. In each recursive call,
    the array is divided into two roughly equal halves. This division takes O(log n) time since the array size is halved in each step.
2. Conquer Phase: After the array is divided into the smallest possible subarrays (single elements), the conquer phase begins.
    In this phase, the subarrays are sorted and merged back together to form larger sorted subarrays. The merge operation
    for each level of recursion takes O(n) time, as it involves comparing and merging all elements of the subarrays.
3. Merge Phase: During the merge phase, the sorted subarrays are merged together to create larger sorted subarrays.
    This merging process takes place for each level of recursion until the entire array is merged back together.
    Since each level of recursion corresponds to one pass over the array, there are log n levels of recursion. Therefore,
    the overall merging process takes O(n log n) time.

The space complexity of merge sort is O(n) because it requires additional memory to store the temporary merged subarrays
during the merge phase. However, merge sort can be implemented as an in-place sorting algorithm by modifying the merge
operation to use the original array and auxiliary space for merging.

https://www.youtube.com/watch?v=JSceec-wEyw&ab_channel=GeeksforGeeks
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # arr is greater then 1

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half) # O(n)


def merge(left, right):
    merged = []
    i = 0  # Index for the left half
    j = 0  # Index for the right half

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


print(merge_sort([]))
print(merge_sort([2]))
print(merge_sort([3, 2]))
print(merge_sort([3, 2, 1]))
print(merge_sort([4, 2, 3, 1]))

# Usage
my_array = [5, 2, 8, 12, 3, 1]
sorted_array = merge_sort(my_array)
print(sorted_array)  # Output: [2, 3, 5, 8, 12]

# l = [3,1,2,4]
#
# l1 = [3,1]
# l1_1 = [3]
# l1_2 = [1]
# left = merge(l1_1, l1_2) # [1,3]
#
# l2 = [2,4]
# l2_1 = [2]
# l2_2 = [4]
# right = merge(l2_1, l2_2) # [2,4]
#
# all = merge(left, right) # [1,2,3,4]
#
#
# print(all)
