
from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sum_with_skip = sum_no_skip = res = arr[0]  # 1
        # [1,-2,0,3]
        #  sum_with_skip = sum_no_skip = res =  1
        # -2, sum_with_skip = max(-1, 1) = 1
        # sum_no_skip = -1, res = 1
        # 0, sum_with_skip =1,sum_no_skip=0, res =1
        # 3, sum_with_skip =
        for num in arr[1:]:
            if sum_with_skip < 0:
                sum_with_skip = 0

            if num >= 0:
                sum_with_skip += num
            else:
                sum_with_skip = max(sum_with_skip + num, sum_no_skip)

            if sum_no_skip < 0:
                sum_no_skip = 0

            sum_no_skip += num
            res = max(res, sum_no_skip, sum_with_skip)
        return res
