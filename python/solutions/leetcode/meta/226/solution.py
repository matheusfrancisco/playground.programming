from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeBfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = collections.deque()
        q.append(root)

        while q:

            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            node.left, node.right = node.right, node.left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs
        if not root:
            return None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left
            return node
        dfs(root)
        return root
