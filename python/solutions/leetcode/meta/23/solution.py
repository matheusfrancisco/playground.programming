# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def merge(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
