# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head, insertVal: int) -> Node:
        # 1->3->4
        # when the prev is bigger then curr we find the tail.

        if head is None:
            n = Node(insertVal)
            n.next = n
            return n

        cur = head

# 1->2->3->5
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break
            elif cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    break
            # 1->3->4

            cur = cur.next

        nw = Node(insertVal, cur.next)
        cur.next = nw
        return head
