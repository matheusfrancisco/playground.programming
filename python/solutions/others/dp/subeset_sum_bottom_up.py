
def subset_sum(arr, total):
    n = len(arr)
    dp = [[-1 for i in range(total + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(total):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][total]

def main():
    input_arr = [[3, 5, 8], [2, 4, 7], [2, 3, 5], [1, 2, 3, 7], [10, 20, 23, 34]]
    total = [13, 8, 5, 6, 57]

    for i in range(len(input_arr)):
        print(str(i + 1) + ".\tDoes a subset of " + str(input_arr[i]) + " sum up to " + str(total[i]) + "?   ", "Yes." if subset_sum(input_arr[i], total[i]) else "No.")
        print("-"*100)

main()
# (out) 1.	Does a subset of [3, 5, 8] sum up to 13?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 2.	Does a subset of [2, 4, 7] sum up to 8?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 3.	Does a subset of [2, 3, 5] sum up to 5?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 4.	Does a subset of [1, 2, 3, 7] sum up to 6?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 5.	Does a subset of [10, 20, 23, 34] sum up to 57?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
