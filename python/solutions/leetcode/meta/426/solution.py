
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None
        curr = root
        stack = []
        head = prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not head:
                head = curr
            if prev:
                curr.left = prev
                prev.right = curr
            prev = curr
            curr = curr.right
        head.left = prev
        prev.right = head

        return head


