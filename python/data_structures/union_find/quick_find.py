

class QuickFindUF:
    def __init__(self, N):
        self.id = [i for i in range(N)]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        """
        Time complexity: O(N)
        """
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid


if __name__ == '__main__':
    uf = QuickFindUF(10)
    uf.union(1, 2)
    uf.union(2, 3)
    # if you add N union operations, the algorithm will take quadratic time

