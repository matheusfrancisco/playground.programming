
def climbing_opt(n, k):
    """bottom up approach
    time : O(nk)
    space: O(n)
    """
    dp = [1, 1, 0]
    for i in range(2,n+1):
        for j in range(1, k+1):
            t = 0
            if i-j < 0:
                continue
            dp[i] += dp[i-j]
            dp.append(0)
    return dp[n]

def main():
    n = int(input())
    for i in range(n):
        n, k = input().split(" ")
        out = climbing_opt(int(n), int(k))
        print(out)

main()
