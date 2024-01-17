

def subset_r(arr, n, total, dp):
    if total == 0:
        return True
    if n == 0:
        return False

    if dp[n][total] != -1:
        return dp[n][total]

    if (arr[n-1] > total):
        dp[n][total] = subset_r(arr, n-1, total, dp)
        return dp[n][total]

    dp[n][total] = subset_r(arr, n-1, total, dp) or subset_r(arr, n-1, total-arr[n-1], dp)
    return dp[n][total]

def subset_sum(arr, total):
    n = len(arr)
    dp = [[-1 for i in range(total + 1)] for j in range(n + 1)]
    return subset_r(arr, n, total, dp)

def main():
    input_arr = [[3, 5, 8], [2, 4, 7], [2, 3, 5], [1, 2, 3, 7], [10, 20, 23, 34]]
    total = [13, 8, 5, 6, 57]

    for i in range(len(input_arr)):
        print(str(i + 1) + ".\tDoes a subset of " + str(input_arr[i]) + " sum up to " + str(total[i]) + "?   ", "Yes." if subset_sum(input_arr[i], total[i]) else "No.")
        print("-"*100)

main()
# (out) 1.	Does a subset of [3, 5, 8] sum up to 13?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 2.	Does a subset of [2, 4, 7] sum up to 8?    No.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 3.	Does a subset of [2, 3, 5] sum up to 5?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 4.	Does a subset of [1, 2, 3, 7] sum up to 6?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
# (out) 5.	Does a subset of [10, 20, 23, 34] sum up to 57?    Yes.
# (out) ----------------------------------------------------------------------------------------------------
