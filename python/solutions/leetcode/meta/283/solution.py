
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = -1
        for i, num in enumerate(nums):
            if nums[i] == 0:
                if last_zero == -1:
                    last_zero = i
                else:
                    continue
            else:
                if last_zero == -1:
                    continue
                else:
                    nums[i], nums[last_zero] = 0, nums[i]
                    while last_zero < len(nums) and nums[last_zero] != 0:
                        last_zero += 1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
