

def two_sum(nums, target):
    n = {}

    for i, k in enumerate(nums):
        n[k] = i

    print(n)

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in n and n[diff] != i:
            return [nums[i], nums[n[diff]]]
    return []


"""

Given an integer array nums, find all unique triplets nums[i]
+ nums[j] + nums[k] = target where i, j, k are distinct. 
Assume that you are given a function twoSum(nums, twoTarget) 
that finds all unique sets of two numbers in nums that add up to twoTarget.

"""
def three_sum(nums, target):
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and nums[i-1] == nums[i]:
            print(f"nums[{i}]: continue", )
            continue
        print(f"calling two_sum({nums[i+1:]}, {target - nums[i]})")
        t = two_sum(nums[i+1:], target - nums[i])
        if t:
            t.append(num)
        print(f"nums[{i}]: ", t)


# print(two_sum([3, 1, 4, 2], 6))
print(three_sum([3, 1, 1, 2], 6))
