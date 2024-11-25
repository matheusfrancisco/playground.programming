from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if S - (2 * left) == x:
                return i
            left += x
        return -1
