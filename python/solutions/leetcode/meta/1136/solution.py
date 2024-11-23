from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for prev, next in relations:
            graph[prev].append(next)

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1

            max_length = 1
            for end_node in graph[node]:
                length = dfs(end_node)
                if length == -1:
                    return 1
                else:
                    max_length = max(length + 1, max_length)
            visited[node] = max_length
            return max_length

        max_length = -1
        for node in graph:
            length = dfs(node)
            if length == -1:
                return -1
            else:
                max_length = max(length, max_length)
        return max_length
