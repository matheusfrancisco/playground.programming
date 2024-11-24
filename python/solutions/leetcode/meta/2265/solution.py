# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.avg = 0
        self.dfs(root)
        return self.avg

    def dfs(self, node):
        if not node:
            return (0, 0)

        if not node.left and not node.right:
            self.avg += 1
            return (node.val, 1)

        l_sum, l_count = self.dfs(node.left)
        r_sum, r_count = self.dfs(node.right)

        cur_avg = (l_sum + r_sum + node.val) // (l_count + r_count + 1)
        if cur_avg == node.val:
            self.avg += 1
        return (
            l_sum + r_sum + node.val,
            l_count + r_count + 1
        )
