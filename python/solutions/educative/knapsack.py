"""
https://www.youtube.com/watch?v=xCbYmUPvc2Q&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=21&pp=iAQB
Top-down solution
The top-down solution, commonly known as the memoization technique, is an enhancement of the 
recursive solution. It overcomes the problem of calculating redundant solutions over and over again 
by storing them in a table.

In the recursive approach, the two variables that kept changing in each call were the 
total weight of the knapsack and the number of items we had. So, we’ll use these two 
variables to define each distinct subproblem. Therefore, we need a 2-D array to store 
these values and the result of any given subproblem when we encounter it for the first time. 
At any later time, if we encounter the same sub-problem, we can return the stored result from the table with an 
O(1)
 lookup instead of recalculating that subproblem.
"""
import pprint

def find_knapsack_top_down(capacity, weights, values, n):
    dp = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    return find_knapsack_value(capacity, weights, values, n, dp)

def find_knapsack_value(capacity, weights, values, n, dp):
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    #If we have solved it earlier, then return the result from memory
    if dp[n][capacity] != -1:
        return dp[n][capacity]
 
    #Otherwise, we solve it for the new combination and save the results in the memory
    if weights[n-1] <= capacity:
        dp[n][capacity] = max(
            values[n-1] + find_knapsack_value(capacity-weights[n-1], weights, values, n-1, dp),
            find_knapsack_value(capacity, weights, values, n-1, dp)
            )
        return dp[n][capacity]

    dp[n][capacity] = find_knapsack_value(capacity, weights, values, n-1, dp)
    return dp[n][capacity] 

def find_knapsack_bottom_up(capacity, weights, values, n):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i-1] <= j:
                m = max(values[i-1]+ dp[i-1][j-weights[i-1]], 
                              dp[i-1][j])
                dp[i][j] =m 
            else:
                dp[i][j] = dp[i-1][j]
 
    pprint.pprint(dp)
    return dp[-1][-1]

d = find_knapsack_bottom_up(6, [1, 2, 3, 5], [1, 5, 4, 8], 4)
pprint.pprint(d)
d = find_knapsack_bottom_up(10, [10, 20, 30], [22, 33, 44], 3)
pprint.pprint(d)
