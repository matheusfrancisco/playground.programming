import collections
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = collections.defaultdict(int)
        h[0] = 1

        acc = 0
        count = 0
        for n in nums:
            acc += n
            if h[acc - k]:
                count += h[acc - k]
            h[acc] += 1

        return count


obj = Solution()
assert obj.subarraySum([1, 1, 1], 2) == 2

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        prefix_sum = res = 0
        # [1,1,1], k= 2
        # {0: 1}
        # p = 1
        # 1-2 in prefix (Not)
        # {1:1, 0:1,}
        # p = 2
        # 2-2 = 0 in there res += p[0], res = 1
        # {0:1, 1:1, 2:1}
        # p = 3

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix:
                res += prefix[prefix_sum - k]
            prefix[prefix_sum] += 1
        return res
