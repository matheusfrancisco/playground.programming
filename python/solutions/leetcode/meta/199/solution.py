from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t = TreeNode(1,
             TreeNode(2, None, TreeNode(5)),
             TreeNode(3, None, TreeNode(4)))


def rightSideView(root):
    if root is None:
        return []

    r = []

    def helper(node, level):
        if level == len(r):
            r.append(node.val)
        for c in [node.right, node.left]:
            if c:
                helper(c, level + 1)
    helper(root, 0)
    return r


print(rightSideView(t) == [1, 3, 4])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
