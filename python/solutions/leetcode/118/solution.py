
def pascal_triangle_temp(n: int) -> list:
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


def main():
    n = int(input())
    for i in range(n):
        j = int(input())
        out = pascal_triangle_temp(j)
        print(out)

main()
