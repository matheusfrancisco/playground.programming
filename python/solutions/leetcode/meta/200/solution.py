import collections
from typing import List

def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visited.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                        (r, c) not in visited):
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_inslands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def set_island_zero(grid, r, c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == '1':
                grid[r][c] = "0"
                for row_inc, col_inc in directions:
                    set_island_zero(grid, r + row_inc, c + col_inc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_inslands += 1
                    set_island_zero(grid, row, col)
        return num_inslands
