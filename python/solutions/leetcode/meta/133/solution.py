"""
# Definition for a Node.
"""
from collections import deque
import collections
 
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    "T: O(N), S: O(N)"

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        cloned = {}
        cloned[node] = Node(node.val, [])

        queue = collections.deque([node])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cloned[cur].neighbors.append(cloned[neighbor])
        return cloned[node]


class Solution2:
    "O(E+V)"

    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if not node:
                return node
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val, [])
            old_to_new[node] = copy
            for nbr in node.neighbors:
                copy.neighbors.append(dfs(nbr))
            return copy

        return dfs(node)

    def cloneGraph_bfs(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
