import collections

def predict_the_winner(nums):
    dp = collections.defaultdict(int)
        
    def score(nums, l, r):
        if l == r:
            return nums[l]
        left = nums[l] - score(nums, l+1, r)
        right = nums[r] - score(nums, l, r-1)
        dp[(left, right)] = max(left, right)
        return dp[(left,right)]
    return score(nums, 0, len(nums) -1) >= 0



def main():
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split()))
        print(predict_the_winner(a))

main()
