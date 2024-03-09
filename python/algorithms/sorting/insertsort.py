def insertsort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] < arr[j]:
                aux = arr[i]
                arr[i], arr[j] = arr[j], aux
    return arr


print(insertsort([8, 7, 6, 5, 4, 3, 2, 1]))
# (out) [1, 2, 3, 4, 5, 6, 7, 8]
