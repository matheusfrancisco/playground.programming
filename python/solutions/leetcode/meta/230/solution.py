from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        elements = self.inorder_not_optimal()(root)
        return elements[k - 1]

    def inorder_not_optimal(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []
