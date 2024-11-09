from typing import List
import collections

def min_coins(coins, amount, s, memo):
    if s == amount:
        return 0

    if s > amount:
        return float('inf')

    if memo[s] != -1:
        print(f"memo hit {s} -> {memo[s]}")
        return memo[s]

    ans = float('inf')
    for coin in coins:
        print(f"{s} -> {s+coin}", amount, memo)
        r = min_coins(coins, amount, s + coin, memo)
        print(f"result from {s}", r)
        if r == float('inf'):
            continue
        print(f"{ans}, {1 + r}")
        ans = min(ans, 1 + r)
        print(f"{s} ->  {s + coin}: r {ans}", memo)

    memo[s] = ans
    return ans


def coin_change(coins, amount):
    memo = [-1] * (amount + 1)
    result = min_coins(coins, amount, 0, memo)
    return result if result != float('inf') else -1


def coin_change_2(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


print(coin_change_2([1, 2, 5], 11))  # 3
print(coin_change([1, 2, 5], 3))  # 3
