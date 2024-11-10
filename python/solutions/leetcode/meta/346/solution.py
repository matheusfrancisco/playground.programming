import collections
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = self.sum = self.head = 0
        self.items = collections.deque()

    def next(self, val: int) -> float:
        self.count += 1
        self.items.append(val)
        if self.count > self.size:
            print(self.items)
            p = self.items.popleft()
            self.sum = self.sum - p + val
            self.count -= 1
        else:
            self.sum = self.sum + val
        return self.sum / min(self.size, self.count)

    def next2(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.sum = self.sum - self.items[tail] + val

        self.head = (self.head + 1) % self.size
        self.items[self.head] = val
        return self.sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)

print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
