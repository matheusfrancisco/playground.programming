import collections
from typing import List

# monotinic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        res = [0] * len(temperatures)
        stack = collections.deque([(0, temperatures[0])])

        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()

                res[i] = abs(i-idx)
            stack.append((idx, temp))

        return res
