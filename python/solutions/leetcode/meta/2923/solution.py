from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        indegree = [0] * len(grid)

        for g in grid:
            i = 1
            while i < len(g):
                if g[i] != 0:
                    indegree[i] += 1
                i += 1

        team = -1
        for i in range(len(indegree)):

            if indegree[i] == 0:
                team = i

        return team
