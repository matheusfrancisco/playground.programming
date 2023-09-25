class QuickUnionWeighted:

    def __init__(self,n):
        self.arr = list(range(n))
        self.sizes = [1] * n

    def union(self, p, q):
        if p == q: return

        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return

        if self.sizes[p_root] < self.sizes[q_root]:
            self.arr[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.arr[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]

    def root(self, p):
        while not p == self.arr[p]:
            p = self.arr[p]
        return p


class WeightedQuickUnionWithPathCompressionUF():
  """Weighted quick-union with path compression algorithm
  The original Java implementation is introduced at:
    https://algs4.cs.princeton.edu/15uf/index.php#1.5
    https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
  Time complexity:
    constructor: O(n)
    union:       amortized ~O(1)
    find:        amortized ~O(1)
  >>> uf = WeightedQuickUnionWithPathCompressionUF(10)
  >>> for (p, q) in [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1),
  ...                (8, 9), (5, 0), (7, 2), (6, 1)]:
  ...     uf.union(p, q)
  >>> uf
  {'roots': [6, 2, 6, 4, 4, 6, 6, 2, 4, 4], 'count': 2}
  >>> uf.find(1)
  6
  >>> uf
  {'roots': [6, 6, 6, 4, 4, 6, 6, 2, 4, 4], 'count': 2}
  >>> uf.connected(7, 0)
  True
  >>> uf
  {'roots': [6, 6, 6, 4, 4, 6, 6, 6, 4, 4], 'count': 2}
  """
  def __init__(self, n):
    self.items = list(range(n))
    self.sizes = [1] * n

  def __repr__(self):
    return "{'roots': %s }" % (self.items)

  def union(self, p, q):
    if p == q:
      return
    p_root = self._root(p)
    q_root = self._root(q)
    if p_root == q_root:
      return

    if self.sizes[p_root] < self.sizes[q_root]:
      self.items[p_root] = q_root
      self.sizes[q_root] += self.sizes[p_root]
    else:
      self.items[q_root] = p_root
      self.sizes[p_root] += self.sizes[q_root]

  def _root(self, p):
    root = self.items[p]
    while not root == self.items[root]:
      self.items[root] = self.items[self.items[root]]
      root = self.items[root]
    self.items[p] = root
    return root

  def find(self, p):
    return self._root(p)

  def connected(self, p, q):
    return p == q or self.find(p) == self.find(q)



if __name__ == '__main__':
    qu = QuickUnionWeighted(10)
    qu.union(4, 3)
    qu.union(3, 8)
    qu.union(6, 5)
    qu.union(9, 4)
    qu.union(2, 1)
    qu.union(5, 0)
    qu.union(8, 9)
    qu.union(7, 2)
    qu.union(6, 1)
    qu.union(7, 3)

    uf = WeightedQuickUnionWithPathCompressionUF(10)
    for (p, q) in [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1),(8, 9), (5, 0), (7, 2), (6, 1)]:
        uf.union(p, q)
        #qu.union(p, q)
    print(uf)
    print(qu.arr)

# (out) {'roots': [6, 2, 6, 4, 4, 6, 6, 2, 4, 4] }
# (out) [6, 2, 6, 4, 4, 6, 6, 2, 4, 4]
