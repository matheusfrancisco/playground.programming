import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = collections.Counter(s)
        odds = 0

        for k, v in d.items():
            if v % 2 == 1:
                odds += 1

        return odds <= 1

class Solution1:
    def canPermutePalindrome(self, s: str) -> bool:
        unpaired_chars = set()

        for char in s:
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            else:
                unpaired_chars.remove(char)

        return len(unpaired_chars) <= 1
