"""
In this example, the binary_search function takes a sorted array (arr) and a target value (target) as input.
It initializes two pointers, low and high, to the start and end indices of the array, respectively.
It then enters a while loop that continues as long as low is less than or equal to high.
In each iteration, the function calculates the middle index mid as the average of low and high.
It compares the value at mid with the target value and adjusts the low and high pointers accordingly.

If the value at mid is equal to the target, the function returns the index mid, indicating that the target value has been found.
If the value at mid is less than the target, the target value must be in the right half of the array, so the low pointer is updated to mid + 1.
If the value at mid is greater than the target, the target value must be in the left half of the array, so the high pointer is updated to mid - 1.

If the while loop finishes without finding the target value, the function returns -1, indicating that the target was not found in the array.

In the example usage, we create a sorted array (my_list) and specify a target value (target_value).
We then call the binary_search function with these inputs and store the result in the result variable.
Finally, we check the value of result to determine if the target value was found or not, and print an appropriate message accordingly.

Binary search is an efficient search algorithm for sorted arrays as it eliminates half of the remaining elements in each iteration.
"""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half of the array
        else:
            high = mid - 1  # Target is in the left half of the array

    return -1  # Target not found in the array


# Example usage:
my_list = [1, 3, 5, 7, 9, 11]
target_value = 7

result = binary_search(my_list, target_value)

if result != -1:
    print(f"The target value {target_value} is found at index {result}.")
else:
    print("The target value is not found in the array.")
