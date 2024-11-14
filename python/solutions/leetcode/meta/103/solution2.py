from typing import List, Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        going_right = True
        res = []

        while q:
            leve_items = []

            for _ in range(len(q)):
                if going_right:
                    top = q.popleft()

                    leve_items.append(top.val)

                    if top.left:
                        q.append(top.left)

                    if top.right:
                        q.append(top.right)
                else:
                    top = q.pop()

                    leve_items.append(top.val)

                    if top.right:
                        q.appendleft(top.right)

                    if top.left:
                        q.appendleft(top.left)

            res.append(leve_items)
            going_right = not going_right

        return res
