from typing import List
import collections

def min_coins(coins, amount, s, memo):
    if s == amount:
        return 0

    if s > amount:
        return float('inf')

    if memo[s] != -1:
        return memo[s]

    ans = float('inf')
    for coin in coins:
        print(coin, amount, s + coin, memo)
        r = min_coins(coins, amount, s + coin, memo)
        if r == float('inf'):
            continue
        print("r:", 1 + r)
        ans = min(ans, 1 + r)

    memo[s] = ans
    return ans


def coin_change(coins, amount):
    memo = [-1] * (amount + 1)
    result = min_coins(coins, amount, 0, memo)
    return result if result != float('inf') else -1


print(coin_change([1, 2, 5], 11))  # 3
