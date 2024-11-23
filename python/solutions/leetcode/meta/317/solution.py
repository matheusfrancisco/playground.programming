from typing import List
import collections

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dist_matrix = [[0] * cols for row in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        BUILDING = 1
        OBSTACLE = 2
        EMPTY_LAND = 0

        min_dist = float("inf")

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == BUILDING:
                    local_dist = float("inf")
                    queue = collections.deque([(row, col, 0)])
                    while queue:
                        cur_row, cur_col, distance = queue.popleft()

                        for i, y in directions:
                            new_row = cur_row + i
                            new_col = cur_col + y
                            if (0 <= new_row < rows) and (0 <= new_col < cols) and grid[new_row][new_col] == EMPTY_LAND:
                                grid[new_row][new_col] -= 1
                                dist_matrix[new_row][new_col] += distance + 1
                                queue.append((new_row, new_col, distance + 1))
                                local_dist = min(local_dist, dist_matrix[new_row][new_col])
                    EMPTY_LAND -= 1
                    min_dist = local_dist

        if min_dist == float("inf"):
            return -1
        return min_dist
