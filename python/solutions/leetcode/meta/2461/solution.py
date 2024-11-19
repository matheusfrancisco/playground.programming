import collections
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        cur_sum = 0
        res = 0

        left = 0
        right = 0
        while right < len(nums):
            cur_sum += nums[right]
            count[nums[right]] += 1

            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                cur_sum -= nums[left]

                left += 1
            if len(count) == right - left + 1 == k:
                res = max(res, cur_sum)

            right += 1

        return res
