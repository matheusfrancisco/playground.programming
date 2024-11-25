
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.string = s
        if not k:
            return self.is_palindrom(0, len(s) - 1)
        memo = {}

        def helper(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            elif not k:
                memo[(i, j, k)] = self.is_palindrom(i, j)
            else:
                while i < j:
                    if self.string[i] != self.string[j]:
                        memo[(i, j, k)] = helper(i + 1, j, k - 1) or helper(i, j-1, k-1)
                        return memo[(i, j, k)]
                    i += 1
                    j -= 1
                memo[(i, j, k)] = True
            return memo[(i, j, k)]
        return helper(0, len(self.string)-1, k)

    def is_palindrom(self, i, j):
        while i < j:
            if self.string[i] != self.string[j]:
                return False
            i += 1
            j -= 1
        return True
