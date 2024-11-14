from typing import List, Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.rangeSumBSTRec(root, low, high)

    def rangeSumBSTRec(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        self.range_sum = 0

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.range_sum += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)
        dfs(root)
        return self.range_sum

    # T: O(N) , S: O(N)

    def rangeSumBSTIte(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans
