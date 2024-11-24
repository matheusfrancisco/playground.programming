
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = num
                    count += 1
                else:
                    count -= 1
        return candidate
