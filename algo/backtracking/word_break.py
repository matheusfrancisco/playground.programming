

"""
Given a string and a list of words, determine if the string can be 
constructed from concatenating words from the list of words. 
A word can be used multiple times.

Input:

target = "algomonster"
words = ["algo", "monster"]
Output: true

Input:

target = "aab"
words = ["a", "c"]
Output: false
"""
from typing import List


def word_break(s: str, words: List[str]) -> bool:
    memo = {}

    def dfs(start):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        ans = False
        for w in words:
            if s[start:].startswith(w):
                if dfs(start + len(w)):
                    ans = True
                    break
        memo[start] = ans
        return ans

    return dfs(0)


print(word_break("algomonster", ["algo", "monster"]))
print(word_break("aab", ["a", "a", "b", "a"]))
print(word_break("aab", ["a", "aa", "b"]))
