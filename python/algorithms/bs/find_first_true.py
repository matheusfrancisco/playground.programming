# arr = [False, False, True, True, True, True, True, True, True, True]
#        0      1     2     3     4     5     6     7     8     9
#                                 ^
#                           true  true  true


def find_boundary(arr):
    left = 0
    right = len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        curr = arr[mid]
        if curr:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
