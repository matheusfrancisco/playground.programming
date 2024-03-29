#https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16

class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.h = collections.defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.h: return False
        self.h[val] = len(self.stack)
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h: return False
        last = self.stack[-1]
        index = self.h[val]
        self.stack[index] = last
        self.h[last] = index
        self.stack.pop()
        del self.h[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
