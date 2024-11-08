"""
Given a string of unique letters, find all of its distinct permutations.

Permutation means arranging things with an order. 
For example, permutations of [1, 2] are [1, 2] and [2, 1]. 
Permutations are best visualized with trees.

Time Complexity
We have n letters to choose in the first level, n - 1 
choices in the second level and so on therefore the 
number of strings we generate is n * (n - 1) * (n - 2) * ... * 1,
or O(n!) (see math basics if you need a refresher on factorial). 
Since each string has length n, generating all the strings requires 
O(n * n!) time.

Space Complexity
The total space complexity is given by the amount of space 
required by the strings we're constructing. 
Like the time complexity, the space complexity is also O(n * n!).
"""

from typing import List

def permutations(letters: str) -> List[str]:

    res = []
    path = []
    used = [False] * len(letters)

    def dfs(start):
        if start == len(letters):
            res.append(''.join(path))
            return
        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(start + 1)
            path.pop()
            used[i] = False
    dfs(0)
    return res


print(permutations('abc'))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# (out) ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# abc
# dfs(0)
#    i = 0, letter = a
#    path = ['a']
#    used = [True, False, False]
#    dfs(1)
#       i = 0, letter = b
#       path = ['a', 'b']
#       used = [True, True, False]
#       dfs(2)
#          i = 0, letter = c
#          path = ['a', 'b', 'c']
#          used = [True, True, True]
#          dfs(3)
#             reach base case, append 'abc' to res
#             res = ['abc']
#          path = ['a', 'b']
#          used = [True, True, False]
#       path = ['a']
#       used = [True, False, False]
#       dfs(2)
#          i = 1, letter = c
#          path = ['a', 'c']
#          used = [True, False, True]
#          dfs(3)
#             reach base case, append 'acb' to res
#             res = ['abc', 'acb']
#          path = ['a']
#          used = [True, False, False]
#    path = []
# ...
