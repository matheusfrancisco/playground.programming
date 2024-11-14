from typing import Optional
# Definition for a binary tree node.
# max = -10
# max = 9
# max = 15
# max = 42
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_path_sum = root.val
        self.dfs(root)

        return self.max_path_sum

    def dfs(self, node):
        if not node:
            return 0

        if not node.left and not node.right:
            self.max_path_sum = max(self.max_path_sum, node.val)
            return node.val

        l_path = self.dfs(node.left)
        r_path = self.dfs(node.right)

        self.max_path_sum = max(
            self.max_path_sum,
            node.val,
            node.val + l_path + r_path,
            node.val + l_path,
            node.val + r_path)
        return max(
            node.val,
            0,
            node.val + l_path,
            node.val + r_path)

class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = [root.val]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            out[0] = max(out[0], left+right+root.val)

            return max(left, right) + root.val
        dfs(root)
        return out[0]
