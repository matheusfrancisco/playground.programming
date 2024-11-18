import heapq
class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heapq.heappush(self.hi,
                           -heapq.heappushpop(self.lo, -num))
        else:
            heapq.heappush(self.lo,
                           -heapq.heappushpop(self.hi, num))

    def findMedian(self) -> float:
        if len(self.hi) == len(self.lo):
            return float(self.hi[0] - self.lo[0])/2.0
        return float(self.hi[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
