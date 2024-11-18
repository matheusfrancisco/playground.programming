from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst_helper(root)[0]

    def bst_helper(self, node):
        if not node:
            return (False, float("inf"), float("-inf"))

        if not node.left and not node.right:
            return (True, node.val, node.val)

        l_is_bst, l_min, l_max = self.bst_helper(node.left)
        r_is_bst, r_min, r_max = self.bst_helper(node.right)

        if l_is_bst and r_is_bst and l_max < node.val < r_min:
            return (True, l_min, r_max)
        elif l_is_bst and not node.right and node.val > l_max:
            return (True, l_min, node.val)
        elif r_is_bst and not node.left and node.val < r_min:
            return (True, node.val, r_max)
        else:
            return (False, float("inf"), float("-inf"))

    def sol2(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        s = [(root, -math.inf, math.inf)]
        while s:
            root, lower, upper = s.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            s.append((root.left, lower, val))
            s.append((root.right, val, upper))
        return True
