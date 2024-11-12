
from typing import List
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        i = j = 0
        res = []
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product = val1 * val2
            freq = min(freq1, freq2)

            if not res or product != res[-1][0]:
                res.append([product, freq])
            else:
                res[-1][1] += freq
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            if freq1 == freq:
                i += 1
            if freq2 == freq:
                j += 1
        return res

        return res
