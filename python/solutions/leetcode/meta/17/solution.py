from typing import List

def get_letters(digit):
    if digit == "2":
        return ["a", "b", "c"]
    if digit == "3":
        return ["d", "e", "f"]
    if digit == "4":
        return ["g", "h", "i"]
    if digit == "5":
        return ["j", "k", "l"]
    if digit == "6":
        return ["m", "n", "o"]
    if digit == "7":
        return ["p", "q", "r", "s"]
    if digit == "8":
        return ["t", "u", "v"]
    if digit == "9":
        return ["w", "x", "y", "z"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        if len(digits) == 0:
            return res

        def dfs(start, path):
            if start == len(digits):
                res.append("".join(path))
                return

            for letter in get_letters(digits[start]):
                path.append(letter)
                dfs(start + 1, path)
                path.pop()

        dfs(0, path)
        return res


print(Solution().letterCombinations("23"))
