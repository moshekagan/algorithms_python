"""
Here's an example that demonstrates a more advanced recursion concept called "backtracking."
Backtracking is a technique where a recursive function explores all possible solutions by making a series of choices and undoing them if they lead to an invalid solution.

Consider the problem of finding all possible permutations of a given list of numbers.
Here's a recursive solution using backtracking:

------------------------------------------------------------------------------------------------------------------------
In this example, the permute function takes a list of numbers (nums) as input and returns a list of all possible permutations.

The base case is when the list is empty, in which case an empty permutation ([]) is returned.

In the recursive case, the function makes a choice by selecting a number from the list (chosen_num).
It creates a new list without the chosen number (remaining_nums) and makes a recursive call to find permutations of the remaining numbers. The recursive call returns a list of sub-permutations (sub_permutations).

Finally, the function appends the chosen number to each sub-permutation and adds the resulting permutations to the permutations list.
Once all choices have been explored, the function returns the list of permutations.

By using backtracking and recursion, this algorithm explores all possible combinations of the numbers in the list
and generates all valid permutations.
"""


def permute(nums):
    # Base case: if the list is empty, return an empty permutation
    if len(nums) == 0:
        return [[]]

    permutations = []  # List to store all permutations

    for i in range(len(nums)):
        # Make a choice by selecting a number from the list
        chosen_num = nums[i]

        # Create a new list without the chosen number
        remaining_nums = nums[:i] + nums[i + 1:]

        # Recursive call to find permutations of the remaining numbers
        sub_permutations = permute(remaining_nums)

        # Append the chosen number to each sub-permutation
        for sub_permutation in sub_permutations:
            permutations.append([chosen_num] + sub_permutation)

    return permutations


# Usage
print(permute([1, 2, 3]))
