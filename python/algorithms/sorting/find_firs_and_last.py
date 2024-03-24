def search_range(nums: list[int], target: int):
    left, right = 0, len(nums) - 1
    last, first = -1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first, last]


print(search_range([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
