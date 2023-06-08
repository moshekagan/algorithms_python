"""
Question: What is the time complexity of the following code snippet?

a) O(1)
b) O(n)
c) O(n^2)
d) O(log n)

"""


def print_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])


