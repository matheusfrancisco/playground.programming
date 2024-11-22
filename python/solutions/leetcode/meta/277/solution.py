
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i

        if self.is_celeb(celebrity, n):
            return celebrity
        return -1

    def is_celeb(self, candidate, n):
        for i in range(n):
            if i == candidate:
                continue
            else:
                if not knows(i, candidate) or knows(candidate, i):
                    return False
        return True
