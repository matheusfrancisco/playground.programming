from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        res = float("inf")
        bits = [0] * 32
        n = len(nums)

        def bits_update(bits, n, diff):
            for i in range(32):
                print(n, (1 << i))
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res
        l = 0

        for right in range(n):
            bits_update(bits, nums[right], 1)

            cur_or = bits_to_int(bits)
            print(bits, 1)
            print(cur_or)
            while cur_or >= k:
                res = min(res, right - l + 1)
                bits_update(bits, nums[l], -1)
                print(bits, 2)
                cur_or = bits_to_int(bits)
                l += 1
        return -1 if res == float("inf") else res


print(Solution().minimumSubarrayLength([1, 2, 3], 2))
