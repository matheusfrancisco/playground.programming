class Solution:
    def countSubstrings(self, s: str) -> int:

        i = 0
        res = 0
        for i in range(len(s)):
            # aaa
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
            # i = 0
            # l = 0
            l = i
            r = i + 1
            # r = 1
            # ab
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1

        return res
