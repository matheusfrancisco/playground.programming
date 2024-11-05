from typing import List
import random

"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
"""

class Solution:

    def __init__(self, w: List[int]):
        self.items = []
        total = 0
        for wi in w:
            total += wi
            self.items.append(total)
        self.w = w
        self.total = total

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        l = 0
        r = len(self.items)

        while l < r:
            mid = (l + r) // 2
            if self.items[mid] < target:
                l = mid + 1
            else:
                # if we mid - 1 we can remove the number
                r = mid
        return l
##  init -> O(N), S: O(N)
##  pickIndex -> O(logN): O(1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
