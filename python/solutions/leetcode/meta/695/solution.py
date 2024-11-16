import collections
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    shape = 0

                    q = collections.deque()
                    visit.add((r, c))
                    q.append((r, c))
                    while q:
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        shape += 1
                        row, col = q.popleft()

                        for dr, dc in directions:
                            r1, c1 = row + dr, col + dc
                            if (r1 in range(rows)) and (c1 in range(cols)) and (r1, c1) not in visit and grid[r1][c1]:
                                q.append((r1, c1))
                                visit.add((r1, c1))
                    ans = max(shape, ans)
        return ans

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0

        def find_area(grid, cur_row, cur_col):
            if (0 <= cur_row < rows) and (0 <= cur_col < cols) and grid[cur_row][cur_col] == 1:
                grid[cur_row][cur_col] = 0
                area = 1
                for r_i, c_i in directions:
                    area += find_area(grid, cur_row+r_i, cur_col+c_i)
                return area
            else:
                return 0

        for r in range(rows):
            for c in range(cols):
                area = find_area(grid, r, c)
                max_area = max(area, max_area)
        return max_area
