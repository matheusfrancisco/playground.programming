import sys

def replace_elements(arr: list[int]) -> list[int]:
    l = len(arr)
    if l == 0:
        return []
    if l == 1:
        return [-1]
    arr.append(-1)

    max_value = arr[l]
    for i in range(l, 0, -1):
        prev = arr[i]
        max_value = max(max_value, prev)
        arr[i] = max_value

    return arr[1::]


def main():
    arr = list(input().split(" "))
    arr = [int(x) for x in arr]
    out = replace_elements(arr)
    print(f"Output: {out}")

assert replace_elements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
main()


