def mergesort(arr: list) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    # return merge2(left, right, mid, len(arr) - mid)
    return merge2(left, right, mid, len(arr) - mid)


def merge(arr: list, arr1: list) -> list[int]:
    i, j = 0, 0
    out = []

    while i < len(arr) and j < len(arr1):
        if arr[i] <= arr1[j]:
            out.append(arr[i])
            i += 1
        else:
            out.append(arr1[j])
            j += 1

    while i < len(arr):
        out.append(arr[i])
        i += 1
    while j < len(arr1):
        out.append(arr1[j])
        j += 1
    return out


def merge2(arr: list, arr1: list, mid, end) -> list[int]:
    i, j = 0, 0
    out = []

    while i < mid and j < end:
        if arr[i] <= arr1[j]:
            out.append(arr[i])
            i += 1
        else:
            out.append(arr1[j])
            j += 1

    while i < mid:
        out.append(arr[i])
        i += 1
    while j < end:
        out.append(arr1[j])
        j += 1
    return out


print(merge([1, 3, 5], [2, 4, 6]))
print(merge2([1, 3, 5], [2, 4, 6], 3, 3))
print(mergesort([6, 5, 4, 3, 2, 1]))
