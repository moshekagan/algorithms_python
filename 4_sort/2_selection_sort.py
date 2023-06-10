"""
Selection sort is another simple sorting algorithm that divides the input list into two parts:
the sorted portion at the beginning and the unsorted portion at the end. It repeatedly finds the smallest element
from the unsorted portion and swaps it with the element at the current position in the sorted portion.

1. The selection_sort function takes an array (arr) as input and performs the selection sort algorithm on it.
2. The variable n is initialized with the length of the array.
3. The outer loop runs from 0 to n-1 and represents the current position in the sorted portion of the array.
4. Inside the outer loop, the inner loop is used to find the minimum element from the remaining unsorted portion of the array.
5. The variable min_index keeps track of the index of the minimum element found so far. It is initially set to the current position (i).
6. The inner loop starts from i + 1 since the elements before i are already in their sorted positions.
7. If an element is found that is smaller than the current minimum element, min_index is updated to the index of the new minimum element.
8. After the inner loop completes, the minimum element from the remaining unsorted portion is found, and its index is stored in min_index.
9. The minimum element is then swapped with the element at the current position (i) using tuple assignment.
10. This process repeats until the entire array is sorted.


Selection sort has a time complexity of O(n^2) in the average and worst case, where n is the number of elements in the array.
Similar to bubble sort, it is not considered an efficient sorting algorithm for large lists, but it is relatively easy to understand and implement.

https://www.youtube.com/watch?v=wnKQsow7ERI&t=19s&ab_channel=JeffKnerr
"""


def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):  # O(n)

        # Find the minimum element in the remaining unsorted portion
        min_index = i
        for j in range(i + 1, n):  # O(n-i) = O(n)
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# O(n^2)


# Usage
my_array = [5, 2, 8, 12, 3]
selection_sort(my_array)
print(my_array)  # Output: [2, 3, 5, 8, 12]
