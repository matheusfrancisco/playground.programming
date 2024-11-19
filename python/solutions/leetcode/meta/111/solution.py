from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        depth = 1

        while q:

            q_size = len(q)
            for _ in range(q_size):
                node = q.popleft()
                if not node:
                    continue

                if not node.left and not node.right:
                    return depth
                q.append(node.left)
                q.append(node.right)
            depth += 1
        return -1

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append([root, 0])
        min_lvl = float("inf")

        while q:

            node, lvl = q.popleft()

            if node.left:
                q.append([node.left, lvl + 1])
            if node.right:
                q.append([node.right, lvl + 1])

            if not node.left and not node.right:
                min_lvl = min(lvl + 1, min_lvl)
                return min_lvl

        return min_lvl
