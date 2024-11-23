import collections
from typing import List
import math
import heapq

class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        v = collections.defaultdict(list)
        for xi, yi in points:
            dist = math.sqrt(math.pow((xi - 0), 2) + math.pow((yi - 0), 2))
            v[dist].append([xi, yi])
            heapq.heappush(heap, dist)

        out = []
        while k:
            dist = heapq.heappop(heap)
            p = v[dist].pop()
            out.append(p)
            k -= 1
        return out

class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            dist = math.sqrt(math.pow((xi - 0), 2) + math.pow((yi - 0), 2))
            heapq.heappush(heap, (dist, xi, yi))

        out = []
        while k:
            _, x, y = heap.pop(0)
            heapq.heapify(heap)
            out.append([x, y])
            k -= 1

        return out

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            dist = math.sqrt(math.pow((xi - 0), 2) + math.pow((yi - 0), 2))
            if len(heap) < k:
                heapq.heappush(heap, (-dist, xi, yi))
            else:
                heapq.heappushpop(heap, (-dist, xi, yi))

        out = [(x, y) for _, x, y in heap]

        return out
