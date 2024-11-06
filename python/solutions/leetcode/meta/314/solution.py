
from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()

        q.append([root, 1])

        colls = collections.defaultdict(list)
        maxi = float("-inf")
        mini = float("inf")
        res = []
        while q:
            node, col = q.popleft()
            colls[col].append(node.val)

            mini = min(mini, col)
            maxi = max(maxi, col)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        for i in range(mini, maxi + 1):
            res.append(colls[i])
        return res
