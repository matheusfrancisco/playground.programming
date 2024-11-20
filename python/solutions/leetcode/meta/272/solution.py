from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = collections.deque([])

        def dfs(node):
            if node:
                dfs(node.left)
                if len(queue) < k:
                    queue.append(node.val)
                else:
                    if abs(queue[0] - target) > abs(node.val - target):
                        queue.popleft()
                        queue.append(node.val)
                    else:
                        return
                dfs(node.right)
        dfs(root)

        return list(queue)
