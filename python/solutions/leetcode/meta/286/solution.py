from typing import List
import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])

        queue = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))
        print(queue)
        if not queue:
            return

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cur_row, cur_col, distance = queue.popleft()
            if distance <= rooms[cur_row][cur_col]:
                rooms[cur_row][cur_col] = distance
                for rinc, cinc in dir:
                    n_row = cur_row + rinc
                    n_col = cur_col + cinc
                    if (0 <= n_row < ROWS) and (0 <= n_col < COLS) and rooms[n_row][n_col] != 1:
                        queue.append((n_row, n_col, distance + 1))
