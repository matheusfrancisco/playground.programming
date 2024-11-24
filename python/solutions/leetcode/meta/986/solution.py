from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            # s1 [1,3]
            # s2 [4,5]
            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            else:
                res.append([max(start1, start2), min(end1, end2)])
                # [1, 4], [5, 9]
                # [2, 6]
                if end1 > end2:
                    j += 1
                else:
                    i += 1

        return res
