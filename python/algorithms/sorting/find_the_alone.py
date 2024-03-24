def single_non_duplicate(nums: list[int]) -> int:
    def to_the_left(mid: int) -> bool:
        if mid == len(nums) - 1:
            return True
        elif mid % 2 == 0:
            return nums[mid] != nums[mid + 1]
        else:
            return nums[mid] != nums[mid - 1]

    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if to_the_left(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return nums[ans]


print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))  # 10
print(single_non_duplicate([3, 3, 7, 7, 10, 10, 11]))  # 11
