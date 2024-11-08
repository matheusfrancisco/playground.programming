# Memoization

Memoization is a fancy word for a simple concept 
(so is the case for a lot of things we learn in school). 
It means saving the previous function call result in a dictionary and reading 
from it when we do the exact same call again. And no I didn't spell it wrong. 
The word is meant to mean writing down on a "memo".

```python

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

the solution is simply saving previous results in a dictionary

```python
def fib(n, memo):
    if n in memo: # check in memo, if found, retrieve and return right away
        return memo[n]

    if n == 0 or n == 1:
        return n

    res = fib(n - 1, memo) + fib(n - 2, memo)

    memo[n] = res # save in memo before returning
    return res

```

## When to memoize

After ou draw the state-space tree, if you see duplicate subtrees, then 
it might be a good time to consider memoization.


## What to memoize

Think about the duplicate subtrees, what attribute(s) do they share? 
In the Fibonacci example, the duplicate subtrees have the same n value. 
Usually, the key to the memo is the start_index or any additional states 
that may appear multiple times during the recursion.

