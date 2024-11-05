from typing import List
import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Edge cases it is possible not have a path return -1
        # if the start is block return -1
        # if the end is block return -1

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = collections.deque([(0, 0, 1)])

        movements = [(0, 1),
                     (0, -1),
                     (1, 0),
                     (-1, 0),
                     (1, 1),
                     (-1, -1),
                     (1, -1),
                     (-1, 1)]

        grid[0][0] = 1
        # BFS for shortest path
        while queue:
            x, y, path_len = queue.popleft()

            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return path_len

            for dx, dy in movements:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                    # overwrite the grid to avoid cycles
                    # if don't want modify the grid we can use a set to store the visited nodes
                    grid[nx][ny] = 1
                    queue.append((nx, ny, path_len + 1))

        return -1


# Time complexity: O(N)
# Space: O(N)

obj = Solution()
assert obj.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
