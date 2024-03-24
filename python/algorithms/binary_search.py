from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = right + left // 2
        curr = arr[mid]
        if curr == target:
            return mid
        if curr < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
