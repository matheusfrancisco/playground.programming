from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            mid_v = nums[mid]
            left = nums[mid - 1] if mid > 0 else float("-inf")
            right = nums[mid + 1] if mid < len(nums) - 1 else float("-inf")

            if left < mid_v > right:
                return mid
            elif left < mid_v < right:
                l = mid + 1
            else:
                r = mid - 1


obj = Solution()
print(obj.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
