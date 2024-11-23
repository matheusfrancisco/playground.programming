from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = max_cons = 0
        r = 0
        # [1,1,1,0,0,0,1,1,1,1,0]
        for r, num in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                max_cons = max(max_cons, r - l + 1)
        return max_cons
