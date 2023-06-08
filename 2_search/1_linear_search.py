"""
In this example, the linear_search function takes an array (arr) and a target value (target) as input.
It iterates over the elements of the array using a for loop and checks if each element is equal to the target value.
If a match is found, the function returns the index of the target value.
If the target value is not found in the array, the function returns -1.

In the example usage, we create an array (my_list) and specify a target value (target_value).
We then call the linear_search function with these inputs and store the result in the result variable.
Finally, we check the value of result to determine if the target value was found or not, and print an appropriate message accordingly.

Please note that this is a basic example of linear search and may not be the most efficient algorithm for large datasets.
There are other search algorithms, such as binary search, that are more suitable for sorted arrays.
"""


# O(n)
def linear_search(arr, target):
    for i in range(len(arr)):   # O(n)
        if arr[i] == target:    # O(1)
            return i  # Found the target, return its index # O(1)
    return -1  # Target not found in the array # O(1)


# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
target_value = 7

result = linear_search(my_list, target_value)

if result != -1:
    print(f"The target value {target_value} is found at index {result}.")
else:
    print("The target value is not found in the array.")