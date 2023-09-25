
class QuickUnion:
    def __init__(self, N: int) -> int:
        self.ids = [i for i in range(N)]

    def root(self, p: int) -> int:
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.ids[proot] = qroot

if __name__ == '__main__':
    qu = QuickUnion(10)
    qu.union(4, 3)
    qu.union(3, 8)
    qu.union(6, 5)
    qu.union(9, 4)
    qu.union(2, 1)
    qu.union(5, 0)
    qu.union(7, 2)
    qu.union(6, 1)
    qu.union(7, 3)
    print(qu.ids)
  #=> [1 8 1 8 3 0 5 1 8 8]
