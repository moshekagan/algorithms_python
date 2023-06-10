"""
Bubble sort is a simple sorting algorithm that repeatedly steps through a list,
compares adjacent elements, and swaps them if they are in the wrong order.
The algorithm gets its name because smaller elements "bubble" to the top of the list during each iteration.


1. The bubble_sort function takes an array (arr) as input and performs the bubble sort algorithm on it.
2. The variable n is initialized with the length of the array.
3. The outer loop runs n-1 times since after each iteration, the largest element is placed at the end of the array, so there is no need to compare it again.
4. Inside the outer loop, the inner loop is used to compare adjacent elements and swap them if they are in the wrong order.
5. For each iteration of the inner loop, the largest element in the remaining unsorted part of the array "bubbles up" to its correct position.
6. The condition arr[j] > arr[j + 1] checks if the current element is greater than the next element. If it is,
    a swap is performed using the tuple assignment arr[j], arr[j + 1] = arr[j + 1], arr[j], which swaps the values of the two elements.
7. After the inner loop completes, the largest element in the unsorted part of the array is placed at the end. This process repeats until the entire array is sorted.


Bubble sort has a time complexity of O(n^2) in the average and worst case, where n is the number of elements in the array.
It is not considered an efficient sorting algorithm for large lists, but it is easy to understand and implement.

https://www.youtube.com/watch?v=9I2oOAr2okY&t=2s&ab_channel=4GeeksAcademy
"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):  # O(n-1) = O(n)

        # Last i elements are already in place
        for j in range(0, n - i - 1):  # O(n-i-1) = O(n-i) = O(n)

            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(n^2)

# Usage
my_array = [5, 2, 8, 12, 3]
bubble_sort(my_array)
print(my_array)  # Output: [2, 3, 5, 8, 12]
