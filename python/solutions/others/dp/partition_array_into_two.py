nums = [1, 2, 3]


print(len(nums))

rows = len(nums)
cols = sum(nums) // 2 + 1
dp = [[-1 for i in range(cols)] for x in range(len(nums))]

print(dp)
# (out)
# [[-1, -1, -1, -1],
# [-1, -1, -1, -1],
# [-1, -1, -1, -1]]
for i in range(rows):
    dp[i][0] = 1
for s in range(1, cols):
    dp[0][s] = nums[0] == s
print(dp)
for i in range(1, rows):
    for s in range(1, cols):
        if dp[i - 1][s]:
            dp[i][s] = dp[i - 1][s]
        elif s >= nums[i]:
            dp[i][s] = dp[i - 1][s - nums[i]]
        else:
            dp[i][s] = 0
        print(i, s, dp)

# (out) [[1, True, False, False], [1, -1, -1, -1], [1, -1, -1, -1]]
# (out) 1 1 [[1, True, False, False], [1, True, -1, -1], [1, -1, -1, -1]]
# (out) 1 2 [[1, True, False, False], [1, True, 1, -1], [1, -1, -1, -1]]
# (out) 1 3 [[1, True, False, False], [1, True, 1, True], [1, -1, -1, -1]]
# (out) 2 1 [[1, True, False, False], [1, True, 1, True], [1, True, -1, -1]]
# (out) 2 2 [[1, True, False, False], [1, True, 1, True], [1, True, 1, -1]]
# (out) 2 3 [[1, True, False, False], [1, True, 1, True], [1, True, 1, True]]
