"""
Given an integer n, generate all strings with n matching parentheses. "matching" parentheses mean

there is equal number of opening and closing parentheses.
each opening parenthesis has matching closing parentheses.
For example, () is a valid string but )( is not a valid string because ) has no matching parenthesis before it and ( has no matching parenthesis after it.
"""

from typing import List

def generate_parentheses(n: int) -> List[str]:
    res = []
    path = []

    def dfs(start, open_count, close_count):
        if start == 2 * n:
            res.append(''.join(path))
            return
        if open_count < n:
            path.append('(')
            dfs(start + 1, open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(start + 1, open_count, close_count + 1)
            path.pop()

    dfs(0, 0, 0)
    return res
