from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val >= nums[l]:
                if nums[l] <= target < mid_val:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mid_val < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
