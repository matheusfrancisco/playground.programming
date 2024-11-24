from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N + N) = O(N)
# build the graph and bfs the graph
# O(N) to build the graph
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        graph = collections.defaultdict(list)

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)

        queue = collections.deque([(p, 0)])
        visited = set([p])
        while queue:
            cur, steps = queue.popleft()
            if cur == q:
                return steps
            else:
                for edge in graph[cur]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, steps + 1))
