"""
1. What is the time complexity of the mystery_function in terms of n?
2. Explain your answer and provide a brief analysis of the code's behavior.
"""


def mystery_function(n):
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            count += 1
    return count



