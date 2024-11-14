
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1 or not l2:
            return l1 or l2
        carry = 0
        res = ListNode(0)
        sentinel = res
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_sum = l1_val + l2_val + carry
            print(l1_val, l2_val)
            print(cur_sum)
            res.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        if carry:
            res.next = ListNode(carry)
        return sentinel.next
