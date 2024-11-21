import collections
from typing import Optional
# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        copy_dict = {root: NodeCopy(root.val)}

        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.random and node.random not in copy_dict:
                copy_dict[node.random] = NodeCopy(node.random.val)
                q.append(node.random)
            copy_dict[node].random = copy_dict.get(node.random, None)
            if node.left and node.left not in copy_dict:
                copy_dict[node.left] = NodeCopy(node.left.val)
                q.append(node.left)

            copy_dict[node].left = copy_dict.get(node.left, None)
            if node.right and node.right not in copy_dict:
                copy_dict[node.right] = NodeCopy(node.right.val)
                q.append(node.right)
            copy_dict[node].right = copy_dict.get(node.right, None)
        return copy_dict[root]
