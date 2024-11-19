
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.island_id = -1
        self.island_areas = {}
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if grid[m][n] == 1:
                    island_area = self.dfs(grid, m, n)
                    self.island_areas[self.island_id] = island_area
                    self.island_id -= 1
        max_area = 0

        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if not grid[m][n]:
                    area = 1
                    surrounding = set()

                    for m_inc, n_inc in self.dir:
                        new_m = m + m_inc
                        new_n = n + n_inc
                        if (0 <= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding.add(grid[new_m][new_n])
                    for island_id in surrounding:
                        area += self.island_areas[island_id]
                    max_area = max(max_area, area)
        return max_area if max_area else len(grid) ** 2

    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[0])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1
            for m_inc, n_inc in self.dir:
                new_m = m + m_inc
                new_n = n + n_inc
                area += self.dfs(grid, new_m, new_n)
            return area
        else:
            return 0
