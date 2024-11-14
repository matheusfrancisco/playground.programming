# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.q_found = False
        self.p_found = False
        ans = self.dfs(root, p, q)
        return ans if self.q_found and self.p_found else None

    def dfs(self, node, p, q):
        if not node:
            return None
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)

        if node == p or node == q:
            if node == p:
                self.p_found = True
            else:
                self.q_found = True
            return node
        if l and r:
            return node
        else:
            return l or r
