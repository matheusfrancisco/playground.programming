
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.largest = 1

        def dfs(node):
            if not node:
                return (False, 0, -10001, 10001)
            if not node.right and not node.left:
                return (True, 1, node.val, node.val)
            l_is_bst, l_size, l_min, l_max = dfs(node.left)
            r_is_bst, r_size, r_min, r_max = dfs(node.right)

            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                cur = 1 + l_size + r_size
                self.largest = max(self.largest, cur)
                return (True, cur, l_min, r_max)
            elif l_is_bst and not node.right and l_max < node.val:
                cur = 1 + l_size
                self.largest = max(self.largest, cur)
                return (True, cur, l_min, node.val)
            elif not node.left and r_is_bst and node.val < r_min:
                cur = 1 + r_size
                self.largest = max(self.largest, cur)
                return (True, cur, node.val, r_max)
            else:
                return (False, 0, -10001, 10001)
        dfs(root)
        return self.largest
