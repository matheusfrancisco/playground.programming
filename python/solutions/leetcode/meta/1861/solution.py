from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])
        # not INPLACE
        out = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    out[i][ROWS-r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    out[c][ROWS-r-1] = "*"
                    i = c - 1
        return out
        # INPLACE
        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1
        # [["#","#","*",".","*","."],
        # ["#","#","#","*",".","."],
        # ["#","#","#",".","#","."]]

        res = []
        for c in range(COLS):
            col = []
            for r in reversed(range(ROWS)):
                col.append(box[r][c])

            res.append(col)

        return res
