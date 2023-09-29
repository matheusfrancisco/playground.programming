class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_m = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefix_m[r][c + 1]
                self.prefix_m[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.prefix_m[r2][c2]
        above = self.prefix_m[r1 - 1][c2]
        left = self.prefix_m[r2][c1 - 1]
        top_left = self.prefix_m[r1 - 1][c1 - 1]
        return bottom_right - above - left + top_left




def main():
    inp = input()
    m = []
    out = []
    nm = None
    if inp == "NumMatrix":
        n, _ = map(int, input().split(" "))
        for i in range(n):
            row = list(map(int, input().split(" ")))
            l = []
            for k in row:
                l.append(k)
            m.append(l)
        nm = NumMatrix(m)
        out.append("null")
    inpts = input().split(" ")
    for i in range(len(inpts)):
        op = [int(x) for x in input().split(" ")]
        out.append(nm.sumRegion(op[0], op[1], op[2], op[3]))
    print(out)



main()
