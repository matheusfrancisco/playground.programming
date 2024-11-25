# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def dfs(node):
            if not node:
                return None

            if node in nodes:
                return node

            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node
            else:
                return l or r
        return dfs(root)
