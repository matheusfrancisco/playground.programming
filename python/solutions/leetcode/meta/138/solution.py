
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        olds = {None: None}
        curr = head
        while curr:
            nw = Node(curr.val, None, None)
            olds[curr] = nw
            curr = curr.next
        curr = head
        while curr:
            nw = olds[curr]
            nw.next = olds[curr.next]
            nw.random = olds[curr.random]
            curr = curr.next

        return olds[head]
