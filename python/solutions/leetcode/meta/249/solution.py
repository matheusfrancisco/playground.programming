from typing import List
import collections

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                grouping[(-1,)].append(string)
            else:
                chars = []
                i = 1
                while i < len(string):
                    chars.append(
                        (ord(string[i]) - ord(string[i-1])) % 26
                    )
                    i += 1
                grouping[tuple(chars)].append(string)
        return list(grouping.values())
# O(N * K) where N = number of strings in strings, where K is the length of the longest string in strings
# O(N * K)
