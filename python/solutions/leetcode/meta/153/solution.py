from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid-1] > mid_val:
                return mid_val
            else:
                if mid_val > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
