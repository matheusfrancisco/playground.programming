



# arr = [2, 3, 4, 7, 11]
def findKthPositive(arr, k):
    if arr[0] != 1:
        if arr[0] - 1 >= k:
            return k
        else:
            k -= arr[0] - 1
    i = 0

    while i < len(arr) - 1:
        diff = arr[i + 1] - arr[i]
        if diff != 1:
            for num in range(arr[i] + 1, arr[i+1]):
                k -= 1
                if not k:
                    return num

        i += 1

    if k:
        return arr[-1] + k

# first tase start at number 1


arr1 = [10, 11, 14, 17, 21]
print(findKthPositive(arr1, 9) == 9)

arr = [2, 3, 4, 7, 11]
# if not start at 1 everything is missing from left
print(findKthPositive(arr, 5) == 9)

# missing in between 2 and 10
arr = [1, 2, 10, 11]
print(findKthPositive(arr, 3) == 5)

# end element
arr = [1, 2, 3, 4]
print(findKthPositive(arr, 2) == 6)
