from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end_point = res[-1][-1]
            if start <= last_end_point:
                res[-1][1] = max(end, last_end_point)
            else:
                res.append([start, end])
        return res

# T: O(nlogn) + O(n) = O(n+ nlogn) = O(nlogn)
# S: O(n)
