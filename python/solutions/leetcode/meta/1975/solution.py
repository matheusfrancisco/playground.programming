from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        sum_m = 0
        neg_cnt = 0
        min_value = float("inf")
        for r in matrix:
            for n in r:
                sum_m += abs(n)
                min_value = min(min_value, abs(n))
                if n < 0:
                    neg_cnt += 1

        if neg_cnt & 1:
            sum_m -= (2 * min_value)

        return sum_m
