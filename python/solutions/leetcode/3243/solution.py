
import collections
from typing import List

class Solution:

    def findShortest(self, adj, n, current, dp):
        if current == n - 1:
            return 0
        if dp[current] != -1:
            return dp[current]

        min_dist = n
        for nei in adj[current]:
            min_dist = min(min_dist,
                           self.findShortest(adj, n, nei, dp) + 1)
        dp[current] = min_dist
        return min_dist

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        adj_list = collections.defaultdict(list)
        dp = [-1] * n
        ans = []
        for i in range(n - 1):
            adj_list[i].append(i + 1)
        for u, v in queries:
            adj_list[u].append(v)
            ans.append(self.findShortest(adj_list, n, 0, dp))
            dp = [-1] * n
        return ans
