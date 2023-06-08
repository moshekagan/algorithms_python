## q1
c - O(n^2) 

The time complexity of the given code snippet is O(n^2),   
which represents a quadratic time complexity.   
The code snippet contains nested loops that iterate over the `numbers` list,  
resulting in a time complexity that grows quadratically with the size of the input.


## q2
time complexity of the `mystery_function` in terms of `n` is `O(n*log(n))`.

Here's an explanation and analysis of the code's behavior:

The `mystery_function` consists of a nested loop. The outer loop runs n times, and the inner loop runs `log(n)` times.   
Inside the inner loop, the variable `j` is repeatedly doubled until it exceeds `n`.

Let's break down the number of iterations in each loop:

The outer loop iterates n times, which gives us a time complexity of `O(n)`.  
The inner loop iterates `log n` times, as `j` is multiplied by 2 in each iteration until it exceeds `n`.  
This results in a time complexity of `O(log n)`.
Since the inner loop is nested inside the outer loop, the total time complexity is the product of the two complexities:  
`O(n) * O(log n) = O(n log n)`.

Therefore, the `mystery_function` has a time complexity of `O(n log n)`.
