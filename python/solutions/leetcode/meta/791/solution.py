
import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = collections.defaultdict(int)
        for char in s:
            c[char] += 1
        new = ""
        for char in order:
            v = c.get(char, 0)
            while v > 0:
                new += char
                v -= 1
            c[char] = v

        for k, v in c.items():
            while v > 0:
                new += k
                v -= 1
        return new

print(Solution().customSortString("cba", "abcd")) # "cbad"
