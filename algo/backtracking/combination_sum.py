"""

Given an array of distinct integers candidates and a target integer target, return a list of all
unique combinations of candidates where the chosen numbers sum to target. You may return the 
combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 
combinations for the given input.

"""

def combination_sum(candidates, target):
    res = []

    def dfs(nums, start, re, path):
        if re == 0:
            res.append(path)
            return
        for j in range(start, len(nums)):
            num = nums[j]
            if re - num < 0:
                continue
            dfs(nums, j, re - num, path + [num])

    candidates.sort()
    dfs(candidates, 0, target, [])
    return res

print(combination_sum([2, 3, 6, 7], 7))
