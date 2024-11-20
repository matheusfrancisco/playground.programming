# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree2(self, root: Optional[TreeNode]) -> bool:

        q = collections.deque()
        q.append(root)
        null_seen = False
        while q:
            if null_seen:
                return not any(q)
            else:
                for _ in range(len(q)):
                    node = q.popleft()
                    if not node:
                        null_seen = True
                    else:
                        if null_seen:
                            return False
                        else:
                            q.append(node.left)
                            q.append(node.right)
        return True

    def isCompleteTree(self, root):
        if not root:
            return True

        queue = [root]
        seen_null = False

        while queue:
            current = queue.pop(0)

            if current is None:
                seen_null = True
            else:
                if seen_null:
                    return False  # Found a non-null after a null

                queue.append(current.left)
                queue.append(current.right)

        return True
