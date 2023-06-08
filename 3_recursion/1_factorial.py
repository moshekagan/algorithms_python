"""
Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller,
similar subproblems. In Python, recursion is achieved by defining a function that calls itself within its own body.


1. Base Case: Every recursive function needs a base case, which is a condition that determines when the function should
    stop calling itself and return a value. The base case is usually defined for the simplest form of the problem that
    can be directly solved without further recursion.

2. Recursive Case: The recursive case defines how the function calls itself with smaller instances of the problem.
    By breaking down the original problem into smaller subproblems, the function can solve the problem
    by solving the subproblems recursively.

3. Progress Towards the Base Case: In order for recursion to work correctly, each recursive call should make progress
    towards reaching the base case. This ensures that the recursive calls eventually converge to the base case,
    preventing infinite recursion.

4. Stack Frames: When a function calls itself, a new instance of the function is created and pushed onto the call stack.
 Each instance of the function is known as a stack frame and contains its own set of variables and execution context. T
 he stack frames are popped off the stack and processed in reverse order once the base case is reached,
 allowing the recursive calls to return values and build up the final result.


------------------------------------------------------------------------------------------------------------------------
In this example, the factorial function calculates the factorial of a number by multiplying it with the factorial of the
preceding number. The base case is when n is 0 or 1, in which case the function returns 1. In the recursive case,
the function calls itself with n - 1 as the argument, making progress towards the base case.

When using recursion, it's important to ensure that the base case is reachable and that the recursive calls converge
towards the base case. Otherwise, the recursion may lead to infinite loops and cause the program to run out of stack space.

Recursion is a powerful technique that can be used to solve problems that exhibit self-similarity or can be broken down
into smaller subproblems. However, it's worth noting that recursive solutions may not always be the most efficient or practical,
especially for large inputs, due to the overhead of function calls and stack frames.
"""

# 5! = 5 * 4 * 3 * 2 * 1

# 5! = 5 * 4! = 5 * 24 = 120
# 4! = 4 * 3! = 4 * 6 = 24
# 3! = 3 * 2! = 3 * 2 = 6
# 2! = 2 * 1! = 2 * 1 = 2
# 1! = 1 * 0! = 1 * 1 = 1
# 0! = 1
def factorial(n):
    if n == 0:
        return 1

    prev_n_fac = factorial(n-1)

    return n * prev_n_fac


print(factorial(5))     # 5!


# Usage
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(14))
