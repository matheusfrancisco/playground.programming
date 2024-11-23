from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.items = collections.defaultdict(list)
        # for i in range(len(nums)):
        #    self.items[nums[i]].append(i)

    def pick(self, target: int) -> int:
        count = pick = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                print(count, target)
                if random.randint(1, count) == count:
                    print(i)
                    pick = i
        return pick

        # return random.choice(self.items[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
