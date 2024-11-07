
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.



for each letter in the input string, we can either include it as a previous
string or start a new string with it. With those two choices, the total
number of operations is 2^n. We also need O(n) to check if the string is 
a palindrome. In total, the complexity is O(2^n*n)


The space is O(n) in the worst case
"""


# this is O(n)
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def partition(s: str):
    res = []

    def dfs(strat, path):
        if strat == len(s):
            res.append(path[:])
            return
        for e in range(strat + 1, len(s) + 1):
            if is_palindrome(s[strat:e]):
                path.append(s[strat:e])
                dfs(e, path)
                path.pop()

    def dfs2(start, cur):
        if start == len(s):
            res.append(cur[:])
            return
        for e in range(start + 1, len(s) + 1):
            prefix = s[start:e]
            if is_palindrome(s[start:e]):
                dfs(e, cur + [prefix])

    dfs2(0, [])
    return res


print(partition("aab"))
print(partition("aab") == [["a", "a", "b"], ["aa", "b"]])
