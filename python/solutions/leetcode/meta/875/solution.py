
from typing import List
import math
# min = 1 banana per hour
# max = max(of piles)
# for Input: piles = [3,6,7,11], h = 8
# the solution is (1,... 11)


# time complex: O(N) * O(logS) -> NlogS
# Space O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if not self.can_eat(piles, mid, h):
                left = mid + 1
            else:
                right = mid
        return left

    def can_eat(self, piles, speed, h):
        hours = 0
        for pile in piles:
            if speed >= pile:
                hours += 1
            else:
                hours += math.ceil(pile/speed)
        return hours <= h


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
# out 4
