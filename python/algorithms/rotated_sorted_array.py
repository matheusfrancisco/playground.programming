def find_min_rotated(arr: list[int]) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        print(l, r)
        if arr[mid] <= arr[-1]:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


print(find_min_rotated([30, 40, 50, 60, 70, 10, 20]))
