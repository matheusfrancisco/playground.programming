

def main():
    s, target = input().split(" ")
    dp = {}
    nums = input().split(" ")
    nums = list(map(int, nums))
    def backtracking(nums, i, t):
        if (i, t) in dp:
            return dp[(i, t)]
        if i == len(nums):
            if t ==  target:
                return 1
            return 0
        dp[(i, t)] = backtracking(nums, i + 1, t - nums[i]) + backtracking(nums, i + 1, t + nums[i])
        return dp[(i, t)]

    return backtracking(nums, 0,  int(target))


print(main())
