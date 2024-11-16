from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right)//2
            if self.can_ship(weights, mid, days):
                right = mid
            else:
                left = mid + 1

        return right

    def can_ship(self, w, k, days):
        cur_weight = 0
        days_taken = 1
        for weight in w:
            cur_weight += weight
            if cur_weight > k:
                days_taken += 1
                cur_weight = weight
        return days_taken <= days
