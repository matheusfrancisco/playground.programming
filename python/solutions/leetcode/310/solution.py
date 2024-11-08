import collections
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = collections.deque()

        for src, neib in adj.items():
            if len(neib) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neib)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                n -= 1
                node = leaves.popleft()
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)


obj = Solution()
print(obj.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))  # [1]
