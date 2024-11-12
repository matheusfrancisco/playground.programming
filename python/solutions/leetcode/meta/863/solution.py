from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)

        res = []
        visited = set([target])

        q = collections.deque([(target, 0)])
        while q:
            node, distance = q.popleft()
            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        q.append((edge, distance + 1))
        return res

# T: O(N) + O(N) -> O(2N) -> O(N)
# S: O(N) + O(N) -> O(2N) -> O(N)

