import collections



def number_of_arithmetic_slides(nums: list[int]) -> int:
    res, n = 0, len(nums)
    dp = [collections.defaultdict(int) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += 1 + dp[j][diff]
            res += dp[j][diff]
    return res


print(number_of_arithmetic_slides([2, 4, 6, 8, 10]))
