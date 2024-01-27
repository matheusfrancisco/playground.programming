#https://leetcode.com/problems/rotate-array/
def reverse_inplace(nums: list[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1
    

def rotate(nums: list[int], k: int) -> list[int]:
    k = k % len(nums)
    reverse_inplace(nums, 0, len(nums) - 1)
    reverse_inplace(nums, 0, k - 1)
    reverse_inplace(nums, k, len(nums) - 1)
    return nums




assert(rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
