# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
import collections

class NestedInteger:
    def __init__(self, value=None):
        """
            If value is not specified, initializes an empty list.
            Otherwise initializes a single integer equal to value.
            """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        res = 0

        queue = collections.deque(nestedList)

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.isInteger():
                    res += cur.getInteger() * depth
                else:
                    queue.extend(cur.getList())
            depth += 1
        return res
    # T: O(N)
    # S: O(N)
