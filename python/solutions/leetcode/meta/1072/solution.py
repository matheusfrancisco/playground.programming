from typing import List
import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        freq = collections.defaultdict(int)
        for current_row in matrix:
            s = ""
            if current_row[0] == 0:
                for r in current_row:
                    s += str(r)
                freq[s] += 1
            else:
                for r in current_row:
                    if r == 1:
                        s += "0"
                    else:
                        s += "1"
                freq[s] += 1
        return max(freq.values())
