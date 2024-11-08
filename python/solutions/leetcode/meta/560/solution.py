import collections
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = collections.defaultdict(int)
        h[0] = 1

        acc = 0
        count = 0
        for n in nums:
            acc += n
            if h[acc - k]:
                count += h[acc - k]
            h[acc] += 1

        return count


obj = Solution()
assert obj.subarraySum([1, 1, 1], 2) == 2
