def n_queens(size):
    rows_visited = set()
    pos_diagonal_visited = set()
    neg_diagonal_visited = set()

    s = 0
    def backtrack(col):
        if col == size:
            nonlocal s
            s += 1
            return 

        for row in range(size):
            if row in rows_visited or (row+col) in pos_diagonal_visited or (row-col) in neg_diagonal_visited:
                continue
            rows_visited.add(row)
            pos_diagonal_visited.add(row + col)
            neg_diagonal_visited.add(row - col)

            backtrack(col + 1)

            rows_visited.remove(row)
            pos_diagonal_visited.remove(row + col)
            neg_diagonal_visited.remove(row - col)

    backtrack(0)
    return s

def main():
    n_case = int(input())
    for i in range(n_case):
        size = int(input())
        out = n_queens(size)
        print(out)

main()
