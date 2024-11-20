from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        self.longest_path = 1
        self.dfs(root, root.val, 0)
        return self.longest_path

    def dfs(self, node, parent, cur_lenght):
        if node:
            if node.val - 1 == parent:
                cur_lenght += 1
                self.longest_path = max(self.longest_path, cur_lenght)
                self.dfs(node.left, node.val, cur_lenght)
                self.dfs(node.right, node.val, cur_lenght)
            else:
                self.dfs(node.left, node.val, 1)
                self.dfs(node.right, node.val, 1)
