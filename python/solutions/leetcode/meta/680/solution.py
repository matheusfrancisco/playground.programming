class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s, i + 1, j) or self.is_palindrome(s, i, j-1)
            else:
                i += 1
                j -= 1
        return True

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# T: O(N)
# S: O(1)
class Solution2:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        k = 1

        while i < j:
            if s[i] != s[j]:
                if k <= 0:
                    return False
                if self.is_palindrome(s, i+1, j) or self.is_palindrome(s, i, j-1):
                    return True
                k -= 1
            else:
                j -= 1
                i += 1

        return True

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome2(self, s: str) -> bool:
        def check(lo, hi, removed=False):
            while lo < hi:
                if s[lo] != s[hi]:
                    if removed:
                        return False
                    return check(lo+1, hi, True) or check(lo, hi-1, True)
                lo += 1
                hi -= 1
            return True
        return check(0, len(s)-1)
# T: O(N)
# S: O(1)
# T: O(N)
# S: O(1)


print(Solution().validPalindrome("aacca"))  # True
