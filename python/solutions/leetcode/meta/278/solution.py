# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # G G G B B
        left = 0
        right = n
        while left < right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return right
