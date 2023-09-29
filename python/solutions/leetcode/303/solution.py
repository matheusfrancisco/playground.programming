class NumArray:

    def __init__(self, nums: list[int]):
        self.prev = []
        s = 0
        for n in nums:
            s += n
            self.prev.append(s)

    def sum_range(self, left: int, right: int) -> int:
        if left - 1 < 0:
            return self.prev[right]
        return self.prev[right] - self.prev[left - 1] 

def main():
    nums = map(int, input().split(" "))
    n = NumArray(nums)
    s = int(input())
    out = []
    for _ in range(s):
        left, right = map(int, input().split(" "))
        out.append(n.sum_range(left, right))
    print(out)


main()
