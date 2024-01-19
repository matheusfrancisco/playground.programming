def min_falling_path_sum(matrix):
    C = len(matrix[0])
    R = len(matrix)
    for r in range(1, R):
        for c in range(C):
            mid = matrix[r - 1][c]
            left = matrix[r - 1][c - 1] if c > 0 else float("inf")
            right = matrix[r - 1][c + 1] if c < R - 1 else float("inf")
            matrix[r][c] = matrix[r][c] + min(mid, left, right)
    return min(matrix[-1])
