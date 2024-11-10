from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        if len(heights) == 1:
            return [0]
        if len(heights) == 0:
            return []
        out = []
        max_h = -1
        for i in reversed(range(len(heights))):
            if max_h < heights[i]:
                out.append(i)
                max_h = heights[i]
        k = []
        for i in range(len(out)-1, -1, -1):
            k.append(out[i])
        return k


print(Solution().findBuildings([4,2,3,1]))
# [0,2,3]
