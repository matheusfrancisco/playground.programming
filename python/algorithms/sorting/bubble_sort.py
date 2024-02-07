

def bubble_sort(arr: list[int]) -> list[int]:
    " time complexity O(n^2)"
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr


arr = bubble_sort([1, 2, 4, 5, 3, 5, 7, 4])
arr == [1, 2, 3, 4, 4, 5, 5, 7]
