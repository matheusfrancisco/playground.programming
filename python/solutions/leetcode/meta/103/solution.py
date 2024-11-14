import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Intuition - Perform Level Order Traversal and store elemenets of the level in a list. For every
        # alternate level, reverse the elements in this list.
        if not root:
            return root

        # Result list to be returned
        result = []
        queue = collections.deque()

        # Boolean variable to keep track of the order in which a level needs to be stored in the result list.
        leftToRight = True

        queue.append(root)

        while queue:
            # List to store the nodes of a particular level
            levelNodes = []

            levelLength = len(queue)

            # Iterating over the elements in the level
            for _ in range(levelLength):

                node = queue.popleft()
                levelNodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # If leftToRight is True, add the elements in the level as it is and set leftToRight to False
            if leftToRight:
                result.append(levelNodes)
                leftToRight = False
            # Else, reverse the elelments in the level and add them to the result. Set leftToRight to True
            else:
                result.append(levelNodes[::-1])
                leftToRight = True

        return result
